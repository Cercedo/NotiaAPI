from django.db import models
from django.utils import timezone

from .params import VL_PATH_DATETIME_FORMAT


def get_background_image_path(instance: models.Model, filename: str) -> str:
    formatted_today_str = timezone.now().strftime(VL_PATH_DATETIME_FORMAT)
    return f"images/note/{formatted_today_str}/{instance.pk}_{filename}"
