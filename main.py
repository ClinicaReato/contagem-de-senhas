import menu
import filtragem
import salvamento
import os
import pandas as pd

caminho_da_planilha = ''

#Configurações do menu
tamanho_lateral_do_menu = 55
titulo = "Teste de menu da Reato"

#apresentação do menu
def main():
    #Variaveis do sistema
    Escolha_do_menu_principal = ''
    

    while Escolha_do_menu_principal != 'Sair':
        global caminho_da_planilha 
        #Apresentação do menu
        print('\n\n')
        menu.linha(tamanho_lateral_do_menu)
        menu.titulo("Sistema de contagem de atendimento dos prestadores",tamanho_lateral_do_menu)
        menu.linha(tamanho_lateral_do_menu)
        menu.linha(tamanho_lateral_do_menu)
        menu.alinhado_a_esquerda(" 1 - Adicionar arquivo",tamanho_lateral_do_menu)
        menu.linha(tamanho_lateral_do_menu)
        menu.alinhado_a_esquerda(' 2 - Gerar relatorio',tamanho_lateral_do_menu)
        menu.linha(tamanho_lateral_do_menu)
        menu.alinhado_a_esquerda(' 0 - Sair',tamanho_lateral_do_menu)
        menu.linha(tamanho_lateral_do_menu)
        #Escolha do usuario
        Escolha_do_menu_principal = input('Digite sua escolha: \n\n')

        match Escolha_do_menu_principal:
            case '0':
                Escolha_do_menu_principal = "Sair"
            case '1':
                os.system('cls')
                caminho_da_planilha = input('Arraste o arquivo para aqui:')
                caminho_da_planilha = caminho_da_planilha.replace("'","")
                caminho_da_planilha = caminho_da_planilha.replace("&","")
                caminho_da_planilha = caminho_da_planilha.strip()
            case '2':
                arquivo_limpo = filtragem.filtrar_planilha(caminho_da_planilha)
                salvamento.Salvar(arquivo_limpo)
            case _:
                print("o valor informado é invalido")

main()