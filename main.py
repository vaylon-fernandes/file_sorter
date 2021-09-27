from pathlib import Path
import os
import shutil


PATH = '../../Downloads'


def sorter():
    os.chdir(PATH)
    folder = os.listdir('.')
    for file in folder:
        extension = Path(file).suffix
        is_folder = extension == ''
        new_directory = extension.removeprefix('.')

        if is_folder:
            continue

        folder_exists = os.path.exists(new_directory)
        if folder_exists:
            shutil.move(file, new_directory)
        else:
            os.mkdir(new_directory)
            shutil.move(file, new_directory)


if __name__ == '__main__':
    sorter()
