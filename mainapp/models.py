from django.db import models

# Create your models here.

class School(models.Model):
    logo= models.ImageField (upload_to="image/",null=True, blank=True)
    whatsapp=models.URLField(verbose_name='Вотсап',null=True, blank=True)
    twitter= models.URLField(verbose_name='Твиттер',null=True, blank=True)
    facebook= models.URLField(verbose_name='Фейсбук',null=True, blank=True)
    name= models.CharField(max_length=120,verbose_name='Название',null=True, blank=True)
    description= models.TextField(verbose_name='Описание',null=True, blank=True)
    admissiontouniversity= models.CharField(max_length=120,verbose_name='Поступлений в Университет',null=True, blank=True)
    staff = models.CharField(max_length=120, verbose_name='Сотрудников',null=True, blank=True)
    students = models.PositiveIntegerField(verbose_name='Количествое учеников',null=True, blank=True)
    successworkyear= models.CharField(max_length=120,verbose_name='Успешных лет',null=True, blank=True)
    mail= models.URLField(verbose_name='Почта')
    address=models.CharField(max_length=120,verbose_name= 'Адрес')
    number=models.PositiveIntegerField(verbose_name='Номер')
    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name='Школа'
        verbose_name_plural='Школы'

class Teacher(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='teachers')
    position= models.CharField(max_length=120,verbose_name='Должность')
    name= models.CharField(max_length=120,verbose_name='Имя')
    photo  = models.ImageField(upload_to="image/",verbose_name='Фото')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name='Учитель'
        verbose_name_plural = 'Учителя'

class Galeria(models.Model):
    school = models.ForeignKey(School,on_delete=models.CASCADE,related_name='galleries')
    photo = models.ImageField(upload_to='image/')
    name = models.CharField(max_length=127,verbose_name='название',null=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галереи'


class Rewiew(models.Model):
    photo = models.ImageField(upload_to='image/')
    name = models.CharField(max_length=127,verbose_name='название',null=True)
    parent = models.CharField(max_length=127,verbose_name='родитель')
    description = models.TextField(verbose_name='описание')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = verbose_name + 'ы'


class News(models.Model):
    school = models.ForeignKey(School,on_delete=models.CASCADE,related_name='news')
    author = models.CharField(max_length=127,verbose_name='автор')
    created_at = models.DateField(auto_now_add=True,verbose_name='Дата создание')
    description = models.TextField(verbose_name='описание')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'