import time
import os
import menu
import seleccion
activarResumen = False #variable bool con valor false
while activarResumen == False:
   menu.menu()
   carrito = seleccion.seleccion()
   aPagar = seleccion.suma(*carrito)
   print("Total a Pagar $",aPagar)
   print("Gracias por Elegirnos")
   time.sleep(6)
   os.system("clear")

#ejemplo de como crear un programa modular o por partes 
#asi cada funcion esta en su propia file y luego se importa 
#a el main.py principal

  
  

  




