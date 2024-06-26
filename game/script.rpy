define odiseo_name = "Odiseo"
define odiseo = Character("Odiseo", color="#c8ffc8")
define penelope = Character("Penélope", color="#e7d532")
define afrodita = Character("Afrodita", color="#ec7171")
define atenea = Character("Atenea", color="#633c0a")
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
image odiseo_sorprendido = "odiseo_sorprendido.png"

image penelope_neutra = "penelope_neutra.png"
image penelope_enojada = "penelope_enojada.png"
image penelope_victima = "penelope_triste.png"
image penelope_feliz = "penelope_feliz.png"
image penelope_avergonzada = "penelope_avergonzada.png"
image penelope_feliz_llorando = "penelope_feliz_llorando.png"

image afrodita_neutra = "afrodita_neutra.png"
image afrodita_enojada = "afrodita_enojada.png"
image afrodita_traviesa = "afrodita_traviesa.png"
image afrodita_feliz = "afrodita_traviesa.png"

image atenea_neutra = "atenea_neutra.png"
image atenea_enojada = "atenea_enojada.png"
image atenea_traviesa = "atenea_feliz.png"

image calypso_silueta = "calypso_desenfocada.png"

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
image aula_llena = "aula_llena.png"
image aula_ajedrez = "aula_ajedrez.png"
image aula_musica = "aula_musica.png"

image puerta_casa_penelope = "puerta_penelope.png"

image final_odiseo_afrodita = "aula_corazones.png"

image calle_tarde = "calle_tarde.png"

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

define bgm_piano_atenea = "piano_atenea.wav"

define sfx_timbre_casa = "timbre_casa.wav"
define bgm_violin_penelope = "violin_penelope.mp3"

define sfx_tocar_puerta = "tocar_puerta.wav"

define sfx_llaves_puerta = "llaves_puerta.wav"

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

    penelope "¿Hola?{w=1.0}¿[player_name]?{w=1.0}¿Estas ahí?"
    odiseo "¿Penélope?{w=1.0}¿Qué haces despierta a esta hora?{w=1.0}¿No deberías estar dormida ya?"
    penelope "Sí, perdón por molestarte a esta hora, pero necesitaba preguntarte algo."

    hide odiseo_dormido
    show odiseo_neutro at left

    odiseo "Okey{w=.5}, dime{w=.5}, ¿qué pasa?"
    hide penelope_neutra
    show penelope_victima at right
    penelope "{w=.5}...{w=.5}"

    pause 3.0

    penelope "Esperaba tu llamado{w=1.0} ¿o no piensas disculparte por lo que hiciste hoy en el colegio?"

    menu:
        "En serio quieres seguir con eso.":
            jump opcion_1

        "Perdón, creí que estabas molesta.":
            jump opcion_2

label opcion_1:
    $ puntaje_penelope = puntaje_penelope + 3
    hide odiseo_neutro
    show odiseo_hartazgo at left

    odiseo "¿En serio quieres seguir con eso?{w=1.0} Ya te dije que no miré a ninguna chica{w=0.5}, solo pasó por donde yo miraba."

    penelope "Eres un inmaduro, no sé si aún te sigo gustando{w=0.5}, me pones muy insegura [player_name]."

    hide odiseo_hartazgo
    show odiseo_romantico at left

    odiseo "Eres la única mujer en la que pienso Penélope{w=0.5}, y siempre te lo dije."

    jump respuesta_penelope

label opcion_2:
    $ puntaje_penelope = puntaje_penelope + 3
    hide odiseo_neutro
    show odiseo_triste at left

    odiseo "Perdón{w=0.5}, creí que estabas molesta y decidí darte tu espacio."

    hide penelope_victima
    show penelope_enojada at right

    penelope "¡CLARO QUE ESTABA MOLESTA!"
    penelope "Pero quería escucharte{w=0.5}, no me gustó lo que pasó hoy."
    hide odiseo_triste
    show odiseo_romantico at left

    odiseo "Lo sé{w=0.5}, pero ya te dije que no estaba mirando a ninguna chica{w=0.5}, mis ojos son solo para ti."

    jump respuesta_penelope

label respuesta_penelope:

    penelope "Es siempre lo mismo contigo{w=0.5}, piensas que con un par de palabras bonitas me tienes a tus pies."
    penelope "Bueno{w=0.5}, mañana no voy a ir al colegio{w=0.5}, no me siento muy bien{w=0.5}, y más vale que no te quites el collar que te regalé."
    hide odiseo_romantico
    show odiseo_feliz at left

    odiseo "Tranquila{w=0.5}, no pienso sacármelo."
    odiseo "Que descanses."
    play sound sfx_cortar_llamada

    hide penelope_enojada

    odiseo "{i}Qué mujer intensa{w=0.5}, mañana veré si la voy a visitar a su casa.{/i}"

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

    pause 2.0

    play music bgm_fondo01

    show odiseo_neutro at left

    pause 1.0

    odiseo "{i}A veces no logro entender a esta mujer{w=0.5}, siempre actúa como si yo le estuviese escondiendo algo.{/i}"
    odiseo "{i}Y{w=1.0} ¿por qué sintió la necesidad de recordarme el collar?{w=0.5} Bueno{w=0.5}, supongo que voy a tener mis respuestas cuando la vea después de clases.{/i}"
    hide odiseo_neutro

    scene black with dissolve
    stop music
    pause 2.0

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
    $ puntaje_afrodita = 0 

    odiseo "Me pregunto si Penélope se siente mejor ya.{w=1.0} ¿Tal vez me envió algún mensaje?"

    show screen celular_odiseo_screen
    odiseo "{i}Sin mensajes todavia{/i}"
    pause 2.0
    hide screen celular_odiseo_screen

    hide odiseo_preocupado
    show odiseo_triste at left

    odiseo "Supongo que seguirá dormida{w=0.5}, como no se sentía muy bien."

    show afrodita_feliz at right

    afrodita "¡Buen día [player_name]!{w=1.0} Tenes mala cara...{w=1.0} ¿Se pelearon con Penélope?{w=0.5} ¿¡Ya no están juntos!?"

    odiseo "Hola Afrodita.{w=1.0} Y no{w=0.5}, no nos separamos.{w=1.0} Seguimos juntos."
    odiseo "Penélope no vino porque está enferma{w=0.5}, y me tiene preocupado."
    hide afrodita_feliz
    show afrodita_traviesa at right

    afrodita "Ay noooooo{w=0.5}, que peeeeeena...{w=1.0} En fin{w=0.5}, mi celular está casi muerto ya y me olvidé el cargador en el aula."
    afrodita "¡AY!{w=1.0} ¡YA SE!{w=0.5} [player_name]{w=0.5}, ¿no me acompañas a buscarlo?"
    odiseo "¿En serio? {w=1.0}¿Ese es tu mejor movimiento?{w=1.0} Ayer estabas más creativa."

    afrodita "JAJA{w=0.5}, no sé de qué hablas tarado{w=0.5}, dale vamos."

    menu:
        "Rechazar el pedido de Afrodita.":
            jump opcion_1_escena_3

        "Aceptar el pedido de Afrodita.":
            jump opcion_2_escena_3

label opcion_1_escena_3:
    hide odiseo_triste
    show odiseo_hartazgo at left

    odiseo "No{w=0.5}, Afrodita.{w=1.0} Ya estoy llegando tarde{w=0.5}, no me quiero demorar más.{w=1.0} Nos estamos viendo."

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
    $ puntaje_afrodita = puntaje_afrodita + 2
    hide odiseo_triste
    show odiseo_romantico at left
    odiseo "Bueno{w=0.5}, igual ya estoy un poco tarde.{w=1.0} Supongo que no pasa nada si pasamos a buscar tu cargador."

    hide afrodita_traviesa
    show afrodita_feliz at right

    afrodita "Sí{w=0.5}, son solo tres segundos.{w=1.0} ¡Vamos!"

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

    afrodita "¡Ahí está!{w=1.0} Listo{w=0.5}, ya no me voy a quedar sin batería."

    show afrodita_feliz at right

    odiseo "Cuidado{w=0.5}, no vayas a romper el escritorio{w=0.5}, que vi que subiste un poco de peso."

    afrodita "¿Ah sí?{w=1.0} Entonces se ve que estuviste muy atento a mi figura."

    odiseo "Ya quisieras{w=0.5}, bueno vamos que no quiero llegar tarde."

    afrodita "Desde cuando sos tan aburrido{w=0.5}, si tienes excelentes calificaciones."

    hide odiseo_neutro

    show odiseo_feliz at left

    odiseo "Por suerte sí{w=0.5}, pero a vos también te iría igual de bien si estudiaras un poco más."

    afrodita "Tampoco quiero parecer una nerd.{w=1.0} Tengo cosas más importantes que hacer."

    hide odiseo_feliz
    show odiseo_romantico at left

    odiseo "Ah {w=1.0}¿sí?{w=1.0} ¿Cómo qué?"

    afrodita "Todavía no logro conseguir una pareja para ir al baile.{w=1.0} Todos me resultan muy aburridos o feos."
    afrodita "Creo que solo hay una persona indicada."
    afrodita "[player_name]{w=0.5}, los dos sabemos que la rubia te tiene harto.{w=1.0} ¿Por qué no le damos una sorpresa y vienes al baile conmigo?"

    menu:
        "Rechazar a Afrodita y seguir con tu día.":
            jump opcion_1_acto_1_escena_4

        "Aceptar a Afrodita y comenzar una nueva relación con ella.":
            jump opcion_2_acto_1_escena_4

label opcion_1_acto_1_escena_4:
    hide odiseo_romantico
    show odiseo_feliz at left
    
    odiseo "A ver{w=0.5}, creo que el tinte te quema las ideas{w=0.5}, no voy a ir contigo al baile."

    odiseo "Y toma{w=0.5}, come este chicle casi me despeinas con tu aliento."

    hide afrodita_feliz
    show afrodita_enojada at right

    afrodita "No puedo creer que {b}A MI{/b}{w=0.5}, me estés diciendo esto [player_name]{w=1.0} ¡voy a hacer lo posible para que tu relación con Penélope esté arruinada!"

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

    show odiseo_romantico at left
    show afrodita_feliz at right

    odiseo "¿Sabes qué?{w=1.0} Tenés razón{w=0.5}, PENÉLOPE siempre está con algún problema{w=0.5}, y la verdad siempre me gustaron más las pelirrojas."

    hide odiseo_romantico
    hide afrodita_feliz
    stop music

    scene black with dissolve
    pause 3.0

    jump escena_collar_afrodita

label final_afrodita:
    scene final_odiseo_afrodita at full_screen with dissolve
    play music bgm_saxofon_afrodita
    narrator "Cuando las cosas funcionan no las cambies{w=0.5}, y cuando no funcionan cámbialas y mejor si es con una pelirroja{w=0.5}, [player_name] y Afrodita pasaron todo el día juntos{w=0.5}, para después de clases acompañarla a la casa{w=0.5}, espera {w=1.0}¿Sus padres no estaban de viaje?"

    return
    
label escena_5:
    scene black with dissolve
    hide screen collar_descargado_screen
    hide screen collar_cargado_screen
    show screen mostrar_estado_corazon
    scene aula_llena at full_screen with dissolve
    play music bgm_murmullos

    pause 2.0

    stop music
    play music bgm_fondo01

    show odiseo_preocupado at left

    odiseo "Qué clase más aburrida... {w=1.0}¿Qué estará haciendo Penélope?{w=1.0} Últimamente discutimos demasiado,{w=0.5} no sé qué pensar."

    narrator "{color=#fff}¡[player_name]!{w=1.0} ¡ATENCIÓN A MI CLASE!{w=1.0} QUE SUS NOTAS NO SE LE SUBAN A LA CABEZA.{/color}"

    odiseo "Disculpe profesor{w=0.5}, es solo que no dormí bien."

    play sound sfx_campana_escuela
    hide screen aula_llena
    scene pasillo_escuela at full_screen with dissolve
    show atenea_neutra at right

    atenea "Buenos días [player_name].{w=1.0} Me resulta extraño que el profesor tenga que llamarte la atención{w=1.0} ¿Está todo bien?"

    show odiseo_neutro at left

    odiseo "Hola Atenea.{w=1.0} Realmente no sé qué pensar{w=0.5}, últimamente con Penélope solo discutimos."

    atenea "¿A qué se debe eso?{w=1.0} Pensaste en hablarlo con ella{w=0.5}, las mejores soluciones a veces son las más fáciles."

    odiseo "Ella piensa que soy un mujeriego{w=0.5}, y no es así.{w=1.0} Me gustaría hablarlo pero hoy no vino a clases{w=0.5}, se sentía enferma."

    atenea "Bueno{w=0.5}, yo ahora tengo que ir al club de Ajedrez{w=0.5}, pero si quieres seguir hablando{w=0.5}, acompáñame y jugamos una partida."

    menu:
        "Aceptar la ayuda de Atenea.":
            jump opcion_1_acto_1_escena_5

        "Rechazar la ayuda de Atenea.":
            jump opcion_2_acto_1_escena_5

label opcion_1_acto_1_escena_5:
    $ puntaje_atenea  = puntaje_atenea + 2 
    hide odiseo_neutro
    show odiseo_feliz at left

    odiseo "Me parece bien{w=0.5}, te voy a dejar jugar con blancas a ver si es suficiente ventaja."

    hide atenea_neutra
    show atenea_feliz at right

    atenea "JA JA{w=0.5}, sabes muy bien que nunca pudiste ganarme{w=0.5}, bueno vamos."

    hide odiseo_feliz
    hide atenea_feliz

    scene black with dissolve
    stop music
    play sound sfx_puerta_cierra
    pause 2.0

    jump escena_6

label opcion_2_acto_1_escena_5:
    hide odiseo_neutro
    show odiseo_feliz at left

    odiseo "No{w=0.5}, tranquila.{w=1.0} Ya le voy a poder encontrar la vuelta{w=0.5}, además no tengo ganas de humillarte."

    hide atenea_neutra
    show atenea_feliz at right

    atenea "Nos vemos más tarde entonces{w=0.5}, y sabes muy bien que nunca me ganaste en una partida [player_name]."

    show odiseo_dormido at left

    odiseo "¡MIRA LA HORA!{w=1.0} Ya se me hizo tarde{w=0.5}, le prometí al club de música ir a escucharlos{w=1.0} ¡Nos vemos!"

    hide odiseo_dormido
    hide atenea_feliz
    show atenea_triste at right

    pause 2.0
    hide atenea_triste

    scene black with dissolve
    stop music
    pause 2.0

    jump escena_8

label escena_6:
    scene black
    show screen mostrar_estado_corazon
    scene aula_ajedrez at full_screen with dissolve
    play music bgm_piano_atenea

    show odiseo_preocupado at left
    show atenea_neutra at right

    odiseo "Entonces quieres que te gane en una partida de Ajedrez{w=0.5} ¿y eso se supone que me ayude a resolver mis problemas?"

    atenea "Precisamente.{w=1.0} En mi opinión{w=0.5}, no existe manera más eficaz de reflexionar que jugando una partida de Ajedrez."

    hide odiseo_preocupado
    show odiseo_neutro at left

    odiseo "De hecho{w=0.5}, sí las hay{w=0.5}, pero está bien{w=0.5}, vamos tú eres blancas."
    hide odiseo_neutro
    hide atenea_neutra
    narrator "La partida entre [player_name] y ATENEA termina tan rápidamente como comenzó."

    show odiseo_sorprendido at left

    odiseo "¡¿Tan rápido?!{w=1.0} Parece que perdí la práctica{w=0.5}, últimamente estuve jugando mucho con Penélope."

    show atenea_feliz at right

    atenea "La práctica es la que hace al maestro así que podrías practicar más seguido conmigo.{w=1.0} Además{w=0.5}, antes durabas un poco más."

    odiseo "Igualmente{w=0.5}, no entiendo cuál fue el error{w=0.5}, en ningún momento comprometí mi reina e igualmente perdí."

    atenea "El problema con tu estrategia fue concentrarte más en la reina que en el rey.{w=1.0} Es verdad que la reina es la pieza más fuerte del tablero{w=0.5}, pero la más importante siempre va a ser el rey."

    hide atenea_feliz
    show atenea_neutra at right

    atenea "¿Se entiende cuál es mi punto?"

    hide odiseo_sorprendido
    show odiseo_preocupado at left

    odiseo "Eres bastante bonita cuando te pones reflexiva."

    atenea "[player_name]{w=0.5}, esto se supondría que sería una charla sobre tú y Penélope{w=0.5}, no cambies el tema."

    menu:
        "Pedirle ayuda directa a ATENEA.":
            jump opcion_1_acto_1_escena_6

        "Razonarlo vos mismo.":
            jump opcion_2_acto_1_escena_6

label opcion_1_acto_1_escena_6:
    $ puntaje_atenea  = puntaje_atenea + 2 
    hide odiseo_preocupado
    show odiseo_neutro at left

    odiseo "Suena como que tú tienes una idea{w=1.0} ¿En qué pensaste Atenea?"

    atenea "No estoy diciendo que necesariamente sea así{w=0.5}, pero tal vez priorizas demasiado los sentimientos de Penélope por sobre los tuyos.{w=1.0} Pones la relación{w=0.5}, por sobre ti."

    hide odiseo_neutro
    show odiseo_sorprendido at left

    odiseo "¿Estás diciendo que debería terminar con Penélope?{w=1.0} ¿Por qué?"

    atenea "Solo te estoy ayudando a pensar un poco fuera de la caja.{w=1.0} Tal vez lo mejor para vos ahora mismo sería concentrarte en vos mismo."

    show odiseo_neutro at left
    odiseo "Lo que dices tiene sentido.{w=1.0} Bueno{w=0.5}, nos vemos Atenea.{w=0.5} Gracias."

    hide atenea_neutra
    odiseo "{i}Le mandaré un mensaje a Penélope.{w=0.5} Esta relación no da para mucho más.{/i}"
    hide odiseo_neutro

    jump escena_collar_atenea

    
label opcion_2_acto_1_escena_6:
    hide odiseo_preocupado
    show odiseo_neutro at left

    odiseo "Okey{w=0.5}, era solo un chiste{w=0.5}, pero creo que esto realmente me ayudó."

    show odiseo_feliz at left

    odiseo "Muchas gracias{w=0.5}, Atenea.{w=1.0} Siempre es bueno hablar contigo{w=0.5}, pero ahora mejor iré a ver a Penélope{w=0.5}, nos vemos."

    hide atenea_neutra
    show atenea_feliz at right

    atenea "Me alegra haber sido de ayuda.{w=1.0} Nos vemos [player_name].{w=1.0} Saluda a Penélope de mi parte."

    hide odiseo_feliz
    hide atenea_feliz

    scene black with dissolve
    stop music
    pause 2.0
    jump escena_7

label final_atenea:
    show screen celular_odiseo_screen
    narrator "[player_name] ve su celular{w=0.5}, y sin aún señales de Penélope{w=0.5}, decide escribirle un mensaje en el que le explica que lo mejor para ambos será que corten la relación{w=0.5}, el aún es muy joven y no se siente preparado para estar en pareja."
    hide celular_odiseo_screen with dissolve

    scene black with dissolve
    pause 1.0
    stop music
    return

label escena_7:
    scene black
    show screen mostrar_estado_corazon
    scene puerta_casa_penelope at full_screen with dissolve
    play music bgm_violin_penelope

    show odiseo_preocupado at left
    play sound sfx_timbre_casa

    odiseo "¡Penélope! {w=1.0}¿Estás en casa?"

    pause 1.0

    play sound sfx_tocar_puerta

    pause 1.0

    play sound sfx_llaves_puerta
    show penelope_feliz at right

    penelope "¡[player_name]!{w=1.0} ¡Hola!{w=0.5} ¿Qué haces aquí?{w=0.5} ¿No deberías estar en clases aun?"

    hide odiseo_preocupado
    show odiseo_feliz at left

    odiseo "Debería{w=0.5}, sí{w=0.5}, pero quería ver cómo estabas{w=0.5}, me tenías muy preocupado."

    hide penelope_feliz
    show penelope_enojada at right
    
    penelope "¿A sí?{w=1.0} ¿Y desde cuándo te preocupo tanto? {w=1.0}Anoche no parecías tan preocupado."

    hide odiseo_feliz
    show odiseo_neutro at left

    odiseo "Por favor{w=0.5}, Penélope{w=0.5}, no empieces.{w=1.0} Sabes muy bien que me importas mucho{w=0.5}, y te estuve notando un poco rara últimamente."

    hide penelope_enojada
    show penelope_avergonzada at right

    penelope "¿Rara?{w=0.5} ¿Yo?{w=0.5} Debe ser cosa tuya{w=0.5}, o seguro que la teñida de Afrodita te anda metiendo ideas en la cabeza."

    hide odiseo_neutro
    show odiseo_preocupado at left

    odiseo "Deja de cambiar el tema{w=0.5}, vamos decime qué te anda pasando."

    hide penelope_avergonzada
    show penelope_enojada at right

    penelope "¡Constantemente se te están confesando otras chicas!{w=0.5} Y todas son más lindas{w=0.5}, interesantes e inteligentes que yo."

    hide odiseo_preocupado
    show odiseo_hartazgo at left

    odiseo "¡Eso no es verdad!{w=1.0} Veamos{w=0.5}, sí obviamente hay chicas interesadas en mí."
    
    hide odiseo_hartazgo
    show odiseo_romantico at left
    
    odiseo "Pero tú eres la mujer que quiero para mí."

    hide penelope_enojada
    show penelope_triste at right

    penelope "Y aunque así sea{w=0.5}, no te creo que nunca dudes de eso.{w=0.5} ¿En serio yo soy la única para vos?"

    menu:
        "Admitir que dudas, pero aun así decidís seguir adelante.":
            jump opcion_1_acto_1_escena_7

        "Esconder tus dudas y mentirle a PENÉLOPE.":
            jump opcion_2_acto_1_escena_7

label opcion_1_acto_1_escena_7:
    hide odiseo_romantico
    show odiseo_hartazgo at left

    odiseo "No voy a mentirte{w=0.5}, hay veces en las que puedo llegar a dudar{w=0.5}, pero me acuerdo de lo bien que me siento a tu lado y las dudas se me despejan."

    show penelope_feliz_llorando at right

    penelope "Siempre encuentras la manera de quedar bien parado.{w=1.0} Me gustas mucho{w=0.5}, [player_name]. Ven entra{w=0.5}, más tarde acompáñame a comprar medicamentos."

    hide penelope_feliz_llorando

    pause 1.0

    hide odiseo_hartazgo
    play sound sfx_puerta_cierra
    scene black with dissolve
    stop music
    pause 1.0
    jump escena_collar_penelope_final_1

label final_penelope_1:
    scene black
    show screen mostrar_estado_corazon
    play music bgm_violin_penelope
    scene puerta_casa_penelope at full_screen with dissolve

    narrator "A veces ser honesto es la solución{w=0.5}, otras veces{w=0.5}, no tanto.{w=1.0} Pero mañana será otro día,{w=0.5} nuevas decisiones nos esperan."
    pause 3.0
    scene black with dissolve
    stop music
    return

label opcion_2_acto_1_escena_7:
    hide odiseo_romantico
    show odiseo_dormido at left

    odiseo "¿Dudar?{w=1.0} ¿De qué dudaría?{w=1.0} Eres la mujer más hermosa que conozco,{w=0.5} no sé quién te pone todas esas ideas en la cabeza."

    hide penelope_triste
    show penelope_enojada at right
    penelope "Okey{w=0.5}, debe ser que aún no me siento bien{w=0.5}, han sido días raros{w=0.5}, mejor vuelvo adentro iré a descansar.{w=1.0} Adiós [player_name]."

    hide odiseo_dormido
    show odiseo_triste at left

    odiseo "Sí{w=0.5}, la verdad{w=0.5}, fueron días raros.{w=1.0} Hasta mañana Penélope."
    play sound sfx_puerta_cierra
    hide penelope_enojada
    odiseo "{i}Creo que debería haber sido más sincero con mis sentimientos.{/i}"

    pause 2.0

    hide odiseo_triste

    scene black with dissolve
    stop music
    pause 1.0

    jump escena_collar_penelope_final_2

label final_penelope_2:
    scene black
    show screen mostrar_estado_corazon
    play sound sfx_puerta_cierra
    play music violin_penelope
    scene calle_tarde at full_screen with dissolve
    show odiseo_hartazgo at left

    odiseo "Después de todo sigo sin entenderla{w=0.5}, no sé lo que le molesta y menos aún lo que le gusta.{w=0.5} Encima que vengo a visitarla{w=0.5}, podría estar con Afrodita ahora mismo en cambio estoy {b}AQUÍ{/b},{w=0.5} me voy a casa supongo que mañana hablaremos."

    scene black with dissolve
    pause 2.0
    
    stop music
    return

label escena_8:
    hide screen collar_descargado_screen
    hide screen collar_cargado_screen
    scene black
    show screen mostrar_estado_corazon
    scene aula_musica at full_screen with dissolve
    show odiseo_neutro at left

    show calypso_silueta at right

    narrator "[player_name] continuará su día escolar{w=0.5}, las mujeres parecen estar al acecho de nuestro galán."

    hide odiseo_neutro
    show odiseo_sorprendido at left

    odiseo "¿Qué?{w=0.5} ¿No hay hombres en esta escuela?"

    hide odiseo_sorprendido
    show odiseo_neutro at left

    narrator "Gracias por jugar la demo de 'El Viaje de Odiseo: Corazones en Conflicto'.{w=0.5} ¡Esperamos que hayas disfrutado esta experiencia!{w=0.5} Mantente atento para la versión completa próximamente."
    hide odiseo_neutro
    # Final de la demo
    return

label escena_collar_afrodita:
    scene black
    show screen mostrar_estado_corazon
    if collar_cargado:
        show screen collar_cargado_screen
        play sound sfx_collar_brilla
        narrator "En este momento tan decisivo para [player_name]{w=0.5}, él recuerda su collar.{w=0.5} Recuerda a Penélope.{w=0.5} Recuerda lo que ella significa para él.{w=0.5} Y con eso{w=0.5}, él comienza a olvidar todo lo sucedido recién."

        menu:
            "[player_name] aprieta el collar":
                $ collar_cargado = False
                jump collar_afrodita_opcion_1a
            "[player_name] no aprieta el collar":
                jump collar_afrodita_opcion_1b
    else:
        show screen collar_descargado_screen
        narrator "En este momento tan decisivo para [player_name]{w=0.5}, él recuerda su collar.{w=0.5} Pero este ya no tiene el mismo valor emocional{w=0.5}, la misma importancia{w=0.5}, que solía tener.{w=0.5} Ya nada puede cambiar la decisión de [player_name]."
        jump collar_afrodita_opcion_2

label collar_afrodita_opcion_1a:
    hide screen collar_cargado_screen
    $ puntaje_afrodita = 0
    narrator "[player_name] aprieta el collar.{w=0.5} Cuando vuelve en sí{w=0.5}, está de vuelta donde todo comenzó a salirse de rumbo..."
    # Transición a la escena y decisión primaria de origen
    jump escena_3

label collar_afrodita_opcion_1b:
    hide screen collar_cargado_screen
    narrator "[player_name] elige no apretar el collar.{w=0.5} Él elige no aferrarse al pasado.{w=0.5} Elige seguir adelante..."
    # Transición a un final dado
    jump final_afrodita

label collar_afrodita_opcion_2:
    hide screen collar_descargado_screen
    narrator "En este momento tan decisivo para [player_name]{w=0.5}, él recuerda su collar.{w=0.5} Pero este ya no tiene el mismo valor emocional{w=0.5}, la misma importancia{w=0.5}, que solía tener.{w=0.5} Ya nada puede cambiar la decisión de [player_name]."
    # Transición a un final dado
    jump final_afrodita


label escena_collar_atenea:
    scene black
    show screen mostrar_estado_corazon
    if collar_cargado:
        show screen collar_cargado_screen
        play sound sfx_collar_brilla
        narrator "En este momento tan decisivo para [player_name]{w=0.5}, él recuerda su collar.{w=0.5} Recuerda a Penélope.{w=0.5} Recuerda lo que ella significa para él.{w=0.5} Y con eso{w=0.5}, él comienza a olvidar todo lo sucedido recién."

        menu:
            "[player_name] aprieta el collar":
                $ collar_cargado = False
                jump collar_atenea_opcion_1a
            "[player_name] no aprieta el collar":
                jump collar_atenea_opcion_1b
    else:
        show screen collar_descargado_screen
        narrator "En este momento tan decisivo para [player_name]{w=0.5}, él recuerda su collar.{w=0.5} Pero este ya no tiene el mismo valor emocional{w=0.5}, la misma importancia{w=0.5}, que solía tener.{w=0.5} Ya nada puede cambiar la decisión de [player_name]."
        jump collar_atenea_opcion_2

label collar_atenea_opcion_1a:
    hide screen collar_cargado_screen
    $ puntaje_atenea = 0
    narrator "[player_name] aprieta el collar.{w=0.5} Cuando vuelve en sí{w=0.5}, está de vuelta donde todo comenzó a salirse de rumbo..."
    # Transición a la escena y decisión primaria de origen
    jump escena_5

label collar_atenea_opcion_1b:
    hide screen collar_cargado_screen
    narrator "[player_name] elige no apretar el collar.{w=0.5} Él elige no aferrarse al pasado.{w=0.5} Elige seguir adelante..."
    # Transición a un final dado
    jump final_atenea

label collar_atenea_opcion_2:
    hide screen collar_descargado_screen
    narrator "En este momento tan decisivo para [player_name]{w=0.5}, él recuerda su collar.{w=0.5} Pero este ya no tiene el mismo valor emocional{w=0.5}, la misma importancia{w=0.5}, que solía tener.{w=0.5} Ya nada puede cambiar la decisión de [player_name]."
    # Transición a un final dado
    jump final_atenea


label escena_collar_penelope_final_1:
    scene black
    show screen mostrar_estado_corazon
    if collar_cargado:
        show screen collar_cargado_screen
        play sound sfx_collar_brilla
        narrator "En este momento tan decisivo para [player_name]{w=0.5}, él recuerda su collar.{w=0.5} Recuerda a Penélope.{w=0.5} Recuerda lo que ella significa para él.{w=0.5} Y con eso{w=0.5}, él comienza a olvidar todo lo sucedido recién."

        menu:
            "[player_name] aprieta el collar":
                $ collar_cargado = False
                jump collar_penelope_final_1_opcion_1a
            "[player_name] no aprieta el collar":
                jump collar_penelope_final_1_opcion_1b
    else:
        show screen collar_descargado_screen
        narrator "En este momento tan decisivo para [player_name]{w=0.5}, él recuerda su collar.{w=0.5} Pero este ya no tiene el mismo valor emocional{w=0.5}, la misma importancia{w=0.5}, que solía tener.{w=0.5} Ya nada puede cambiar la decisión de [player_name]."
        jump collar_atenea_opcion_2

label collar_penelope_final_1_opcion_1a:
    hide screen collar_cargado_screen
    $ puntaje_atenea = 0
    narrator "[player_name] aprieta el collar.{w=0.5} Cuando vuelve en sí{w=0.5}, está de vuelta donde todo comenzó a salirse de rumbo..."
    # Transición a la escena y decisión primaria de origen
    jump escena_5

label collar_penelope_final_1_opcion_1b:
    hide screen collar_cargado_screen
    narrator "[player_name] elige no apretar el collar.{w=0.5} Él elige no aferrarse al pasado.{w=0.5} Elige seguir adelante..."
    # Transición a un final dado
    jump final_penelope_1

label collar_penelope_final_1_opcion_2:
    hide screen collar_descargado_screen
    narrator "En este momento tan decisivo para [player_name]{w=0.5}, él recuerda su collar.{w=0.5} Pero este ya no tiene el mismo valor emocional{w=0.5}, la misma importancia{w=0.5}, que solía tener.{w=0.5} Ya nada puede cambiar la decisión de [player_name]."
    # Transición a un final dado
    jump final_penelope_1


label escena_collar_penelope_final_2:
    scene black
    show screen mostrar_estado_corazon
    if collar_cargado:
        show screen collar_cargado_screen
        play sound sfx_collar_brilla
        narrator "En este momento tan decisivo para [player_name]{w=0.5}, él recuerda su collar.{w=0.5} Recuerda a Penélope.{w=0.5} Recuerda lo que ella significa para él.{w=0.5} Y con eso{w=0.5}, él comienza a olvidar todo lo sucedido recién."

        menu:
            "[player_name] aprieta el collar":
                $ collar_cargado = False
                jump collar_penelope_final_2_opcion_1a
            "[player_name] no aprieta el collar":
                jump collar_penelope_final_2_opcion_1b
    else:
        show screen collar_descargado_screen
        narrator "En este momento tan decisivo para [player_name]{w=0.5}, él recuerda su collar.{w=0.5} Pero este ya no tiene el mismo valor emocional{w=0.5}, la misma importancia{w=0.5}, que solía tener.{w=0.5} Ya nada puede cambiar la decisión de [player_name]."
        jump collar_atenea_opcion_2

label collar_penelope_final_2_opcion_1a:
    hide screen collar_cargado_screen
    $ puntaje_atenea = 0
    narrator "[player_name] aprieta el collar.{w=0.5} Cuando vuelve en sí{w=0.5}, está de vuelta donde todo comenzó a salirse de rumbo..."
    # Transición a la escena y decisión primaria de origen
    jump escena_5

label collar_penelope_final_2_opcion_1b:
    hide screen collar_cargado_screen
    narrator "[player_name] elige no apretar el collar.{w=0.5} Él elige no aferrarse al pasado.{w=0.5} Elige seguir adelante..."
    # Transición a un final dado
    jump final_penelope_2

label collar_penelope_final_2_opcion_2:
    hide screen collar_descargado_screen
    narrator "En este momento tan decisivo para [player_name]{w=0.5}, él recuerda su collar.{w=0.5} Pero este ya no tiene el mismo valor emocional{w=0.5}, la misma importancia{w=0.5}, que solía tener.{w=0.5} Ya nada puede cambiar la decisión de [player_name]."
    # Transición a un final dado
    jump final_penelope_2
