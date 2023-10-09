# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define a = Character("Ranger", who_color="#db0000")
define e = Character("Walken")
image walken = "walken/walken.png"
image walken happy = "walken/walken happy.png"
image walken serious = "walken/walken serious.png"
image walken furious = "walken/walken furious.png"
image black = "#000"


# El juego comienza aquí.

label start:

    stop music

    with dissolve

    scene black

    e "¿Está despierto? Prepararlo cuanto antes."

    "La camilla era comoda, pero lo notas, es una camilla tipica de enfermeria. Aunque tengas los ojos cerrados, notas las luces del techo."

    ". . ."

    a "(Mi cabeza está dandome vueltas...)"

    "Te llevas la mano a la cabeza. No han parado de moverte desde hace dos horas, y ademas has notado varias inyecciones. Tu traje reforzado parece haber sido recargado durante todo el rato que estuviste recibiendo pruebas."

    "Abres los ojos con lentitud, mientras te sientas en la camilla."

    play music anxiety volume 0.5 loop

    scene terminal with dissolve

    show walken with dissolve:
        ypos -100
        xpos 200

    # Presenta las líneas del diálogo.

    e "Muy bien Ranger, sé que estas fuera de contexto, mucho tiempo atrapado en el salvaje centro."

    "Te paras un momento a revisar tu alrededor, caracteristica del entrenamiento. Buscas situarte, hacer en tu mente un poco de contexto. Mirando al hombre frente a ti, notas que su traje reforzado es americano - como el tuyo, pero con otro logo de escuadrón."

    e "Dejame presentarme. Soy el capitan del 66º regimiento del ejercito de los Estados Unidos, Alfred Walken. Veterano de la guerra anglo-germana, de la gran guerra BETA y de la operación Cherry Blossom."

    e "Quiero dejar algo claro Ranger... Las cosas han cambiado. Es un milagro que tu seas el ultimo superviviente del 75º regimiento. Ahora mismo te fusionaré con mi unidad, y eso te convierte en mi subordinado."

    "Con la poca fuerza que tienes, al estar aún despertandote, haces un saludo marcial. Poco despues terminas de levantarte de la camilla."    

    scene black with dissolve

    play music dead_body volume 0.5 loop

    e "Comencemos por el principio Ranger. Año 2073." with dissolve  
    
    scene marte with dissolve:
        ypos -250
        xpos -100
        zoom 1.2

    e "Aún ni habia comenzado la guerra anglo-germana para cuando encontramos a los BETA por primera vez en Marte. El primer contacto salió horrible, y por ello es que ocurrió una de las mayores catastrofes de la humanidad..."
    
    scene luna with dissolve:
        ypos -250
        xpos -100
        zoom 1.2

    e "...Las caidas de las colmenas en la Luna, y en la Tierra."

    scene tierra with dissolve:
        ypos -300
        xpos -400
        zoom 0.6
        

    e "Cuando Moon Base cayó... Hive 01 aterrizó en Kashgar."

    scene tierra_acerca with dissolve:
        zoom 1.4

    e "Era el fin de la humanidad para 2075."

    scene mapabeta1 with dissolve:
        zoom 1.3

    e "Cuando aterrizó la U.N.S. lanzó una grata bienvenida llena de bombardeos orbitales. Los chinos lo apoyaron con cabezas nucleares."

    scene nuke

    pause 0.5

    scene nuke2:
        zoom 1.1
        ypos -250

    pause 0.5 
    
    scene mapabeta2 with dissolve:
        zoom 1.3

    pause 2.0

    scene mapabeta3 with dissolve:
        zoom 1.3

    pause 2.0

    e "Aún así, no fueron detenidos y comenzaron su expansión por todo el globo. En menos de un año Eurasia habia caido."

    scene black with dissolve

    e "La gran guerra BETA fue brutal y despiadada. El enemigo no tenia moralidad, arrasaba con todo y no tenian ningún instinto de supervivencia."

    scene beta_hive with dissolve:
        zoom 2.0
        linear 4.0 ypos -200
        linear 4.0 zoom 0.55
    
    pause 8.0

    e "No existió refugio contra los BETA. Allá adonde iban, toda tierra se volviá infertil. La humanidad llegó a estar a una maldita semana de ser extinguida..."

    scene black with dissolve

    e "Y aún así la humanidad siguió luchando hasta el maldito final... Operation Cherry Blossom en 2076, el gran sacrificio del escuadrón SKULL."

    scene korea with dissolve:
        zoom 2.0
        linear 4.0 xpos -80
        linear 3.0 zoom 0.8 xpos 0

    pause 2.0

    e "La élite de la humanidad, en un solo escuadrón, sin miedo a la muerte, primeros en cargar hacia el objetivo... Nadie se sorprendió cuando fueron designados a entrar a Kashgar y arrasar con todo lo que viesen..."

    scene eagle with dissolve:
        # zoom 0.7
        # xpos -50
        zoom 2.0
        linear 3.0 xpos -400
        linear 1.0 zoom 0.7 xpos -50

    e "Nuestros mejores pilotos pelearon allí, la ultima esperanza de que la humanidad derrotase a los BETA."

    e "Fue un asalto orbital, muchos recursos se usaron para una medida tan desesperada. El Stalin entró en la colmena y jamas volvió a ser visto."

    scene black with dissolve

    play music crash volume 0.5 loop

    show walken with dissolve:
        ypos -100
        xpos 200

    e "¿Crees que todo acabó ahí? No estariamos en la situación en la que estamos si eso fuese así."

    show walken serious with dissolve:
        ypos -100
        xpos 200

    e "Tras la Operation Cherry Blossom, los Skull fueron dados por muertos, aunque se sabe que hay supervivientes."

    e "Sin embargo, ese no fue el menor de nuestros problemas. Activaron la clausula SC31, la U.N.S. fue disuelta, y poco despues los BETA volvieron a atacar..."

    show walken furious with dissolve:
        ypos -100
        xpos 200

    e "Sabes... Soy estadounidense pero lo que hizo mi gobierno aquél dia... Jamas lo pienso perdonar."

    hide walken furious with dissolve

    scene gbomb1 with dissolve:
        zoom 1.2
    pause 0.2
    scene gbomb2:
        zoom 1.2
    pause 0.8
    scene gbomb3:
        zoom 1.2
    pause 2.0

    scene black with dissolve

    e "La tierra no volvería a ser la misma..."

    scene grancolapso with dissolve

    pause 2.0

    scene tierra_40 with dissolve:
        zoom 0.6
        xpos -400
        ypos -300

    e "Nuestro querido planeta quedó irreparable."

    play music acceptance volume 0.5 loop

    scene tierra_40_usa with dissolve:
        zoom 0.6
        xpos -400
        ypos -300

    e "Lo hicieron para arrasar a los BETA, y luego miles se fueron en las naves colonia. Huyeron, ya que al parecer, cuatro años después el mundo ha querido avanzar y los BETA parecen haber regresado."

    scene terminal with dissolve

    show walken serious with dissolve:
        ypos -100
        xpos 200

    e "Y aquí nos encontramos. Ha pasado un mes desde el incidente del Prometheus, con la ISAF recientemente establecida, somos la coalición del oeste quienes estamos metiendo mas recursos."
    

    e "Algo mas, ¿Ranger?"

    show walken with dissolve:
        ypos -100
        xpos 200

    menu:
        "Nada mas señor.":
            a "Nada mas capitán Walken. Prefiero no molestarle, si aquí en Fort Lewis debe haber algún lugar donde informarse... Ni sé que es la coalición ni nada."
            
            show walken serious:
                ypos -100
                xpos 200

            e "Bien, ve al hangar, allí te pondrán a punto para tu Raptor. Ahora perteneces a los 'Hunters', bienvenido de vuelta Ranger."

            show walken happy:
                ypos -100
                xpos 200

            "Walken te saluda con una sonrisa, parece que encontrarte fue una buena noticia."

            "Le devuelves el saludo, y poco despues ambos separais caminos. Te diriges al hangar."

            jump hangar

        "A decir verdad... ¿Coalición?":
            a "La verdad es que sí. Me gustaria saber que demonios es la coalición..."

            show walken serious:
                ypos -100
                xpos 200

            e "Estoy encargado del tratado de seguridad mutua entre Estados Unidos y el Imperio de Japón, estos dos gobiernos representan una coalición."

            e "Parecerá extraño, pero tras Babylon, la operación de éxodo y lanzamiento de las bombas el cual ha dejado la Tierra así, las islas niponas quedaron sumergidas."

            a "(Sumergidas... Espera, ¿entonces como quedó Eurasia? No lo vi en la terminal.)"

            a "Comprendo señor. Entonces los japoneses son nuestros aliados mas cercanos."

            e "Así es... Aunque tambien mantenemos conversaciones con el gobierno ruso. La Federación Rusa ha resultado ser un mejor aliado que lo fueron los commies. Igualmente, ahora mismo deberia dirigirse al hangar, allí le haran una introducción al Raptor."

            show walken:
                ypos -100
                xpos 200

            e "Bienvenido a los 'Hunters'."

            show walken happy:
                ypos -100
                xpos 200
            
            "Walken te saluda, y posteriormente se retira. Tu le devuelves el saludo y te retiras al hangar."

            hide walken with dissolve

            jump hangar

    # Finaliza el juego:

    return
