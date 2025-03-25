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
    root.mainloop()
    
def main_app():
    window = tk.Tk()
    window.title("Password Manager")
    
    tk.Label(window, text='Welcome!').pack(pady=10)
    tk.Button(window, text='Add Password', width=20).pack(pady=5)
    tk.Button(window, text='View Passwords', width=20).pack(pady=5)
    tk.Button(window, text='Exit', width=20, command=window.destroy).pack(pady=20)

    window.mainloop()

if __name__ == '__main__':
    login_screen()