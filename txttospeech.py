from gtts import gTTS
import os

# the text i want to speech
myText = "Hope is everything"

# specify language
language = 'en'


output = gTTS(text=myText, lang=language, slow=False)

# save output as an mp3 file
output.save("txttospeechoutput.mp3")

# audio to automatically play
os.system("start txttospeechoutput.mp3")
