RED = '\033[31m'
GREEN = '\033[32m'
BLUE = '\033[34m'
RESET = '\033[39m'

print(RED+"BIENVENIDOS A MI TRIVIA"+RESET)
nombre = input("\n Cuál es tu nombre: ")
puntaje = 0
print("\n Hola", nombre, "elige una opción")

print(GREEN+"""
    1) Historia     3) Deportes
    2) Programacion        4) Cultura General...
    """+RESET)

# Leemos lo que ingresa el usuario
print("Seleccione un numero de las opciones mostradas y luego presione enter para poder acceder a la trivia asignada"
)

eligio = int(input("\n Selecciona una opcion: "))
#
while(eligio>0):
      if eligio == 1:
        print("\n Empecemos nuestra Trivia de Historia")
          
        #PRIMERA PREGUNTA
        print("\n1) Cuantos departamentos constituyen el territorio peruano ")

        #ALTERNATIVAS
        print(" a) 24 departamentos") #Respuesta correcta
        print(" b) 20 departamentos") 
        print(" c) 25 departamentos")
        print(" d) 23 departamentos") 

          #INGRESAR RESPUESTA
        print("\n Ingrese solamente la letra de las alternativas mostradas")
        respuesta_1 = input("\n Ingresa respuesta: ")
        while respuesta_1 not in ("a", "b", "c", "d", "x"):
          respuesta_1 = input("\n Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
    #VALIDACION DE RESPUESTA
        if respuesta_1 == "a":
          puntaje += 10
          print(GREEN+"\n Muy bien ", nombre," La respuesta es correcta!!, tu puntaje actual es de ", puntaje, "puntos"+RESET)
        elif respuesta_1 == "b":
          puntaje -= 5
          print(RED+"\n Respuesta Incorrecta,", nombre, "tienes", puntaje, "puntos"+RESET)
        elif respuesta_1 == "c":
          puntaje -= 5
          print(RED+"\n Respuesta Incorrecta,", nombre, "tienes", puntaje, "puntos"+RESET)
        elif respuesta_1 == "x":
          puntaje +=20
          print("\n Felicitaciones", nombre, " obtuviste 20 puntos extra")
          print("\n Tienes un total de ", puntaje, "puntos")
        else:
          puntaje -= 5
          print(RED+"\n Respuesta Incorrecta,", nombre, "tienes", puntaje, "puntos"+RESET)

        #SEGUNDA PREGUNTA
        print("\n2) Quien fue el ultimo soberano inca ")

        #ALTERNATIVAS
        print(" a) Pachacutec") 
        print(" b) Manco Capac") 
        print(" c) Atahualpa")#Respuesta correcta
        print(" d) Mayta Capac.") 

        #INGRESAR RESPUESTA
        print("\n Ingrese solamente la letra de las alternativas mostradas")
        respuesta_1 = input("\n Ingresa respuesta: ")
        while respuesta_1 not in ("a", "b", "c", "d", "x"):
          respuesta_1 = input("\n Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

        #VALIDACION DE RESPUESTA
        if respuesta_1 == "a":
          puntaje -= 5
          print(RED+"\n Respuesta Incorrecta,", nombre, "tienes", puntaje, "puntos"+RESET)
        elif respuesta_1 == "b":
          puntaje -= 5
          print(RED+"\n Respuesta Incorrecta,", nombre, "tienes", puntaje, "puntos"+RESET)
        elif respuesta_1 == "c":
          puntaje += 10
          print(GREEN+"\n Muy bien ", nombre," La respuesta es correcta!!, tu puntaje actual es de ", puntaje, "puntos"+RESET)
        elif respuesta_1 == "x":
          puntaje +=20
          print("\n Felicitaciones", nombre, " obtuviste 20 puntos extra")
          print("\n Tienes un total de ", puntaje, "puntos")
        else:
          puntaje -= 5
          print(RED+"\n Respuesta Incorrecta,", nombre, "tienes", puntaje, "puntos"+RESET)
    
        #TERCERA PREGUNTA
        print("\n3) En que año se proclamo la independencia del Peru ")
    
        #ALTERNATIVAS
        print(" a) 1832") 
        print(" b) 1920") 
        print(" c) 1848")
        print(" d) 1821") #Respuesta correcta
    
        #INGRESAR RESPUESTA
        print("\n Ingrese solamente la letra de las alternativas mostradas")
        respuesta_1 = input("\n Ingresa respuesta: ")
        while respuesta_1 not in ("a", "b", "c", "d", "x"):
          respuesta_1 = input("\n Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
      
          #VALIDACION DE RESPUESTA
        if respuesta_1 == "a":
          puntaje -= 5
          print(RED+"\n Respuesta Incorrecta,", nombre, "tienes un TOTAL de", puntaje, "puntos"+RESET)
        elif respuesta_1 == "b":
          puntaje -= 5
          print(RED+"\n Respuesta Incorrecta,", nombre, "tienes un TOTAL de", puntaje, "puntos"+RESET)
        elif respuesta_1 == "c":
          puntaje -= 5
          print(RED+"\n Respuesta Incorrecta,", nombre, "tienes un TOTAL de", puntaje, "puntos"+RESET)
        elif respuesta_1 == "x":
          puntaje +=20
          print("\n Felicitaciones", nombre, " obtuviste 20 puntos extra")
          print("\n Tienes un total de ", puntaje, "puntos")
        else:
          puntaje += 10
          print(GREEN+"\n Muy bien ", nombre," La respuesta es correcta!!, tu puntaje TOTAL es de ", puntaje, "puntos"+RESET)
        print("Escoja una ")
        print("""
    1) Historia     3) Deportes
    2) Programacion        4) Cultura General...
    """)
        eligio = int(input("\n Escoja una opcion nuevamente "))
      elif eligio == 2:
        print("\n Empecemos nuestra Trivia de PROGRAMACION")
        tema_elegido = "programacion"
        #PRIMERA PREGUNTA
        print("\n1) Marque la respuesta correcta: ")
    
        #ALTERNATIVAS
        print(" a) Javascript es un lenguaje de programacion de bajo nivel")
        print(" b) Javascript fue creado en el año 2020") 
        print(" c) html y css son lenguajes de programacion")
        print(" d) Python es un luenguaje de programacion de alto nivel") #Respuesta correcta
    
        #INGRESAR RESPUESTA
        print("\n Ingrese solamente la letra de las alternativas mostradas")
        respuesta_1 = input("\n Ingresa respuesta: ")
        while respuesta_1 not in ("a", "b", "c", "d", "x"):
            respuesta_1 = input("\n Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: "
            )
    
        #VALIDACION DE RESPUESTA
        if respuesta_1 == "a":
            puntaje -= 5
            print(RED+"\n Respuesta Incorrecta,", nombre, "tienes", puntaje, "puntos"+RESET)
        elif respuesta_1 == "b":
            puntaje -= 5
            print(RED+"\n Respuesta Incorrecta,", nombre, "tienes", puntaje, "puntos"+RESET)
        elif respuesta_1 == "c":
            puntaje -= 5
            print(RED+"\n Respuesta Incorrecta,", nombre, "tienes", puntaje, "puntos"+RESET)
        elif respuesta_1 == "x":
            puntaje +=20
            print("\n Felicitaciones", nombre, " obtuviste 20 puntos extra")
            print("\n Tienes un total de ", puntaje, "puntos")
        else:
            puntaje += 10
            print(GREEN+"\n Muy bien ", nombre," La respuesta es correcta!!, tu puntaje actual es de ", puntaje, "puntos"+RESET)
          
        #SEGUNDA PREGUNTA
        print("\n2) En que año se creo Internet ")
    
        #ALTERNATIVAS
        print(" a) 1995")
        print(" b) 1969") #Respuesta correcta
        print(" c) 2000")
        print(" d) 1959") 
    
        #INGRESAR RESPUESTA
        print("\n Ingrese solamente la letra de las alternativas mostradas")
        respuesta_1 = input("\n Ingresa respuesta: ")
        while respuesta_1 not in ("a", "b", "c", "d", "x"):
            respuesta_1 = input("\n Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: "
            )
    
        #VALIDACION DE RESPUESTA
        if respuesta_1 == "a":
            puntaje -= 5
            print(RED+"\n Respuesta Incorrecta,", nombre, "tienes", puntaje, "puntos"+RESET)
        elif respuesta_1 == "b":
            puntaje += 10
            print(GREEN+"\n Muy bien ", nombre," La respuesta es correcta!!, tu puntaje actual es de ", puntaje, "puntos"+RESET)
        elif respuesta_1 == "c":
            puntaje -= 5
            print(RED+"\n Respuesta Incorrecta,", nombre, "tienes", puntaje, "puntos"+RESET)
        elif respuesta_1 == "x":
            puntaje +=20
            print("\n Felicitaciones", nombre, " obtuviste 20 puntos extra")
            print("\n Tienes un total de ", puntaje, "puntos")
        else:
            puntaje -= 5
            print(RED+"\n Respuesta Incorrecta,", nombre, "tienes", puntaje, "puntos"+RESET)
    
        #TERCERA PREGUNTA
        print("\n3) Quien fue el creador de php ")
    
        #ALTERNATIVAS
        print(" a) Mark Zuckerberg")
        print(" b) Guido van Rossum") 
        print(" c) Rasmus Lerdorf") #Respuesta correcta
        print(" d) Bill Gates") 
    
        #INGRESAR RESPUESTA
        print("\n Ingrese solamente la letra de las alternativas mostradas")
        respuesta_1 = input("\n Ingresa respuesta: ")
        while respuesta_1 not in ("a", "b", "c", "d", "x"):
            respuesta_1 = input("\n Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: "
            )
    
        #VALIDACION DE RESPUESTA
        if respuesta_1 == "a":
            puntaje -= 5
            print(RED+"\n Respuesta Incorrecta,", nombre, "tienes un TOTAL de", puntaje, "puntos"+RESET)
        elif respuesta_1 == "b":
            puntaje -= 5
            print(RED+"\n Respuesta Incorrecta,", nombre, "tienes un TOTAL de", puntaje, "puntos"+RESET)
        elif respuesta_1 == "c":
            puntaje += 10
            print(GREEN+"\n Muy bien ", nombre," La respuesta es correcta!!, tu puntaje TOTAL es de ", puntaje, "puntos"+RESET)
        elif respuesta_1 == "x":
            puntaje +=20
            print("\n Felicitaciones", nombre, " obtuviste 20 puntos extra")
            print("\n Tienes un total de ", puntaje, "puntos")
          
        else:
            puntaje -= 5
            print(RED+"\n Respuesta Incorrecta,", nombre, "tienes un TOTAL de", puntaje, "puntos"+RESET)
        print("\n Escoja un tema para su trivia")
        print("""
    1) Historia     3) Deportes
    2) Programacion        4) Cultura General...
    """)
        eligio = int(input("\n Escoja una opcion nuevamente "))
        
      elif eligio == 3:
        print("\n Empecemos nuestra Trivia de DEPORTES")
        tema_elegido = "deportes"
        
        #PRIMERA PREGUNTA
        print("\n1) En que ciudad de EEUU tienen su sede los Kings, el equipo de la NBA ? ")
    
        #ALTERNATIVAS
        print(" a) Houston") 
        print(" b) Sacramento") #Respuesta correcta
        print(" c) Dallas")
        print(" d) New Jersey") 

    #INGRESAR RESPUESTA
        print("\n Ingrese solamente la letra de las alternativas mostradas")
        respuesta_1 = input("\n Ingresa respuesta: ")
        while respuesta_1 not in ("a", "b", "c", "d", "x"):
            respuesta_1 = input("\n Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
        #VALIDACION DE RESPUESTA
        if respuesta_1 == "a":
            puntaje -= 5
            print(RED+"\n Respuesta Incorrecta,", nombre, "tienes", puntaje, "puntos"+RESET)
        elif respuesta_1 == "b":
            puntaje += 10
            print(GREEN+"\n Muy bien ", nombre," La respuesta es correcta!!, tu puntaje actual es de ", puntaje, "puntos"+RESET)
        elif respuesta_1 == "c":
            puntaje -= 5
            print(RED+"\n Respuesta Incorrecta,", nombre, "tienes", puntaje, "puntos"+RESET)
        elif respuesta_1 == "x":
            puntaje +=20
            print("\n Felicitaciones", nombre, " obtuviste 20 puntos extra")
            print("\n Tienes un total de ", puntaje, "puntos")
        else:
            puntaje -= 5
            print(RED+"\n Respuesta Incorrecta,", nombre, "tienes", puntaje, "puntos"+RESET)
    
       #SEGUNDA PREGUNTA
        print("\n2) Desde cuando es deporte olimpico el ping pong ? ")
    
        #ALTERNATIVAS
        print(" a) Desde Seul 1988") #Respuesta correcta
        print(" b) Desde Atenas 1896") 
        print(" c) Desde Barcelona 1992")
        print(" d) Desde Londres 1948") 
    
        #INGRESAR RESPUESTA
        print("\n Ingrese solamente la letra de las alternativas mostradas")
        respuesta_1 = input("\n Ingresa respuesta: ")
        while respuesta_1 not in ("a", "b", "c", "d", "x"):
          respuesta_1 = input("\n Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
    
        #VALIDACION DE RESPUESTA
        if respuesta_1 == "a":
          puntaje += 10
          print(GREEN+"\n Muy bien ", nombre," La respuesta es correcta!!, tu puntaje actual es de ", puntaje, "puntos"+RESET)
        elif respuesta_1 == "b":
          puntaje -= 5
          print(RED+"\n Respuesta Incorrecta,", nombre, "tienes", puntaje, "puntos"+RESET)
        elif respuesta_1 == "c":
          puntaje -= 5
          print(RED+"\n Respuesta Incorrecta,", nombre, "tienes", puntaje, "puntos"+RESET)
        elif respuesta_1 == "x":
          puntaje +=20
          print("\n Felicitaciones", nombre, " obtuviste 20 puntos extra")
          print("\n Tienes un total de ", puntaje, "puntos")
        else:
          puntaje -= 5
          print(RED+"\n Respuesta Incorrecta,", nombre, "tienes", puntaje, "puntos"+RESET)
    
        #TERCERA PREGUNTA
        print("\n3) Quien gano la copa de Europa de futbol en el año 2008? ")
    
        #ALTERNATIVAS
        print(" a) Rusia") 
        print(" b) Brasil") 
        print(" c) Alemania")
        print(" d) España") #Respuesta correcta
    
        #INGRESAR RESPUESTA
        print("\n Ingrese solamente la letra de las alternativas mostradas")
        respuesta_1 = input("\n Ingresa respuesta: ")
        while respuesta_1 not in ("a", "b", "c", "d", "x"):
          respuesta_1 = input("\n Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
      
        #VALIDACION DE RESPUESTA
        if respuesta_1 == "a":
          puntaje -= 5
          print(RED+"\n Respuesta Incorrecta,", nombre, "tienes un total de", puntaje, "puntos"+RESET)
        elif respuesta_1 == "b":
          puntaje -= 5
          print(RED+"\n Respuesta Incorrecta,", nombre, "tienes un total de", puntaje, "puntos"+RESET)
        elif respuesta_1 == "c":
          puntaje -= 5
          print(RED+"\n Respuesta Incorrecta,", nombre, "tienes un total de", puntaje, "puntos"+RESET)
        elif respuesta_1 == "x":
          puntaje +=20
          print("\n Felicitaciones", nombre, " obtuviste 20 puntos extra")
          print("\n Tienes un total de ", puntaje, "puntos")
        else:
          puntaje += 10
          print(GREEN+"\n Muy bien ", nombre," La respuesta es correcta!!, tu puntaje TOTAL es de ", puntaje, "puntos"+RESET)
        print("\n Escoja un tema para su trivia")
        print("""
    1) Historia     3) Deportes
    2) Programacion        4) Cultura General...
    """)
        eligio = int(input("\n Escoja una opcion nuevamente "))
      elif eligio == 4:
            print("\n Empecemos nuestra Trivia de CULTURA GENERAL")
            tema_elegido = "cultura_general"
            #PRIMERA PREGUNTA
            print("\n1) ¿Cuántos litros de sangre tiene una persona adulta?")

            #ALTERNATIVAS
            print(" a) Tiene entre 2 y 4 litros")
            print(" b) Tiene entre 4 y 6 litros")  #Respuesta correcta
            print(" c) Tiene 10 litros")
            print(" d) Tiene 7 litros")
        
            #INGRESAR RESPUESTA
            print("\n Ingrese solamente la letra de las alternativas mostradas")
            respuesta_1 = input("\n Ingresa respuesta: ")
            while respuesta_1 not in ("a", "b", "c", "d", "x"):
                respuesta_1 = input("\n Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: "
                )
        
            #VALIDACION DE RESPUESTA
            if respuesta_1 == "a":
                puntaje -= 5
                print(RED+"\n Respuesta Incorrecta,", nombre, "tienes", puntaje, "puntos"+RESET)
        
            elif respuesta_1 == "b":
                puntaje += 10
                print(GREEN+"\n Muy bien ", nombre," La respuesta es correcta!!, tu puntaje actual es de ", puntaje, "puntos"+RESET)
            elif respuesta_1 == "c":
                puntaje -= 5
                print(RED+"\n Respuesta Incorrecta,", nombre, "tienes", puntaje, "puntos"+RESET)
            elif respuesta_1 == "x":
                puntaje +=20
                print("\n Felicitaciones", nombre, " obtuviste 20 puntos extra")
                print("\n Tienes un total de ", puntaje, "puntos")
            else:
                puntaje -= 5
                print(RED+"\n Respuesta Incorrecta,", nombre, "tienes", puntaje, "puntos"+RESET)
        
            #SEGUNDA PREGUNTA
            print("\n2) ¿Cuál es el país más grande y el más pequeño del mundo?")
        
            #ALTERNATIVAS
            print(" a) Rusia y Vaticano") #Respuesta correcta
            print(" b) China y Nauru")  
            print(" c) Canadá y Mónaco")
            print(" d) Estados Unidos y Malta")
        
            #INGRESAR RESPUESTA
            print("\n Ingrese solamente la letra de las alternativas mostradas")
            respuesta_1 = input("\n Ingresa respuesta: ")
            while respuesta_1 not in ("a", "b", "c", "d", "x"):
                respuesta_1 = input("\n Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: "
                )
        
            #VALIDACION DE RESPUESTA
            if respuesta_1 == "a":
                puntaje += 10
                print(GREEN+"\n Muy bien ", nombre," La respuesta es correcta!!, tu puntaje actual es de ", puntaje, "puntos"+RESET)
            elif respuesta_1 == "b":
                puntaje -= 5
                print(RED+"\n Respuesta Incorrecta,", nombre, "tienes", puntaje, "puntos"+RESET)
            elif respuesta_1 == "c":
                puntaje -= 5
                print(RED+"\n Respuesta Incorrecta,", nombre, "tienes", puntaje, "puntos"+RESET)
            elif respuesta_1 == "x":
                puntaje +=20
                print("\n Felicitaciones", nombre, " obtuviste 20 puntos extra")
                print("\n Tienes un total de ", puntaje, "puntos")
            else:
                puntaje -= 5
                print(RED+"\n Respuesta Incorrecta,", nombre, "tienes", puntaje, "puntos"+RESET)
              
        #TERCERA PREGUNTA
            print("\n3) ¿Cuál es el libro más vendido en el mundo después de la Biblia?")
        
            #ALTERNATIVAS
            print(" a) El Señor de los Anillos") 
            print(" b) El Principito")  
            print(" c) La Odisea")
            print(" d) Don Quijote de la Mancha") #Respuesta correcta
        
            #INGRESAR RESPUESTA
            print("\n Ingrese solamente la letra de las alternativas mostradas")
            respuesta_1 = input("\n Ingresa respuesta: ")
            while respuesta_1 not in ("a", "b", "c", "d", "x"):
                respuesta_1 = input("\n Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: "
                )
        
            #VALIDACION DE RESPUESTA
            if respuesta_1 == "a":
                puntaje -= 5
                print(RED+"\n Respuesta Incorrecta,", nombre, "tienes un total de", puntaje, "puntos"+RESET)
            elif respuesta_1 == "b":
                puntaje -= 5
                print(RED+"\n Respuesta Incorrecta,", nombre, "tienes un total de", puntaje, "puntos"+RESET)
            elif respuesta_1 == "c":
                puntaje -= 5
                print(RED+"\n Respuesta Incorrecta,", nombre, "tienes un total de", puntaje, "puntos"+RESET)
            elif respuesta_1 == "x":
                puntaje +=20
                print("\n Felicitaciones", nombre, " obtuviste 20 puntos extra")
                print("\n Tienes un total de ", puntaje, "puntos")
            else:
                puntaje += 10
                print(GREEN+"Muy bien ", nombre," La respuesta es correcta!!, tu puntaje TOTAL es de ", puntaje, "puntos"+RESET)
            print("\n Escoja un tema para su trivia")
            print("""
    1) Historia     3) Deportes
    2) Programacion        4) Cultura General...
    """)
            eligio = int(input("\n Escoja una opcion nuevamente "))
            
      else:
        print(RED+"\n Opción no válida, intentelo nuevamente"+RESET)
        eligio = int(input("\n Selecciona una opcion: "))







          

      
    
