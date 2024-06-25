from django.db import models
from parler.models import TranslatableModel, TranslatedFields


class Product(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=200),
        description=models.TextField()
    )

    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
