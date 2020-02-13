from django.db import models
from datetime import datetime


class Respond(models.Model):
    """Відгуки"""
    name = models.CharField("Ім'я", max_length=20)
    email = models.CharField("E-mail", max_length=150, unique=True)
    text = models.TextField("Текст відгуку")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Відгук"
        verbose_name_plural = "Відгуки"


class Useful(models.Model):
    """Корисне"""
    category = models.TextField()
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name


class DriversCourses(models.Model):
    """Курси водіїв"""
    docs = models.TextField("Необхідні документи")
    category = models.CharField("Категорії навчання", max_length=2)
    program = models.TextField("Програма навчання")
    url = models.SlugField(max_length=160, unique=True)

    class Leasson:
        name = models.TextField("Назва лекції")
        date = models.DateTimeField("Дата та час проведення", default=datetime.today)

    def __str__(self):
        return self.name


class Contacts(models.Model):
    """Контакти"""
    contact_phone = models.SlugField(max_length=12)
    address = models.CharField(max_length=150)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name


class BaseEducation(models.Model):
    """База навчання"""
    name = "Технікум"
    url = models.SlugField(max_length=160, unique=True)

    class ClassRoom:
        name = models.CharField()
        image = models.ImageField()

        class Meta:
            verbose_name = "Клас"
            verbose_name_plural = "Класи"

    class Teachers:
        name = models.CharField()
        image = models.ImageField()

        class Meta:
            verbose_name = "Викладач"
            verbose_name_plural = "Викладачі"

    def __str__(self):
        return self.name
