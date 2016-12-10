import subprocess as sp


def say(text=None,voice=None):
  text = " '" + text + "'"
  if voice != None:
    voice = " -v " + voice
  else:
    voice = ""
  sp.call("espeak" + voice + text, shell=True)

if __name__ in "__main__":
     sp.call("espeak -v kill -f /home/pi/lyric", shell=True)
