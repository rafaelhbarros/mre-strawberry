import functools
import uuid
from typing import Type, cast

from django.db import models


UUIDField = cast(
    Type[models.UUIDField],
    functools.partial(
        models.UUIDField,
        default=uuid.uuid4,
        editable=False,
        unique=True,
    ),
)

class Recording(models.Model):
    uuid = UUIDField()
    participant = models.CharField(max_length=128)
    host = models.CharField(max_length=128)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    expiration = models.DateTimeField()
