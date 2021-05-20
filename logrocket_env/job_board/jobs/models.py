from django.db import models

class Job(models.Model):
    title = models.CharField("Title", max_length=50)
    contactPhone = models.CharField("Contact Phone", max_length=13)
    contactEmail = models.EmailField("Contact Email", max_length=20)
    description = models.CharField("Description", max_length=750)
    posterName = models.CharField("Poster Name", max_length=25)
    postingDate = models.DateField("Posting Date", auto_now_add=True)

    def __str__(self):
        return self.title