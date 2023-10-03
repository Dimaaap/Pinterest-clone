from PIL import Image
from .exceptions import ImageFormatException, ImageSizeException

MAX_IMAGE_SIZE = 10 * 1024 * 1024  # 10 MB


def validate_image_format(image_file):
    if image_file:
        try:
            img = Image.open(image_file)
            allowed_formats = {"JPEG", "JPG", "PNG", "GIF"}
            if img.format not in allowed_formats:
                raise ImageFormatException()
        except Exception as e:
            raise FileNotFoundError("Не вдалось відкрити файл із зображенням")
    return image_file


def validate_image_size(image_file):
    if image_file:
        if image_file.size > MAX_IMAGE_SIZE:
            raise ImageSizeException()
    return image_file


def image_validator(image_file):
    try:
        validate_image_format(image_file)
        validate_image_size(image_file)
    except ImageFormatException:
        return "Зображення має неправильний формат.Перевірте,будь ласка формат зображення"
    except ImageSizeException:
        return "Зображення має надто великий об'єм. Максимальний розмір файлу - 10 МБ"
    return True


