from django.db import models

# Create your models here.

# Identificar los elementos de la tabla
class Wishlist(models.Model):
    id= models.AutoField(primary_key=True) 
    title = models.CharField(max_length=200, verbose_name="Titulo") # Titulo de la lista
    image = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name="Imagen") # Imagen de la lista
    description = models.TextField(null=True, blank=True, verbose_name="Descripcion") # Descripcion de la lista

    # Mostrar titulo y descripcion en el admin 
    def __str__(self):
        fila = "Titulo: " + self.title + " | descripcion: " + self.description
        return fila
    
     # Eliminar contenido
    def delete(self, using=None, keep_parents=False):
       
        if self.image:
            self.image.storage.delete(self.image.name)
        super().delete(using, keep_parents)