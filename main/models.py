from django.db import models

# Create your models here.


class Electronic(models.Model):

    COLORS = [
        ('red', 'red'),
        ('blue', 'blue'),
        ('black', 'black'),
        ('white', 'white'),
    ]

    brand = models.CharField('Electronic brand', max_length=30)
    name = models.CharField('Electronic name', max_length=40)
    price = models.PositiveIntegerField('Electronic price')
    discount_price = models.PositiveIntegerField('Electronic discount price')
    description = models.TextField('Electronic description')
    image = models.ImageField('Electronic image', upload_to='products')
    date = models.DateTimeField(auto_now=True)
    color = models.CharField(choices=COLORS, max_length=60)

    def __str__(self):
        return self.name


