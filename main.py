from termcolor import colored
from os import system
from time import sleep


class JogoDaVelha:
    jogador = colored('X', 'cyan')
    continuar = True
    matriz = [0, 1, 2, 3, 4, 5, 6, 7, 8]


    def limpar():
        system('cls')


    #Troca o valor do índice escolhido pelo valor da variavel jogador
    def trocar_indice(jogada):
        if JogoDaVelha.matriz[jogada] == colored('X', 'cyan') or JogoDaVelha.matriz[jogada] == colored('O', 'yellow'):
            return 'Este lugar esta ocupado'

        else:
            JogoDaVelha.matriz[jogada] = JogoDaVelha.jogador


    #Como o nome indica, o método exibe a matriz na tela
    def exibir():
        print()

        matriz = JogoDaVelha.matriz
        # Exibe os valores contidos na lista de forma formatada
        print(
        """                        
                    |       |         
                {0}   |   {1}   |   {2}
                    |       |
            — — — — — — — — — — — — —
                    |       |
                {3}   |   {4}   |   {5}
                    |       |
            — — — — — — — — — — — — —
                    |       |
                {6}   |   {7}   |   {8}
                    |       |
            
        """.format(matriz[0], matriz[1], matriz[2], matriz[3], matriz[4], matriz[5], matriz[6], matriz[7], matriz[8]))


    def sair():
        sair = str(input('Sair? [S/N] -> ')).upper()

        if sair == 'S':
            print('Saindo...')
            sleep(1)
            JogoDaVelha.limpar( )
            JogoDaVelha.continuar = False

        else:
            JogoDaVelha.limpar()
            JogoDaVelha.matriz = [0, 1, 2, 3, 4, 5, 6, 7, 8]


    #O método analisa a matriz e indica se ha um vencedor, se houver ele exibira qual foi
    def vencedor():
        #Lista que contém as combinações de vitória.
        matriz = JogoDaVelha.matriz

        comb_vencedora = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]

        #O laço de repetição desempacota os valores da lista e os coloca em 3 variaveis. Logo em seguida confirma se os valores contidos nas variaveis correspondem ao valor inserido na variavel "jogador". Caso os valores correspondam ao valor contido na variavel "jogador" o programa printa na tela o numero do jogador vencedor, exibe a matriz e troca o valor da variavel "continuar" para False parando então o loop principal.
        for a, b, c in comb_vencedora:

            if matriz[a] == matriz[b] == matriz[c] == JogoDaVelha.jogador:
                JogoDaVelha.limpar()

                print(f'\nO jogador {"1" if JogoDaVelha.jogador == colored("X", "cyan") else "2"} ganhou\n')
                
                JogoDaVelha.exibir()
                JogoDaVelha.sair()

        if JogoDaVelha.continuar == True:
                    JogoDaVelha.empate()        


    def empate():
        matriz = JogoDaVelha.matriz
        cont = 0
        for c in matriz:
            if type(c) == str:
                cont += 1

        if cont == 9:
            JogoDaVelha.limpar()
            print('EMPATE')
            JogoDaVelha.exibir()
            JogoDaVelha.sair()


#O laço continua ativo enquanto o valor de "continuar" for True
while JogoDaVelha.continuar:
    JogoDaVelha.limpar()

    print(f'Jogador -> {"1" if JogoDaVelha.jogador == colored("X", "cyan") else "2"}')
    JogoDaVelha.exibir()

    print('-=' * 20)

    while True:
        jogada = None
        try:
            jogada = int(input('-> '))

        except ValueError:
            print('Digite um numero inteiro!')

        if type(jogada) != int:
            print('Digite um valor valido!') 

        elif jogada > 8 or jogada < 0:
            print('Digite um numero entre 0 e 8')

        elif JogoDaVelha.trocar_indice(jogada) == 'Este lugar esta ocupado':
            print(JogoDaVelha.trocar_indice(jogada))
            continue

        else:
            break

    print('=-' * 20)
    JogoDaVelha.vencedor()

    if JogoDaVelha.jogador == colored('X', 'cyan'):
        JogoDaVelha.jogador = colored('O', 'yellow')
    
    else:
        JogoDaVelha.jogador = colored('X', 'cyan')
