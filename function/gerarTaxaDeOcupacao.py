import pandas as pd


def criar_tx_ocupacao(mes, ano):

    dias_do_mes = pd.date_range(start=f'{ano}-{mes:02d}-01', end=f'{ano}-{mes:02d}-{pd.Period(f"{ano}-{mes:02d}").days_in_month}', freq='D')

    # Criar o DataFrame com os dias do mês no formato DD/MM/AAAA
    df_dias = pd.DataFrame(dias_do_mes, columns=['Data'])

    df_dias['TOTAL DE ACOLHIDOS NO DIA ANTERIOR']               = None
    df_dias['TOTAL DE ACOLHIDOS RECEPCIONADOS NO DIA']          = None
    df_dias['TOTAL DE ACOLHIDOS TRANSFERIDOS NO DIA']           = None
    df_dias['TOTAL DE ACOLHIDOS REINSERIDOS NO DIA']            = None
    df_dias['N. TOTAL DE ACOLHIDOS EVADIDOS/DESLIGADOS NO DIA'] = None
    df_dias['FINAL']                                            = None
    
    # Convertendo para o formato DD/MM/AAAA
    df_dias['Data'] = df_dias['Data'].dt.strftime('%d/%m/%Y')

    #df_dias.iloc[0, 1] = 'TOTAL DE ACOLHIDOS NO DIA ANTERIOR'
    #df_dias.iloc[0, 2] = 'TOTAL DE ACOLHIDOS RECEPCIONADOS NO DIA'  
    #df_dias.iloc[0, 3] = 'TOTAL DE ACOLHIDOS TRANSFERIDOS NO DIA'
    #df_dias.iloc[0, 4] = 'TOTAL DE ACOLHIDOS REINSERIDOS NO DIA'
    #df_dias.iloc[0, 5] = 'N. TOTAL DE ACOLHIDOS EVADIDOS/DESLIGADOS NO DIA'
    #df_dias.iloc[0, 6] = 'FINAL'
    
    return df_dias 
