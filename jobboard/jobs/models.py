from django.db import models

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    salary_type = models.CharField(max_length=10, choices=[('mensal', 'Mensal'), ('anual', 'Anual')])
    prerequisites = models.TextField()

    def __str__(self):
        return self.title