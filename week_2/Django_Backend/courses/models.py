from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    head_of_dept = models.CharField(max_length=100)
    budget = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    credits = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
