from shutil import move, copy2
import gradio as gr
import os
from pathlib import Path
from datetime import datetime
from environment import YT_SAVE_AUDIO, YT_USE_CACHE, CACHE_FILE, TEMP_PATH, OUTPUT_PATH, DOWNLOAD_PATH, RECORDING_PATH, DEFAULT_LANGUAGE
from functions import *
import subprocess

process = subprocess.Popen('cmd', creationflags=subprocess.CREATE_NEW_CONSOLE, stdin=subprocess.PIPE)
process.stdin.write(('%s\n' % "python ../aly.py").encode('utf-8'))
process.stdin.flush()

# import sys
# sys.path.append("..")
# import aly


# Aly = aly.Aly()
# now_text = ""

# def process_aly():
#     while 1:
#         queue.get()
#         Aly.ask_chatgpt(now_text)
#         time.sleep(10)
#     return

# queue = multiprocessing.Manager().Queue()
# p_aly = multiprocessing.Process(target=process_aly, args=(queue,))

def get_yt_default_options():
    options = []
    if YT_SAVE_AUDIO:
        options.append("Save Audio")
    if YT_USE_CACHE:
        options.append("Use Cache")
    return options


def set_yt_preview(url):
    data = get_video_data(url)
    if data is not None:
        thumbnail_url, author, title, length, publish_date = data
        preview = f"""
        #### {title}<br>
        by **{author}**<br><br>
        **Duration**: {length//3600:0>2}:{(length//60)%60:0>2}:{length%60:0>2}<br>
        **Published**: {publish_date.date()}"""

        return [gr.update(value=thumbnail_url),
                gr.update(value=preview)]
    return [gr.update(value=None),
            gr.update(value=None)]



def save_recording(filepath):
    if filepath is not None:
        filename = f'{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.{filepath.rsplit(".", 1)[-1]}'
        move(filepath, RECORDING_PATH/filename)
        return gr.update(value=f"Saved recording under {str(RECORDING_PATH.absolute() / filename)}")
    else:
        return gr.update(value="Please record audio first.")


def mp3_to_subtitles(filepath, model_language, model, language):
    outputs, files = audio_to_text(filepath, model_language,
                                   model, language, OUTPUT_PATH)
    process.stdin.write(('%s\n' % outputs[0]).encode('utf-8'))
    process.stdin.flush()
    remove_file(filepath)
    return outputs + [files]



def change_model_options(choice, model):
    if choice == "multilingual":
        return gr.update(choices=["tiny", "base", "small", "medium", "large"])
    elif choice == "english-only":
        return gr.update(
            choices=["tiny", "base", "small", "medium"],
            value=model if model != "large" else "medium")
    else:
        raise ValueError("Unexpected Error.")


def change_language_options(choice):
    if choice == "multilingual":
        return gr.update(
            choices=list(LANGUAGES.keys()),
            value=DEFAULT_LANGUAGE,
            interactive=True)
    elif choice == "english-only":
        return gr.update(
            choices=["english"],
            value="english",
            interactive=False)
    else:
        raise ValueError("Unexpected Error.")


def reset_value():
    return gr.update(value=None)


def reset_value_not_visible():
    return gr.update(value=None, visible=False)


def get_css():
    try:
        with open("style.css", "r") as f:
            return f.read()
    except:
        raise Exception("style.css could not be found.")
