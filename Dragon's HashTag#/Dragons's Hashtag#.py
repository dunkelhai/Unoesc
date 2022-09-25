import sys
import time


def iniciarjogo():
    print('''\n                ██████╗░██████╗░░█████╗░░██████╗░░█████╗░███╗░░██╗██╗░██████╗
                ██╔══██╗██╔══██╗██╔══██╗██╔════╝░██╔══██╗████╗░██║╚█║██╔════╝
                ██║░░██║██████╔╝███████║██║░░██╗░██║░░██║██╔██╗██║░╚╝╚█████╗░
                ██║░░██║██╔══██╗██╔══██║██║░░╚██╗██║░░██║██║╚████║░░░░╚═══██╗
                ██████╔╝██║░░██║██║░░██║╚██████╔╝╚█████╔╝██║░╚███║░░░██████╔╝
                ╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░╚═════╝░░╚════╝░╚═╝░░╚══╝░░░╚═════╝░

                ██╗░░██╗░█████╗░░██████╗██╗░░██╗████████╗░█████╗░░██████╗░░░░██╗░██╗░ 
                ██║░░██║██╔══██╗██╔════╝██║░░██║╚══██╔══╝██╔══██╗██╔════╝░██████████╗ 
                ███████║███████║╚█████╗░███████║░░░██║░░░███████║██║░░██╗░╚═██╔═██╔═╝ 
                ██╔══██║██╔══██║░╚═══██╗██╔══██║░░░██║░░░██╔══██║██║░░╚██╗██████████╗ 
                ██║░░██║██║░░██║██████╔╝██║░░██║░░░██║░░░██║░░██║╚██████╔╝╚██╔═██╔══╝ 
                ╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝░╚═════╝░░╚═╝░╚═╝░░░ ''')
    print("\nNobre Herói, seja bem-vindo ao Dragon's Hashtag#!")
    time.sleep(3)
    print("\nNós aldeões estamos muito felizes e aliviados por ter chegado!"
          "\nPor favor, nos ajude! Uma maldição há muito assola nosso vilarejo. "
          "\nO terrível dragão Negro acordou em sua fortaleza e se prepara para destruir o vilarejo. "
          "\nA única forma de derrota-lo é em um duelo de jogo da velha. "
          "\nA maldição diz que apenas um cavaleiro puro de coração poderá vencer o dragão e devolvê-lo ao sono profundo de mil anos trazendo a paz novamente.")


def agradecimento():
    time.sleep(3)
    print(
        "\nCaro Jogador, muito obrigado por ter jogado o Dragon's Hashtag# ! \nFique à vontade para enviar dúvidas, críticas ou sugestões!")


def criadores():
    time.sleep(3)
    print('\n::::::: DEVELOPED BY :::::::'
          '\nAlysson Oliveira\nPatricia Prestes\nRaiza Zardo\nStephani Rolim')


def escolherpersonagens():
    time.sleep(3)
    print("\nAgora Nobre Herói, por favor escolha um personagem para enfrentar o Dragão!")


def menuprincipal():
    global transformer, personagem
    time.sleep(3)
    print("\n\nVocê está no Menu Principal.")
    time.sleep(3)
    print("O que deseja fazer?\n\n1 para INICIAR O JOGO.\n2 para COMO JOGAR.\n3 para SAIR.\n")
    menuescolha = input()

    if menuescolha == '1':
        escolherpersonagens()
        loopdowhile = 1
        while loopdowhile == 1:
            personagem = input(
                "\nEscolha seu personagem:\n\n1 para Ladino. (🗡)\n2 para Guerreiro. (⚔)\n3 para Paladino. (🛡)\n4 para Arqueiro. (🏹)\n")
            if personagem == '1':
                transformer = '☣'
                loopdowhile = 2
            elif personagem == '2':
                transformer = '⚔'
                loopdowhile = 2
            elif personagem == '3':
                transformer = '☮'
                loopdowhile = 2
            elif personagem == '4':
                transformer = '➳'
                loopdowhile = 2
            else:
                print(
                    "Por favor Nobre Herói, escolha um Herói válido! Seja rápido, não sabemos quanto tempo iremos aguentar o ataque dragônico!")
        informacoespersonagens()
        prologo()

    elif menuescolha == '2':
        comojogar()
        menuprincipal()

    elif menuescolha == '3':
        print(
            '\nInfelizmente nosso vilarejo vai perecer e todos nós vamos queimar até a morte!\n\nMesmo assim deseja sair?\n\n1 para "SIM, VOCÊS TEM MINHA PERMISSÃO PARA MORRER! (SAIR DO JOGO)"\n2 para "NÃO, MUDEI DE IDEIA E VOU DERROTAR O DRAGÃO! (INICIAR JOGO)"')
        sair = input('\n')
        if sair == '1':
            print('\n ˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆ')
            print('''\n                                           ...
                                         ;::::;                            
                                       ;::::; :;                           
                                     ;:::::'   :;                          
                                    ;:::::;     ;.                         
                                   ,:::::'       ;           OOO\          
                                   ::::::;       ;          OOOOO\         
                                   ;:::::;       ;         OOOOOOOO        
                                  ,;::::::;     ;'         / OOOOOOO       
                                ;:::::::::`. ,,,;.        /  / DOOOOOO     
                              .';:::::::::::::::::;,     /  /     DOOOO    
                             ,::::::;::::::;;;;::::;,   /  /        DOOO   
                            ;`::::::`'::::::;;;::::: ,#/  /          DOOO  
                            :`:::::::`;::::::;;::: ;::#  /            DOOO 
                            ::`:::::::`;:::::::: ;::::# /              DOO 
                            `:`:::::::`;:::::: ;::::::#/               DOO 
                             :::`:::::::`;; ;:::::::::##                OO 
                             ::::`:::::::`;::::::::;:::#                OO 
                             `:::::`::::::::::::;'`:;::#                O  
                              `:::::`::::::::;' /  / `:#                   
                               ::::::`:::::;'  /  /   `# ''')
            sys.exit('\n\nTodos do Vilarejo queimaram até a morte!\n        ::::::: R.I.P :::::::')
        elif sair == '2':
            print('\nEstamos muito felizes por ter voltado e não desistir Nobre Herói!\n')
            escolherpersonagens()
            loopdowhile = 1
            while loopdowhile == 1:
                personagem = input(
                    "\nEscolha seu personagem:\n\n1 para Ladino. (🗡)\n2 para Guerreiro. (⚔)\n3 para Paladino. (🛡)\n4 para Arqueiro. (🏹)\n")
                if personagem == '1':
                    transformer = '☣'
                    loopdowhile = 2
                elif personagem == '2':
                    transformer = '⚔'
                    loopdowhile = 2
                elif personagem == '3':
                    transformer = '☮'
                    loopdowhile = 2
                elif personagem == '4':
                    transformer = '➳'
                    loopdowhile = 2
                else:
                    print(
                        "Por favor Nobre Herói, escolha um Herói válido! Seja rápido, não sabemos quanto tempo iremos aguentar o ataque dragônico!")
            prologo()
            informacoespersonagens()

    else:
        sys.exit('\nComo não escolheu nenhuma das opções válidas, o jogo foi encerrado!')


def ranking():
    time.sleep(3)
    print('''\n                ██████╗░░█████╗░███╗░░██╗██╗░░██╗██╗███╗░░██╗░██████╗░░░░██╗░██╗░
                ██╔══██╗██╔══██╗████╗░██║██║░██╔╝██║████╗░██║██╔════╝░██████████╗
                ██████╔╝███████║██╔██╗██║█████═╝░██║██╔██╗██║██║░░██╗░╚═██╔═██╔═╝
                ██╔══██╗██╔══██║██║╚████║██╔═██╗░██║██║╚████║██║░░╚██╗██████████╗
                ██║░░██║██║░░██║██║░╚███║██║░╚██╗██║██║░╚███║╚██████╔╝╚██╔═██╔══╝
                ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░╚═════╝░░╚═╝░╚═╝░░░
                                ''')
    print('\n::::::: CONTADOR ATUAL DE VITÓRIAS CONTRA O DRAGÃO :::::::\n')
    print(f'Ladino: {pontosladino}')
    print(f'Guerreiro: {pontosguerreiro}')
    print(f'Paladino: {pontospaladino}')
    print(f'Arqueiro: {pontosarqueiro}')


def gameover():
    time.sleep(3)
    print('''\n                ███████╗██╗███╗░░░███╗  ██████╗░███████╗  ░░░░░██╗░█████╗░░██████╗░░█████╗░░░░██╗░██╗░
                ██╔════╝██║████╗░████║  ██╔══██╗██╔════╝  ░░░░░██║██╔══██╗██╔════╝░██╔══██╗██████████╗
                █████╗░░██║██╔████╔██║  ██║░░██║█████╗░░  ░░░░░██║██║░░██║██║░░██╗░██║░░██║╚═██╔═██╔═╝
                ██╔══╝░░██║██║╚██╔╝██║  ██║░░██║██╔══╝░░  ██╗░░██║██║░░██║██║░░╚██╗██║░░██║██████████╗
                ██║░░░░░██║██║░╚═╝░██║  ██████╔╝███████╗  ╚█████╔╝╚█████╔╝╚██████╔╝╚█████╔╝╚██╔═██╔══╝
                ╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝  ╚═════╝░╚══════╝  ░╚════╝░░╚════╝░░╚═════╝░░╚════╝░░╚═╝░╚═╝░░░
                ''')


def ladinovitoria():
    print(
        '\nParabéns Nobre Herói Ladino! Graças à sua ajuda, conseguimos derrotar o terrível Dragão e agora fomos libertados!\nMuito obrigado, do fundo dos corações de todos os aldeões!')
    time.sleep(3)
    print('''\n                                                   \             //                            
                                                    \\           _!_                            
                                                     \\         /___\                           
                                                      \\        [+++]                           
                                                       \\    _ _\^^^/_ _                        
                           ,a_a                         \\/ (    '-'  ( )                       
                          {/ xx\_                       /( \/ | <&>   /\ \                      
                          {\ ,_oo)                     (* \  / \     /  > )                     
                          {/  (_^_@\_________________      "`   >::::\ / /                      
                .=.      {/ \___)))*)---------------"`         /:::' |/_)                       
                .=.`\   {/   /=;  @/                          /  /|  |                          
                   \ `\{/(   \/\                             (  / (  /                          
                    \  `. `\  ) )                            / /   \ \                          
                     \    // /_/_                          _/ /     \ \                         
                      '==''---))))                        /___|    /___|                        
                                           ''')


def paladinovitoria():
    print(
        '\nParabéns Nobre Herói Paladino! Graças à sua ajuda, conseguimos derrotar o terrível Dragão e agora fomos libertados!\nMuito obrigado, do fundo dos corações de todos os aldeões!')
    time.sleep(3)
    print('''\n                                                        \             //
                                                         \\           _!_              
                                                          \\         /___\             
                                                           \\        [+++]             
                                                            \\    _ _\^^^/_ _          
                                ,a_a                         \\/ (    '-'  ( )         
                               {/ xx\_                       /( \/ | {&}   /\ \        
                               {\ ,_oo)                        \  / \     / _> )       
                               {/  (_^_@\_________________      "`   >:::;-'`""'-.     
                     .=.      {/ \___)))*)---------------"`         /:::/         \    
                    (.=.`\   {/   /=;  @/                          /  /||   {&}   |    
                        \ `\{/(   \/\                             (  / (\         /    
                         \  `. `\  ) )                            / /   \'-.___.-'     
                          \    // /_/_                          _/ /     \ \           
                           '==''---))))                        /___|    /___|          
''')


def arqueirovitoria():
    print(
        '\nParabéns Nobre Herói Arqueiro! Graças à sua ajuda, conseguimos derrotar o terrível Dragão e agora fomos libertados!\nMuito obrigado, do fundo dos corações de todos os aldeões!')
    time.sleep(3)
    print('''\n                                                           _|__        //
                                                          /    |      _!_        
                                                         /     |     /___\       
                                                        /      |     [+++]       
                                                        \      |  _ _\^^^/_ _    
                                ,a_a                  <--\------ (    '-'  ( )   
                               {/ xx\_                    \   ( \/ | <&>   /\ \  
                               {\ ,_oo)                    \  | \  / \    / > )  
                               {/  (_^_@\_________________  \_/  "`  >::::\ / /  
                     .=.      {/ \___)))*)---------------"`         /:::' |/_)   
                    (.=.`\   {/   /=;  @/                          /  /|  |      
                        \ `\{/(   \/\                             (  / (  /      
                         \  `. `\  ) )                            / /   \ \      
                          \    // /_/_                          _/ /     \ \     
                           '==''---))))                        /___|    /___|    
    ''')


def guerreirovitoria():
    print(
        '\nParabéns Nobre Herói Guerreiro! Graças à sua ajuda, conseguimos derrotar o terrível Dragão e agora fomos libertados!\nMuito obrigado, do fundo dos corações de todos os aldeões!')
    time.sleep(3)
    print('''\n   
                                                                    ,   A           {}                             
                                                                   / \, | ,        .--.                           
                                                                  |    =|= >      /.--.\                          
                                                                   \ /` | `       |====|                          
                                                                    `   |         |`::`|                          
                                                                        |     .-;`\..../`;_.-^-._                 
                                                                       /\\/  /  |...::..|`   :   `|               
                                                                       |:'\ |   /   ::  |   .:.   |               
                  	             ,a_a                                   \ /\;-,/\   ::  |..:::::..|               
                                {/ xx\_                                 |\ <` >  >._::_.| ':::::' |               
                                {\ ,_oo)                                | `""`  /   ^^  |   ':'   |               
                                {/  (_^_@\________________              |       |       \    :    /               
                      .=.      {/ \___)))*)---------------              |       |        \   :   /                
                     (.=.`\   {/   /=;  @/                              |       |___/\___|`-.:.-`                 
                         \ `\{/(   \/\                                  |        \_ || _/    `                    
                          \  `. `\  ) )                                 |        <_ >< _>                         
                           \    // /_/_                                 |        |  ||  |                         
                            '==''---))))                                |        |  ||  |                         
                                                                        |       _\.:||:./_                        
                                                                        |.     /____/\____\                  
        ''')


def vitoriadragao():
    print(
        '\nQue pena Nobre Herói! Infelizmente você não foi capaz de vencer o terrível Dragão!\nE ele acabou destruindo todo o vilarejo. Talvez na próxima você consiga, se planejar melhor sua estratégia e se prepar melhor!')
    time.sleep(3)
    print('''\n                                  __                  __
                                 ( _)                ( _)               
                                / / \\              / /\_\_             
                               / /   \\            / / | \ \            
                              / /     \\          / /  |\ \ \           
                             /  /   ,  \ ,       / /   /|  \ \          
                            /  /    |\_ /|      / /   / \   \_\         
                           /  /  |\/ _ '_|\    / /   /   \    \\        
                          |  /   |/  v \v\ \  / |    |    \    \\       
                          |    |\|      \_\_ /  /    |     \    \\      
                          |  | |/    \.\ o\o)  /      \     |    \\     
                          \    |     /\\`V-V  /        |    |     \\    
                           | \/    /_| \\_|  /         |    | \    \\   
                           | |    /__/_     /   _____  |    |  \    \\  
                           \|    [__]  \_/  |_________  \   |   \    () 
                            /    [___] (    \         \  |\ |   |   //  
                           |    [___]                  |\| \|   /  |/   
                          /|    [____]                  \  |/\ / / ||   
                         (  \   [____ /     ) _\      \  \    \| | ||   
                          \  \  [_____|    / /     __/    \   / / //    
                          |   \ [_____/   / /        \    |   \/ //     
                          |   /  '----|   /=\____   _/    |   / //      
                       __ /  /        |  /   ___/  _/\    \  | ||       
                      (/-(/-\)       /   \  (/\/\)/  |    /  | /        
                                    (/\/\)           /   /   //         
                                           _________/   /    /          
                                          \____________/    (           
    ''')


def empate():
    print('Interessante... parece que temos um empate! O Herói está no nível do Dragão!'
          '\nBem, pelo menos assim, teremos mais tempo de organizar o nosso vilarejo e nos defender. '
          '\nMas mesmo assim, precisamos vencer esse Dragão!')
    time.sleep(3)
    print('''\n                                                               _\/                 
                                                            .-'.'`)                           
                                                         .-' .'                               
                                   .                  .-'     `-.          __\/               
                                    \.    .  |,   _.-'       -:````)   _.-'.'``)              
                                     \`.  |\ | \.-_.           `._ _.-' .'`                   
                                    __) )__\ |! )/ \_.          _.-'      `.                  
                                _.-'__`-' =`:' /.' / |      _.-'      -:`````)                
                          __.--' ( (@> ))  = \ ^ `'. |_. .-'           `.                     
                         : @       `^^^    == \ ^   `. |<                `.                   
                         VvvvvvvvVvvvv)    =  ;   ^  ;_/ :           -:``````)                
                           (^^^^^^^^^^=  ==   |      ; \. :            `.                     
                        ((  `-----------.  == |  ^   ;_/   :             `.                   
                        /\             /==   /       : \.  :     _..--``````)                 
                      __\ \_          ; ==  /  ^     :_/   :      `.                          
                    ><__   _```---.._/ ====/       ^ : \. :         `.                        
                        / / `._  ^  ;==   /  ^        :/ .            `.                      
                        \/ ((  `._ / === /       ^    `.'       _.--`````)                    
                        (( /\     ;===  /      ^     .'        `.                             
                         __\ \_  : === | ^ /                     `.                           
                      >><__   _``--...__.-'   ^  /  ^              `.                         
                           / / `._        ^    .'              .--`````)     .--..            
                           \/   :=`--...____.-'  ^     .___.-'|            .' .--.`.   (      
                          ((    | ===    \                  `.|__.         ; ^:   `.'   )     
                                 :  ====  \  ^      ^         `. |          ;  `;   `../__    
                               .-'\====    \    .       ^      `.|___.       ;^  `;       \   
                            .-'    :  ===   \.-'              ^  `.  |        ;  ^ `;      )  
                         .-'    ^   \==== .-'         ^            `.|___.     ;     ;    (   
                      .-'         ^  :=.-'                 ^        `.   |      ;     ;       
                    .'      ^       .-'          ^               ^    ;_/__.    ;  ^   ;      
                    : ^        ^ .-'     ^                   ^   ;     ;   |    ;       ;     
                    :    ^    .-'    ^          ^      ^     _.-'    ^  ;_/    ; ^      ;     
                    :  ^    .'                           _.-"    ^      ; \.  ;      ^  ;     
                     `.   ^ :   ^         ^       ^__.--"               ;_/  ;          ;     
                       `.^  :                __.--"\         ^     ^    ; \ ;     ^     ;     
                         `-.:       ^___.---"\ ===  \   ^               ;_/'        ^  ;      
                            ``.^         `.   `\===  \         ^     ^       ^        ;       
                               `.     ^    `.   `-. ==\                          ^   ;        
                                _`-._        `.    `\= \    ^           ^           ;         
                        __..--''    _`-._^     `.    `-.`\         ^          ^    ;          
                       (-(-(-(-(--''     `-._  ^ `.     `\`\              ^      .'           
                                     __..---''     `._     `-. ^      ^      ^ .'             
                            __..---''    ___....---'`-`)      `---...____..---'               
                           (-(-(-(-(---''             '                                       
     ''')


def prologo():
    print('\nEra uma vez, um vilarejo que se localizava entre as montanhas do condado de Santa Catarina.')
    print('''\n                                          
           ~         ~~          __                      
                  _T      .,,.    ~--~ ^^                
            ^^   // \                    ~               
                 ][O]    ^^      ,-~ ~                   
              /''-I_I         _II____                    
           __/_  /   \ ______/ ''   /'\_,__              
             | II--    \,--:--..,_/,.-{ },               
           ; '/__\,.--';|   |[] .-.| O{ _ }              
           :' |  | []  -|   ''--:.;[,.'\,/               
           '  |[]|,.--'' '',   ''-,.    |                
             ..    ..-''    ;       ''. '           ''')
    time.sleep(3)
    print(
        '\nTodos viviam uma vida pacífica, até que um certo dia, um terrível Dragão apareceu para queimar e destruir tudo.')
    time.sleep(3)
    print('''\n                       ____ __             
                      { --.\  |          .)%%%)%%     
                       '-._\\ | (\___   %)%%(%%(%%%   
                           `\\|{/ ^ _)-%(%%%%)%%;%%%  
                       .'^^^^^^^  /`    %%)%%%%)%%%'  
                      //\   ) ,  /       '%%%%(%%'    
                ,  _.'/  `\<-- \<                     
                 `^^^`     ^^   ^^  ''')
    time.sleep(3)
    print('\nAgora prepare-se para enfrentar esse malvado Dragão e libertar o vilarejo!')
    print('''\n                     __.-/|      
                     \`O_O'                 
                      =( )=  +-------------+
                        V|   | Cai Dentro! |
              /\  /\   / |   +-------------+
             ) /^\) ^\/ _)\     |           
             )   /^\/   _) \    |           
             )   _ /  / _)  \___|_          
         /\  )/\/ ||  | )_)\___,|))         
        <  >      |(,,) )__)    |           
         ||      /    \)___)\\              
         | \____(      )___) )____          
          \______(_______;;;)__;;;)    ''')
    time.sleep(3)


def informacoespersonagens():
    print('\nSó uma informação rápida sobre os símbolos dos personagens Nobre Herói.')
    time.sleep(3)
    print('\n\n::::::: VILÃO :::::::')
    print(
        '\nO símbolo que representa o Dragão 🐲 é a caveira ☠, pois o Dragão traz à morte para os aldeões do vilarejo.')
    time.sleep(3)
    print(
        '\n::::::: HeróiS :::::::\n\nO símbolo que represente o Ladino 🗡 é o símbolo da radiação ☣, pois a radiação é silenciosa e mortal como o Ladino.')
    print(
        'O símbolo que represente o Guerreiro ⚔ são as duas espadas cruzadas ⚔, pois o Guerreiro usa as duas espadas para lutar.')
    print(
        'O símbolo que represente o Paladino 🛡 é o símbolo da paz ☮, pois o Paladino está sempre em busca da paz e da proteção.')
    print(
        'O símbolo que represente o Arqueiro 🏹 é a flecha ➳, pois o Arqueiro usa as flechas para acertar os alvos e inimigos.')
    time.sleep(3)


def comojogar():
    print('\n::::::: COMO JOGAR :::::::'
          '\n\nO objetivo desse jogo, é derrotar o temível dragão, que vem assolando o vilarejo por muito tempo. '
          'A batalha com o dragão, será por meio de um jogo chamado de Jogo da Velha.'
          '\nO objetivo do jogo, é completar uma sequência de 3 itens em ordem, seja na horizontal, vertical ou diagonal.'
          '\nA cada turno, tanto o jogador 1 (Herói) como o jogador 2 (Dragão), serão requisitados para selecionarem um número corresponde ao local que desejam movimentar a peça.'
          '\nEsses locais estão representados pelo mapa de posições a seguir:')
    print('\n'
          ' 7 | 8 | 9 '
          '\n-----------'
          '\n 4 | 5 | 6 '
          '\n-----------'
          '\n 1 | 2 | 3 ')
    time.sleep(2)


tabuleiro = {'7': ' ', '8': ' ', '9': ' ',
             '4': ' ', '5': ' ', '6': ' ',
             '1': ' ', '2': ' ', '3': ' '}

tabuleiroChaves = []

for chave in tabuleiro:
    tabuleiroChaves.append(chave)


def imprimirTabuleiro(tabuleiro):
    print('                                      |████')
    print('                                      |')
    print('                                      |')
    print('                                (███████████)')
    print('                              (███████████████)')
    print('                              █████████████████')
    print('                              ██ ██ ██ ██ ██ ██')
    print('                              █████████████████')
    print('                              █ ' + ' ' + tabuleiro['7'] + '  ║' + tabuleiro['8'] + '  ║' + tabuleiro[
        '9'] + '    █')
    print('                              █ ════║═══║════' + ' █')
    print('                              █ ' + ' ' + tabuleiro['4'] + '  ║' + ' ' + tabuleiro['5'] + ' ║' + tabuleiro[
        '6'] + '    █')
    print('                              █ ════║═══║════' + ' █')
    print('                              █ ' + ' ' + tabuleiro['1'] + '  ║' + tabuleiro['2'] + '  ║' + tabuleiro[
        '3'] + '    █')
    print('                              █████████████████\n')

global listapontos
listapontos = []
global pontosladino
pontosladino = 0
global pontosguerreiro
pontosguerreiro = 0
global pontosarqueiro
pontosarqueiro = 0
global pontospaladino
pontospaladino = 0

def game():
    global transformer, count, pontospaladino, pontosarqueiro, pontosguerreiro, listapontos, pontosladino

    iniciarjogo()
    menuprincipal()
    count = 0

    for i in range(20):
        time.sleep(1)
        imprimirTabuleiro(tabuleiro)
        print("Vez do " + transformer + ". Mover para qual lugar?")

        movimento = input()

        if tabuleiro[movimento] == ' ':
            tabuleiro[movimento] = transformer
            count += 1
        else:
            print("Esse lugar já está preenchido Nobre Herói.\nPara qual lugar deseja mover?")
            continue

        if count >= 5:
            if tabuleiro['7'] == tabuleiro['8'] == tabuleiro['9'] != ' ':
                imprimirTabuleiro(tabuleiro)
                print("\nGame Over.\n")
                print(":::::::" + ' ' + transformer + " VENCEU! :::::::")
                if transformer == '☣':
                    gameover()
                    ladinovitoria()
                    pontosladino += 1
                    listapontos.append(pontosladino)
                    listapontos.sort(reverse=True)
                    ranking()
                    break
                elif transformer == '⚔':
                    gameover()
                    guerreirovitoria()
                    pontosguerreiro += 1
                    listapontos.append(pontosguerreiro)
                    listapontos.sort(reverse=True)
                    ranking()
                    break
                elif transformer == '☮':
                    gameover()
                    paladinovitoria()
                    pontospaladino += 1
                    listapontos.append(pontospaladino)
                    listapontos.sort(reverse=True)
                    ranking()
                    break
                elif transformer == '➳':
                    gameover()
                    arqueirovitoria()
                    pontosarqueiro += 1
                    listapontos.append(pontosladino)
                    listapontos.sort(reverse=True)
                    ranking()
                    break
                elif transformer == '☠':
                    gameover()
                    vitoriadragao()
                    ranking()
                    break
                else:
                    empate()
                    break
            elif tabuleiro['4'] == tabuleiro['5'] == tabuleiro['6'] != ' ':
                imprimirTabuleiro(tabuleiro)
                print("\nGame Over.\n")
                print(":::::::" + ' ' + transformer + " VENCEU! :::::::")
                if transformer == '☣':
                    gameover()
                    ladinovitoria()
                    pontosladino += 1
                    listapontos.append(pontosladino)
                    listapontos.sort(reverse=True)
                    ranking()
                    break
                elif transformer == '⚔':
                    gameover()
                    guerreirovitoria()
                    pontosguerreiro += 1
                    listapontos.append(pontosguerreiro)
                    listapontos.sort(reverse=True)
                    ranking()
                    break
                elif transformer == '☮':
                    gameover()
                    paladinovitoria()
                    pontospaladino += 1
                    listapontos.append(pontospaladino)
                    listapontos.sort(reverse=True)
                    ranking()
                    break
                elif transformer == '➳':
                    gameover()
                    arqueirovitoria()
                    pontosarqueiro += 1
                    listapontos.append(pontosladino)
                    listapontos.sort(reverse=True)
                    ranking()
                    break
                elif transformer == '☠':
                    gameover()
                    vitoriadragao()
                    ranking()
                    break
                else:
                    empate()
                    break
            elif tabuleiro['1'] == tabuleiro['2'] == tabuleiro['3'] != ' ':
                imprimirTabuleiro(tabuleiro)
                print("\nGame Over.\n")
                print(":::::::" + ' ' + transformer + " VENCEU! :::::::")
                if transformer == '☣':
                    gameover()
                    ladinovitoria()
                    pontosladino += 1
                    listapontos.append(pontosladino)
                    listapontos.sort(reverse=True)
                    ranking()
                    break
                elif transformer == '⚔':
                    gameover()
                    guerreirovitoria()
                    pontosguerreiro += 1
                    listapontos.append(pontosguerreiro)
                    listapontos.sort(reverse=True)
                    ranking()
                    break
                elif transformer == '☮':
                    gameover()
                    paladinovitoria()
                    pontospaladino += 1
                    listapontos.append(pontospaladino)
                    listapontos.sort(reverse=True)
                    ranking()
                    break
                elif transformer == '➳':
                    gameover()
                    arqueirovitoria()
                    pontosarqueiro += 1
                    listapontos.append(pontosladino)
                    listapontos.sort(reverse=True)
                    ranking()
                    break
                elif transformer == '☠':
                    gameover()
                    vitoriadragao()
                    ranking()
                    break
                else:
                    empate()
                    break
            elif tabuleiro['1'] == tabuleiro['4'] == tabuleiro['7'] != ' ':
                imprimirTabuleiro(tabuleiro)
                print("\nGame Over.\n")
                print(":::::::" + ' ' + transformer + " VENCEU! :::::::")
                if transformer == '☣':
                    gameover()
                    ladinovitoria()
                    pontosladino += 1
                    listapontos.append(pontosladino)
                    listapontos.sort(reverse=True)
                    ranking()
                    break
                elif transformer == '⚔':
                    gameover()
                    guerreirovitoria()
                    pontosguerreiro += 1
                    listapontos.append(pontosguerreiro)
                    listapontos.sort(reverse=True)
                    ranking()
                    break
                elif transformer == '☮':
                    gameover()
                    paladinovitoria()
                    pontospaladino += 1
                    listapontos.append(pontospaladino)
                    listapontos.sort(reverse=True)
                    ranking()
                    break
                elif transformer == '➳':
                    gameover()
                    arqueirovitoria()
                    pontosarqueiro += 1
                    listapontos.append(pontosladino)
                    listapontos.sort(reverse=True)
                    ranking()
                    break
                elif transformer == '☠':
                    gameover()
                    vitoriadragao()
                    ranking()
                    break
                else:
                    empate()
                    break
            elif tabuleiro['2'] == tabuleiro['5'] == tabuleiro['8'] != ' ':
                imprimirTabuleiro(tabuleiro)
                print("\nGame Over.\n")
                print(":::::::" + ' ' + transformer + " VENCEU! :::::::")
                if transformer == '☣':
                    gameover()
                    ladinovitoria()
                    pontosladino += 1
                    listapontos.append(pontosladino)
                    listapontos.sort(reverse=True)
                    ranking()
                    break
                elif transformer == '⚔':
                    gameover()
                    guerreirovitoria()
                    pontosguerreiro += 1
                    listapontos.append(pontosguerreiro)
                    listapontos.sort(reverse=True)
                    ranking()
                    break
                elif transformer == '☮':
                    gameover()
                    paladinovitoria()
                    pontospaladino += 1
                    listapontos.append(pontospaladino)
                    listapontos.sort(reverse=True)
                    ranking()
                    break
                elif transformer == '➳':
                    gameover()
                    arqueirovitoria()
                    pontosarqueiro += 1
                    listapontos.append(pontosladino)
                    listapontos.sort(reverse=True)
                    ranking()
                    break
                elif transformer == '☠':
                    gameover()
                    vitoriadragao()
                    ranking()
                    break
                else:
                    empate()
                    break
            elif tabuleiro['3'] == tabuleiro['6'] == tabuleiro['9'] != ' ':
                imprimirTabuleiro(tabuleiro)
                print("\nGame Over.\n")
                print(":::::::" + ' ' + transformer + " VENCEU! :::::::")
                if transformer == '☣':
                    gameover()
                    ladinovitoria()
                    pontosladino += 1
                    listapontos.append(pontosladino)
                    listapontos.sort(reverse=True)
                    ranking()
                    break
                elif transformer == '⚔':
                    gameover()
                    guerreirovitoria()
                    pontosguerreiro += 1
                    listapontos.append(pontosguerreiro)
                    listapontos.sort(reverse=True)
                    ranking()
                    break
                elif transformer == '☮':
                    gameover()
                    paladinovitoria()
                    pontospaladino += 1
                    listapontos.append(pontospaladino)
                    listapontos.sort(reverse=True)
                    ranking()
                    break
                elif transformer == '➳':
                    gameover()
                    arqueirovitoria()
                    pontosarqueiro += 1
                    listapontos.append(pontosladino)
                    listapontos.sort(reverse=True)
                    ranking()
                    break
                elif transformer == '☠':
                    gameover()
                    vitoriadragao()
                    ranking()
                    break
                else:
                    empate()
                    break
            elif tabuleiro['7'] == tabuleiro['5'] == tabuleiro['3'] != ' ':
                imprimirTabuleiro(tabuleiro)
                print("\nGame Over.\n")
                print(":::::::" + ' ' + transformer + " VENCEU! :::::::")
                if transformer == '☣':
                    gameover()
                    ladinovitoria()
                    pontosladino += 1
                    listapontos.append(pontosladino)
                    listapontos.sort(reverse=True)
                    ranking()
                    break
                elif transformer == '⚔':
                    gameover()
                    guerreirovitoria()
                    pontosguerreiro += 1
                    listapontos.append(pontosguerreiro)
                    listapontos.sort(reverse=True)
                    ranking()
                    break
                elif transformer == '☮':
                    gameover()
                    paladinovitoria()
                    pontospaladino += 1
                    listapontos.append(pontospaladino)
                    listapontos.sort(reverse=True)
                    ranking()
                    break
                elif transformer == '➳':
                    gameover()
                    arqueirovitoria()
                    pontosarqueiro += 1
                    listapontos.append(pontosladino)
                    listapontos.sort(reverse=True)
                    ranking()
                    break
                elif transformer == '☠':
                    gameover()
                    vitoriadragao()
                    ranking()
                    break
                else:
                    empate()
                    break
            elif tabuleiro['1'] == tabuleiro['5'] == tabuleiro['9'] != ' ':
                imprimirTabuleiro(tabuleiro)
                print("\nGame Over.\n")
                print(":::::::" + ' ' + transformer + " VENCEU! :::::::")
                if transformer == '☣':
                    gameover()
                    ladinovitoria()
                    pontosladino += 1
                    listapontos.append(pontosladino)
                    listapontos.sort(reverse=True)
                    ranking()
                    break
                elif transformer == '⚔':
                    gameover()
                    guerreirovitoria()
                    pontosguerreiro += 1
                    listapontos.append(pontosguerreiro)
                    listapontos.sort(reverse=True)
                    ranking()
                    break
                elif transformer == '☮':
                    gameover()
                    paladinovitoria()
                    pontospaladino += 1
                    listapontos.append(pontospaladino)
                    listapontos.sort(reverse=True)
                    ranking()
                    break
                elif transformer == '➳':
                    gameover()
                    arqueirovitoria()
                    pontosarqueiro += 1
                    listapontos.append(pontosladino)
                    listapontos.sort(reverse=True)
                    ranking()
                    break
                elif transformer == '☠':
                    gameover()
                    vitoriadragao()
                    ranking()
                    break
                else:
                    empate()
                    break

        if count == 9:
            print("\n::::::: GAME OVER! :::::::\n")
            print("\n::::::: EMPATOU! :::::::\n")
            gameover()
            time.sleep(3)
            empate()
            break

        if personagem == '1':
            if transformer == '☣':
                transformer = '☠'
            else:
                transformer = '☣'

        elif personagem == '2':
            if transformer == '⚔':
                transformer = '☠'
            else:
                transformer = '⚔'
        elif personagem == '3':
            if transformer == '☮':
                transformer = '☠'
            else:
                transformer = '☮'
        elif personagem == '4':
            if transformer == '➳':
                transformer = '☠'
            else:
                transformer = '➳'

    agradecimento()
    criadores()
    jogarnovamente = input(
        "\nGostaria de tentar enfrentar o Dragão mais uma vez Nobre Herói?\n1 para SIM.\n2 para NÃO.\n")
    if jogarnovamente == '1':
        for chave in tabuleiroChaves:
            tabuleiro[chave] = " "
        game()
    else:
        menunovamente = input("\nGostaria de voltar ao menu principal Nobre Herói?\n1 para SIM.\n2 para NÃO.\n")
        if menunovamente == '1':
            game()

game()