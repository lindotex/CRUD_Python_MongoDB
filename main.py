import os
import time
from add import Adicionar
from remover import Remover
from read import Exibir
from atualizar import Atualizar
from prettytable import PrettyTable

def limpar_terminal():
    print('\033c', end='')
    
loop_on = True

while loop_on == True:
    t = PrettyTable(['Numero','Opcao'])
    print('SISTEMA DE CONTROLE')
    print('Projeto de CRUD com Python e MongoDB')
    print('')
    print('Escolha entre as opcoes:')
    t.add_row(['1','Criar'])
    t.add_row(['2','Deletar'])
    t.add_row(['3','Exibir'])
    t.add_row(['4','Atualizar'])
    t.add_row(['5','Sair'])
    print(t)
    escolha = input("Digite uma opção (1, 2, 3, 4 ou 5): ")
        
    if escolha == '1':
        print(f'Opcao selecionada: {escolha}... aguarde.')
        time.sleep(2)
        limpar_terminal()
        adicionar = Adicionar
        adicionar.adicionar()
        
    if escolha == '2':
        print(f'Opcao selecionada: {escolha}... aguarde.')
        time.sleep(2)
        limpar_terminal()
        remover = Remover
        remover.remover()
        
    if escolha == '3':
        print(f'Opcao selecionada: {escolha}... aguarde.')
        time.sleep(2)
        set_freeze = True
        limpar_terminal()
        while set_freeze:
            exibir = Exibir
            exibir.exibir()
            print('Gostaria de voltar ao menu? Y/N')
            get_menu = input()
            if (get_menu == 'Y') or (get_menu== 'y'):
                set_freeze = False
            if (get_menu == 'N') or (get_menu== 'n'):
                print('Estamos encerrando o sistema.')
                time.sleep(2)
                set_freeze = False
                loop_on = False  
        limpar_terminal()
        
    if escolha == '4':
        print(f'Opcao selecionada: {escolha}... aguarde.')
        time.sleep(2)
        limpar_terminal()
        atualizar = Atualizar
        atualizar.atualizar()
        
    if escolha == '5':
        print(f'Opcao selecionada: {escolha}... aguarde.')
        time.sleep(2)
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
        print(f'Valor {escolha} nao e uma opcao valida, estamos retornando ao menu principal...')
        time.sleep(2)
        limpar_terminal()

    
print("Voce Finalizou o sistema.")

