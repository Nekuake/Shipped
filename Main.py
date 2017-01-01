import random
import time
print("BIENVENIDO AL SHIPEADOR. DONDE TODO EL MUNDO PUEDE SER SHIPEADO CON LO QUE SEA")
Run = 1
while Run == 1:
  time.sleep (2)
  persona1 = 0
  persona2 = 0
  C = 0
  Done = 0
  Fraserundone = 0
  while persona1 == 0:
    persona1int = random.randint(1,30)
    if persona1int == 1:
      persona1 = "Dalas"
    elif persona1int == 2:
      persona1 = "Aguirre"
    elif persona1int == 3:
      persona1 = "Santiago Abascal ESPAÑOL"
    elif persona1int == 4:
      persona1 = "el entrenador Pokémon neoliberal"
    elif persona1int == 5:
      persona1 = "tu amigo furry que retwittea YIFF"
    elif persona1int == 6:
      persona1 = "JUAN DEMONIO"
    elif persona1int == 7:
      persona1 = "uno de los bots que te siguen"
    elif persona1int == 8:
      persona1 = "tu persona"
    elif persona1int == 9:
      persona1 = "el pesado que te corrige las faltas"
    elif persona1int == 10:
      persona1 = "Hitler"
    elif persona1int == 11:
      persona1 = "Stalin"
    elif persona1int == 12:
      persona1 = "Franco"
    elif persona1int == 13:
      persona1 = "Fernando VII y su macrosomía genital"
    elif persona1int == 14:
      persona1 = "el Rubius"
    elif persona1int == 15:
      persona1 = "Joven Chano"
    elif persona1int == 16:
      persona1 = "Jorge Cremades"
    elif persona1int == 17:
      persona1 = "Rajoy"
    elif persona1int == 18:
      persona1 = "la Merkel"
    elif persona1int == 19:
      persona1 = "Terelu Campos"
    elif persona1int == 20:
      persona1 = "el desarrollador"
    elif persona1int == 21:
      persona1 = "tu crush"
  while persona2 == 0:
    persona2int = random.randint(1,30)
    if persona2int == 1:
      persona2 = "Dalas"
    elif persona2int == 2:
      persona2 = "Aguirre"
    elif persona2int == 3:
      persona2 = "Santiago Abascal ESPAÑOL"
    elif persona2int == 4:
      persona2 = "el entrenador Pokémon neoliberal"
    elif persona2int == 5:
      persona2 = "tu amigo furry que retwittea YIFF"
    elif persona2int == 6:
      persona2 = "JUAN DEMONIO"
    elif persona2int == 7:
      persona2 = "uno de los bots que te siguen"
    elif persona2int == 8:
      persona2 = "tu persona"
    elif persona2int == 9:
      persona2 = "el pesado que te corrige las faltas"
    elif persona2int == 10:
      persona2 = "Hitler"
    elif persona2int == 11:
      persona2 = "Stalin"
    elif persona2int == 12:
      persona2 = "Franco"
    elif persona2int == 13:
      persona2 = "Fernando VII y su macrosomía genital"
    elif persona2int == 14:
      persona2 = "El Rubius"
    elif persona2int == 15:
      persona2 = "Joven Chano"
    elif persona2int == 16:
      persona2 = "Jorge Cremades"
    elif persona2int == 17:
      persona2 = "Rajoy"  
    elif persona2int == 18:
      persona2 = "la Merkel"
    elif persona2int == 19:
      persona2 = "Terelu Campos"
    elif persona2int == 20:
      persona2 = "el desarrollador"
    elif persona2int == 21:
      persona2 = "tu crush"
  while C == 0:
    Cint = random.randint(1,30)
    if Cint == 1:
      C = "el ano"
    elif Cint == 2:
      C= "un dildo más grande que un Bad Dragon"
    elif Cint == 3:
      C= "el pene"
    elif Cint == 4:
      C= "la lengua"
    elif Cint == 5:
      C= "toda su colección de videos porno amateur"
    elif Cint == 6:
      C = "una charla sobre el postmodernismo con Cohen de fondo"
    elif Cint == 7:
      C = "veinte poemas de amor y una canción desesperada"
    elif Cint == 8:
      C = "un fursuit manchado de lujuria"
    elif Cint == 9:
      C = "la casa de Pin&Pon"
    elif Cint == 10:
      C = "todo su amor comprimido en una tierna caricia"
    elif Cint == 11:
      C = "una agenda de ms Wonderful"
    elif Cint == 12:
      C = "una unión de manos simbólica"
    elif Cint == 13:
      C = "una imagen descorazonadora"
    elif Cint == 14:
      C = "un beso negro"
    elif Cint == 15:
      C = "un buen faje en el baño"
    elif Cint == 16:
      C = "su infinita riqueza"
    elif Cint == 17:
      C = "un hijo bastardo y tonto"
  while Done == 0:
    Doneint = random.randint(1,10)
    if Doneint == 1:
      print(persona1 + " le metió " + C + " a " + persona2 + " por donde nunca sale el sol.")      
      Done = 1
    elif Doneint == 2:
      print(persona1 + " se le quedó mirando a los ojos y, con " + C + " le quedó claro a " + persona2 + " que era el amor de su vida")
      Done = 1
    elif Doneint == 3:
      print("Con todo el dolor de su corazón, " + persona1 + " tuvo que dejar marchar a " + persona2 + " siendo " + C + " el único recuerdo que guardaría.")
      Done = 1
    elif Doneint == 4:
      print(persona1 + " siempre escondería que la verdadera razón por la que amaba a " + persona2 + " era " + C)
      Done = 1
    elif Doneint == 5:
      print("ENAMORADOS: El fanfic que se hizo best-seller, ahora con " + persona1 + " y cómo " + C + " cambió su visión de su amor a " + persona2)
      Done = 1
  time.sleep(2)
  print("¿Quiere tirar otra vez? (Y/N)")
  Runinp = input("> ").upper()
  while Runinp.upper() not in ("Y", "N"):
    print("ERROR DE ENTRADA, POR FAVOR USE (Y/N)")
    Runinp = input("> ").strip().upper()
  if Runinp == "Y":
    time.sleep(1)
    while Fraserundone == 0:
      Fraserun = random.randint(1,15)
      if Fraserun == 1:
        print ("Shippear y otras drogas")
        Fraserundone = 1
      elif Fraserun == 2:
        print ("¿Esta es la única salida a mi depresión latente?")
        Fraserundone = 1
      elif Fraserun == 3:
        print ("Puede que esta frase dé para paja")
        Fraserundone = 1
      elif Fraserun == 4:
        print ("Recuerde que puedes llevar a cabo todo lo que salga aquí con el desarrollador")
        Fraserundone = 1
      elif Fraserun == 5:
        print ("¿No deberías probar a salir por ahí y ligar en vez de estar en el ordenador?")
        Fraserundone = 1
      elif Fraserun == 6:
        print ("¡Seguimos para bingo!")
        Fraserundone = 1
      elif Fraserun == 7:
        print ("Los usuarios del shipeador aseguran ser un 50% más virgenes una vez utilizado")
        Fraserundone = 1
      elif Fraserun == 8:
        print ("Utilizando sangre de unicornio para la próxima frase...")
  else : 
    Run = 0
exit    
        
