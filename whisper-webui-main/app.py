import gradio as gr
from logic import *
from environment import OUTPUT_PATH, DOWNLOAD_PATH, RECORDING_PATH, CACHE_FILE, DEFAULT_MODEL_LANGUAGE, DEFAULT_MODEL, DEFAULT_LANGUAGE


# python app.py --input_audio_max_duration -1
# create output folder
OUTPUT_PATH.mkdir(parents=True, exist_ok=True)
# create download folder
DOWNLOAD_PATH.mkdir(parents=True, exist_ok=True)
# create recording folder
RECORDING_PATH.mkdir(parents=True, exist_ok=True)
# update or create cache file
update_cachefile(CACHE_FILE)



# context = "Hello world"

# while 1:
#     print(time.asctime(time.localtime(time.time())) + "tmp3: hhh\n")
#     process.stdin.write(('%s\n' % context).encode('utf-8'))
#     process.stdin.flush()
#     time.sleep(5)



with gr.Blocks(css=get_css(), title="Transcription", theme="default") as page:
    # Title
    gr.Markdown(
        """## Generate a transcript for YouTube, a video/audio file or your microphone.""")

    # Whisper Model Options
    with gr.Row() as r1:
        # model language
        with gr.Column(scale=1) as c1_1:
            model_language = gr.Radio(
                choices=["multilingual", "english-only"],
                label="Choose a model language",
                value=DEFAULT_MODEL_LANGUAGE
            )

        # model size
        with gr.Column(scale=2) as c1_2:
            model = gr.Radio(
                choices=["tiny", "base", "small", "medium", "large"],
                label="Choose a model",
                value=DEFAULT_MODEL
            )

        # audio or translation language
        with gr.Column(scale=1) as c1_3:
            language = gr.Dropdown(
                label="Select a language (original or english for translation)",
                choices=list(LANGUAGES.keys()),
                value=DEFAULT_LANGUAGE,
                type="value",
                interactive=True
            )

    # Input / Output
    with gr.Row() as r2:
        # Input
        with gr.Column(scale=2, min_width=500) as c2_1:

            # Audio Tab
            with gr.Tab("Audio", id=0):
                audio_file_input2 = gr.Audio(
                    label="Audio", source="upload", type="filepath")
                with gr.Row():
                    reset_button2 = gr.Button("Clear", elem_id="clear-button2")
                    text_button2 = gr.Button(
                        "Submit", elem_id="submit-button2")

            # Microphone Recording Tab
            with gr.Tab("Microphone", id=1):
                audio_file_input3 = gr.Audio(
                    label="Audio Recording", source="microphone", type="filepath")
                save_recording_button3 = gr.Button("Save Recording")
                save_recording_out3 = gr.Markdown()
                with gr.Row():
                    reset_button3 = gr.Button("Clear", elem_id="clear-button3")
                    text_button3 = gr.Button(
                        "Submit", elem_id="submit-button3")

        # Output
        with gr.Column(scale=3, min_width=500, elem_id="output") as c2_2:
            with gr.Tab("Text", elem_id="output0"):
                text_output = gr.Textbox(show_label=False)
            with gr.Tab("Table", elem_id="output1"):
                text_markdown_output = gr.Markdown(
                    label="Table",
                    value="| Start | End | Text |\n|----|----|----|\n|0|0||")
            with gr.Tab("Table (interactive)", elem_id="output2"):
                text_table_output = gr.DataFrame(
                    headers=["Start", "End", "Text"],
                    datatype=["number", "number", "str"],
                    value=None)
            with gr.Tab("JSON", elem_id="output3"):
                text_json_output3 = gr.JSON(label="JSON")
            with gr.Tab("JSON (raw)", elem_id="output4"):
                text_json_output4 = gr.JSON(label="JSON")
            with gr.Tab("Downloads", elem_id="output5"):
                files_output5 = gr.Files(value=None)

    # Whisper Model Options
    model_language.change(
        fn=change_model_options,
        inputs=[model_language, model],
        outputs=[model])
    model_language.change(
        fn=change_language_options,
        inputs=[model_language],
        outputs=[language])


    # Audio Tab
    text_button2.click(
        fn=mp3_to_subtitles,
        inputs=[audio_file_input2, model_language, model, language],
        outputs=[text_output, text_markdown_output, text_table_output, text_json_output3, text_json_output4, files_output5])
    reset_button2.click(
        fn=reset_value, inputs=[], outputs=[audio_file_input2])

    # Recording Tab
    save_recording_button3.click(
        fn=save_recording,
        inputs=[audio_file_input3],
        outputs=[save_recording_out3]
    )
    text_button3.click(
        fn=mp3_to_subtitles,
        inputs=[audio_file_input3, model_language,
                model, language],
        outputs=[text_output, text_markdown_output, text_table_output, text_json_output3, text_json_output4, files_output5])
    reset_button3.click(
        fn=reset_value, inputs=[], outputs=[audio_file_input3])
    reset_button3.click(
        fn=reset_value, inputs=[], outputs=[save_recording_out3]
    )

page.launch(server_name="0.0.0.0")
