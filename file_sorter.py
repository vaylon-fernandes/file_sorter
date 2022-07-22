import os
from pathlib import Path
import shutil
from keywords import keywords
from ignore import ignore
from folder_paths import folder_path


def sorter(source_folder: str):
    os.chdir(source_folder)
    folder = os.listdir(".")
    for file in folder:
        source = Path(file)
        extension = source.suffix
        file_type = extension.removeprefix(".")
        is_folder = os.path.isdir(file)
        is_video = extension == ".mp4" or extension == ".mkv" or extension == ".avi"
        to_ignore = [True for ignore_keyword in ignore if ignore_keyword in extension]
        courses_folder_exists = os.path.exists("courses")

        if is_folder or any(to_ignore):
            continue

        new_directory = folder_path[file_type]
        keyword_present = [True for keyword in keywords if keyword in file]

        if any(keyword_present) and is_video:
            if not courses_folder_exists:  # if courses folder doesn't exist, create it
                os.mkdir("courses")
            destination = "courses"
            shutil.move(file, destination)
        else:
            folder_exists = os.path.exists(new_directory)
            if folder_exists:
                increment = 0
                while True:
                    file_exists = os.path.exists(f"{new_directory}\\{file}")
                    if not file_exists:
                        shutil.move(file, new_directory)
                        break
                    increment += 1
                    new_name = f"{source.stem}_{increment}{source.suffix}"
                    try:
                        os.rename(file, f"{new_directory}\\{new_name}")
                    except FileExistsError:
                        continue
                    break
            else:
                new_folder = Path() / new_directory
                new_folder.mkdir(parents=True, exist_ok=True)
                shutil.move(file, new_folder)


if __name__ == "__main__":
    PATH = "../../Downloads"
    sorter(source_folder=PATH)
