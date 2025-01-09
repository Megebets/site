import os

def print_tree(path, indent=''):
    """
    Функция для рекурсивного вывода древовидной структуры каталога.

    Args:
        path: Путь к каталогу.
        indent: Отступ для текущего уровня вложенности.
    """

    for root, dirs, files in os.walk(path):
        level = root.replace(path, '').count(os.sep)
        indent = ' ' * 4 * level
        print(indent + os.path.basename(root))

        dirs[:] = [d for d in dirs if d not in ['__pycache__', 'migrations', 'node_modules', 'venv']]
        for f in files:
            print(indent + '  ' + f)

# Замените 'путь_к_вашему_проекту' на фактический путь к вашему проекту
path = 'C:/Users/Sh/Desktop/site/anketa'
print_tree(path)