from operator import index
from tqdm import tqdm
from time import sleep
import os
import sys
sys.path.append(os.path.realpath("."))
import inquirer
import pandas as pd
from openpyxl.styles import PatternFill, Font
from openpyxl import Workbook, load_workbook
import matplotlib.pyplot as plt

# ----------------------------------------------

class Op_update():
    def options_update():
        os.system('cls')
        print('\tAtualizar informações sobre férias')
        sleep(1)
        os.system('cls')
        print('Escolha para quem dar férias!\n')
        sleep(1)
        while True:
            questions = [
                inquirer.List(
                    'atualizar',
                    message='',
                    choices=['Professores de Educação Básica', 'Auxiliar de Serviços de Educação Básica', 'Assistente Tecnico de Educação Básica']
                ),
            ]
            answers = inquirer.prompt(questions)['atualizar']
            if answers == 'Professores de Educação Básica':
                qtde_ferias = int(input('Dar férias de quantos dias? '))
                planilhaServidores = pd.read_excel('servidores.xlsx')
                planilhaServidores.loc[planilhaServidores['nmefet']=='PROFESSOR DE EDUCACAO BASICA', 'ferias'] = qtde_ferias
                planilhaServidores.to_excel('servidores.xlsx', index=False)
                sleep(1)
                print(f'Atualizando para {qtde_ferias} dias de férias.')  
            elif answers == 'Auxiliar de Serviços de Educação Básica':
                qtde_ferias = int(input('Dar férias de quantos dias? '))
                planilhaServidores = pd.read_excel('servidores.xlsx')
                planilhaServidores.loc[planilhaServidores['nmefet']=='AUXILIAR DE SERVICOS DE EDUCACAO BASICA', 'ferias'] = qtde_ferias
                planilhaServidores.to_excel('servidores.xlsx', index=False)
                sleep(1)
                print(f'Atualizando para {qtde_ferias} dias de férias.')
            elif answers == 'Assistente Tecnico de Educação Básica':
                qtde_ferias = int(input('Dar férias de quantos dias? '))
                planilhaServidores = pd.read_excel('servidores.xlsx')
                planilhaServidores.loc[planilhaServidores['nmefet']=='ASSISTENTE TECNICO DE EDUCACAO BASICA', 'ferias'] = qtde_ferias
                planilhaServidores.to_excel('servidores.xlsx', index=False)
                sleep(1)
                print(f'Atualizando para {qtde_ferias} dias de férias.') 
            continuar = input('Atualizar novamente? S/n').upper()
            if continuar == 'S':
                continue
            else:
                sleep(1)
                os.system('cls')
                break
