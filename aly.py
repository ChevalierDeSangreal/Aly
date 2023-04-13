import openai
from TTS.api import TTS
import pyaudio
import wave
import time
import signal
 



class Aly:
    def __init__(self):
        openai.api_key = "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"
        self.conv_list = []
        self.show_conv_list = []
        self.tts = TTS(model_name="tts_models/multilingual/multi-dataset/your_tts", progress_bar=False, gpu=True)
        self.chunk = 1024
    
    def ask_chatgpt(self, promot):
        self.conv_list.append({"role":"user", "content":promot})
        self.show_conv_list.append({"role":"user", "content":promot, "time":time.asctime(time.localtime(time.time()))})
        
        print("Waiting for ChatGPT...")
        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = self.conv_list
        )
        ans = response.choices[0].message['content']
        self.conv_list.append({"role":"user", "content":ans})
        self.show_conv_list.append({"role":"user", "content":ans, "time":time.asctime(time.localtime(time.time()))})
        print(time.asctime(time.localtime(time.time())) + f" User: {ans}\n")
        self.play_voice(ans)

    def play_voice(self, text):
        print("Waiting for STT...")
        self.tts.tts_to_file(text, speaker_wav="D:\\Software\\Python\\Aly\\cloning\\OldCat_slice.wav", language="en", file_path="output.wav")
        fil = wave.open("output.wav", "rb")
        player = pyaudio.PyAudio()
        stream = player.open(format = player.get_format_from_width(fil.getsampwidth()),
				channels = fil.getnchannels(),
				rate = fil.getframerate(),
                output=True)
        data = fil.readframes(self.chunk)
        while len(data) > 0:
            stream.write(data)
            data = fil.readframes(self.chunk)
        
        stream.stop_stream()
        stream.close()
        player.terminate()



if __name__ == "__main__":
    Alysia = Aly()
    while True:
        context = input(time.asctime(time.localtime(time.time())) + " User: ")
        print(context)
        Alysia.ask_chatgpt(context)
        