import pandas as pd

def cont_trabalho(df, mes_ref):

    trab_formal             = len(df[(df['MÊS DE REF.'] == mes_ref)
                              & (df['TIPO DE REGISTRO'].isin(['PERMANÊNCIA', 'ENTRADA']))
                              & (df['TIPO DE VÍNCULO DE TRABALHO'] == 'FORMAL')])

    trab_informal           = len(df[(df['MÊS DE REF.'] == mes_ref)
                              & (df['TIPO DE REGISTRO'].isin(['PERMANÊNCIA', 'ENTRADA']))
                              & (df['TIPO DE VÍNCULO DE TRABALHO'] == 'INFORMAL')])

    return{
        "formal":   trab_formal,
        "informal": trab_informal
        }
