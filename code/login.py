import customtkinter
import sqlite3
from tkinter import messagebox

def check_login():
    user_email = email.get
    user_password = password.get
    
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor
    
    cursor.execute("SELECT * FROM users WHERE email=? AND password=?", (user_email, user_password))
    result = cursor.fetchone()
    
    if result:
        messagebox.showinfo("Login", "Login realizado com sucesso")
        print('Usuário logado:', user_email)
        
    else:
        messagebox.showerror('Erro,' 'E-mail ou senha incorretos!')
    
    conn.close()


customtkinter.set_appearance_mode('Dark')
customtkinter.set_default_color_theme('green')

window = customtkinter.CTk()
window.geometry('500x320')

text = customtkinter.CTkLabel(window, text= 'Assitente Gshop', font=('Arial', 24, 'bold'))
text.pack(padx=10, pady=10)

email = customtkinter.CTkEntry(window, placeholder_text='Seu E-mail')
email.pack(padx=10, pady=10)

password = customtkinter.CTkEntry(window, placeholder_text='Sua Senha', show='*')
password.pack(padx=10, pady=10)

checkbox = customtkinter.CTkCheckBox(window, text='Lembre do meu usuário')
checkbox.pack(padx=10, pady=10)

button = customtkinter.CTkButton(window,text='Login', command=check_login)
button.pack(padx=10, pady=15)

window.mainloop()