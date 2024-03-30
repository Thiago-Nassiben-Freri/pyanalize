import tkinter as tk
from tkinter import messagebox
from functions import calcular_estatisticas

def exibir_resultados():
    numeros = entrada_numeros.get()
    media, moda, mediana = calcular_estatisticas(numeros)
    
    if media is None:
        messagebox.showerror("Erro", "Por favor, insira números válidos.")
        return
    
    resultado_label.config(text=f"Média: {media:.1f}\nModa: {moda:.1f}\nMediana: {mediana:.1f}")

def fechar_janela():
    root.destroy()


root = tk.Tk()
root.title("Calculadora de Estatísticas")

root.iconbitmap('C:/Users/tnass/OneDrive/Área de Trabalho/VS Code/python/projetos_5/projeto_pyanalyze/images/pyanalize_UdL_icon.ico')

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

instrucao_label = tk.Label(frame, text="Digite os números separados por vírgula:")
instrucao_label.grid(row=0, column=0, padx=5, pady=5)

entrada_numeros = tk.Entry(frame)
entrada_numeros.grid(row=0, column=1, padx=5, pady=5)

calcular_btn = tk.Button(frame, text="Calcular", command=exibir_resultados)
calcular_btn.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

resultado_label = tk.Label(frame, text="")
resultado_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

voltar_btn = tk.Button(frame, text="Voltar", command=fechar_janela)
voltar_btn.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()

