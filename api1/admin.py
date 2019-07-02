from django.contrib import admin
from info.models import Student,Teacher,Department, StudentFee,TecaherInfo,AssignTeacher
admin.site.register(Student)
admin.site.register(StudentFee)
admin.site.register(Department)
admin.site.register(Teacher)
admin.site.register(TecaherInfo)
# Register your models here.
