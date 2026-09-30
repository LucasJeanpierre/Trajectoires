from django.db import models

# Create your models here.


class Alumnus(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    graduation_year = models.PositiveIntegerField()

    class Meta:
        verbose_name = "alumnus"
        verbose_name_plural = "alumni"
        ordering = ["-graduation_year", "last_name", "first_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.graduation_year})"
