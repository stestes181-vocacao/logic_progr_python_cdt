'''
pyintaller
converte um arquivo: python em um arquivo * exe;

tkinter, messagebox, customtkinter 
importar esse ou os pacotes.

Programa em CMD - Tela preta, interagir por teclado , sem ineterface gráfica
programa em GUI - Tela com janelas, botoes, campos de texto, etc.Intergair por mouse e teclado.

'''

# importar o pacote customtkinter
import customtkinter

# Configurações iniciais do customtkinter
customtkinter.set_appearance_mode("dark")  # Modo escuro
customtkinter.set_default_color_theme("dark-blue")  # Tema de cor escuro

# Criar a janela e definir o tamanho
janela = customtkinter.CTk()
janela.geometry("400x300")


janela.title("Explicação do Módulo Pacote - GUI 💛💙")

texto = customtkinter.CTkLabel(janela, text="Tela de fazer login")

email = customtkinter.CTkEntry(janela, placeholder_text="Digite seu email")

botao_login = customtkinter.CTkButton(janela, text="Login", command=click_login)



texto.pack(pady=10, padx=10)
email.pack(pady=10, padx=10)
botao_login.pack(pady=10, padx=10)



janela.mainloop()
