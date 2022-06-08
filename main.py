import time
from tqdm import tqdm
from time import sleep
import os
import sys
from changeColor import Op_chanceColor

from update import Op_update
sys.path.append(os.path.realpath("."))
import inquirer
from localizar import Op_localizar
from insert import Op_insert
from delete import Op_delete
from update import Op_update
from datetime import datetime

# ----------------------------------------------

data = datetime.now()
data = data.strftime('%d/%m/%Y %H:%M')

inicio = time.time()

with open('arquivo.txt','a') as arquivo:
    arquivo.write(f'Logg\nInicialização: {data}\n')
    time.sleep(3)

class Menu():    
    os.system('cls')
    def __init__(self, insert, localizar, update):
        self.__inserir = insert
        self.__localizar = localizar
        self.__atualizar = update
    
    def get_inserir(self):
        return self.__inserir
    def set_inserir(self,inserir):
        self.inserir = inserir
    def get_localizar(self):
        return self.__localizar
    def set_localizar(self, localizar):
        self.localizar = localizar
    def get_atualizar(self):
        return self.__atualizar
    def set_atualizar(self, atualizar):
        self.__atualizar = atualizar
        
    def loading(self):
        for i in tqdm(range(100)):
            sleep(0.01)
        sleep(1)
            
    def slowprint(texto, atraso=0.1):
        for c in texto:
            print(c,end='',flush=True)
            sleep(atraso)
    slowprint('\33[105mTRABALHANDO COM PLANILHAS - Thaiza Favarelli - 1DES\33[m')
            
    def intro(self):
        os.system('cls')
        print('''
              \33[33mENTRANDO . . .\33[m
              ''')
        sleep(1)
        print(f'\33[33mData e hora de login: {data}\33[m')
        sleep(1.5)
        os.system('cls')
            
    def options(self):
        while True:
            questions = [
                inquirer.List(
                    "Escolha",
                    message="O que deseja fazer?",
                    choices=['Localizar dados na planilha', 'Inserir dados na planilha', 'Apagar dados da planilha', 'Atualizar dados da planilha', 'Mudar cor do cabeçalho', '\33[33mFechar\33[m'],
                ),
            ]
            answers = inquirer.prompt(questions)['Escolha']
            if answers == 'Localizar dados na planilha':
                sleep(1)
                Op_localizar.options_loc()
                print('\n')
                sleep(2)
            elif answers == 'Inserir dados na planilha':
                sleep(1)
                Op_insert.options_insert()
                print('\n')
                sleep(2)      
            elif answers == 'Apagar dados da planilha':
                Op_delete.options_delete() 
            elif answers == 'Atualizar dados da planilha':
                 sleep(1)
                 Op_update.options_update()
                 print('\n')
                 sleep(1)
            elif answers == 'Mudar cor do cabeçalho':
                Op_chanceColor.options_changeColor()
            elif answers == '\33[33mFechar\33[m':
                print(''' 
                      \33[33mJá vai? 
                      Não precisa de mais nada?\33[m
                      ''')
                sleep(1.5)
                os.system('cls')
                print('''
                      \33[33mAté Logo!!
                      . . .\33[m
                      ''')
                sleep(1)
                data = datetime.now()
                data = data.strftime('%d/%m/%Y %H:%M')
                print(f'Data de encerramento: {data}')
                break
                        
menu = Menu('','','')

menu.loading()
menu.intro()
menu.options()

fim = time.time()
delta = (round)(fim - inicio,2)

sleep(1)
print(f'Tempo de duração no programa: {delta}s')