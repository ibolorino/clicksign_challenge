from django.core.exceptions import ValidationError
from django.db import models


class Folder(models.Model):
    name = models.SlugField("Nome da Pasta", max_length=255)
    level = models.IntegerField("Nível da Pasta", editable=False)
    parent_folder = models.ForeignKey(
        "Folder",
        verbose_name="Pasta mãe",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.full_path}"

    @property
    def full_path(self):
        path = f"{self.name}/"
        if self.parent_folder:
            path = self.parent_folder.full_path + path
        return path

    def clean(self):
        parent_folder = self.parent_folder
        self.level = 0
        if parent_folder:
            self.level = parent_folder.level + 1
        if Folder.objects.filter(name=self.name, level=self.level).exists():
            raise ValidationError("Folder already exists")
