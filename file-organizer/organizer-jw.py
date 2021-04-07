import os
import shutil
from datetime import datetime

log_folder = "/home/dev/Downloads/logs/"
os.chdir('/home/dev/Downloads')
initial_folder = os.path.realpath('/home/dev/Downloads/dctfs')
organizer_log = open(log_folder + "organizer-jw.log", "a")
target_folder = os.path.realpath('/home/dev/Downloads/teste-move-script/clientes/')

for file in os.listdir(initial_folder):
    file_lazy = file.split('-')[0]
    folder_list = []
    os.chdir(target_folder)
    for folder in os.listdir(target_folder):
        if folder.startswith(file_lazy):
            moved_folder = os.path.join(os.path.realpath(folder) + '/declaracoes')
            folder_list.append(moved_folder)
    print(folder_list[0])
    os.chdir(initial_folder)
    print(os.path.realpath(file))
    print("\n")

    shutil.move(file, folder_list[0])
    print(f'{datetime.now().strftime("%d/%m/%Y-%H:%M")} - arquivo: '
          f'{file} movido para: {folder_list[0]}', file=organizer_log)
