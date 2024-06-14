define odiseo_name = "Odiseo"
define odiseo = Character("Odiseo", color="#c8ffc8")
define penelope = Character("Penélope", color="#ffc8c8")
define narrator = Character(None)

default player_name = "Odiseo"

# Definimos las imágenes de los personajes
image odiseo_dormido = "odiseo_neutro.png"
image odiseo_neutro = "odiseo_neutro.png"
image odiseo_hartazgo = "odiseo_neutro.png"
image odiseo_romantico = "odiseo_neutro.png"
image odiseo_triste = "odiseo_neutro.png"
image odiseo_feliz = "odiseo_neutro.png"
image penelope_neutra = "penelope_neutro.png"
image penelope_silueta = "penelope_neutro.png"
image penelope_enojada = "penelope_neutro.png"
image penelope_victima = "penelope_neutro.png"

image corazon_gris = "corazon_gris.png"
image corazon_amarillo = "corazon_amarillo.png"

# Fondo de la habitación
image habitacion = "habitacion.png"
image logo = "logo.png"
image collar_descargado = "collar_descargado.png"
image collar_cargado = "collar_cargado.png"

# SFX y BGM
define sfx_telefono = "telefono_sonando.mp3"
define bgm_grillos = "grillos_y_brisa.ogg"
define sfx_cortar_llamada = "cortar_llamada.ogg"
define sfx_collar_brilla = "collar_brilla.ogg"

# Variable temporal para almacenar el nombre introducido
default temp_name = ""

# Variable collar cargado
default collar_cargado = True
default estado_corazon = "Gris"

define puntaje_penelope = 0
define puntaje_afrodita = 0
define puntaje_atenea = 0

# Pantallas para los diferentes estados del corazón
screen corazon_gris():
    add "corazon_gris.png" xpos 0.95 ypos 0.05 anchor (1.0, 0.0)

screen corazon_amarillo():
    add "corazon_amarillo.png" xpos 0.95 ypos 0.05 anchor (1.0, 0.0)

screen corazon_rojo():
    add "corazon_rojo.png" xpos 0.95 ypos 0.05 anchor (1.0, 0.0)

screen corazon_marron():
    add "corazon_marron.png" xpos 0.95 ypos 0.05 anchor (1.0, 0.0)

# Pantalla principal que muestra el estado del corazón basado en el puntaje
screen mostrar_estado_corazon():
    if puntaje_penelope > puntaje_afrodita and puntaje_penelope > puntaje_atenea:
        use corazon_amarillo
    elif puntaje_afrodita > puntaje_penelope and puntaje_afrodita > puntaje_atenea:
        use corazon_rojo
    elif puntaje_atenea > puntaje_penelope and puntaje_atenea > puntaje_afrodita:
        use corazon_marron
    elif puntaje_afrodita == puntaje_atenea and puntaje_penelope == puntaje_afrodita and puntaje_atenea == puntaje_penelope:
        use corazon_gris

screen collar_cargado_screen():
    frame:
        background Solid("#000")  # Fondo negro
        xfill True
        yfill True
        add "collar_cargado.png" at truecenter

screen collar_descargado_screen():
    frame:
        background Solid("#000")  # Fondo negro
        xfill True
        yfill True
        add "collar_descargado.png" at truecenter

screen logo_screen():
    frame:
        background Solid("#000")  # Fondo negro
        xfill True
        yfill True
        add "logo.png" at truecenter

# Pantalla de entrada de nombre
screen name_input():
    frame:
        xalign 0.5
        yalign 0.5
        vbox:
            spacing 10
            label "Elige el nombre de tu personaje"
            textbutton "Elegir mi nombre" action [Show("input_name"), Hide("name_input")]
            textbutton "Elegir nombre predeterminado (Odiseo)" action [SetVariable("player_name", odiseo_name), Hide("name_input"), Show("display_name")]

# Pantalla de entrada de texto para el nombre
screen input_name():
    frame:
        xalign 0.5
        yalign 0.5
        vbox:
            spacing 10
            label "Introduce tu nombre:"
            input value VariableInputValue("temp_name") length 20 allow "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
            textbutton "Confirmar" action [SetVariable("player_name", temp_name), Hide("input_name"), Show("display_name")]

# Pantalla principal con el mensaje
screen display_name():
    vbox:
        align (0.5, 0.5)
        spacing 20
        label "Tu nombre es [player_name]"
        textbutton "Continuar" action[SetVariable("odiseo", Character(player_name, color="#c8ffc8")),Hide("display_name"), Return()]

transform full_screen:
    xpos 0.5
    ypos 0.5
    xanchor 0.5
    yanchor 0.5
    xsize config.screen_width
    ysize config.screen_height

# Juego principal
label start:
    call screen name_input
    jump game_start
    return

label game_start:
    hide screen collar_descargado_screen
    hide screen collar_cargado_screen
    show screen logo_screen with dissolve
    pause 2.0
    hide screen logo_screen with dissolve
    show screen mostrar_estado_corazon
    scene habitacion at full_screen with dissolve 

    play sound sfx_telefono
    pause 2.0

    #play music bgm_grillos

    show odiseo_dormido at left
    show penelope_neutra at right

    penelope "¿Hola? ¿[player_name]? ¿Estas ahí?"
    odiseo "¿Penélope? ¿Qué haces despierta a esta hora? ¿No deberías estar dormida ya?"
    penelope "Sí, perdón por molestarte a esta hora, pero necesitaba preguntarte algo."

    hide odiseo_dormido
    show odiseo_neutro at left

    odiseo "Okey, dime, ¿qué pasa?"

    hide penelope_neutra
    show penelope_silueta at right

    penelope "..."
    stop music

    pause 3.0

    penelope "Esperaba tu llamado ¿o no piensas disculparte por lo que hiciste hoy en el colegio?"

    menu:
        "En serio quieres seguir con eso.":
            jump opcion_1

        "Perdón, creí que estabas molesta.":
            jump opcion_2

label opcion_1:
    $ estado_corazon = "Amarillo"
    $ puntaje_penelope = puntaje_penelope + 3
    hide odiseo_neutro
    show odiseo_hartazgo at left

    odiseo "¿En serio quieres seguir con eso? Ya te dije que no miré a ninguna chica, solo pasó por donde yo miraba."

    hide penelope_silueta
    show penelope_victima at right

    penelope "Eres un inmaduro, no sé si aún te sigo gustando, me pones muy insegura Odiseo."

    hide odiseo_hartazgo
    show odiseo_romantico at left

    odiseo "Sos la única mujer en la que pienso Penélope, y siempre te lo dije."

    jump respuesta_penelope

label opcion_2:
    $ estado_corazon = "Amarillo"
    $ puntaje_penelope = puntaje_penelope + 3
    hide odiseo_neutro
    show odiseo_triste at left

    odiseo "Perdón, creí que estabas molesta y decidí darte tu espacio."

    hide penelope_silueta
    show penelope_enojada at right

    penelope "¡CLARO QUE ESTABA MOLESTA! Pero quería escucharte, no me gustó lo que pasó hoy."

    hide odiseo_triste
    show odiseo_romantico at left

    odiseo "Lo sé, pero ya te dije que no estaba mirando a ninguna chica, mis ojos son solo para vos."

    jump respuesta_penelope

label respuesta_penelope:
    hide penelope_enojada
    show penelope_silueta at right

    penelope "Es siempre lo mismo con vos, piensas que con un par de palabras bonitas me tienes a tus pies. Bueno, mañana no voy a ir al colegio, no me siento muy bien, y más vale que no te quites el collar que te regalé."

    hide odiseo_romantico
    show odiseo_feliz at left

    odiseo "Tranquila, no pienso sacármelo. Que descanses."

    #play sound sfx_cortar_llamada

    odiseo "Qué mujer intensa, mañana veré si la voy a visitar a su casa."

    scene black with dissolve
    pause 1.0

    jump escena_collar

label escena_2:
    scene black
    hide screen collar_descargado_screen
    hide screen collar_cargado_screen
    show screen mostrar_estado_corazon
    odiseo "HOLAAAA SE FINALIZO TODO"
    return

label escena_collar:
    scene black
    show screen mostrar_estado_corazon
    if collar_cargado:
        show screen collar_cargado_screen
        #play sound sfx_collar_brilla
        narrator "En este momento tan decisivo para [player_name], él recuerda su collar. Recuerda a Penélope. Recuerda lo que ella significa para él. Y con eso, él comienza a olvidar todo lo sucedido recién."

        menu:
            "[player_name] aprieta el collar":
                $ collar_cargado = False
                jump collar_opcion_1a
            "[player_name] no aprieta el collar":
                jump collar_opcion_1b
    else:
        show screen collar_descargado_screen
        narrator "En este momento tan decisivo para [player_name], él recuerda su collar. Pero este ya no tiene el mismo valor emocional, la misma importancia, que solía tener. Ya nada puede cambiar la decisión de [player_name]."
        jump collar_opcion_2

label collar_opcion_1a:
    hide screen collar_cargado_screen
    narrator "[player_name] aprieta el collar. Cuando vuelve en sí, está de vuelta donde todo comenzó a salirse de rumbo..."
    # Transición a la escena y decisión primaria de origen
    jump game_start

label collar_opcion_1b:
    hide screen collar_cargado_screen
    narrator "[player_name] elige no apretar el collar. Él elige no aferrarse al pasado. Elige seguir adelante..."
    # Transición a un final dado
    jump escena_2

label collar_opcion_2:
    hide screen collar_descargado_screen
    narrator "En este momento tan decisivo para [player_name], él recuerda su collar. Pero este ya no tiene el mismo valor emocional, la misma importancia, que solía tener. Ya nada puede cambiar la decisión de [player_name]."
    # Transición a un final dado
    jump escena_2
