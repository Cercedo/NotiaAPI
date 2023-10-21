from importlib import import_module

from dependency_injector.containers import DeclarativeContainer
from django.apps import AppConfig
from django.utils.module_loading import module_has_submodule

MODELS_MODULE_NAME = "infrastructure.orms.models"


class NoteConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "note"
    container: DeclarativeContainer

    def import_models(self):
        super().import_models()

        is_module_package = module_has_submodule(
            self.module, MODELS_MODULE_NAME
        )
        if is_module_package:
            models_module_name = f"{self.name}.{MODELS_MODULE_NAME}"
            self.models_module = import_module(models_module_name)  # type: ignore

    def ready(self) -> None:
        from note.infrastructure.configs import Container

        self.container = Container()
