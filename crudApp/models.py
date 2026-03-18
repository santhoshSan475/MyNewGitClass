from django.db import models

# Create your models here.


class StudentModel(models.Model):
    admissionNo = models.IntegerField()
    studentName = models.CharField(max_length=200)
    department = models.CharField(max_length=150)
    gender = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.studentName

