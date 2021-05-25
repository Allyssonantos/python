from pytube import YouTube
import moviepy.editor as mp 
import re 
import os 

# Digite o link do video e o local que deseja salva o mp3 #
link = input("Digite o link do video que deseja baixar: ")
path = input( "Digite o diretório que deseja salva o vídeo: ")
yt = YouTube(link)

#começa o Download #
print("Baixando...")
ys = yt.strams.filter(only_audio=True).first().download(path)
print("Download completo!")

# Converte mp4 para mp3 #
print("Convertendo arquivo...")
for file in os.listdir(path):
    if re.search("mp4", file):
        mp4_patch = os.path.join(path, file)
        mp3_patch = os.path.join(path, os.path.splitext(file)[0]+'.mp3')
        new_file = mp.AudioFileClip(mp4_patch)
        new_file.write_audiofile(mp3_patch)
        os.remove(mp4_patch)
print("Sucesso")
