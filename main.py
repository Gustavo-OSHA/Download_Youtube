from pytube import YouTube

url = input('Digite o link do video: ')

youtube = YouTube(url)

print('iniciando')
print('Titulo:'+youtube.title)
video = youtube.streams.get_highest_resolution()
video.download()
