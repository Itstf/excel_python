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

class Op_delete():
    def options_delete():
        while True:
            planilhaServidores = pd.read_excel('servidores.xlsx')
            questions = [
                inquirer.List(
                    'apagar',
                    message='Qual coluna deseja deletar? ',
                    choices=['teto', 'judic', 'eventual', 'ir', 'prev', 'rem_pos'],
                ),
            ]
            answers = inquirer.prompt(questions)['apagar']
            if answers == 'teto':
                planilhaServidores.drop(['teto'], axis=1, inplace=True)
                planilhaServidores.to_excel('servidores.xlsx', index=False)
            elif answers == 'judic':
                planilhaServidores.drop(['judic'], axis=1, inplace=True)
                planilhaServidores.to_excel('servidores.xlsx', index=False)
            elif answers == 'eventual':
                planilhaServidores.drop(['eventual'], axis=1, inplace=True)
                planilhaServidores.to_excel('servidores.xlsx', index=False)
            elif answers == 'ir':
                planilhaServidores.drop(['ir'], axis=1, inplace=True)
                planilhaServidores.to_excel('servidores.xlsx', index=False)           
            elif answers == 'prev':
                planilhaServidores.drop(['prev'], axis=1, inplace=True)
                planilhaServidores.to_excel('servidores.xlsx', index=False)   
            elif answers == 'rem_pos':
                planilhaServidores.drop(['rem_pos'], axis=1, inplace=True)
                planilhaServidores.to_excel('servidores.xlsx', index=False)
            continuar = input('Deletar algo mais? S/n \n').upper()
            if continuar == 'S':
                sleep(1)
                os.system('cls')
                continue
            else:
                sleep(1)
                os.system('cls')
                break