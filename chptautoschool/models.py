from django.db import models
from datetime import datetime


class Respond(models.Model):
    """Відгуки"""
    name = models.CharField("Ім'я", max_length=20, help_text="Введіть ваше ім'я")
    email = models.CharField("E-mail", max_length=150, unique=True, help_text="Введіть email")
    text = models.TextField("Текст відгуку", help_text="Введіть текст відгуку")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Відгук"
        verbose_name_plural = "Відгуки"


class Useful(models.Model):
    """Корисне"""
    name = models.CharField(max_length=150)
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


class ContactPhone(models.Model):
    phone = models.CharField(max_length=12)

    class Meta:
        verbose_name = "Телефон"
        verbose_name_plural = "Телефони"

    def __str__(self):
        return self.phone


class Contacts(models.Model):
    """Контакти"""
    contact_phone = models.ManyToManyField(ContactPhone, verbose_name="Контактний телефон")
    address = models.CharField(max_length=150)
    url = models.SlugField(max_length=160, unique=True)

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакти"

    def __str__(self):
        return self.name



class BaseEducation(models.Model):
    """База навчання"""
    name = models.CharField(max_length=100, default="Технікум")
    url = models.SlugField(max_length=160, unique=True)


class ClassRoom(models.Model):
    name = models.CharField(max_length=100)

    # image = models.ImageField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Клас"
        verbose_name_plural = "Класи"


class Teachers(models.Model):
    name = models.CharField(max_length=100)

    # image = models.ImageField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Викладач"
        verbose_name_plural = "Викладачі"
