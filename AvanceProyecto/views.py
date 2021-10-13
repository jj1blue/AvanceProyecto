from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader 
import datetime

def producto1(request):
   return render(request, "producto1.html")
   
def saludo(request):
   nombre = "El juan"
   apelldo = "Miranda"
   docext = open ("C:\Users\javie\Internet avanzado\MiPrimerPrayecto\MiPrimerPrayecto\miplantilla.html")
   plt = Template(docext.read())
   docext.close()
   
   ctx = Context({"nombre_persona": nombre, "apellido_persona": apelldo})
   
   documento = plt.render(ctx)
   return(HttpResponse(documento))

def damefecha(request):
   fecha_actual=datetime.datetime.now()
   documento1 = """
               <html>
               <body>
               <h1>
               Fecha y hora actuales %s
               </h1>
               </body>
               </html>
               """ %fecha_actual
   return HttpResponse(documento1)

def calcularedad(request,anio):
    edadActual = 18
    periodo = anio - 2021
    edadFutura = edadActual + periodo
    documento = """
               <html>
               <body>
               <h1>
               En el año %s tendras %s años
               </h1>
               </body>
               </html>
               """ %(anio , edadFutura); return HttpResponse(documento)