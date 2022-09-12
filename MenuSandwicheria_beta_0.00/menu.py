import time


def menu():
  titulo = "-- BIENVENIDOS A LA SANDWICHERIA --"
  
  for x in range(0,len(titulo)):
    print(titulo[x],end =" ")
  print("\n\nMenu\n")
  time.sleep(0.8)
  print("  #1__Pizza Mozzarella ($25)\n")
  time.sleep(0.8)  
  print("  #2__Hamburguesa ($5)\n")
  time.sleep(0.8)
  print("  #3__Empanadas ($2)\n")
  time.sleep(0.8)
  print("  #4__Enviar Pedido\n")
  time.sleep(0.8)
   

