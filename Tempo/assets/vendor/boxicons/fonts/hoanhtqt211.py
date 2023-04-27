import psutil
import tkinter as tk

from tkinter import *

def get_system_status():
  
    cpu_usage = psutil.cpu_percent()
    mem = psutil.virtual_memory()
    mem_usage = mem.used / mem.total * 100

    
    cpu_label.configure(text="Sử Dung CPU: {:.2f}%".format(cpu_usage))
    mem_label.configure(text="Sử Dung Ram: {:.2f}%".format(mem_usage))

def get_process_info():
   
    process_list = []
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            proc_info = proc.info
            process_list.append("{} ({})".format(proc_info['name'], proc_info['pid']))
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    process_label.configure(text="\n".join(process_list))

root = tk.Tk()

root.title("giao diện tiến trình, dung lượng")
root.geometry('500x600')

system_button = tk.Button(root, text="Xem Dung Lượng", command=get_system_status)
system_button.pack()
system_button.pack(side = LEFT)

process_button = tk.Button(root, text="Xem Tiến Trình", command=get_process_info)
process_button.pack()
process_button.pack(side = RIGHT)


process_label = tk.Label(root, text=" ")
process_label.pack()


cpu_label = tk.Label(root, text="CPU Sử Dụng: ")
cpu_label.pack()

process_label = tk.Label(root, text=" ")
process_label.pack()



mem_label = tk.Label(root, text="Memory Sử Dụng : ")
mem_label.pack()

process_label = tk.Label(root, text=" ")
process_label.pack()
process_label = tk.Label(root, text=" ")
process_label.pack()


process_label = tk.Label(root, text="Process list: ", bg="violet", )
process_label.pack()
process_label = tk.Label(root, text=" ")
process_label.pack()


root.mainloop()
