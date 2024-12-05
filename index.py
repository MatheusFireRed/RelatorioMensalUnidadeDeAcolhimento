import pandas as pd

from function.movimentacoes         import cont_movimentacoes
from function.beneficios            import cont_beneficio
from function.trabalho              import cont_trabalho
from function.estrangeiros          import cont_estrangeiros
from function.juridico              import cont_juridico
from function.gerarTaxaDeOcupacao   import criar_tx_ocupacao

nome_tabela_ppa = "PLANILHA DE MONITORAMENTO - ALTA COMPLEXIDADE - EIXO ADULTO - ALBERGUE MARTIN LUTHER KING JR.xlsx"

df = pd.read_excel(nome_tabela_ppa, skiprows=5)

#CONVERSÃO DAS COLUNAS PARA DATETIME
df['DATA DO ACOLHIMENTO ATUAL DD/MM/AAAA'] = pd.to_datetime(df['DATA DO ACOLHIMENTO ATUAL DD/MM/AAAA'], errors='coerce')
df['DATA DO DESLIGAMENTO DD/MM/AAAA'] = pd.to_datetime(df['DATA DO DESLIGAMENTO DD/MM/AAAA'], errors='coerce')


#VARIAVEIS
mes_ref                 = '11_NOV_2024'
nome_tb_tx_ocupacao     = 'TaxaDeOcupacao.xlsx'
mes = None
ano = None


if(mes_ref == "11_NOV_2024"):

    mes = 11
    ano = 2024
    
if(mes_ref == "12_DEZ_2024"):

    mes = 12
    ano = 2024



#ONTAR MOVIMENTAÇÕES DE USUÁRIOS
movimentacoes   = cont_movimentacoes(df, mes_ref, mes, ano)

#CAD E BENEFICIOS
beneficios      = cont_beneficio(df, mes_ref)


#TRABALHO
trabalho        = cont_trabalho(df, mes_ref)

#ESTRANGEIROS
estrangeiros    = cont_estrangeiros(df, mes_ref)

#JURIDICO
juridico        = cont_juridico(df, mes_ref)


#GERAR TABELA TAXA DE OCUPAÇÃO
df_dias         = criar_tx_ocupacao(mes, ano)
df_dias.to_excel(nome_tb_tx_ocupacao, index=False)

#MOVIMENTAÇÕES USUÁRIOS
print("Reinserções PVTN: ",                             movimentacoes["pvtn"])
print("Reinserções comunitárias: ",                     movimentacoes["comunitario"])
print("Reinserções familiares: ",                       movimentacoes["familiar"])
print("Reinserções referênciadas ao CREAS: ",           movimentacoes["ref_creas"])
print("Acolhidos Transferidos para outras unidades: ",  movimentacoes["transferidos"])
print("Total de acolhidos desligados da unidade: ",     movimentacoes["desligados"])
print("Total de acolhidos que passaram pela unidade: ", movimentacoes["total_acolhidos"])
print("Total de acolhidos que vieram a óbito: ",        movimentacoes["obitos"])
print("Total de acolhidos no ultimo dia na unidade: ",  movimentacoes["total_acolh_final"])
print("Total de acolhidos recepcionados: ",             movimentacoes["recepcionados"])


print("")
print("")

#BENEFICIOS
print("Total de acolhidos que recebem o Bolsa Família: ",   beneficios["bf"])
print("Total de acolhidos que recebem o BPC: ",             beneficios["bpc"])
print("Total de acolhidos que não recebem benefícios: ",    beneficios["n_benef"])
print("Total de acolhidos que recebem outro benéficio: ",   beneficios["outro_benef"])
print("Total de acolhidos inscritos no CAD Único: ",        beneficios["inscr_cad"])


print("")
print("")

#TRABALHO
print("Total de acolhidos que trabalham formalmente: ",     trabalho["formal"])
print("Total de acolhidos que trabalham informalmente: ",   trabalho["informal"])


print("")
print("")

#ESTRANGEIROS
print("Total de estrangeiros acolhidos na unidade: ", estrangeiros["estrangeiros"])
print("Total de refugiados acolhidos na unidade: ",   estrangeiros["refugiados"])
print("Total de imigrantes acolhidos na unidade: ",   estrangeiros["imigrantes"])


print("")
print("")

#JURIDICO
print("Total de acolhidos com processo juducial: ",         juridico["processo"])
print("Total de acolhidos em liberdade condicional: ",      juridico["lib_condicional"])
print("Total de acolhidos egressos do sistema penal: ",     juridico["egressos"])
