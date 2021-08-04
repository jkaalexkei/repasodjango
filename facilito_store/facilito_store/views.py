# from django.http import HttpResponse


from django.shortcuts import redirect, render
from django.contrib.auth import authenticate#permite autenticar usuarios y conocer si este existe en la BD

from django.contrib.auth import login,logout

from django.contrib import messages
from .forms import FormularioRegistro

# def index(request):
# #el parametro request es obligatorio
#     mensaje = 'información del archivo<h1 style="color:blue;">views.py</h1>'

#     return HttpResponse(mensaje)


def index(request):#el parametro request es obligatorio
    
  
    
    return render(request,'index.html',{
        
        #este diccionario hace referencia a un contexto
        #admite cualquier tipo de dato string, enteros, booleanos, listas, tuplas, diccionarios
        #se puede definir N cantidad de valores de la manera clave:valor
        
        # 'mensaje':'soy el texto de la variable mensaje del archivo views.py'
        
        
        
        'titulo':'productos',
   
        
        'productos':[
            
            #esto es una lista de diccionarios
            {'titulo':'laptop','precio':20,'stock':True},
            {'titulo':'mouse','precio':30,'stock':False},
            {'titulo':'teclado','precio':40,'stock':True},
            {'titulo':'imipresora','precio':50,'stock':False},
            
        ]
        
    })


def iniciodesesion(request):
    
    if request.method=='POST':
        #creamos dos variables usuario y clave para capturar esa informacion
        
        usuario=request.POST.get('username')#el metodo get retorna un valor
        clave=request.POST.get('password')
        
        #luego que se capturan los datos se procede a realizar la autenticacion
        
        user = authenticate(username=usuario,password=clave)
        #si retorna un usuario se almacena en la variable de lo contrario devuelve None
        
        if user:
            login(request,user)#la funcion login recibe como parametros la peticion y el usuario
            
            messages.success(request,'Bienvenido {}'.format(user.username))
            #mediante esta instruccion podemos enviar un mensaje al cliente bien sea de confirmacion o de error
            
            return redirect ('inicio')#la funcion redirect permite redirigir a un template en particular
        else:
            messages.error(request,'Usuario no valido')
            
    
    return render(request,'usuarios/login.html',{
        
        
    })


def cerrarsesion(request):
    
    logout(request)#la funcion logout requiere como argumento la peticion que mantiene la sesion iniciada
    
    messages.success(request,'Haz finalizado la sesión correctamente ')
    
    return redirect('login')


def registro(request):
    
    formulario = FormularioRegistro({
        #si se quiere que la instancia del formulario se inicialice con valores por defecto se hace mediante un diccionario donde las claves del mismo es el nombre de los campos
        
        'username':'alexander',
        'email':'jkaalexkei@gmail.com',
        
    })
    
    if request.method=='POST':
        pass
    
    return render(request,'usuarios/registro.html',{
        
        'formulario':formulario
    })