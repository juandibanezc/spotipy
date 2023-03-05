class ImageError(Exception):
	pass


class NoImageFoundError(ImageError):
	pass


class InvalidAudioFile(Exception):
	pass

class InvalidImageFile(Exception):
	pass