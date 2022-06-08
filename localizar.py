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

class Op_localizar():
    def options_loc():
        while True:
            os.system('cls')
            questions = [
                inquirer.List(
                    'localizar',
                    message='O que deseja localizar? ',
                    choices=['Cargo por nome inteiro da pessoa','Descrição Item do Servidor (ativo)','Descrição Item do Servidor (inativo)', 'grafico'],
                ),
            ]
            answers = inquirer.prompt(questions)['localizar']
            if answers == 'Descrição Item do Servidor (ativo)':
                planilhaServidores = pd.read_excel('servidores.xlsx')
                print(planilhaServidores.loc[planilhaServidores['descsitser']=='ATIVO', ['nome', 'descsitser', 'descinst', 'descunid']])                                    
            elif answers == 'Descrição Item do Servidor (inativo)':
                planilhaServidores = pd.read_excel('servidores.xlsx')
                print(planilhaServidores.loc[planilhaServidores['descsitser']=='INATIVO', ['nome', 'descsitser', 'descinst', 'descunid']])
            elif answers == 'Cargo por nome inteiro da pessoa':
                while True:
                    planilhaServidores = pd.read_excel('servidores.xlsx')
                    procurar_nome = input('\n\33[94mPor qual nome deseja procurar?\33[m\n').upper()
                    sleep(1)
                    print('')
                    print('-'*20)
                    print('\33[33mESSA PESSOA TEM UM CARGO COMO:\33[m')
                    print(planilhaServidores.loc[planilhaServidores['nome']==procurar_nome,['nmefet']])
                    print('-'*20)
                    continuar = input('\nProcurar novamente? S/n').upper()
                    if continuar == 'S':
                        continue
                    else:
                        break
            elif answers == 'grafico':
                labels = ['ATIVO', 'INATIVO', 'ATIVO/NAO CONSIDERADOS RECEBIMENTOS EXTRA SISAP', 'ATIVO/NAO ESTAO INFORMADOS OS VALORES EXTRA SISAP', 'DESIGNADO AO SERVICO ATIVO']
                qtde = [313101, 5317, 30, 419, 1788]
                
                ax1 = plt.subplots()
                
                ax1.pie(qtde, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90) 
                plt.show()
            continuar = input('\33[33m\nLocalizar mais dados?\33[m S/n').upper()
            if continuar == 'S':
                continue
            else:
                break