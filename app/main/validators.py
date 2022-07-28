from django.core.exceptions import ValidationError


def image_size_validator(file):
    image_size = 500

    if file.size > image_size * 1024:
        raise ValidationError("Image Size Could not be Greater than {}".format(image_size))