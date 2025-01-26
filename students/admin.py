from django.contrib import admin
from .models import Student, Course

# Student modeli uchun admin panelni sozlash
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'age', 'grade')  # Ko'rsatiladigan ustunlar
    search_fields = ('first_name', 'last_name', 'grade')  # Qidiruv uchun ustunlar
    list_filter = ('age', 'grade')  # Filtrlar
    ordering = ('id',)  # Tartanlash bo'yicha

# Course modeli uchun admin panelni sozlash
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')  # Ko'rsatiladigan ustunlar
    search_fields = ('name',)  # Qidiruv uchun ustunlar
    filter_horizontal = ('students',)  # Many-to-Many maydonni boshqarish

