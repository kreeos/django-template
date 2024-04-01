from django.db import models

class SampleModel(models.Model):
    text = models.CharField(max_length=30)

    class Meta:
        db_table = 'sample_model'
        verbose_name = 'Sample Model'
        verbose_name_plural = 'Sample Models'
