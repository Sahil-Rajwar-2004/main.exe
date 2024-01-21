import os
import webbrowser

about = """
CLI main.exe
version: 0.1
homepage: https://www.github.com/Sahil-Rajwar-2004/main.exe/
created: 22-01-2024
status: updating
author: Sahil Rajwar

why main.exe?

the main aim to build this was to merge command line interface with some extra functionality that we do in
our day to day life such as browsing the internet. I already specified some url links which are given below.

1. open insta (open instagram)
2. open yt (open youtube)
3. open reddit (open reddit)
4. open gh (open github)

Note: This project is open source, and contributions are welcome.
      If you have any ideas or improvements, feel free to make changes.
      Your contributions are appreciated.

"""

RUNNING = True

INSTAGRAM = "https://instagram.com/"
GITHUB = "https://github.com/"
YOUTUBE = "https://youtube.com/"
REDDIT = "https://www.reddit.com/"

def show_dirs():
    tag = None
    for x in os.listdir():
        if os.path.isfile(x):
            tag = "file"
        else:
            tag = "directory"
        print(f"{x} ({tag})")

while RUNNING:
    try:
        cmd = input(f"[{os.getcwd()}]: ")
        if cmd == "exit" or cmd == "qqq":
            RUNNING = False

        elif cmd == "ls" or cmd == "dir":
            show_dirs()

        elif cmd == "cls":
            os.system(cmd)

        elif cmd == "about":
            print(about)

        elif cmd.startswith("cd "):
            new_dir = cmd.split(" ",1)[1]
            try:
                os.chdir(new_dir)
            except FileNotFoundError:
                print(f"Directory '{new_dir}' not found.")

        elif cmd.startswith("details "):
            file_name = cmd.split(" ",1)[1]
            try:
                file_stat = os.stat(file_name)
                print(f"File: {file_name}")
                print(f"Size: {file_stat.st_size} bytes")
                print(f"Created: {file_stat.st_ctime}")
                print(f"Modified: {file_stat.st_mtime}")
            except FileNotFoundError:
                print(f"File '{file_name}' not found.")

        elif cmd.startswith("mkdir "):
            new_dir_name = cmd.split(" ",1)[1]
            try:
                os.mkdir(new_dir_name)
                print(f"Directory '{new_dir_name}' created.")
            except FileExistsError:
                print(f"Directory '{new_dir_name}' already exists.")

        elif cmd.startswith("delete "):
            file_to_delete = cmd.split(" ",1)[1]
            try:
                os.remove(file_to_delete)
                print(f"File '{file_to_delete}' deleted.")
            except FileNotFoundError:
                print(f"File '{file_to_delete}' not found.")

        elif cmd.startswith("rmdir "):
            dir_to_delete = cmd.split(" ",1)[1]
            try:
                os.rmdir(dir_to_delete)
                print(f"Directory '{dir_to_delete}' deleted.")
            except FileNotFoundError:
                print(f"Directory '{dir_to_delete}' not found.")

        elif cmd.startswith("cat "):
            file_name = cmd.split(" ",1)[1]
            try:
                with open(file_name,"r") as file:
                    content = file.read()
                    print(content)
            except FileNotFoundError:
                print(f"File '{file_name}' not found.")
            except Exception as error:
                print(f"An error occured: {error}")

        elif cmd.startswith("open "):
            name = cmd.split(" ",1)[1]
            if name.lower() == "insta":
                webbrowser.open(INSTAGRAM)
            elif name.lower() == "gh":
                webbrowser.open(GITHUB)
            elif name.lower() == "yt":
                webbrowser.open(YOUTUBE)
            elif name.lower() == "reddit":
                webbrowser.open(REDDIT)
            else:
                print("unknown request!")

        elif cmd.startswith("browse "):
            url = cmd.split(" ",1)[1]
            webbrowser.open(url)

        else:
            print("invalid command!")

    except KeyboardInterrupt as error:
        print(error)
    except Exception as error:
        print(error)
