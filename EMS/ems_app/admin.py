from django.contrib import admin

# Register your models here.
from .models import Employee




# @admin.register(Student)
class StaffAdmin(admin.ModelAdmin):
     fields = [
            "name",
            "age",
            "gender",
            "joining_date",
            "designation",
            "place",
            "contact_no",
            "education"
        ]

admin.site.register(Employee, StaffAdmin)