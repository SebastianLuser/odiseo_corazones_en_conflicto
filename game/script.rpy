define odiseo_name = "Odiseo"
define odiseo = Character("Odiseo", color="#c8ffc8")
define penelope = Character("Penélope", color="#e7d532")
define afrodita = Character("Afrodita", color="#ec7171")
define narrator = Character(None)

default player_name = "Odiseo"

# Definimos las imágenes de los personajes
image odiseo_dormido = "odiseo_dormido.png"
image odiseo_neutro = "odiseo_neutro.png"
image odiseo_hartazgo = "odiseo_hartazgo.png"
image odiseo_romantico = "odiseo_romantico.png"
image odiseo_triste = "odiseo_triste.png"
image odiseo_feliz = "odiseo_feliz.png"
image odiseo_preocupado = "odiseo_triste.png"

image penelope_neutra = "penelope_neutra.png"
image penelope_enojada = "penelope_enojada.png"
image penelope_victima = "penelope_triste.png"
image penelope_feliz = "penelope_feliz.png"

image afrodita_neutra = "afrodita_neutra.png"
image afrodita_enojada = "afrodita_enojada.png"
image afrodita_traviesa = "afrodita_traviesa.png"
image afrodita_feliz = "afrodita_traviesa.png"

image atenea_neutra = "atenea_neutra.png"
image atenea_enojada = "atenea_enojada.png"
image atenea_traviesa = "atenea_feliz.png"

image corazon_gris = "corazon_gris.png"
image corazon_amarillo = "corazon_amarillo.png"
image corazon_rojo = "corazon_rojo.png"
image corazon_marron = "corazon_marron.png"

# Fondo de la habitación
image habitacion = "habitacion.png"
image habitacion_manana = "habitacion_manana.png"
image pasillo_escuela = "pasillo_01.png"
image aula_escuela = "aula_vacia.png"
image fondo_corazones = "fondo_corazones.png"

image logo = "logo.png"

image collar_descargado = "collar_descargado.png"
image collar_cargado = "collar_cargado.png"

image celular_odiseo = "odiseo_celular.png"

# SFX y BGM
define sfx_telefono = "telefono_sonando.mp3"
define bgm_grillos = "grillos_y_brisa.wav"
define sfx_cortar_llamada = "cortar_llamada.wav"
define sfx_collar_brilla = "collar_brilla.wav"

define sfx_pajaros = "pajaros_cantando.wav"
define bgm_fondo01 = "musica_fondo01.mp3"

define sfx_campana_escuela = "campana_escuela.mp3"
define bgm_murmullos = "murmullos.wav"

define sfx_puerta_cierra = "puerta_cierra.wav"
define bgm_saxofon_afrodita = "saxofon_afrodita.wav"

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

screen celular_odiseo_screen():
    frame:
        background Solid("#000")  # Fondo negro
        xfill True
        yfill True
        add "odiseo_celular.png" at truecenter

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

    play music bgm_grillos

    show odiseo_dormido at left
    show penelope_neutra at right

    penelope "¿Hola? ¿[player_name]? ¿Estas ahí?"
    odiseo "¿Penélope? ¿Qué haces despierta a esta hora? ¿No deberías estar dormida ya?"
    penelope "Sí, perdón por molestarte a esta hora, pero necesitaba preguntarte algo."

    hide odiseo_dormido
    show odiseo_neutro at left

    odiseo "Okey, dime, ¿qué pasa?"
    hide penelope_neutra
    show penelope_victima at right
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

    penelope "Eres un inmaduro, no sé si aún te sigo gustando, me pones muy insegura Odiseo."

    hide odiseo_hartazgo
    show odiseo_romantico at left

    odiseo "Eres la única mujer en la que pienso Penélope, y siempre te lo dije."

    jump respuesta_penelope

label opcion_2:
    $ estado_corazon = "Amarillo"
    $ puntaje_penelope = puntaje_penelope + 3
    hide odiseo_neutro
    show odiseo_triste at left

    odiseo "Perdón, creí que estabas molesta y decidí darte tu espacio."

    hide penelope_victima
    show penelope_enojada at right

    penelope "¡CLARO QUE ESTABA MOLESTA! Pero quería escucharte, no me gustó lo que pasó hoy."

    hide odiseo_triste
    show odiseo_romantico at left

    odiseo "Lo sé, pero ya te dije que no estaba mirando a ninguna chica, mis ojos son solo para ti."

    jump respuesta_penelope

label respuesta_penelope:

    penelope "Es siempre lo mismo contigo, piensas que con un par de palabras bonitas me tienes a tus pies. Bueno, mañana no voy a ir al colegio, no me siento muy bien, y más vale que no te quites el collar que te regalé."

    hide odiseo_romantico
    show odiseo_feliz at left

    odiseo "Tranquila, no pienso sacármelo. Que descanses."

    play sound sfx_cortar_llamada

    hide penelope_enojada

    odiseo "{i}Qué mujer intensa, mañana veré si la voy a visitar a su casa.{/i}"

    scene black with dissolve
    pause 3.0

    jump escena_2

label escena_2:
    scene black
    hide screen collar_descargado_screen
    hide screen collar_cargado_screen
    show screen mostrar_estado_corazon
    scene habitacion_manana at full_screen with dissolve
    play sound sfx_pajaros
    play music bgm_fondo01

    show odiseo_neutro at left

    odiseo "{i}A veces no logro entender a esta mujer, siempre actúa como si yo le estuviese escondiendo algo. Y ¿por qué sintió la necesidad de recordarme el collar? Bueno, supongo que voy a tener mis respuestas cuando la vea después de clases.{/i}"

    hide odiseo_neutro

    scene black with dissolve
    stop music
    pause 3.0

    jump escena_3

label escena_3:
    scene black
    hide screen collar_descargado_screen
    hide screen collar_cargado_screen
    show screen mostrar_estado_corazon
    scene pasillo_escuela at full_screen with dissolve
    play sound sfx_campana_escuela
    play music bgm_murmullos
    play music bgm_fondo01
    show odiseo_preocupado at left

    odiseo "Me pregunto si Penélope se siente mejor ya. ¿Tal vez me envió algún mensaje?"

    show screen celular_odiseo_screen
    odiseo "{i}Sin mensajes todavia{/i}"
    pause 4.0
    hide screen celular_odiseo_screen

    hide odiseo_preocupado
    show odiseo_triste at left

    odiseo "Supongo que seguirá dormida, como no se sentía muy bien."

    show afrodita_feliz at right

    afrodita "¡Buen día Odiseo! Tenes mala cara... ¿Se pelearon con Penélope? ¿¡Ya no están juntos!?"

    odiseo "Hola Afrodita. Y no, no nos separamos. Seguimos juntos. Penélope no vino porque está enferma, y me tiene preocupado."

    hide afrodita_feliz
    show afrodita_traviesa at right

    afrodita "Ay noooooo, que peeeeeena... En fin, mi celular está casi muerto ya y me olvidé el cargador en el aula. ¡AY, YA SE! Odiseo, ¿no me acompañas a buscarlo?"

    odiseo "¿En serio? ¿Ese es tu mejor movimiento? Ayer estabas más creativa."

    afrodita "JAJA, no sé de qué hablas tarado, dale vamos."

    menu:
        "Rechazar el pedido de Afrodita.":
            jump opcion_1_escena_3

        "Aceptar el pedido de Afrodita.":
            jump opcion_2_escena_3

label opcion_1_escena_3:
    hide odiseo_triste
    show odiseo_hartazgo at left

    odiseo "No, Afrodita. Ya estoy llegando tarde, no me quiero demorar más. Nos estamos viendo."

    hide odiseo_hartazgo
    hide afrodita_traviesa
    show afrodita_enojada at right

    pause 2.0
    hide afrodita_enojada
    scene black with dissolve
    stop music
    pause 2.0

    jump escena_5


label opcion_2_escena_3:
    hide odiseo_triste
    show odiseo_romantico at left
    $ puntaje_afrodita = puntaje_afrodita + 2
    odiseo "Bueno, igual ya estoy un poco tarde. Supongo que no pasa nada si pasamos a buscar tu cargador."

    hide afrodita_traviesa
    show afrodita_feliz at right

    afrodita "Sí, son solo tres segundos. ¡Vamos!"

    hide afrodita_feliz
    pause 1.0
    hide odiseo_romantico

    scene black with dissolve
    stop music
    pause 1.0

    jump escena_4

label escena_4:
    scene black
    hide screen collar_descargado_screen
    hide screen collar_cargado_screen
    show screen mostrar_estado_corazon
    scene aula_escuela at full_screen with dissolve
    play sound sfx_puerta_cierra
    play music bgm_saxofon_afrodita

    show odiseo_neutro at left

    afrodita "¡Ahí está! Listo, ya no me voy a quedar sin batería."

    show afrodita_feliz at right

    odiseo "Cuidado, no vayas a romper el escritorio, que vi que subiste un poco de peso."

    afrodita "¿Ah sí? Entonces se ve que estuviste muy atento a mi figura."

    odiseo "Ya quisieras, bueno vamos que no quiero llegar tarde."

    afrodita "Desde cuando sos tan aburrido, si tienes excelentes calificaciones."

    hide odiseo_neutro

    show odiseo_feliz at left

    odiseo "Por suerte sí, pero a vos también te iría igual de bien si estudiaras un poco más."

    afrodita "Tampoco quiero parecer una nerd. Tengo cosas más importantes que hacer."

    hide odiseo_feliz
    show odiseo_romantico at left

    odiseo "Ah ¿sí? ¿Cómo qué?"

    afrodita "Todavía no logro conseguir una pareja para ir al baile. Todos me resultan muy aburridos o feos. Creo que solo hay una persona indicada."

    afrodita "ODISEO, los dos sabemos que la rubia te tiene harto. ¿Por qué no le damos una sorpresa y vienes al baile conmigo?"

    menu:
        "Rechazar a Afrodita, y seguir con tu día.":
            jump opcion_1_acto_1_escena_4

        "Aceptar a Afrodita, y comenzar una nueva relación con ella.":
            jump opcion_2_acto_1_escena_4

label opcion_1_acto_1_escena_4:
    hide odiseo_romantico
    show odiseo_feliz at left
    
    odiseo "A ver, creo que el tinte te quema las ideas, no voy a ir contigo al baile."

    odiseo "Y toma, come este chicle casi me despeinas con tu aliento."

    hide afrodita_feliz
    show afrodita_enojada at right

    afrodita "No puedo creer que A MI, me estés diciendo esto ODISEO ¡voy a hacer lo posible para que tu relación con Penélope esté arruinada!"

    hide afrodita_enojada
    play sound sfx_puerta_cierra
    hide odiseo_feliz
    pause 2.0

    scene black with dissolve
    stop music
    pause 1.0

    jump escena_5

label opcion_2_acto_1_escena_4:
    $ puntaje_afrodita = puntaje_afrodita + 2
    scene fondo_corazones at full_screen with dissolve

    odiseo "¿Sabes qué? Tenés razón, PENÉLOPE siempre está con algún problema, y la verdad siempre me gustaron más las pelirrojas."

    narrator "Cuando las cosas funcionan no las cambies, y cuando no funcionan cámbialas y mejor si es con una pelirroja, Odiseo y Afrodita pasaron todo el día juntos, para después de clases acompañarla a la casa, espera ¿Sus padres no estaban de viaje?"

    hide odiseo_romantico
    hide afrodita_feliz
    stop music

    scene black with dissolve
    pause 3.0

    jump escena_collar_afrodita

label escena_5:
    # Continuar con la siguiente escena aquí
    return

label escena_collar_afrodita:
    scene black
    show screen mostrar_estado_corazon
    if collar_cargado:
        show screen collar_cargado_screen
        play sound sfx_collar_brilla
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
    $ puntaje_afrodita = 0
    narrator "[player_name] aprieta el collar. Cuando vuelve en sí, está de vuelta donde todo comenzó a salirse de rumbo..."
    # Transición a la escena y decisión primaria de origen
    jump escena_3

label collar_opcion_1b:
    hide screen collar_cargado_screen
    narrator "[player_name] elige no apretar el collar. Él elige no aferrarse al pasado. Elige seguir adelante..."
    # Transición a un final dado
    jump escena_final_afrodita

label collar_opcion_2:
    hide screen collar_descargado_screen
    narrator "En este momento tan decisivo para [player_name], él recuerda su collar. Pero este ya no tiene el mismo valor emocional, la misma importancia, que solía tener. Ya nada puede cambiar la decisión de [player_name]."
    # Transición a un final dado
    jump escena_final_afrodita
