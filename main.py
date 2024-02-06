import os.path
from src import py_file


main_dir = os.getcwd()
logs_dir = os.path.join(main_dir,"logs/")

cache_dirs = [os.path.join(main_dir,"src/__pycache__"),
              os.path.join(main_dir,"devtools/__pycache__"),
              ]
logs_dev = os.path.join(logs_dir,"logs_dev.log")
logs_run = os.path.join(logs_dir,"logs_run.log")

# Supprime les dossiers __pycache__
for i in cache_dirs :
    py_file.delete_directory(i)


# Supprime les fichiers d'une liste
files_to_clean = [logs_dev,
                  logs_run,
                  ]
py_file.delete_file(files_to_clean)
