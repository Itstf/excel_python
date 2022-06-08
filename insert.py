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

class Op_insert():
    def options_insert():
        planilhaServidores = pd.read_excel('servidores.xlsx')
        linha = len(planilhaServidores)
        for i in range(len(planilhaServidores.columns)):
            planilhaServidores.loc[linha, planilhaServidores.columns[i]] = input(f'Insira {planilhaServidores.columns[i]}: ')
        planilhaServidores.to_excel('servidores.xlsx', index=False)