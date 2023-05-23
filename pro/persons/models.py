from django import forms

from django.db import models
from multiselectfield import MultiSelectField


class Department(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Course(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Purpose(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


# class Materials(models.Model):
#     pen = models.BooleanField('pen', default=False)
#     note_book = models.BooleanField('note book', default=False)
#     exam_paper = models.BooleanField('exam paper', default=False)

# def __str__(self):
#     return self.name


# class Gender(models.Model):
#     GEN_CHOICES = (('M', 'Male'), ('F', 'Female'),)
#     gender = MultiSelectField(max_length=40, choices=GEN_CHOICES)
#
#
# class Materials_Required(models.Model):
#     M_REQUIRED = (('dnb', 'Debit Note Book'), ('pen', 'Pen'), ('ep', 'Exam_Papers'),)
#     materials_required = MultiSelectField(max_length=40, choices=M_REQUIRED)


class Person(models.Model):
    name = models.CharField(max_length=124)
    Date_Of_Birth = models.DateField()
    age = models.IntegerField()
    male = models.BooleanField('Male',  default=False)
    female = models.BooleanField('Female', default=False)
    # gender = models.ForeignKey(Gender,max_length=0, on_delete=models.SET_NULL, blank=True, null=True)
    phone_number = models.IntegerField()
    email = models.EmailField(max_length=200)
    address = models.TextField(max_length=300)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, blank=True, null=True)
    Purpose = models.ForeignKey(Purpose, on_delete=models.SET_NULL, blank=True, null=True)
    pen = models.BooleanField('Pen', default=False)
    note = models.BooleanField('Note Book', default=False)
    paper = models.BooleanField('Exam Paper', default=False)
    # materials_required = models.ForeignKey(Materials_Required,max_length=0, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name
