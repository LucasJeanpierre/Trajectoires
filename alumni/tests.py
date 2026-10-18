# Create your tests here.

from django.test import TestCase
from django.urls import reverse

from .models import Alumnus, StudyStage


class AlumniPagesTests(TestCase):
    def setUp(self):
        self.alumnus = Alumnus.objects.create(
            first_name="John",
            last_name="Doe",
            graduation_year=2020,
            status=Alumnus.Status.APPROVED,
        )
        self.stages = [
            StudyStage.objects.create(
                alumnus=self.alumnus,
                program="Preparatory class",
                institution="Central High School",
                start_year=2020,
                end_year=2022,
            ),
            StudyStage.objects.create(
                alumnus=self.alumnus,
                program="Engineering degree",
                institution="Technical University",
                start_year=2022,
            ),
        ]

    def test_alumni_list_displays_alumnus(self):
        response = self.client.get(reverse("alumni:list"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.alumnus.first_name)
        self.assertContains(response, self.alumnus.last_name)
        self.assertContains(response, str(self.alumnus.graduation_year))
        self.assertContains(
            response,
            reverse("alumni:detail", kwargs={"pk": self.alumnus.pk}),
        )

    def test_alumnus_detail_displays_all_study_stages(self):
        response = self.client.get(
            reverse("alumni:detail", kwargs={"pk": self.alumnus.pk})
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.alumnus.first_name)
        self.assertContains(response, self.alumnus.last_name)
        for stage in self.stages:
            self.assertContains(response, stage.program)
            self.assertContains(response, stage.institution)
            self.assertContains(
                response, f"{stage.start_year} - {stage.end_year or 'ongoing'}"
            )
