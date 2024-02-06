import os.path
import shutil

def merge(*args, fill_value = None):
    '''Merge plusieurs listes en une seule
    '''
    max_length = max([len(lst) for lst in args])
    result = []
    for i in range(max_length):
        result.append([
        args[k][i] if i < len(args[k]) else fill_value for k in range(len(args))
        ])
    return result

def flatten_list(nested_list):
    '''Applati les listes imbriquées\n
    dans une liste
    '''
    if not bool(nested_list):
        return nested_list
    if isinstance(nested_list[0], list):
        return flatten_list(*nested_list[:1]) + flatten_list(nested_list[1:])
    return nested_list[:1] + flatten_list(nested_list[1:])

def memo_file_manipulation():
    '''Affiche un mémo sur la manipulation
    de fichiers
    '''
    clear_screen()
    print("Path at terminal when executing this file")
    print(os.getcwd() + "\n")

    print("This file path, relative to os.getcwd()")
    print(__file__ + "\n")

    print("This file full path (following symlinks)")
    full_path = os.path.realpath(__file__)
    print(full_path + "\n")

    print("This file directory and name")
    path, filename = os.path.split(full_path)
    print(path + ' --> ' + filename + "\n")

    print("This file directory only")
    print(os.path.dirname(full_path))


def clear_screen():
    '''Nettoie l'écran\n
    (du terminal ;) ).
    '''
    os.system(['clear', 'cls'][os.name == 'nt'])

def delete_directory(directory_path):
    '''Supprime un dossier et son contenu\n
    Les chemins de dossier doivent être des chemins absolus.\n
    Pour obtenir un chemin absolu :\n
    os.path.abspath("nom-du-fichier-ici")\n
    '''
    if os.path.isdir(directory_path):
        shutil.rmtree(directory_path)
        print(f'Dossier {directory_path} supprimé.')
    else:
        pass

def delete_file(file_path):
    '''Supprime le ou les fichiers indiqués
    '''
    for i in file_path:
        if os.path.exists(i):
            os.remove(i)
            print(f'Fichier {i} supprimé.')
        else:
            pass
