RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m' 
RESET = '\033[39m'

import random
import time

print(BLUE+"BIENVENIDOS A MI TRIVIA"+RESET)

#VARIABLES
nombre = input("\nCuál es tu nombre: ")
puntaje = random.randint(0, 10)
time.sleep(0.5)

#ELIGE UNA OPCION
print(CYAN+"\nHola",nombre,"elige una opción: "+RESET)
time.sleep(0.5)
print(GREEN+"""
      1) Historia     3) Deportes
      2) Programacion        4) Cultura General...
      """+RESET)

#INSTRUCCIONES
print(MAGENTA+"Seleccione un numero de las opciones mostradas y luego presione enter para poder acceder a la trivia asignada"+RESET
)
time.sleep(1)
eligio = int(input(CYAN+"\nSelecciona una opcion: "+RESET))
print("\n")
for numero_carga in range(5, 0, -1):
  print(CYAN+"cargando preguntas..."+RESET)
  time.sleep(1)

print(MAGENTA+"\nTu puntaje inicial sera de", puntaje,"puntos. Mucha suerte",nombre+"!!!"+RESET)

while(eligio>0):
######################################################################################
      if eligio == 1:
        print(YELLOW+"\nEmpecemos nuestra Trivia de Historia"+RESET)
        time.sleep(1)
#------------------------------------------------------------------------------------#
        #PRIMERA PREGUNTA
        print("\n1) Cuantos departamentos constituyen el territorio peruano ")
        time.sleep(0.5)     
        #ALTERNATIVAS
        altern_0 = ["a)", "b)", "c)", "d)"]
        altern_1 = [24, 20, 25, 23]
        for number in range (0, 4):
          print(" ",altern_0[number],altern_1[number],"departamentos") 
          time.sleep(0.5)
        #INGRESAR RESPUESTA
        print(BLUE+"\n Ingrese solamente la letra de las alternativas mostradas"+RESET)
        respuesta_1 = input("\n Ingresa respuesta: ")
        while respuesta_1 not in ("a", "b", "c", "d", "x"):
          respuesta_1 = input("\n Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
        #VALIDACION DE RESPUESTA
        respuestas = ["a", "b", "c", "d", "x"]
        if respuesta_1 == respuestas[0]:
          puntaje += 10 
          print(GREEN+"\n Muy bien ", nombre," La respuesta es correcta!!, tu puntaje actual es de ", puntaje, "puntos"+RESET)
          time.sleep(2)
        elif respuesta_1 == respuestas[4]:
          puntaje +=20
          print(GREEN+"\nFelicitaciones", nombre, " obtuviste 20 puntos extra"+RESET)
          print(GREEN+"Tienes un total de ", puntaje, "puntos"+RESET)
          time.sleep(2)
        else:
          puntaje -= 5
          print(RED+"\n Respuesta Incorrecta,", nombre, "tienes", puntaje, "puntos"+RESET)
          time.sleep(2)
#------------------------------------------------------------------------------------#
        #SEGUNDA PREGUNTA
        print("\n2) Quien fue el ultimo soberano inca ? ")
        time.sleep(0.5)
        #ALTERNATIVAS
        altern_0 = ["a)", "b)", "c)", "d)"]
        altern_1 = ["Pachacutec", "Manco Capac", "Atahualpa", "Mayta Capac"]
        for number in range (0, 4):
          print(" ",altern_0[number],altern_1[number]) 
          time.sleep(0.5)
        #INGRESAR RESPUESTA
        print(BLUE+"\n Ingrese solamente la letra de las alternativas mostradas"+RESET)
        respuesta_1 = input("\n Ingresa respuesta: ")
        while respuesta_1 not in ("a", "b", "c", "d", "x"):
          respuesta_1 = input("\n Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

        #VALIDACION DE RESPUESTA
        respuestas = ["a", "b", "c", "d", "x"]
        if respuesta_1 == respuestas[2]:
          puntaje += 10 
          print(GREEN+"\n Muy bien ", nombre," La respuesta es correcta!!, tu puntaje actual es de ", puntaje, "puntos"+RESET)
          time.sleep(2)
        elif respuesta_1 == respuestas[4]:
          puntaje +=20
          print(GREEN+"\nFelicitaciones", nombre, " obtuviste 20 puntos extra"+RESET)
          print(GREEN+"Tienes un total de ", puntaje, "puntos"+RESET)
          time.sleep(2)
        else:
          puntaje -= 5
          print(RED+"\n Respuesta Incorrecta,", nombre, "tienes", puntaje, "puntos"+RESET)
          time.sleep(2)
#-----------------------------------------------------------------------------------# 
        #TERCERA PREGUNTA
        print("\n3) En que año se proclamo la independencia del Peru ")
        time.sleep(0.5)
        #ALTERNATIVAS
        altern_0 = ["a)", "b)", "c)", "d)"]
        altern_1 = [1832, 1920, 1848, 1821]
        for number in range (0, 4):
          print(" ",altern_0[number],altern_1[number]) 
          time.sleep(0.5)
        #INGRESAR RESPUESTA
        print(BLUE+"\n Ingrese solamente la letra de las alternativas mostradas"+RESET)
        respuesta_1 = input("\n Ingresa respuesta: ")
        while respuesta_1 not in ("a", "b", "c", "d", "x"):
          respuesta_1 = input("\n Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
      
        #VALIDACION DE RESPUESTA
        respuestas = ["a", "b", "c", "d", "x"]
        if respuesta_1 == respuestas[3]:
          puntaje += 10 
          print(GREEN+"\n Muy bien ", nombre," La respuesta es correcta!!, tu puntaje actual es de ", puntaje, "puntos"+RESET)
          time.sleep(2)
        elif respuesta_1 == respuestas[4]:
          puntaje +=20
          print(GREEN+"\nFelicitaciones", nombre, " obtuviste 20 puntos extra"+RESET)
          print(GREEN+"Tienes un total de ", puntaje, "puntos"+RESET)
          time.sleep(2)
        else:
          puntaje -= 5
          print(RED+"\n Respuesta Incorrecta,", nombre, "tienes", puntaje, "puntos"+RESET)
          time.sleep(2)
#......................................................................................#
        #RULETA DE LA SUERTE        
        print(GREEN+"\nRULETA DE LA SUERTE\n"+RESET)
        
        for ruleta in range(50,random.randint(15, 45), -random.randint(2, 5)):
          print(ruleta)
          time.sleep(0.5)
        puntaje+=ruleta
        print(GREEN+"\nTu puntaje total sera de ",puntaje," puntos"+RESET)
          
        #DESEAS VOLVER A JUGAR
        volver_jugar=input("\nDeseas volver a jugar? Escriba un 'si' para continuar en caso contrario presione cualquier otra tecla: ")
        if(volver_jugar=="si"):
          time.sleep(0.5)
          print(CYAN+"\nEscoja una opcion nuevamente"+RESET)
          time.sleep(0.5)
          print(GREEN+"""
      1) Historia     3) Deportes
      2) Programacion        4) Cultura General...
      """+RESET)
          time.sleep(0.5)
          eligio = int(input("\nIngrese la opcion que desee jugar: "))
          puntaje = random.randint(0, 10)
          print("\n")
          for numero_carga in range(5, 0, -1):
            print(CYAN+"cargando preguntas..."+RESET)
            time.sleep(1)
          print(MAGENTA+"\nTu puntaje inicial sera de", puntaje,"puntos.Mucha suerte",nombre+"!!!"+RESET)
        else:
          print("Gracias por todo", nombre,"!!")
          break
###############################################################################           
      elif eligio == 2:
        print("\nEmpecemos nuestra Trivia de PROGRAMACION")
        tema_elegido = "programacion"
#--------------------------------------------------------------------------------------#
        #PRIMERA PREGUNTA
        print("\n1) Marque la respuesta correcta: ")
        #ALTERNATIVAS
        altern_0 = ["a)", "b)", "c)", "d)"]
        altern_1 = ["Javascript es un lenguaje de programacion de bajo nivel", "Javascript fue creado en el año 2020", "Html y css son lenguajes de programacion", "Python es un luenguaje de programacion de alto nivel"]
        for number in range (0, 4):
          print(" ",altern_0[number],altern_1[number]) 
          time.sleep(0.5)
        #INGRESAR RESPUESTA
        print(BLUE+"\n Ingrese solamente la letra de las alternativas mostradas"+RESET)
        respuesta_1 = input("\n Ingresa respuesta: ")
        while respuesta_1 not in ("a", "b", "c", "d", "x"):
            respuesta_1 = input("\n Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: "
            )
    
        #VALIDACION DE RESPUESTA
        respuestas = ["a", "b", "c", "d", "x"]  
        if respuesta_1 == respuestas[3]:
          puntaje += 10 
          print(GREEN+"\n Muy bien ", nombre," La respuesta es correcta!!, tu puntaje actual es de ", puntaje, "puntos"+RESET)
          time.sleep(2)
        elif respuesta_1 == respuestas[4]:
          puntaje +=20
          print(GREEN+"\nFelicitaciones", nombre, " obtuviste 20 puntos extra"+RESET)
          print(GREEN+"Tienes un total de ", puntaje, "puntos"+RESET)
          time.sleep(2)
        else:
          puntaje -= 5
          print(RED+"\n Respuesta Incorrecta,", nombre, "tienes", puntaje, "puntos"+RESET)
          time.sleep(2)
#--------------------------------------------------------------------------------------#
        #SEGUNDA PREGUNTA
        print("\n2) En que año se creo Internet ")    
        #ALTERNATIVAS
        altern_0 = ["a)", "b)", "c)", "d)"]
        altern_1 = [1995, 1969, 2000, 1959]
        for number in range (0, 4):
          print(" ",altern_0[number],altern_1[number]) 
          time.sleep(0.5) 
        #INGRESAR RESPUESTA
        print(BLUE+"\n Ingrese solamente la letra de las alternativas mostradas"+RESET)
        respuesta_1 = input("\n Ingresa respuesta: ")
        while respuesta_1 not in ("a", "b", "c", "d", "x"):
            respuesta_1 = input("\n Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: "
            )
    
        #VALIDACION DE RESPUESTA
        respuestas = ["a", "b", "c", "d", "x"]  
        if respuesta_1 == respuestas[2]:
          puntaje += 10 
          print(GREEN+"\n Muy bien ", nombre," La respuesta es correcta!!, tu puntaje actual es de ", puntaje, "puntos"+RESET)
          time.sleep(2)
        elif respuesta_1 == respuestas[4]:
          puntaje +=20
          print(GREEN+"\nFelicitaciones", nombre, " obtuviste 20 puntos extra"+RESET)
          print(GREEN+"Tienes un total de ", puntaje, "puntos"+RESET)
          time.sleep(2)
        else:
          puntaje -= 5
          print(RED+"\n Respuesta Incorrecta,", nombre, "tienes", puntaje, "puntos"+RESET)
          time.sleep(2)
#------------------------------------------------------------------------------------#    
        #TERCERA PREGUNTA
        print("\n3) Quien fue el creador de php ")    
        #ALTERNATIVAS
        altern_0 = ["a)", "b)", "c)", "d)"]
        altern_1 = ["Mark Zuckerberg", "Guido van Rossum", "Rasmus Lerdorf", "Bill Gates"]
        for number in range (0, 4):
          print(" ",altern_0[number],altern_1[number]) 
          time.sleep(0.5)    
        #INGRESAR RESPUESTA
        print(BLUE+"\n Ingrese solamente la letra de las alternativas mostradas"+RESET)
        respuesta_1 = input("\n Ingresa respuesta: ")
        while respuesta_1 not in ("a", "b", "c", "d", "x"):
            respuesta_1 = input("\n Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: "
            )
    
        #VALIDACION DE RESPUESTA
        respuestas = ["a", "b", "c", "d", "x"]
        if respuesta_1 == respuestas[2]:
          puntaje += 10 
          print(GREEN+"\n Muy bien ", nombre," La respuesta es correcta!!, tu puntaje actual es de ", puntaje, "puntos"+RESET)
          time.sleep(2)
        elif respuesta_1 == respuestas[4]:
          puntaje +=20
          print(GREEN+"\nFelicitaciones", nombre, " obtuviste 20 puntos extra"+RESET)
          print(GREEN+"Tienes un total de ", puntaje, "puntos"+RESET)
          time.sleep(2)
        else:
          puntaje -= 5
          print(RED+"\n Respuesta Incorrecta,", nombre, "tienes", puntaje, "puntos"+RESET)
          time.sleep(2)
#......................................................................................#
        #RULETA DE LA SUERTE        
        print(GREEN+"\nRULETA DE LA SUERTE\n"+RESET)
        
        for ruleta in range(50,random.randint(15, 45), -random.randint(2, 5)):
          print(ruleta)
          time.sleep(0.5)
        puntaje+=ruleta
        print(GREEN+"\nTu puntaje total sera de ",puntaje," puntos"+RESET)
          
        #DESEAS VOLVER A JUGAR
        volver_jugar=input("\nDeseas volver a jugar? Escriba un 'si' para continuar en caso contrario presione cualquier otra tecla: ")
        if(volver_jugar=="si"):
          time.sleep(0.5)
          print(CYAN+"\nEscoja una opcion nuevamente"+RESET)
          time.sleep(0.5)
          print(GREEN+"""
      1) Historia     3) Deportes
      2) Programacion        4) Cultura General...
      """+RESET)
          time.sleep(0.5)
          eligio = int(input("\nIngrese la opcion que desee jugar: "))
          puntaje = random.randint(0, 10)
          print("\n")
          for numero_carga in range(5, 0, -1):
            print(CYAN+"cargando preguntas..."+RESET)
            time.sleep(1)
          print(MAGENTA+"\nTu puntaje inicial sera de", puntaje,"puntos.Mucha suerte",nombre+"!!!"+RESET)
        else:
          print("Gracias por todo", nombre,"!!")
          break
##################################################################################        
      elif eligio == 3:
        print("\n Empecemos nuestra Trivia de DEPORTES")
        tema_elegido = "deportes"
#--------------------------------------------------------------------------------#        
        #PRIMERA PREGUNTA
        print("\n1) En que ciudad de EEUU tienen su sede los Kings, el equipo de la NBA ? ")    
        #ALTERNATIVAS
        altern_0 = ["a)", "b)", "c)", "d)"]
        altern_1 = ["Houston", "Sacramento", "Dallas", "New Jersey"]
        for number in range (0, 4):
          print(" ",altern_0[number],altern_1[number]) 
          time.sleep(0.5) 
    #INGRESAR RESPUESTA
        print(BLUE+"\n Ingrese solamente la letra de las alternativas mostradas"+RESET)
        respuesta_1 = input("\n Ingresa respuesta: ")
        while respuesta_1 not in ("a", "b", "c", "d", "x"):
            respuesta_1 = input("\n Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
        #VALIDACION DE RESPUESTA
        respuestas = ["a", "b", "c", "d", "x"]  
        if respuesta_1 == respuestas[1]:
          puntaje += 10 
          print(GREEN+"\n Muy bien ", nombre," La respuesta es correcta!!, tu puntaje actual es de ", puntaje, "puntos"+RESET)
          time.sleep(2)
        elif respuesta_1 == respuestas[4]:
          puntaje +=20
          print(GREEN+"\nFelicitaciones", nombre, " obtuviste 20 puntos extra"+RESET)
          print(GREEN+"Tienes un total de ", puntaje, "puntos"+RESET)
          time.sleep(2)
        else:
          puntaje -= 5
          print(RED+"\n Respuesta Incorrecta,", nombre, "tienes", puntaje, "puntos"+RESET)
          time.sleep(2)
#-----------------------------------------------------------------------------#    
       #SEGUNDA PREGUNTA
        print("\n2) Desde cuando es deporte olimpico el ping pong ? ")
    
        #ALTERNATIVAS
        altern_0 = ["a)", "b)", "c)", "d)"]
        altern_1 = ["Desde Seul 1988", "Desde Atenas 1896", "Desde Barcelona 1992", "Desde Londres 1948"]
        for number in range (0, 4):
          print(" ",altern_0[number],altern_1[number]) 
          time.sleep(0.5)    
        #INGRESAR RESPUESTA
        print(BLUE+"\n Ingrese solamente la letra de las alternativas mostradas"+RESET)
        respuesta_1 = input("\n Ingresa respuesta: ")
        while respuesta_1 not in ("a", "b", "c", "d", "x"):
          respuesta_1 = input("\n Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
    
        #VALIDACION DE RESPUESTA
        respuestas = ["a", "b", "c", "d", "x"]  
        if respuesta_1 == respuestas[0]:
          puntaje += 10 
          print(GREEN+"\n Muy bien ", nombre," La respuesta es correcta!!, tu puntaje actual es de ", puntaje, "puntos"+RESET)
          time.sleep(2)
        elif respuesta_1 == respuestas[4]:
          puntaje +=20
          print(GREEN+"\nFelicitaciones", nombre, " obtuviste 20 puntos extra"+RESET)
          print(GREEN+"Tienes un total de ", puntaje, "puntos"+RESET)
          time.sleep(2)
        else:
          puntaje -= 5
          print(RED+"\n Respuesta Incorrecta,", nombre, "tienes", puntaje, "puntos"+RESET)
          time.sleep(2)
#-----------------------------------------------------------------------------------#    
        #TERCERA PREGUNTA
        print("\n3) Quien gano la copa de Europa de futbol en el año 2008? ")    
        #ALTERNATIVAS
        altern_0 = ["a)", "b)", "c)", "d)"]
        altern_1 = ["Rusia", "Brasil", "Alemania", "España"]
        for number in range (0, 4):
          print(" ",altern_0[number],altern_1[number]) 
          time.sleep(0.5)    
        #INGRESAR RESPUESTA
        print(BLUE+"\n Ingrese solamente la letra de las alternativas mostradas"+RESET)
        respuesta_1 = input("\n Ingresa respuesta: ")
        while respuesta_1 not in ("a", "b", "c", "d", "x"):
          respuesta_1 = input("\n Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
      
        #VALIDACION DE RESPUESTA
        respuestas = ["a", "b", "c", "d", "x"]
        if respuesta_1 == respuestas[3]:
          puntaje += 10 
          print(GREEN+"\n Muy bien ", nombre," La respuesta es correcta!!, tu puntaje actual es de ", puntaje, "puntos"+RESET)
          time.sleep(2)
        elif respuesta_1 == respuestas[4]:
          puntaje +=20
          print(GREEN+"\nFelicitaciones", nombre, " obtuviste 20 puntos extra"+RESET)
          print(GREEN+"Tienes un total de ", puntaje, "puntos"+RESET)
          time.sleep(2)
        else:
          puntaje -= 5
          print(RED+"\n Respuesta Incorrecta,", nombre, "tienes", puntaje, "puntos"+RESET)
          time.sleep(2)
#......................................................................................#
        #RULETA DE LA SUERTE        
        print(GREEN+"\nRULETA DE LA SUERTE\n"+RESET)
        
        for ruleta in range(50,random.randint(15, 45), -random.randint(2, 5)):
          print(ruleta)
          time.sleep(0.5)
        puntaje+=ruleta
        print(GREEN+"\nTu puntaje total sera de ",puntaje," puntos"+RESET)
          
        #DESEAS VOLVER A JUGAR
        volver_jugar=input("\nDeseas volver a jugar? Escriba un 'si' para continuar en caso contrario presione cualquier otra tecla: ")
        if(volver_jugar=="si"):
          time.sleep(0.5)
          print(CYAN+"\nEscoja una opcion nuevamente"+RESET)
          time.sleep(0.5)
          print(GREEN+"""
      1) Historia     3) Deportes
      2) Programacion        4) Cultura General...
      """+RESET)
          time.sleep(0.5)
          eligio = int(input("\nIngrese la opcion que desee jugar: "))
          puntaje = random.randint(0, 10)
          print("\n")
          for numero_carga in range(5, 0, -1):
            print(CYAN+"cargando preguntas..."+RESET)
            time.sleep(1)
          print(MAGENTA+"\nTu puntaje inicial sera de", puntaje,"puntos.Mucha suerte",nombre+"!!!"+RESET)
        else:
          print("Gracias por todo", nombre,"!!")
          break
##################################################################################        
      elif eligio == 4:
            print("\n Empecemos nuestra Trivia de CULTURA GENERAL")
            tema_elegido = "cultura_general"
#---------------------------------------------------------------------------------#       
            #PRIMERA PREGUNTA
            print("\n1) ¿Cuántos litros de sangre tiene una persona adulta?")
            #ALTERNATIVAS
            altern_0 = ["a)", "b)", "c)", "d)"]
            altern_1 = ["Tiene entre 2 y 4 litros", "Tiene entre 4 y 6 litros", "Tiene 10 litros", "Tiene 7 litros"]
            for number in range (0, 4):
              print(" ",altern_0[number],altern_1[number]) 
              time.sleep(0.5)     
            #INGRESAR RESPUESTA
            print(BLUE+"\n Ingrese solamente la letra de las alternativas mostradas"+RESET)
            respuesta_1 = input("\n Ingresa respuesta: ")
            while respuesta_1 not in ("a", "b", "c", "d", "x"):
                respuesta_1 = input("\n Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: "
                )        
            #VALIDACION DE RESPUESTA
            respuestas = ["a", "b", "c", "d", "x"]
            if respuesta_1 == respuestas[1]:
              puntaje += 10 
              print(GREEN+"\n Muy bien ", nombre," La respuesta es correcta!!, tu puntaje actual es de ", puntaje, "puntos"+RESET)
              time.sleep(2)
            elif respuesta_1 == respuestas[4]:
              puntaje +=20
              print(GREEN+"\nFelicitaciones", nombre, " obtuviste 20 puntos extra"+RESET)
              print(GREEN+"Tienes un total de ", puntaje, "puntos"+RESET)
              time.sleep(2)
            else:
              puntaje -= 5
              print(RED+"\n Respuesta Incorrecta,", nombre, "tienes", puntaje, "puntos"+RESET)
              time.sleep(2)
#-------------------------------------------------------------------------------#        
            #SEGUNDA PREGUNTA
            print("\n2) ¿Cuál es el país más grande y el más pequeño del mundo?")
            #ALTERNATIVAS
            altern_0 = ["a)", "b)", "c)", "d)"]
            altern_1 = ["Rusia y Vaticano", "China y Nauru", "Canadá y Mónaco", "Estados Unidos y Malta"]
            for number in range (0, 4):
              print(" ",altern_0[number],altern_1[number]) 
              time.sleep(0.5)        
            #INGRESAR RESPUESTA
            print(BLUE+"\n Ingrese solamente la letra de las alternativas mostradas"+RESET)
            respuesta_1 = input("\n Ingresa respuesta: ")
            while respuesta_1 not in ("a", "b", "c", "d", "x"):
                respuesta_1 = input("\n Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: "
                )       
            #VALIDACION DE RESPUESTA
            respuestas = ["a", "b", "c", "d", "x"]
            if respuesta_1 == respuestas[0]:
              puntaje += 10 
              print(GREEN+"\n Muy bien ", nombre," La respuesta es correcta!!, tu puntaje actual es de ", puntaje, "puntos"+RESET)
              time.sleep(2)
            elif respuesta_1 == respuestas[4]:
              puntaje +=20
              print(GREEN+"\nFelicitaciones", nombre, " obtuviste 20 puntos extra"+RESET)
              print(GREEN+"Tienes un total de ", puntaje, "puntos"+RESET)
              time.sleep(2)
            else:
              puntaje -= 5
              print(RED+"\n Respuesta Incorrecta,", nombre, "tienes", puntaje, "puntos"+RESET)
              time.sleep(2)
#--------------------------------------------------------------------------#              
            #TERCERA PREGUNTA
            print("\n3) ¿Cuál es el libro más vendido en el mundo después de la Biblia?")
        
            #ALTERNATIVAS
            altern_0 = ["a)", "b)", "c)", "d)"]
            altern_1 = ["El Señor de los Anillos", "El Principito", "La Odisea", "Don Quijote de la Mancha"]
            for number in range (0, 4):
              print(" ",altern_0[number],altern_1[number]) 
              time.sleep(0.5)         
            #INGRESAR RESPUESTA
            print(BLUE+"\n Ingrese solamente la letra de las alternativas mostradas"+RESET)
            respuesta_1 = input("\n Ingresa respuesta: ")
            while respuesta_1 not in ("a", "b", "c", "d", "x"):
                respuesta_1 = input("\n Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: "
                )
            #VALIDACION DE RESPUESTA
            respuestas = ["a", "b", "c", "d", "x"]
            if respuesta_1 == respuestas[3]:
              puntaje += 10 
              print(GREEN+"\n Muy bien ", nombre," La respuesta es correcta!!, tu puntaje actual es de ", puntaje, "puntos"+RESET)
              time.sleep(2)
            elif respuesta_1 == respuestas[4]:
              puntaje +=20
              print(GREEN+"\nFelicitaciones", nombre, " obtuviste 20 puntos extra"+RESET)
              print(GREEN+"Tienes un total de ", puntaje, "puntos"+RESET)
              time.sleep(2)
            else:
              puntaje -= 5
              print(RED+"\n Respuesta Incorrecta,", nombre, "tienes", puntaje, "puntos"+RESET)
              time.sleep(2)
#......................................................................................#
            #RULETA DE LA SUERTE        
            print(GREEN+"\nRULETA DE LA SUERTE\n"+RESET)            
            for ruleta in range(50,random.randint(15, 45), -random.randint(2, 5)):
              print(ruleta)
              time.sleep(0.5)
            puntaje+=ruleta
            print(GREEN+"\nTu puntaje total sera de ",puntaje," puntos"+RESET)                        #DESEAS VOLVER A JUGAR
            volver_jugar=input("\nDeseas volver a jugar? Escriba un 'si' para continuar en caso contrario presione cualquier otra tecla: ")
            if(volver_jugar=="si"):
              time.sleep(0.5)
              print(CYAN+"\nEscoja una opcion nuevamente"+RESET)
              time.sleep(0.5)
              print(GREEN+"""
          1) Historia     3) Deportes
          2) Programacion        4) Cultura General...
          """+RESET)
              time.sleep(0.5)
              eligio = int(input("\nIngrese la opcion que desee jugar: "))
              puntaje = random.randint(0, 10)
              print("\n")
              for numero_carga in range(5, 0, -1):
                print(CYAN+"cargando preguntas..."+RESET)
                time.sleep(1)
              print(MAGENTA+"\nTu puntaje inicial sera de", puntaje,"puntos.Mucha suerte",nombre+"!!!"+RESET)
            else:
              print("Gracias por todo", nombre,"!!")
              break            
      else:
        print(RED+"\n Opción no válida, intentelo nuevamente"+RESET)
        eligio = int(input("\n Selecciona una opcion: "))







          

      
    
