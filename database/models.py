from django.db import models


# One-to-Many
class Department(models.Model):

    name = models.CharField(
        max_length=100,
        unique=True
    )

    location = models.CharField(
        max_length=100
    )

    def __str__(self):
        return self.name


class Project(models.Model):

    name = models.CharField(
        max_length=100
    )

    deadline = models.DateField()

    def __str__(self):
        return self.name


class Employee(models.Model):

    name = models.CharField(
        max_length=100
    )

    email = models.EmailField(
        unique=True
    )

    salary = models.IntegerField()

    joining_date = models.DateField()

    # One-to-Many
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='employees'
    )

    # Many-to-Many
    projects = models.ManyToManyField(
        Project,
        related_name='employees'
    )

    def __str__(self):
        return self.name


# One-to-One
class EmployeeProfile(models.Model):

    employee = models.OneToOneField(
        Employee,
        on_delete=models.CASCADE,
        related_name='profile'
    )

    phone_number = models.CharField(
        max_length=15
    )

    address = models.TextField()

    emergency_contact = models.CharField(
        max_length=15
    )

    def __str__(self):
        return self.employee.name