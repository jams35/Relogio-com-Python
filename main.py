#Adicionadas as importações das bibliotecas utilizadas no projeto, incluindo: os, tkinter, time, para permitir o uso das funcionalidades necessárias ao projeto.
import tkinter as tk
from tkinter import *
import os
from time import strftime

# Cria a janela raiz da interface gráfica do usuário e configura suas propriedades
root = tk.Tk()  # cria uma nova janela
root.title('Relógio desktop com Python')  # define o título da janela
root.geometry('600x320')  # define a largura e a altura da janela
root.maxsize(600, 320)  # define o tamanho máximo da janela
root.minsize(600, 320)  # define o tamanho mínimo da janela
root.configure(background='#282a36')  # define a cor de fundo da janela

# Define a mensagem de boas-vindas para o usuário atual do sistema operacional
def get_mensagemBV():
    # Obtém o nome do usuário atual do sistema operacional
    nomeUsuario = os.getlogin()
    
    # Define a mensagem de boas-vindas na interface gráfica do usuário
    mensagemBV.config(text='Olá, ' + nomeUsuario)


# Define funções para atualizar a data e o horário no aplicativo
def get_data():
    # Obtém a data atual e formata no padrão: Dia da semana, dia do mês, mês e ano.
    data_atual = strftime('%a, %d, %b, %Y')
    
    # Define o texto do Label de data para a data atual
    data.config(text=data_atual)

def get_horario():
    # Obtém o horário atual em um formato legível para humanos
    hora_atual = strftime('%H:%M:%S')
    
    # Define o texto do Label de horário para o horário atual
    horario.config(text=hora_atual)
    
    # Aguarda um segundo e chama a função get_horario novamente. Isso mantém o relógio atualizado em tempo real
    horario.after(1000, get_horario)


# Cria um Canvas para dar margem entre os elementos da interface gráfica
margin = tk.Canvas(root, width=600, height=30, bg='#282a36', bd=0, highlightthickness=0, relief='ridge')
margin.pack()

# Cria um Label para a mensagem de boas-vindas do usuário
mensagemBV = Label(root, bg='#282a36', fg="#bd93f9", font=('Poppins', 16))
mensagemBV.pack()

# Cria um Label para a data atual
data = Label(root, bg='#282a36', fg="#bd93f9", font=('Poppins', 14))
data.pack(pady=2)

# Cria um Label para o horário atual
horario = Label(root, bg='#282a36', fg="#bd93f9", font=('Poppins', 64, 'bold'))
horario.pack(pady=2)

# Chama as funções de atualização para definir a mensagem de boas-vindas, data e horário
get_mensagemBV()
get_data()
get_horario()

# Inicia a interface gráfica do usuário
root.mainloop()  # O método mainloop() é usado para manter a janela do aplicativo em execução para processar eventos de entrada do usuário.