from gtts import gTTS
import os

text="comment ca va Mahashree?"
lang="fr"

obj=gTTS(text=text, lang=lang, slow=False)

obj.save("voice.mp3")

os.system("voice.mp3")
