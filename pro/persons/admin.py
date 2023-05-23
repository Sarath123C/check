from django.contrib import admin

# Register your models here.
from persons.models import Department, Person, Course,Purpose

admin.site.register(Course)
admin.site.register(Department)
admin.site.register(Purpose)
admin.site.register(Person)


