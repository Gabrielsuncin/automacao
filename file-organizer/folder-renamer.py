import os
from datetime import datetime

log_folder = "/home/dev/Downloads/logs/"
renamer_log = open(log_folder + "renamer.log", "a")
target_folder = os.path.realpath('/home/dev/Downloads/clientes/')
folder_final_name = "declaracoes"
incorrect_names = ["Declaracoes", "Declarações", "declarações", "declaracoe", "DECLARACOES", "DECLARAÇÕES"]

for folder in os.listdir(target_folder):
    os.chdir(target_folder)
    try:
        files_dir = os.listdir(folder)
        for item in files_dir:
            if item in incorrect_names:
                os.chdir(folder)
                os.rename(item, folder_final_name)
                print(f'{datetime.now().strftime("%d/%m/%Y-%H:%M")} - pasta:{os.path.realpath(item)} '
                      f'renomeada para: {os.path.realpath(folder_final_name)}', file=renamer_log)
            else:
                print(f'Nenhuma pasta com nome incorreto', file=renamer_log)
    except:
        print(f'{datetime.now().strftime("%d/%m/%Y-%H:%M")} - Falha ao renomear pasta')


