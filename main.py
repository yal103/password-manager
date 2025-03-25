# Runs the app

import tkinter as tk
from tkinter import messagebox

def login_screen():
    
    def verify_password():
        password = entry.get()
        if password == 'master123': # will replace later with encrypted
            root.destroy()
            main_app()
        else:
            messagebox.showerror("Error", "Incorrect Password")
            
    root = tk.Tk()
    root.title("Password Manager Login") 
    root.geometry("300x150")
    
    tk.Label(root, text="Enter Master Password").pack(pady=10)
    entry = tk.Entry(root, show="*")
    entry.pack()
    tk.Button(root, text='Login', command=verify_password).pack(pady=10)
    root.bind('<Return>', lambda event=None: verify_password())
    root.mainloop()
    
def main_app():
    window = tk.Tk()
    window.title("Password Manager")
    
    tk.Label(window, text='Welcome!').pack(pady=10)
    tk.Button(window, text='Add Password', command=add_password_screen, width=20).pack(pady=5)
    tk.Button(window, text='View Passwords', width=20).pack(pady=5)
    tk.Button(window, text='Exit', width=20, command=window.destroy).pack(pady=20)

    window.geometry("300x200")
    window.mainloop()
    
def add_password_screen():
    window = tk.Toplevel()
    window.title("Add Password")
    
    tk.Label(window, text='Website').grid(row=0, column=0, padx=10, pady=5)
    website_entry = tk.Entry(window)
    website_entry.grid(row=0, column=1, padx=10, pady=5)
    
    tk.Label(window, text='Username/Email').grid(row=1, column=0, padx=10, pady=5)
    username_entry = tk.Entry(window)
    username_entry.grid(row=1, column=1, padx=10, pady=5)
    
    tk.Label(window, text='Password').grid(row=2, column=0, padx=10, pady=5)
    password_entry = tk.Entry(window)
    password_entry.grid(row=2, column=1, padx=10, pady=5)
    
    def save_password():
        website = website_entry.get()
        username = username_entry.get()
        password = password_entry.get()
        
        if website and username and password:
            # will add encryption and file saving later
            print(f'{website} | {username} | {password}')
            messagebox.showinfo("Success", "Password Saved")
            window.destroy()
        else:
            messagebox.showerror("Error", "Please fill all fields")
    
    tk.Button(window, text='Save', command=save_password).grid(row=3, column=0, columnspan=2, padx=10, pady=10)
    
    

if __name__ == '__main__':
    login_screen()