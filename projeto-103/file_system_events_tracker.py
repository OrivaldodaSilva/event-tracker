import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from_dir='C:/Users/Arthur Lopes/Desktop/Game-code/docs'
class FileEventHandler(FileSystemEventHandler):
    def on_created(self,event):
        print(f'olá,{event.src_path}foi criado')
    def on_deleted(self, event):
        print(f'olá alguem excluiu {event.src_path}')
    def on_modified(self, event):
        print(f'olá alguem modificou {event.src_path}')
    def on_moved(self, event):
        print(f'olá alguem moveu {event.src_path}para{event.dest_path}')
# Inicialize a Classe Gerenciadora de Eventos
event_handler = FileEventHandler()

# Inicialize o Observer
observer = Observer()

# Agende o Observer
observer.schedule(event_handler, from_dir, recursive=True)

# Inicie o Observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("executando...")
except KeyboardInterrupt:
    print("interrompido!")
    observer.stop()