class ImageFormatException(Exception):
    default_message = f"Wrong image`s format. It must be one of the next formats: JPEG, JPG, GIF, PNG"

    def __init__(self, message=default_message):
        self.message = message
        super().__init__(self.message)


class ImageSizeException(Exception):
    default_message = f"Uploaded image`s size is more than 10MB"

    def __init__(self, message=default_message):
        self.message = message
        super().__init__(self.message)