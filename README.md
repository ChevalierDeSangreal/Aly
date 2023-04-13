## About Aly

Aly is a combination of several open source project. Having ChatGPT from OpenAI as a core, Aly aims at **realizing voice communication wich ChatGPT**, which means that you speak to ChatGPT, and it answer you in voice. 

Aly hasn't been completely finished yet, and there are lots of things to be improved. But its basic function has been completed.

Every key components of Aly comes from others' open source procect (except ChatGPT). The UI comes from [whisper Web UI](https://github.com/AndreMarkert/whisper-webui); The conversion from voice to text comes from the [OpenAI whisper](https://github.com/openai/whisper); The Part of ChatGPT uses the api provided by OpenAI; The final part, conversion from text back to voice comes from [coqui-TTS](https://github.com/coqui-ai/TTS).


![example](.\\pics\\eg.png "example")

To see the performance, you may listen to the output.wav file.


## Features

- from voice to voice

- Benefit from the prominent performance of ChatGPT

- Multi-Language support

- Custom voice tone

- Processing locally except the part concerning ChatGPT

- Low computational resource requirement, even only CPU!

## Background

The idea comes to me that having these excellent open source code, it sounds exciting to combine them as a voice to voice program. Actually I believe that I'm not the first to have this idea, and probably someone has finished this work. But well, I just couldn't find it. So concerning that this work is not so complex, and it's a good chance for me to improve my poor code ability, I decided to write Aly for myself to use.

I have put Aly on GitHub because I believe it might help others who share the same thought as me.

I don't expect there will be anyone interested at this project, so I do not have a plan to write the Install and Usage part in Readme. Actually I think the time it takes to run my code might not be shorter than the time it takes to write one by yourself. But if you really want to run Aly, or you want to make Aly better, you can connect with me by email 415545488@qq.com.

## Drawback to be improved

- Too slow!!!

&emsp;&emsp;It takes around fifteen to converse from voice to text using the medium model of whisper on my device with 3080ti. Switching to the small model only helps little. The model couldn't make my GPU fully used. Using the online GPU might help? But I hope Aly could be run locally if possible.

- Not local

&emsp;&emsp;Using the OpenAI api for ChatGPT, Aly couldn't run without Internet.

- Perfomance not so good on Chinese

&emsp;&emsp;The perfomance on Chinese is not so satisfying. The problem occurs on the stage of TTS, in Chinese the voice couldn't imitate the example very well. The words are correct and are able to be distinguish. But is not please enough for me.

- ugly UI


## Credits

- OpenAI Whisper https://openai.com/blog/whisper/, https://github.com/openai/whisper
- Whisper Web UI https://github.com/AndreMarkert/whisper-webui
- coqui-TTS https://github.com/coqui-ai/TTS