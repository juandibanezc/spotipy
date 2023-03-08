from .exceptions import InvalidAudioFile, InvalidImageFile

class ImageFile:
    def __init__(self, file_path: str):
        if not file_path.endswith(self.ext):
            raise InvalidImageFile(
                f"Invalid image file format. Expecting a {self.ext} file"
            )
        self.filename = file_path

class AudioFile:
    def __init__(self, file_path: str):
        if not file_path.endswith(self.ext):
            raise InvalidAudioFile(
                f"Invalid audio file format. Expecting a {self.ext} file"
            )
        self.filename = file_path

class MP3File(AudioFile):
    ext = "mp3"

    def play(self):
        print("playing {} as mp3".format(self.filename))

class WavFile(AudioFile):
    ext = "wav"

    def play(self):
        print("playing {} as wav".format(self.filename))


class OggFile(AudioFile):
    ext = "ogg"

    def play(self):
        print("playing {} as ogg".format(self.filename))


class PNGFile(ImageFile):
    ext = "png"

class JPEGFile(ImageFile):
    ext = "jpeg"

class SVGFile(ImageFile):
    ext = "svg"