from django.db import models

# Create your models here.

class Phone(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    OS_version = models.CharField(max_length=50)
    RAM = models.IntegerField()
    internal_memory_capacity = models.IntegerField()
    ppi = models.IntegerField()
    processor = models.CharField(max_length=50)
    image_size = models.CharField(max_length=50)
    number_cameras = models.IntegerField()

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Phone'
        verbose_name_plural = 'Phones'

class Samsung(models.Model): 
    phone_id = models.ForeignKey("Phone", on_delete=models.CASCADE, null=True, blank=True)
    top_android = models.CharField(max_length=50)

    def __str__(self):
        return f'Samsung phone_id={self.phone_id}'

    class Meta:
        verbose_name = 'Samsung'
        verbose_name_plural = 'Samsung'

class Xiaomi(models.Model): 
    phone_id = models.ForeignKey("Phone", on_delete=models.CASCADE, null=True, blank=True)
    quality_price = models.CharField(max_length=50)

    def __str__(self):
        return f'Xiaomi phone_id={self.phone_id}'

    class Meta:
        verbose_name = 'Xiaomi'
        verbose_name_plural = 'Xiaomi'

class Apple(models.Model): 
    phone_id = models.ForeignKey("Phone", on_delete=models.CASCADE, null=True, blank=True)
    optimization = models.CharField(max_length=50)

    def __str__(self):
        return f'Apple phone_id={self.phone_id}'

    class Meta:
        verbose_name = 'Apple'
        verbose_name_plural = 'Apple'
