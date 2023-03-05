from models.song import Song

def run_app():
  songDict = {
      "name": "Flowers",
      "audio_file_path": "files/audios/Forever_Young_Otis_McDonald.mp3",
      "duration_ms": "242",
      "image_file_path": "files/images/otis_mcdonald.jpeg",
  }

  song1 = Song(name="Flowers", audio_file_path="files/audios/Forever_Young_Otis_McDonald.mp3",
              duration_ms=123, image_file_path="files/images/otis_mcdonald.jpeg"
              )

  song1.play()

if __name__ == '__main__':
    run_app()