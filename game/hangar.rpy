define a = Character("Ranger", who_color="#db0000")
define s = Character("Sagara", who_color="#f0e800")
define m = Character("Melvina", who_color="#8b00e8")
image melvina = "melvina/mevina.png"
image melvina happy = "melvina/mevina happy.png"
image melvina happy2 = "melvina/mevina happy2.png"
image melvina happy3 = "melvina/mevina happy(ce).png"
image melvina happy4 = "melvina/mevina happy2(ce).png"
image melvina plm = "melvina/mevina planmal.png"
image melvina sobr = "melvina/mevina sobreinfo.png"
image melvina sonr = "melvina/mevina son.png"
image melvina surp = "melvina/mevina surp.png"
image melvina susp = "melvina/mevina suspiro.png"
image black = "#000"
image shiranui_Second = "bg/shiranui_Second.png"
image shiranui_SecondRED = "bg/shiranui_SecondRED.png"

label hangar:

    stop music

    play music quiet_moment volume 0.5 loop

    scene lewis_hangar

    a "Creo que esto es el hangar... ¿Donde deberia ir?"

    menu:

        "Aquella mecanica quizá...":
            a "Quiza aquella mujer..."

            show melvina susp with dissolve:
                    zoom 0.5
                    ypos 100
                    xpos 200

            "Te acercas caminando, con algo de dificultad hacia una chica de tez morena, por como va vestida parece que es una mecanica, ademas de sus manos manchadas de aceite."

            "Acercandote, ella nota tu presencia y se encara para confrontarte."

            show melvina with dissolve:
                    zoom 1.0
                    ypos 100
                    xpos 200

            m "Hmm?"

            show melvina surp:
                    ypos 100
                    xpos 200

            m "Es posible que debas ir a la enfermeria amigo."

            show melvina:
                    zoom 1.0
                    ypos 100
                    xpos 200

            "Algo pudiste entender, pero habla con un marcado acento australiano."

            a "Ah ya... Mira me mandaron a venir a probar el Raptor. Ya tuve bastantes pruebas por hoy."

            "Te apoyas en la barandilla, algo cansado."

            show melvina surp:
                    ypos 100
                    xpos 200

            m "No pareces ni estar en forma de subir, lo siento colega, deberias irte a enfermeria antes de venir a pilotar."

            "Ese acento australiano tan marcado otra vez, esta comenzando a cansarte la situación, demasiada insistencia."

            show melvina:
                    zoom 1.0
                    ypos 100
                    xpos 200

            a "No soy tu colega... El capitán Walken no te informó o que, ¿Esperas que me vaya y no trabajes en preparar el maldito Raptor?"

            show melvina plm:
                    zoom 1.0
                    ypos 100
                    xpos 200

            m "Wow, atras, tampoco hace falta ser tan bruto. Bueno ya que insistes...*puff*"

            show melvina sobr:
                    zoom 1.0
                    ypos 100
                    xpos 200

            m "Soy la ingeniera jefa Melvina Vidya Advani, a cargo del mantenimiento de los Raptor de los 'Hunters'. Todos me llaman Melvina o Mel, como mas te sientas comodo, amigo."

            show melvina happy3:
                    zoom 1.0
                    ypos 100
                    xpos 200
            
            a "Puedes decirme el Ranger. El capitán Walken comentó que mi identidad es restringida."

            play music harmonious volume 0.5 loop

            show melvina happy4:
                    zoom 1.0
                    ypos 100
                    xpos 200

            m "Jajajajaja..."

            show melvina plm:
                    zoom 1.0
                    ypos 100
                    xpos 200

            m "Ya, ya... Me informaron de antes. Tu Raptor esta preparado, hemos cargado un cuarto de combustible para propulsores, y el sistema de armas tendras que calibrarlo a tu gusto. Cuatro rifles AWMS-24, todos equipados con munición penetrante alto explosivo."

            show melvina happy2:
                    zoom 1.0
                    ypos 100
                    xpos 200
            
            a "¿Estamos reservando los penetrantes de carga deseschable?"

            show melvina sobr:
                    zoom 1.0
                    ypos 100
                    xpos 200

            m "Como entenderás tanto mantener un TSF como el Raptor como la munición en el estado que estamos, es realmente dificil. De hecho ni siquiera te equipe todos los cargadores posibles, sino un cuarto de la carga estandar."

            show melvina happy2:
                    zoom 1.0
                    ypos 100
                    xpos 200
            
            a "Al menos eso me dará mayor ligereza."

            show melvina susp:
                    zoom 1.0
                    ypos 100
                    xpos 200

            m "Hmmm meh, sí, menos peso. No te preocupes, no hay nadie como yo preparando TSF."

            "Mel te levanta la mano en señal de aprobación guiñandote el ojo. No da mucha confianza honestamente."

            a "Sí... Lo voy a sacar a pasear entonces... Hace un año que no vuelo un TSF."

            show melvina happy:
                    zoom 1.0
                    ypos 100
                    xpos 200

            a "(Con todo lo que ha pasado la verdad me llega a sorprender que me dejen pilotar de la nada un Raptor... Los rangers somos... eramos muy buenos en Eagles y Falcons, pero esto es un gran salto.)"
            
            m "Ohh... Quizá debas pasar por simulador entonces jujuju."

            a "Ni en broma. La mejor prueba es la real."

            a "(Y perderme esta oportunidad. Nadie sería tan tonto de evitar probar el grandioso F-22A Raptor, ingenieria estadounidense de calidad.)"

            a "(Quizá me estoy emocionando de mas...)"

            show melvina plm:
                    zoom 1.0
                    ypos 100
                    xpos 200

            m """Por toda tu cara se puede leer "Dejarme pilotar esta preciosidad" jajajaja."""

            a "Dificil ocultar la emoción de pilotar un top TSF del mundo... (Aunque es lo unico por lo que ahora me esta sacando una sonrisa.)"

        "Los japoneses.":
            a "Que hacen en Fort Lewis un par de japoneses..."

            "Lentamente y con cuidado te acercas a uno de los puestos de TSF japoneses... Habian desde Shiranui de primera generación, en su caracteristico color negro, pero los que habian despues..."

            scene shiranui_SecondRED with dissolve:
                zoom 1.25

            a "(Nunca vi un Shiranui así... Su presencia irradia... Ira, furia.)"

            a "(Noto partes del Shiranui pero es mucho mas avanzado. El hecho de que esté aquí indica que los japoneses y los americanos sí que tienen una relación bastante estrecha y sin embargo... Ahora mismo me siento un extraño.)"

            "Te apoyas en una de las barandillas para ver con cuidado ese extraño Shiranui."

            a "El desarrollo de esto tuvo que ser acojonante... Me pregunto como será que se enfrente a los Raptor..."

        "Exit":
            return

    return