import PySide6.QtWidgets as QtWidgets
import sys
import time
import vlc
import random
import os

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'black', 'white', 'gray', 'pink']


def get_music_directory(color, song_num):
    path = f'Videos/{color}/{song_num}.mp4'
    if os.path.exists(path): # since some colors only have 9 files
        return path
    else: # if no path found play the first song
        song_num = 1
        return f'Videos/{color}/{song_num}.mp4'


def main():
    instance = vlc.Instance()
    player = instance.media_player_new()

    for i in len(colors):
        song_num = random.randint(1, 10)
        song_directory = get_music_directory(colors[i], song_num) # retrieve directory
        media = instance.media_new(song_directory) # set media player to directory
        player.set_media(media)

        vlc_app = QtWidgets.QApplication([]) # open video widget
        vlc_widget = QtWidgets.QFrame()
        vlc_widget.resize(720, 1280)
        vlc_widget.show()

        player.set_nsobject(vlc_widget.winId())

        player.play()

        vlc_app.exec()


if __name__ == "__main__":
    main()
