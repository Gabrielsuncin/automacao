import os
import shutil
from datetime import datetime

os.chdir('/home/dev/Downloads')
pasta_atual = os.path
file_organizer = open("organizer.log", "a")
for files in os.listdir():
    if files.endswith(('.png', '.jpeg', '.jpg', '.svg')):
        shutil.move(files, "/home/dev/Downloads/imagens")
        print(f'{datetime.now()} - arquivo: {files} movido para: {os.path.realpath(files)}', file=file_organizer)
    elif files.endswith(('.docx', '.csv', '.xlsx')):
        shutil.move(files, "/home/dev/Downloads/office")
        print(f'{datetime.now()} - arquivo: {files} movido para: {os.path.realpath(files)}', file=file_organizer)
    elif files.endswith('.pdf'):
        shutil.move(files, "/home/dev/Downloads/pdfs")
        print(f'{datetime.now()} - arquivo: {files} movido para: {os.path.realpath(files)}', file=file_organizer)
    elif files.endswith(('.db', '.sql')):
        shutil.move(files, "/home/dev/Downloads/backups/backups-db")
        print(f'{datetime.now()} - arquivo: {files} movido para: {os.path.realpath(files)}', file=file_organizer)
    elif files.endswith('.postman_collection.json'):
        shutil.move(files, "/home/dev/Downloads/backups/backups-postman")
        print(f'{datetime.now()} - arquivo: {files} movido para: {os.path.realpath(files)}', file=file_organizer)
    elif files.endswith('.txt'):
        shutil.move(files, "/home/dev/Downloads/anotacoes")
        print(f'{datetime.now()} - arquivo: {files} movido para: {os.path.realpath(files)}', file=file_organizer)

