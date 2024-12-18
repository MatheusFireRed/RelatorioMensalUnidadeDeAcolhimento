import json
import os
import subprocess
import tkinter as tk
from tkinter import messagebox

def enviar_informacoes():
    mes_ref             = mes_ref_variavel.get()
    ini_acolhidos_valor = ini_acolhidos.get()
    atividades_valor    = atividades.get()

    if not ini_acolhidos_valor.isdigit():
        messagebox.showerror("Error", "O número de acolhidos deve ser um valor numérico.")
        return
    
    with open("dados.json", "w") as f:
        json.dump({"mes_ref": mes_ref, "ini_acolhidos": int(ini_acolhidos_valor), "atividades": int(atividades_valor)}, f)

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


#CRIAR JANELA PRINCIPAL
janela = tk.Tk()
janela.title("Gerar Relatórios Mensais")
janela.geometry("500x500")

#OPÇÕES DO MENU SUSPENSO*************************************************************************
opcoes = ['01_JAN_2024', '02_FEV_2024', '03_MAR_2024', '04_ABR_2024', '05_MAI_2024', 
          '06_JUN_2024', '07_JUL_2024', '08_AGO_2024', '09_SET_2024', '10_OUT_2024',
          '11_NOV_2024', '12_DEZ_2024', '01_JAN_2025', '02_FEV_2025', '03_MAR_2025'] 

mes_ref_variavel = tk.StringVar()
mes_ref_variavel.set(opcoes[0])

#CRIAR MENU SUSPENSO******************************************************************************
label_suspenso = tk.Label(janela, text='Mês de referência para o relatório')
label_suspenso.pack(pady=10)

menu_suspenso = tk.OptionMenu(janela, mes_ref_variavel, *opcoes)
menu_suspenso.pack(pady=10)

#CRIAR INPUT COM NUMERO DE USUÁRIOS NO INÍCIO DO MÊS**********************************************
label_ini_acolhidos = tk.Label(janela, text='Nº acolhidos início do mês:')
label_ini_acolhidos.pack(pady=10)

ini_acolhidos = tk.Entry(janela, width=30)
ini_acolhidos.pack(pady=0)


#CRIAR INPUT PARA NÚMERO DE ATIVIDADES REALIZADAS NA UNIDADE NO MÊS DE REFERÊNCIA******************************
label_atividades = tk.Label(janela, text='Nº atividades no mês')
label_atividades.pack(pady=10)

atividades = tk.Entry(janela, width=30)
atividades.pack(pady=0)


#CRIAR BOTÃO PARA GERAR RELATÓRIOS******************************************************************************
btn_executar = tk.Button(janela, text="Gerar Relatórios", command=executar_acoes, bg="green", font=("Arial", 12))
btn_executar.pack(pady=50)

janela.mainloop()
