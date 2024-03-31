import os
import shutil

os.chdir("C:/Users/juand/Downloads")

while (True):

    if os.path.exists("Documentos") == True:
        pass
    else:
        os.mkdir("Documentos")
        continue

    if os.path.exists("Comprimidos") == True:
        pass
    else:
        os.mkdir("Comprimidos")
        continue

    if os.path.exists("Exe") == True:
        pass
    else:
        os.mkdir("Exe")
        continue

    if os.path.exists("Fotos") == True:
        pass
    else:
        os.mkdir("Fotos")
    break


# Documentos
ex_documentos = r".pdf", r".doc", r".docx", r".txt", r".xlsl", r".ppt", r".pptx", r".xls"
documentos = [_ for _ in os.listdir() if _.endswith(ex_documentos)]

for i in documentos:
    shutil.move(i, "Documentos")

# Comprimidos
ex_comprimidos = r".rar", r".zip", r".7z"
comprimidos = [_ for _ in os.listdir() if _.endswith(ex_comprimidos)]

for i in comprimidos:
    shutil.move(i, "Comprimidos")

# Ejecutables
ex_exe = r".exe", r".iso", r".ISO"
exe = [_ for _ in os.listdir() if _.endswith(ex_exe)]

for i in exe:
    shutil.move(i, "Exe")

# Fotos
ex_fotos = r".png", r".jpg", r".jpeg", r".gif", r".tiff", r".bmb", r".webp"
fotos = [_ for _ in os.listdir() if _.endswith(ex_fotos)]

for i in fotos:
    shutil.move(i, "Fotos")
