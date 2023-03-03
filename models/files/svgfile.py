class ImageFile:
    def __init__(self, file_path):
        self.file_path = file_path


class SVGFile(ImageFile):

    def __init__(self, file_path, ext):
        super().__init__(file_path)
        self.ext = ext