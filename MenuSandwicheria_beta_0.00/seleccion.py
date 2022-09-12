import os

def seleccion():
  
  salida = 0
  pedido = [0,0,0]
  
  while salida == 0:
       x = int(input("Elegir una opcion: "))
       if x == 1:
          pedido[x-1] = pedido[x-1] + 1
       elif x == 2:
          pedido[x-1] = pedido[x-1] + 1 
       elif x == 3:
          pedido[x-1] = pedido[x-1] + 1
       elif x == 4:
         salida = 1
       
         
       
  pedido[0] *= 25
  pedido[1] *= 5
  pedido[2] *= 2
  os.system("clear")
  return pedido

def suma(x,y,z):
  return (x + y + z)


  
  