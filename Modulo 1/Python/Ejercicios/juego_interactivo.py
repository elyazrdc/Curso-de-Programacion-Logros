print("Responde las preguntas con las respuesta en pantalla para poder avanzar")
print("Estas un almacén abandonado, oscuro. En frente de ti hay una mesa con una linterna, al costado logras divisar unas escaleras ¿Qué haces?")
print("LINTERNA -	Tomar la linterna")
print("ESCALERAS -	Ir hacia las escaleras")

answer1 = input()

if answer1 == "linterna":
    print("Tomaste la linterna. Sus baterías están agotadas, la luz que emana es débil. Logras ver una puerta y decides entrar ahí, una vez la pesada puerta se cierra escuchas un ruido, uno distinto al del metal chocando contra el marco de la puerta ¿Ahora qué?")
    print("CAMINAR -    Seguir caminando, buscando una salida")
    print("ESPERAR -    Apagar la linterna y esperar")
    answer1 = input().strip().lower()
    
    if answer1 == "caminar":
        print("Sigues caminando, buscando una salida: Al seguir caminando, la linterna muestra un cuerpo extraño. Al verlo de reojo empiezas a correr. Escuchas fuertes pasos detrás de ti que te persiguen. Logras escapar escondiéndote debajo de una repisa")
        print("BUSCAR -     Alumbrar y buscar")
        print("RASTRAS -    Agacharte y alejarte a rastras")
        answer1 = input().strip().lower()
        
        if answer1 == "buscar":
            print("Al buscar logras encontrar un palo y una nueva linterna. Escuchas ruidos a la distancia. Que escoges")
            print("LINTERNA -   Tomar la nueva linterna")
            print("PALO -   Tomar el palo")
            answer1 = input().strip().lower()
            
            if answer1 == "linterna":
                print("La nueva linterna muestra a la creatura, sin embargo, muestra tambien la salida. Echas a correr con todas tus fuerzas y logras salir. Parece que lo perdiste. Ganaste")
            elif answer1 == "palo":
                print("Tomas un palo para algo se abalanza sobre ti. Forcejeas en el suelo con todas tus fuerzas. La creatura te quita el palo que acabas de tomar y lo usa contra ti. Game Over")
        elif answer1 == "rastras":
            print("Te mueves a rastras. Llegas hasta una pared, parece haber una ventana hacia afuera. Que haras")
            print("VENTANA -    Rompes la ventana para salir, pero la creatura podria encontrarte")
            print("PUERTA -     Corres hacia la puerta, la creatura podria encontrarte")
            answer1 = input().strip().lower()
            if answer1 == "ventana":
                print("Rompes la ventana y la escalas rapidamente. Te cortas y raspas todo el cuerpo. Algo te jala del pie pero logras salir. Escapas. Fin del juego")
            elif answer1 == "puerta":
                print("Corres hacia la puerta. Unos pasos pesados suenan a tu lado, persiguiendote. Algo te golpea y caes al suelo, donde forcejeas. Recibes un fuerte golpe en la cabeza y te desmayas. Game Over")
    elif answer1 == "esperar":
        print("Al apagar la linterna, los pasos continúan, sin embargo, cesan al son de un último ruido fuerte. Parece que lo que sea que fuere ya no esta, pero no es seguro.")
        print("Logras ver un palo y unas pilas, pero solo tienes tiempo para agarrar uno ¿Que haras?")
        print("PALO -   Tomar el palo y seguir")
        print("PILAS - Tomas las pilas y seguir")
        answer1 = input().strip().lower()
        
        if answer1 == "palo":
            print("Aquello volvio. Logras interceptarlo con el palo. Forcejeas con el hasta que logras escapar. Corres hasta lo que parece ser una salida. Esta bloqueada. Logras ver una ventana, pero no es seguro correr hacia alli. Que haces")
            print("VENTANA -    Correr hacia la ventana")
            print("PUERTA -     Forcejeas la puerta para abrirla")
            
            answer1 = input().strip().lower()
            
            if answer1 == "ventana":
                print("Corres hacia la ventana y te tiras. Escapas del lugar y corres hacia la libertad. Fin del Juego")
            elif answer1 == "puerta":
                print("Forcejeas en la puerta. Eres golpeado por algo y te desmayas. Game Over")
            
        if answer1 == "pilas":
            print("Recoges las pilas. Tu linterna ahora esta como nueva. Alumbras hacia el frente. Aquello estaba justo en frente de ti. Te empuja y te golpea repetidas veces. Game Over")
        
        
elif answer1 == "escaleras":
    print("Las luces parpadean un instante y luego se apagan por completo. Todo lo que queda es el silencio... y el eco hueco de tus pasos al comenzar a subir por la escalera de emergencia. Encuentras una cuerda y otras escaleras")
    print("CUERDA -     Tomas la cuerda")
    print("ESCALERA -   Caminas hacia las escaleras")
    answer1 = input().strip().lower()
    
    if answer1 == "cuerda":
        print("Tomas la cuerda, con ella continuas por el piso. Encuentras una puerta.")
        print("PUERTA -     Forcejeas la puerta para entrar")
        print("VENTANA -    Parece haber una ventana cerca, puedes usar la cuerda para bajar")
        answer1 = input().strip().lower()
        
        if answer1 == "puerta":
            print("Forcejeas la puerta, no logras entrar")
            print("BAJAR -    Bajar al piso anterior")
            print("SUBIR -  Subir al piso supeior")
            answer1 = input().strip().lower()
            
            if answer1 == "bajar":
                print("Intentas bajar las escaleras pero un ruido crujiente te advierte de su pesimo estado. Que haras")
                print("BAJAR -  Ignorar y seguir bajando")
                print("SUBIR -  Reflexionar y subir en su lugar")
                answer1 = input().strip().lower()
                
                if answer1 == "bajar":
                    print("Bajas las escaleras. Estas de repente se rompen y caes. Te golpeas fuertemente la cabeza y te desmayas. Game Over")
                elif answer1 == "subir":
                    print("Estas en el techo. Ves unas escaleras de emergencia algo oxidadas. Escuchas pasos viniendo del piso de abajo. Parece que algo te esta buscando. No tienes mucho tiempo")
                    print("EMERGENCIA - Usar las escaleras de emergencia")
                    print("CUERDA -     Usar la cuerda para bajar")
                    answer1 = input().strip().lower()
                    
                    if answer1 == "emergencia":
                        print("Usas las escaleras de emergencia. Logras bajar hasta el suelo y salir corriendo. Escapaste")
                    elif answer1 == "cuerda":
                        print("Usas la cuerda, pero no parece llegar hasta abajo. Bajas a traves de ella pero algo falla. Caes desde el techo y te golpeas la cabeza y te rompes una pierna. Pierdes el conocimiento mientras aquello te esta buscando. Game Over")
        elif answer1 == "ventana":
            print("Rompes la ventana y usas la cuerda para bajar. En el trayecto resbalas y caes. Parece que te rompiste algo, pero puedes caminar. Escapaste.")
    elif answer1 == "escalera":

        print("Estas en el techo. Ves unas escaleras de emergencia algo oxidadas. Escuchas pasos viniendo del piso de abajo. Parece que algo te esta buscando. No tienes mucho tiempo")
        print("EMERGENCIA - Usar las escaleras de emergencia")
        print("CUERDA -     Usar la cuerda para bajar")
        answer1 = input().strip().lower()
                    
        if answer1 == "emergencia":
            print("Usas las escaleras de emergencia. Logras bajar hasta el suelo y salir corriendo. Escapaste")
        elif answer1 == "cuerda":
            print("Usas la cuerda, pero no parece llegar hasta abajo. Bajas a traves de ella pero algo falla. Caes desde el techo y te golpeas la cabeza y te rompes una pierna. Pierdes el conocimiento mientras aquello te esta buscando. Game Over")