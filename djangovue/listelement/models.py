from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Título')
    url_clean = models.CharField(max_length=255, verbose_name='URL')
    
    class Meta:
        verbose_name = ("Categoría")
        verbose_name_plural = ("Categorias")

    def __str__(self):
        return self.title

class Type(models.Model):
    title = models.CharField(max_length=255, verbose_name='Título')
    url_clean = models.CharField(max_length=255, verbose_name='URL')    

    class Meta:
        verbose_name = ("Tipado")
        verbose_name_plural = ("Tipados")

    def __str__(self):
        return self.title

class Element(models.Model):
    title = models.CharField(max_length=255, verbose_name='Título')
    url_clean = models.CharField(max_length=255, verbose_name='URL')
    description = models.TextField(verbose_name='Descripción')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Elemento")
        verbose_name_plural = ("Elementos")

    def __str__(self):
        return self.title
