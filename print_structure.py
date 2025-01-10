import os

def print_tree(path, indent='', exclude_dirs=['__pycache__', 'migrations', 'node_modules', 'venv' , '.gitignore']):
    """
    Функция для рекурсивного вывода древовидной структуры каталога.

    Args:
        path: Путь к каталогу.
        indent: Отступ для текущего уровня вложенности.
        exclude_dirs: Список каталогов, которые не будут выводиться.
    """

    for root, dirs, files in os.walk(path, followlinks=True):
        level = root.replace(path, '').count(os.sep)
        indent = ' ' * 4 * level
        print(indent + os.path.basename(root)) # Убрал encoding, print сам разберется

        for f in files:
            print(indent + '    ' + f) # Улучшил отступ

        # Выводим только те каталоги, которые не нужно исключать
        for d in dirs:
            if d not in exclude_dirs:
                print_tree(os.path.join(root, d), indent + '    ') # Улучшил отступ

# Используем raw-строку
path = r'C:\Users\Sh\Desktop\anketa'
print_tree(path)