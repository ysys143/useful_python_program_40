from gtts import gTTS

text = "저희는 지금 파이썬을 공부하고 있습니다."
tts = gTTS(text, lang='ko')
tts.save('result.mp3')
