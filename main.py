import tkinter as tk
import pyinstaller.main
import shutil
import os

def generate_executable():
    script_file = 'executable.py'
    pyinstaller.main.run([
        'pyinstaller',
        '--onefile',
        script_file
    ])
    
    dist_folder = os.path.join(os.getcwd(), 'dist')
    exe_file = os.path.join(dist_folder, os.path.splitext(script_file)[0])
    shutil.move(exe_file, '.')
    shutil.rmtree(dist_folder)
    
    print('Executable file generated!')

root = tk.Tk()
root.title('Generate Executable') 

btn = tk.Button(root, text='Generate', command=generate_executable)
btn.pack(pady=20)

root.mainloop()
