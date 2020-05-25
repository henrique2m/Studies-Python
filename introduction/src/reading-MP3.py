from pygame import mixer
import os
file = os.path.join(os.path.dirname(__file__), '../music/music.mp3')
print(file)
mixer.init()
mixer.music.load(file)
mixer.music.play()

stop = input("Digite algo para parar: ")