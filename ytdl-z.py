from pytube import YouTube
from pytube import Playlist
import os
from moviepy.editor import AudioFileClip


class Youtube_Downloader:
    home_folder = f'c:/Users/{os.getlogin()}' if os.name == 'nt' else f'/home/{os.getlogin()}'

    def start(self):
        print("Enter video/playlist url")
        url = input(">>> ")
        print("What to download?\n1. audio\n2. video")
        vid_or_aud = input("(1 or 2)\n>>> ")
        if url.startswith("https://youtu.be/") and vid_or_aud == "1":
            self.download_audio(url)
        elif url.startswith("https://youtu.be/") and vid_or_aud == "2":
            self.download_video(url)
        elif url.startswith("https://youtube.com/playlist?list=") and vid_or_aud == "1":
            self.download_audio_playlist(url)
        elif url.startswith("https://youtube.com/playlist?list=") and vid_or_aud == "2":
            self.download_video_playlist(url)
        else:
            print("enter a valid url")

    def convert_to_audio(self, path):
        path = f"{self.home_folder}/Music/ytdl-z/" if path is None else path
        files = os.listdir(path)
        for file in files:
            if file.endswith('.mp4'):
                full_path = os.path.join(path, file)
                vClip = AudioFileClip(full_path)

                mp3_filename = file.removesuffix('4').strip() + '3'
                mp3_full_path = os.path.join(path, mp3_filename)

                vClip.write_audiofile(mp3_full_path)
                vClip.close()

                os.remove(full_path)

    def download_audio(self, url):
        yt = YouTube(url)
        print(f"downloading... {yt.title}")

        download_location = f"{self.home_folder}/Music/ytdl-z/"
        try:
            yt.streams.get_audio_only().download(download_location)
        except:
            print("error...")
        finally:
            print(f"successfully downloaded {yt.title} at {download_location}")
            self.convert_to_audio(download_location)

    def download_video(self, url):
        yt = YouTube(url)
        print(f"downloading... {yt.title}")

        download_location = f"{self.home_folder}/Videos/ytdl-z/"
        try:
            yt.streams.filter(progressive=True).get_highest_resolution().download(download_location)
        except:
            print("error...")

        print(f"successfully downloaded {yt.title} at {download_location}")

    def download_video_playlist(self, url):
        pl = Playlist(url)
        download_location = f'{self.home_folder}/Videos/ytdl-z/Playlists/{pl.title}'

        for yt in pl.videos:
            try:
                yt.streams.filter(progressive=True).get_highest_resolution().download(download_location)
                print(f"downloaded.. {yt.title}")
            except:
                print("error...")

        print(f"successfully downloaded {pl.title} at {download_location}")

    def download_audio_playlist(self, url):
        pl = Playlist(url)
        download_location = f'{self.home_folder}/Music/ytdl-z/Playlists/{pl.title}'

        for yt in pl.videos:
            try:
                yt.streams.get_audio_only().download(download_location)
                print(f"downloaded.. {yt.title}")
            except:
                print("error...")

        print(f"successfully downloaded {pl.title} at {download_location}")
        self.convert_to_audio(download_location)


if __name__ == '__main__':
    app = Youtube_Downloader()
    app.start()
