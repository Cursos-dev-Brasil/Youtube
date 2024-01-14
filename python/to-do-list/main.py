import tkinter as tk 
from tkinter import messagebox

def add_tarefa():
    tarefa = entrada_tarefa.get()
    if tarefa:
        lista_tarefas.insert(tk.END, tarefa)
        entrada_tarefa.delete(0, tk.END)
    else:
        messagebox.showwarning("Digite uma tarefa!")

def rem_tarefa():
    try:
        selecao = lista_tarefas.curselection()
        lista_tarefas.delete(selecao)
    except:
        messagebox.showwarning("Selecione uma tarefa!")

janela = tk.Tk()
janela.title("Lista de tarefas")

entrada_tarefa = tk.Entry(janela, width=30)
entrada_tarefa.pack(pady=10)

btn_add = tk.Button(janela, text="Adicionar tarefa", command=add_tarefa)
btn_add.pack(pady=5)

lista_tarefas = tk.Listbox(janela, selectmode=tk.SINGLE, width=40, height=10)
lista_tarefas.pack(pady=10)

btn_rem = tk.Button(janela, text="Remover tarefa", command=rem_tarefa)
btn_rem.pack(pady=5)

janela.mainloop()