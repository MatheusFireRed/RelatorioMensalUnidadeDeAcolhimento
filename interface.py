import json
import os
import subprocess
import tkinter as tk

def enviar_informacoes():
    mes_ref = mes_ref_variavel.get()
    with open("dados.json", "w") as f:
        json.dump({"mes_ref": mes_ref}, f)

    # Executar o outro programa
    subprocess.run(["python", "index.py"])


def executar_programa():

    caminho_arquivo = "index.py"

    try:
        if caminho_arquivo.endswith(".py"):
            subprocess.run(["python", caminho_arquivo], check=True)
        else:
            os.startfile(caminho_arquivo)  # Para executáveis, como .exe
    except Exception as e:
        tk.messagebox.showerror("Erro", f"Não foi possível executar o arquivo.\n{e}")

def executar_acoes():

    enviar_informacoes()
    executar_programa()

janela = tk.Tk()
janela.title("Gerar Relatórios Mensais")
janela.geometry("500x500")

opceos = ['01_JAN_2024', '02_FEV_2024', '03_MAR_2024', '04_ABR_2024', '05_MAI_2024', 
          '06_JUN_2024', '07_JUL_2024', '08_AGO_2024', '09_SET_2024', '10_OUT_2024',
          '11_NOV_2024', '12_DEZ_2024'] 

mes_ref_variavel = tk.StringVar()
mes_ref_variavel.set(opceos[0])

menu_suspenso = tk.OptionMenu(janela, mes_ref_variavel, *opceos)
menu_suspenso.pack(pady=20)

btn_executar = tk.Button(janela, text="Gerar Relatórios", command=executar_acoes, bg="green", font=("Arial", 12))
btn_executar.pack(pady=50)

janela.mainloop()