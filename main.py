import os
import time
from add import Adicionar
from remover import Remover
from read import Exibir
from atualizar import Atualizar

def limpar_terminal():
    print('\033c', end='')
    
loop_on = True

while loop_on == True:
    print('SISTEMA DE CONTROLE')
    print('')
    print('Projeto de CRUD com Python e MongoDB')
    print('')
    print('Escolha entre as opcoes:')
    print('1 - Criar')
    print('2 - Deletar')
    print('3 - Exibir ')
    print('4 - Atualizar ')
    print('5 - Sair ')
    escolha = input("Digite uma opção (1, 2 ou 3): ")
        
    if escolha == '1':
        limpar_terminal()
        adicionar = Adicionar
        adicionar.adicionar()
        
    if escolha == '2':
        limpar_terminal()
        remover = Remover
        remover.remover()
        
    if escolha == '3':
        set_freeze = True
        limpar_terminal()
        while set_freeze:
            exibir = Exibir
            exibir.exibir()
            print('Gostaria de voltar ao menu? Y/N')
            get_menu = input()
            if (get_menu == 'Y') or (get_menu== 'y'):
                set_freeze = False
        limpar_terminal()
        
    if escolha == '4':
        limpar_terminal()
        atualizar = Atualizar
        atualizar.atualizar()
        
    if escolha == '5':
        limpar_terminal()
        loop_on = False  
    
    if escolha not in ['1','2','3','4','5']:
        print(f'Opcao selecionada: {escolha}... aguarde.')
        time.sleep(1)
        print('.')
        time.sleep(1)
        print('...')
        time.sleep(1)
        print('.....')
        time.sleep(1)

    
print("Voce Finalizou o sistema.")

