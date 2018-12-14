from pydub import AudioSegment
import os

path=os.getcwd()

def convert_wav(path):
	for archivo in os.listdir(path):
		name_file=archivo.split('.')
		sound = AudioSegment.from_file(archivo,name_file[1])
		sound.export(name_file[0]+".wav", format="wav")


convert_wav(path)