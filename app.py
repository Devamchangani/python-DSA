
# # import subprocess

# # # Replace 'shortcut_path' with the path to your shortcut file
# # s = input(": ")
# # shortcut_path = f'C:\\Users\\Admin\\Desktop\\{s}.lnk'

# # try:
# #     subprocess.Popen(['start', shortcut_path], shell=True)
# #     print(f'Opened shortcut: {shortcut_path}')
# # except FileNotFoundError:
# #     print(f'Error: Shortcut not found at {shortcut_path}')
# # except Exception as e:
# #     print(f'An error occurred: {str(e)}')


# import os

# # Replace 'file_path' with the path to the file you want to open
# file_path = r"C:\Users\Admin\Documents\er.pdf"

# try:
#     os.startfile(file_path)
#     print(f'Opened {file_path}')
# except FileNotFoundError:
#     print(f'Error: File not found at {file_path}')
# except Exception as e:
#     print(f'An error occurred: {str(e)}')


import os

# Replace 'file_name' with the name of the file you want to find (including extension)
file_name = 'Chapter 13 - Practice Set.pdf'

def search_file(starting_directory, target_file_name):
    for root, dirs, files in os.walk(starting_directory):
        if target_file_name in files:
            file_path = os.path.join(root, target_file_name)
            try:
                os.startfile(file_path)
                print(f'Opened {file_path}')
                return  # Exit the function if the file is found and opened
            except Exception as e:
                print(f'Error opening {file_path}: {str(e)}')

# Replace 'C:\\' with the root directory where you want to start the search
search_directory = 'C:\\'

search_file(search_directory, file_name)
