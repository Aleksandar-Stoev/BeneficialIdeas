from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import UploadedFile
from django.utils.deconstruct import deconstructible

@deconstructible
class FileSizeValidator:
    def __init__(self, max_size_mb=2, message=None):
        self.max_size_mb = max_size_mb
        self.message = message or f"File size must be less than {self.max_size_mb}MB!"

    def __call__(self, file: UploadedFile):
        if file.size > self.max_size_mb * 1024 * 1024:
            raise ValidationError(self.message)
