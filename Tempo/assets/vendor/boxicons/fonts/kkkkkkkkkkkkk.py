import tkinter as tk
import psutil

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("400x400")
        self.master.title("Đăng nhập")
        self.create_widgets()
        
    def create_widgets(self):
        self.username_label = tk.Label(self.master, text="Tên đăng nhập:")
        self.username_label.pack()
        self.username_entry = tk.Entry(self.master)
        self.username_entry.pack()
        self.password_label = tk.Label(self.master, text="Mật khẩu:")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.master, show="*")
        self.password_entry.pack()
        self.login_button = tk.Button(self.master, text="Đăng nhập", command=self.login)
        self.login_button.pack()
    
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        # Kiểm tra thông tin đăng nhập từ cơ sở dữ liệu hoặc tệp tin mật khẩu ở đây
        
        if username == "kay" and password == "kaykay123":
            self.show_process_list()
        else:
            tk.messagebox.showerror("Đăng nhập không thành công", "Tên đăng nhập hoặc mật khẩu của bạn không đúng!")
    
    def show_process_list(self):
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                proc_info = proc.as_dict(attrs=['pid', 'name'])
            except psutil.NoSuchProcess:
                pass
            else:
                print(proc_info['pid'], proc_info['name'])
        
root = tk.Tk()
app = Application(master=root)
app.mainloop()