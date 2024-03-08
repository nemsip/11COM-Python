import torch
from TTS.api import TTS

inputText = input(f"What do you want Mr McLeod to say?\n>_ ")

device = "cuda" if torch.cuda.is_available() else "cpu"

print(TTS().list_models())

tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

wav = tts.tts(text=inputText, speaker_wav=r"%USERPROFILE%\Desktop\MrMcLeod\Enhanced.mp3", language="en")

# tts.voice_conversion_to_file(source_wav="my/source.wav", target_wav="my/target.wav", file_path="mmcout.wav")

tts.tts_to_file(text=inputText, speaker_wav=r"%USERPROFILE%\Desktop\MrMcLeod\Enhanced.mp3"", language="en", file_path="mmcout.wav")

