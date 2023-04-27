from tkinter import *
from tkinter import messagebox
import psutil

# Tạo form đăng nhập
root = Tk()
root.geometry('300x200')
root.title("Đăng nhập")

# Tạo biến lưu trữ thông tin đăng nhập
username = StringVar()
password = StringVar()

# Tạo các Label và Entry để nhập thông tin đăng nhập
Label(root, text="Tài khoản").place(x=30, y=50)
Entry(root, textvariable=username).place(x=100, y=50)

Label(root, text="Mật khẩu").place(x=30, y=80)
Entry(root, textvariable=password, show="*").place(x=100, y=80)

# Hàm kiểm tra thông tin đăng nhập
def login():
    if username.get() == "kay" and password.get() == "kaykay123":
        messagebox.showinfo("Đăng nhập thành công", "Chào mừng bạn đến với hệ thống!")
        root.destroy()  # Đóng form đăng nhập
        show_processes()  # Hiển thị danh sách quản lý tiến trình CPU và RAM
    else:
        messagebox.showerror("Lỗi đăng nhập", "Tài khoản hoặc mật khẩu không đúng!")

# Tạo Button để đăng nhập
Button(root, text="Đăng nhập", command=login).place(x=100, y=120)

# Hàm hiển thị danh sách quản lý tiến trình CPU và RAM
def show_processes():
    processes = []
    for proc in psutil.process_iter(attrs=['pid', 'name', 'cpu_percent', 'memory_percent']):
        processes.append([proc.info['pid'], proc.info['name'], proc.info['cpu_percent'], proc.info['memory_percent']])
    
    # Tạo form hiển thị danh sách quản lý tiến trình
    top = Toplevel()
    top.title("Danh sách quản lý tiến trình")
    top.geometry("600x400")
    
    # Tạo và điền thông tin quản lý tiến trình vào Table
    table = Frame(top)
    table.pack(side=TOP, padx=5, pady=5)
    
    Label(table, text="PID", font="Bold").grid(row=0, column=0, padx=5, pady=5, sticky=W)
    Label(table, text="Tên tiến trình", font="Bold").grid(row=0, column=1, padx=5, pady=5, sticky=W)
    Label(table, text="%CPU", font="Bold").grid(row=0, column=2, padx=5, pady=5, sticky=W)
    Label(table, text="%RAM", font="Bold").grid(row=0, column=3, padx=5, pady=5, sticky=W)
    
    for i, process in enumerate(processes):
        pid = Label(table, text=process[0])
        name = Label(table, text=process[1])
        cpu = Label(table, text=process[2])
        ram = Label(table, text=process[3])

        pid.grid(row=i+1, column=0, padx=5, pady=5, sticky=W)
        name.grid(row=i+1, column=1, padx=5, pady=5, sticky=W)
        cpu.grid(row=i+1, column=2, padx=5, pady=5, sticky=W)
        ram.grid(row=i+1, column=3, padx=5, pady=5, sticky=W)

# Chạy form đăng nhập
root.mainloop()