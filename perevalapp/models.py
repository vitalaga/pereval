from django.db import models


class Users(models.Model):
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=15, blank=True)
    fam = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    otc = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f'{self.fam} {self.name} {self.otc}'


class PerevalAdded(models.Model):
    NEW = 'new'
    PENDING = 'pending'
    ACCEPTED = 'accepted'
    REJECTED = 'rejected'

    STATUS = [
        ('new', 'новый'),
        ('pending', 'на проверке'),
        ('accepted', 'одобрено'),
        ('rejected', 'информация не принята')
    ]
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='user')
    coords = models.ForeignKey('Coords', on_delete=models.CASCADE, blank=True, null=True)
    level = models.ForeignKey('Level', on_delete=models.CASCADE, blank=True, null=True)
    beauty_title = models.CharField(max_length=255, verbose_name='Тип препятствия', blank=True, null=True)
    title = models.CharField(max_length=255, verbose_name='Название', blank=True, null=True)
    other_titles = models.CharField(max_length=255, verbose_name='Другое название', blank=True, null=True)
    connect = models.TextField(blank=True, null=True)
    add_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS, default=NEW)

    def __str__(self):
        return f'{self.pk} {self.beauty_title}'

    class Meta:
        verbose_name = 'Перевал'
        verbose_name_plural = 'Перевалы'


class Coords(models.Model):
    latitude = models.FloatField(verbose_name="Широта", blank=True, null=True)
    longitude = models.FloatField(verbose_name="Долгота", blank=True, null=True)
    height = models.FloatField(verbose_name="Высота", blank=True, null=True)

    def __str__(self):
        return f"широта: {self.latitude}, долгота: {self.longitude}, высота: {self.height}"

    class Meta:
        verbose_name = 'Координаты'
        verbose_name_plural = 'Координаты'


class Level(models.Model):
    winter = models.CharField(max_length=10, verbose_name='Зима', blank=True, null=True)
    summer = models.CharField(max_length=10, verbose_name='Лето', blank=True, null=True)
    autumn = models.CharField(max_length=10, verbose_name='Осень', blank=True, null=True)
    spring = models.CharField(max_length=10, verbose_name='Весна', blank=True, null=True)

    def __str__(self):
        return f'Зима: {self.winter}, лето: {self.summer}, осень: {self.autumn}, весна: {self.spring}'

    class Meta:
        verbose_name = 'Уровень сложности'
        verbose_name_plural = 'Уровени сложности'


class Images(models.Model):
    pereval = models.ForeignKey(PerevalAdded, on_delete=models.CASCADE, related_name='images', blank=True, null=True)
    image = models.ImageField(upload_to='images/', verbose_name='Изображение', blank=True, null=True)
    title = models.CharField(max_length=255, verbose_name="Название", blank=True, null=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'id: {self.pk}, title:{self.title}'

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


