from django.db import models

# Create your models here.


class BacSeries(models.Model):
    name = models.CharField(max_length=100, unique=True)
    period = models.CharField(
        max_length=100,
        blank=True,
        help_text='E.g. "since 2021", "1995-2020", "before 1995".',
    )
    display_order = models.PositiveIntegerField(
        default=0,
        help_text="Display order (e.g. most recent series first).",
    )

    class Meta:
        verbose_name = "bac series"
        verbose_name_plural = "bac series"
        ordering = ["display_order", "name"]

    def __str__(self):
        return f"{self.name} ({self.period})" if self.period else self.name


class Alumnus(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    graduation_year = models.PositiveIntegerField(verbose_name="graduation year")
    bac_series = models.ForeignKey(
        BacSeries,
        on_delete=models.PROTECT,
        related_name="alumni",
        null=True,
        blank=True,
        help_text="Temporarily optional: no reference data is seeded yet.",
    )

    class Meta:
        verbose_name = "alumnus"
        verbose_name_plural = "alumni"
        ordering = ["-graduation_year", "last_name", "first_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.graduation_year})"
