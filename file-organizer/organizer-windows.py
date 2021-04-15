import os
import shutil


class Organizer(object):
    def __init__(self):
        self.login_user = os.getlogin()
        self.download_folder = f'c:/users/{self.login_user}/Downloads'
        self.folders = ['Imagens', 'Arquivos-office', 'Pdfs', 'Backups-db', 'Anotacoes', 'Installers', 'Zips']
        self.documents_folder = f'c:/users/{self.login_user}/OneDrive/Documents'

    def get_documents_folder(self):
        try:
            os.chdir(f'c:/users/{self.login_user}/OneDrive/Documents')
            self.documents_folder = f'c:/users/{self.login_user}/OneDrive/Documents'
        except FileNotFoundError:
            try:
                os.chdir(f'c:/users/{self.login_user}/OneDrive/Documentos')
                self.documents_folder = f'c:/users/{self.login_user}/OneDrive/Documentos'
            except FileNotFoundError:
                os.chdir(f'c:/users/{self.login_user}/Documents')
                self.documents_folder = f'c:/users/{self.login_user}/Documents'
        return self.documents_folder

    def folder_normalizer(self):
        doc_items = os.listdir(self.documents_folder)
        for folder in self.folders:
            if folder not in doc_items:
                os.chdir(self.documents_folder)
                os.mkdir(folder)
        os.chdir(self.download_folder)

    def move_file(self, file, target_folder):
        from datetime import datetime
        file_organizer = open("organizer.log", "a")
        from random import randint
        try:
            moved_file = shutil.move(file, f'{self.documents_folder}/{target_folder}/')
            print(f'{datetime.now()} - arquivo: {file} movido para: {os.path.realpath(moved_file)}',
                  file=file_organizer)
        except Exception:
            new_name = f"{''.join(file.split('.')[0:-1])}({randint(1, 99)}).{file.split('.')[-1]}"
            os.rename(file, new_name)
            moved_file = shutil.move(new_name, f'{self.documents_folder}/{target_folder}/')
            print(f'{datetime.now()} - arquivo: {new_name} movido para: {os.path.realpath(moved_file)}',
                  file=file_organizer)

    def organize_files(self):
        os.chdir(self.download_folder)
        for files in os.listdir():
            if files.endswith(('.png', '.jpeg', '.jpg', '.svg', '.jfif')):
                self.move_file(file=files, target_folder="Imagens")
            elif files.endswith(('.docx', '.doc', '.docm', '.odt', '.csv', '.xlsx', '.xls', '.xlt', '.pptx', '.ppt')):
                self.move_file(file=files, target_folder="Arquivos-office")
            elif files.endswith(('.tar', '.zip', '.targz', '.rar', '.xz')):
                self.move_file(file=files, target_folder="Zips")
            elif files.endswith(('.exe', '.msi')):
                self.move_file(file=files, target_folder="Installers")
            elif files.endswith('.pdf'):
                self.move_file(file=files, target_folder="Pdfs")
            elif files.endswith(('.db', '.sql')):
                self.move_file(file=files, target_folder="Backups-db")
            elif files.endswith('.txt'):
                self.move_file(file=files, target_folder="Anotacoes")

    def run(self):
        self.get_documents_folder()
        self.folder_normalizer()
        self.organize_files()
        return


if __name__ == '__main__':
    d = Organizer()
    d.run()
