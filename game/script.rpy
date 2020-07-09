# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Marujo", color="#6060b8")
define t = Character("Tripulação")
define c = Character("Capitã", color="#d85693")
define p = Character("Player", color="#ff00d0")
define d = Character("Doutor", color="#14ac0f")
define who = Character("???")

# This is just because I like to separate things one from another, so I did this
# for further reading and understanding better my code and my scripting.
# Declare images used at the background.

image storm = im.Scale("Pirate_Storm_temp.jpg", 1280, 960)
image calm convoy = im.Scale("Calm_Convoy_temp.jpg", 1280, 960)
image bedroom = im.Scale("Pirate_Room_Temp.jpg", 1280, 800)

# Declare the characters' images.
image player = im.Scale("Player_temp.png", 400, 600)
image doutor = im.Scale("Doutor_temp.png", 400, 600)
image marujo = im.Scale("Marujo_temp.png", 400, 600)
image capita = im.Scale("Player2_temp.png", 400, 600)

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # scene bg room
    scene storm 
    with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy

    # These display lines of dialogue.

    narrator "Não consigo me mexer... Mal consigo respirar direito..."

    show marujo at left with dissolve

    m "Capitã! Naufrágio à frente!"

    show capita at right 

    c "Vamos passar por fora para não bater em nada!"

    m "Parece que tem alguém em cima de umas madeiras, capitã!"
    
    c "Não importa, deixe-o para morrer! Se não sobreviver é por que não merece o perigoso oceano!"

    m "Mas capitã, é apenas uma menina..."

    c "O que? Tragam-na para o navio, imediatamente!"

    hide marujo

    t "Aye!"

    scene black with fade

    p "Que frio... Minha cabeça e minha perna direita doem... O que aconteceu comigo?"

    p "Argh! Por que meu corpo dói tanto quando tento me mexer?"
    
    scene bedroom with fade

    p "Onde estou? Que lugar é esse?"

    d "Finalmente acordou, bela adormecida?"

    p "Quem... é você?"

    show doutor with dissolve

    d "Eu sou o Dr. Ironwill. Não se preocupe, você está segura aqui."

    d "Consegue se lembrar de algo?"

    p "Me lembrar...? Me lembrar... do que?"

    d "Qual seu nome? Onde você estava? De onde você veio?"

    p "Eu..."

    with vpunch

    p "Aaaai!"

    show bedroom with fade
    
    p "Não... Eu tento me lembrar, mas minha cabeça ainda dói muito... O que houve comigo? Por que não consigo me lembrar de nada?"

    d "Por favor se acalme."

    d "Eu entendo como deve ser assustador, mas me escute."

    d "Acredito que você tenha perdido a memória no acidente. Nós a encontramos em cima de algumas madeiras, possivelmente de um naufrágio."  
    
    d "É provável que o ferimento em sua cabeça tenha sido de um baque e com isso você perdeu a memória, mas não acredito que seja permanente, deve voltar aos poucos."

    p "Naufrágio?"

    d "Sim, no meio do oceano. Você se lembra por que foi ao mar?"

    p "Não, eu sinto muito..."

    p "Doutor Ironwill, o senhor me disse que fui achada no mar... Onde... Onde nós estamos?"

    d "Ah sim, que falta de educação a minha! A senhorita está no navio da Capitã Anne Read! A grande bucaneira que nunca perdeu em batalha para nenhum humem!"

    p "Bucaneira? O senhor quer dizer uma pirata?"

    d "É como costumam nos chamar, mas não se preocupe. Se você fosse homem, ela nem teria se dado ao trabalho de lhe resgatar."

    d "Quando você estiver melhor, poderá sair e ver o navio por si própria. Por hora, é melhor que descanse um pouco."

    p "Sim, claro. Obrigado, Doutor."

    narrator "Não é como se eu tivesse muito lugar para ir..."

    p "Doutor, minha perna também está doendo e não acho que consigo mexê-la."

    d "Ah sim. Pela gravidade dos hematomas, acredito que alguma coisa tenha caido sobre elas. A imobilizei para que não mexesse, a fim de se recuperar mais rápido."  
    d "Você vai ficar um tempo nessa cama enquanto se recupera, então nem tente sair dela sem falar comigo, hein!"

    p "Sim, senhor..."

    hide doctor
    show black with fade

    narrator "Dias se passaram, as dores que sentia foram diminuindo, mas o Dr. Ironwill ainda não me deixava levantar e eu continuava a ver os dias passando naquela rede."

    narrator "De tempos em tempos vinham homens na cabine do doutor. Muitos com dores no corpo, outros com cortes e às vezes seus dedos estavam completamente pretos."  
    
    narrator "O Dr. Ironwill parece ser alguém muito respeitado, mas ele não se parece com ninguém do navio. Na verdade, ele destoa muito dos outros marinheiros."

    scene bedroom with fade
    show doutor

    d "Como se sente?"

    p "Não sinto mais dor, mas ainda não consigo mexer a perna direito."

    d "Isso foi por que ela ficou muito tempo imobilizada. Agora você pode voltar a andar para fazer o sangue circular e sua perna volte a ter força para te sustentar."

    d "Está pronta para finalmente conhecer o navio?"

    narrator "Dr. Ironwill me estendeu seu braço e entregou um pedaço de madeira para que eu usasse de bengala. Já em pé, ele foi me guiando pelo corredor até o convés do navio."

    scene calm convoy with dissolve

    narrator "No convés, tinham homens e mulheres trabalhando, cuidando de cordas, limpando o chão e mexendo nas velas."

    show who at left with dissolve

    who "Olá, Doutor Ironwill. Parece que nossa convidada já está melhor."

    show doutor at right with dissolve

    d "Ah sim, ela precisa exercitar um pouco as pernas para que ela possa voltar a andar sozinha."

    d "Deixe-me apresentá-la a..."

    # This ends the game.

    scene black with fade

    "...Continua"

    return
