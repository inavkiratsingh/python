from pytube import Playlist

link = input("Enter the link of the playlist : ")

yt_playlist = Playlist(link)

for video in yt_playlist.videos:
    video.streams.get_highest_resolution().download("E:\Python\softwares\c++ paras")
    print("Video Download : ", video.title)

print("\nAll videos are downloaded")