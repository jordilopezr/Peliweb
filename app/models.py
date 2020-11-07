from django.db import models

# Create your models here.
class Cliente(models.Model):
        nro_doc = models.CharField(max_length=20, primary_key=True)
        tipo_doc = models.CharField(max_length=20)
        nombre_completo = models.CharField(max_length=50) 
        fecha_nac = models.DateField(max_length=20)                
        genero = models.CharField(max_length=20)
        telefono = models.IntegerField(default=0) 
        email = models.EmailField(max_length=50)
        pasword = models.CharField(max_length=10)
        direccion = models.CharField(max_length=250) 
        ofertas = models.BooleanField(max_length=1)

        def __str__(self):
            return self.nro_doc


class Tipo(models.Model):
        id = models.IntegerField(primary_key=True)
        descripcion = models.CharField(max_length=50)

        def __str__(self):
            return self.descripcion
        
    
class Producto(models.Model):
        id = models.IntegerField(primary_key=True)
        nombre = models.CharField(max_length=50)
        descripcion = models.CharField(max_length=250)
        url = models.CharField(max_length=100)
        href = models.CharField(max_length=100)
        precio = models.FloatField(max_length=20)
        cod_tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)

        def __str__(self):
            return self.nombre


class Pedido(models.Model):       
        fec_prestamo = models.DateField(max_length=20)
        fec_devolucion = models.DateField(max_length=20)       
        cod_prod = models.ForeignKey(Producto, on_delete=models.CASCADE)        
        cod_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)  







        
