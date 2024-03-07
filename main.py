
import tkinter as tk
from bd import *

def exibir():

    # exibir_bd()
    for widget in janela.winfo_children():
        widget.destroy()
    

    cursor.execute("Select * from tarefas")
    linhas = cursor.fetchall()
    linhas_labels = []

    for linha in linhas:
        linha_label = tk.Label(janela, text=f"--------------------------------------\nDescrição: {linha[1]}\nInicio: {linha[2]}\nFim: {linha[3]}\nStatus: {linha[4]}", bg=cor_fundo, fg=cor_texto)
        linha_label.pack(pady=10)
        linhas_labels.append(linha_label)
        janela.widgets_to_destroy = linhas_labels

    
    cursor.close()
    conexao.close()


def cadastrar_tarefa():
    descricao = descricao_entry.get()
    data_inicio = data_inicio_entry.get()
    data_termino = data_termino_entry.get()
    status = status_entry.get().lower()
    
    print("Tarefa cadastrada:")
    print("Descrição:", descricao)
    print("Data Início:", data_inicio)
    print("Data Término:", data_termino)
    print("Status:", status)


    cadastrar_bd(descricao, data_inicio, data_termino, status)


    exibir()


def excluir_tarefa():
    cursor.execute('Delete from tarefas where status = "concluído"')
    conexao.commit()
    exibir()






janela = tk.Tk()
janela.geometry("700x700")
janela.title("Gerenciador de Tarefas")
janela.configure(bg='black')  



cor_fundo = 'black'
cor_texto = 'white'
cor_botao = 'red'



frame_cadastro = tk.Frame(janela, bg=cor_fundo)
frame_cadastro.pack(pady=20)


tk.Label(frame_cadastro, text="Descrição:", bg=cor_fundo, fg=cor_texto).grid(row=0, column=0, padx=10, pady=5)
descricao_entry = tk.Entry(frame_cadastro, bg=cor_fundo, fg=cor_texto, insertbackground='white')
descricao_entry.grid(row=0, column=1, padx=10, pady=5)


tk.Label(frame_cadastro, text="Data Início:", bg=cor_fundo, fg=cor_texto).grid(row=1, column=0, padx=10, pady=5)
data_inicio_entry = tk.Entry(frame_cadastro, bg=cor_fundo, fg=cor_texto,insertbackground='white')
data_inicio_entry.grid(row=1, column=1, padx=10, pady=5)



tk.Label(frame_cadastro, text="Data Término:", bg=cor_fundo, fg=cor_texto).grid(row=2, column=0, padx=10, pady=5)
data_termino_entry = tk.Entry(frame_cadastro, bg=cor_fundo, fg=cor_texto,insertbackground='white')
data_termino_entry.grid(row=2, column=1, padx=10, pady=5)



tk.Label(frame_cadastro, text="Status:", bg=cor_fundo, fg=cor_texto).grid(row=3, column=0, padx=10, pady=5)
status_entry = tk.Entry(frame_cadastro, bg=cor_fundo, fg=cor_texto, insertbackground='white')
status_entry.grid(row=3, column=1, padx=10, pady=5)



botao_cadastrar = tk.Button(janela, text="Cadastrar Tarefa", bg=cor_botao, fg=cor_texto, command=cadastrar_tarefa)
botao_cadastrar.pack(pady=10)


botao_exibir = tk.Button(janela, text="Exibir tarefas" , bg=cor_botao, fg=cor_texto, command=exibir)
botao_exibir.pack(pady=10)


botao_excluir = tk.Button(janela, text='Excluir tarefas concluídas' , bg=cor_botao, fg=cor_texto, command=excluir_tarefa)
botao_excluir.pack(pady=10)

janela.mainloop()

