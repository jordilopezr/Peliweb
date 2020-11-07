from django.test import TestCase
from app.models import Tipo, Producto


class PorcionesTestCase(TestCase):
     def setUp(self):
        tipo1 = Tipo.objects.createt(id=1,descripcion="Accion")
        Producto.objects.create(id = 3, nombre="Crodds",descripcion ="Peli infantil",url=".",href=".",precio=5000,cod_tipo=tipo1)


def test_Producto_tipo(self):
      Productos1 = Producto.objects.get(id=1)
      self.assertEqual(Productos1.cod_tipo.descripcion,"Accion")  

def test_Producto_precio(self):
       Productos2 = Producto.objects.get(id=1)
       self.assertEqual(Productos2.precio*3,10000)