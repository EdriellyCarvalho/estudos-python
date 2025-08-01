import os
import shutil
from tkinter import Tk, filedialog

Tk().withdraw()
source = filedialog.askdirectory(title="Selecione a pasta que deseja organizar")

if not source:
    print("Nenhuma pasta selecionada. Encerrando...")
    exit()

print(f"Organizando arquivos em: {source}")

for file in os.listdir(source):
    path = os.path.join(source, file)

    if os.path.isdir(path):
        continue
    ext = os.path.splitext(file)[1].replace('.', '')
    if not ext:
        ext = "sem_extensao"
    dest = os.path.join(source, ext)
    os.makedirs(dest, exist_ok=True)

    shutil.move(path, os.path.join(dest, file))

print("✅ Organização concluída com sucesso!")