from django.contrib import admin

# Register your models here.
from .models import Cliente, Tipo, Producto, Pedido


#metodo que me permite listar todos los productos en admin
class ClienteAdmin(admin.ModelAdmin):
      list_display=("nro_doc","tipo_doc","nombre_completo","fecha_nac","genero","telefono","email","pasword","direccion","ofertas")
      search_fields=("nro_doc",)
      list_filter=("tipo_doc",)  

class TipoAdmin(admin.ModelAdmin):
      list_display=("id","descripcion")
      search_fields=("id",)
      list_filter=("descripcion",)  

class ProductoAdmin(admin.ModelAdmin):
      list_display=("id","nombre","descripcion","url","precio","cod_tipo")
      search_fields=("id",)
      list_filter=("cod_tipo",) 

class PedidoAdmin(admin.ModelAdmin):
      list_display=("fec_prestamo","fec_devolucion","cod_prod","cod_cliente")
      search_fields=("id",)
      date_hierarchy="fec_prestamo"



#registramos las clases en admin
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Tipo, TipoAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Pedido, PedidoAdmin)
