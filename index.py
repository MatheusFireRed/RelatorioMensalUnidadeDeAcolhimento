import pandas as pd

from function.movimentacoes         import cont_movimentacoes
from function.beneficios            import cont_beneficio
from function.trabalho              import cont_trabalho
from function.estrangeiros          import cont_estrangeiros
from function.juridico              import cont_juridico
from function.gerarTaxaDeOcupacao   import criar_tx_ocupacao
from function.preencherTxOcupacao   import preencher_tx_ocupacao
from function.gerarDevolutiva       import gerar_devolutiva
from function.gerarMrosc            import gerar_mrosc
from function.preencherDevolutiva   import preencher_devolutiva


nome_tabela_ppa = "PLANILHA DE MONITORAMENTO - ALTA COMPLEXIDADE - EIXO ADULTO - ALBERGUE MARTIN LUTHER KING JR.xlsx"

df = pd.read_excel(nome_tabela_ppa, skiprows=5)

#CONVERSÃO DAS COLUNAS PARA DATETIME
df['DATA DO ACOLHIMENTO ATUAL DD/MM/AAAA']  = pd.to_datetime(df['DATA DO ACOLHIMENTO ATUAL DD/MM/AAAA'], errors='coerce')
df['DATA DO DESLIGAMENTO DD/MM/AAAA']       = pd.to_datetime(df['DATA DO DESLIGAMENTO DD/MM/AAAA'], errors='coerce')


#VARIAVEIS
mes_ref                 = '11_NOV_2024'
nome_tb_tx_ocupacao     = 'TaxaDeOcupacao.xlsx'
nome_tb_devolutiva      = 'Devolutiva.xlsx'
nome_tb_mrosc           = "MROSC.xlsx"
mes                     = int(mes_ref[:2])
ano                     = int(mes_ref[-4:])
ini_acolhidos           = 135


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
df_dias = criar_tx_ocupacao(mes, ano)
df_dias = preencher_tx_ocupacao(df, mes_ref, df_dias, ini_acolhidos)
df_dias.to_excel(nome_tb_tx_ocupacao, index=False)

#VARIAVEIS PARA MROSC E DEVOLUTIVA

pvtn                    = movimentacoes["pvtn"]
comunitario             = movimentacoes["comunitario"]
familiar                = movimentacoes["familiar"]
ref_creas               = movimentacoes["ref_creas"]
transferidos            = movimentacoes["transferidos"]
desligados              = movimentacoes["desligados"]
total_acolhidos         = movimentacoes["total_acolhidos"]
obitos                  = movimentacoes["obitos"]
total_acolhidos_final   = movimentacoes["total_acolh_final"]
recepcionados           = movimentacoes["recepcionados"]


bf                      = beneficios["bf"]
bpc                     = beneficios["bpc"]
n_benef                 = beneficios["n_benef"]
outro_benef             = beneficios["outro_benef"]
inscr_cad               = beneficios["inscr_cad"]


formal                  = trabalho["formal"]
informal                = trabalho["informal"]


estrangeiros_cont       =  estrangeiros['estrangeiros']
refugiados              =  estrangeiros['refugiados']
imigrantes              =  estrangeiros['imigrantes']

cont_processo           = juridico["processo"]
cont_lib_condicional    = juridico["lib_condicional"]
cont_egressos           = juridico["egressos"]

#GERAR DEVOLUTIVA
df_devolutiva = gerar_devolutiva()

df_devolutiva = preencher_devolutiva(   df_devolutiva,
                                        pvtn,
                                        comunitario,
                                        familiar,
                                        ref_creas,
                                        transferidos,
                                        desligados,
                                        total_acolhidos,
                                        obitos,
                                        total_acolhidos_final,
                                        recepcionados,
                                        bf,
                                        bpc,
                                        n_benef,
                                        outro_benef,
                                        inscr_cad,
                                        formal,
                                        informal,
                                        estrangeiros_cont,
                                        refugiados,
                                        imigrantes,
                                        cont_processo,
                                        cont_lib_condicional,
                                        cont_egressos
                                     )

print(df_devolutiva)

df_devolutiva.to_excel(nome_tb_devolutiva, index=False)

#GERAR MROSC
df_mrosc = gerar_mrosc()

df_mrosc.to_excel(nome_tb_mrosc, index=False)


