from django.db import models


class Camp(models.Model):
    class Meta:
        verbose_name = "Лагерь"
        verbose_name_plural = "Лагеря"

    camp_id = models.AutoField(verbose_name='ID лагеря', primary_key=True, unique=True)
    name = models.CharField(verbose_name='Название лагеря', max_length=255)
    geography = models.TextField(verbose_name='Расположение лагеря')

    def __str__(self):
        return str(self.name)


class Instructor(models.Model):
    class Meta:
        verbose_name = "Инструктор"
        verbose_name_plural = "Инструкторы"

    instructor_id = models.AutoField(verbose_name='ID инструктора', primary_key=True, unique=True)
    fio = models.CharField(verbose_name='ФИО инструктора', max_length=255)
    experience = models.IntegerField(verbose_name='Опыт работы инструктора')

    def __str__(self):
        return str(self.fio)


class Tourist(models.Model):
    class Meta:
        verbose_name = "Турист"
        verbose_name_plural = "Туристы"

    tourist_id = models.AutoField(verbose_name='ID туриста', primary_key=True, unique=True)
    camp_id = models.ForeignKey(Camp, verbose_name='ID лагеря', on_delete=models.SET(-1))
    instructor_id = models.ForeignKey(Instructor, verbose_name='ID инструктора', on_delete=models.SET(-1))
    i_name = models.CharField(verbose_name='Имя туриста', max_length=255)
    f_name = models.CharField(verbose_name='Фамилия туриста', max_length=255)
    o_name = models.CharField(verbose_name='Отчество туриста', max_length=255)
    birth = models.DateField(verbose_name='Дата рождения туриста', max_length=255)

    def __str__(self):
        return f"Турист - {self.f_name} {self.i_name}"
