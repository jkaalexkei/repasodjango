from django.http import HttpResponse

from django.shortcuts import render
from django.contrib.auth import authenticate#permite autenticar usuarios y conocer si este existe en la BD

from django.contrib.auth import login,logout


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
            
            print('usuario autenticado')
        else:
            print('usuario no autenticado')
            
        
    
    return render(request,'usuarios/login.html',{
        
        
    })
