from wq.db import rest
from .models import FileModel

rest.router.register_model(
    FileModel,
    fields="__all__",
)