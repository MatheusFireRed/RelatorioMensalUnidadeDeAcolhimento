import pandas as pd


def preencher_tx_ocupacao(df, mes_ref, df_dias, ini_acolhidos):
    linhas = len(df_dias)

    coluna  = 1
    qtd_dia = 0

    df_dias.iloc[0, coluna] = ini_acolhidos
    coluna = 0
    
    for i in range(linhas):
        
        data_tx = df_dias.iloc[i, coluna]

        df['DATA DO ACOLHIMENTO ATUAL DD/MM/AAAA'] = pd.to_datetime(df['DATA DO ACOLHIMENTO ATUAL DD/MM/AAAA'], format='%d/%m/%Y')

        data_tx = pd.to_datetime(data_tx, format='%d/%m/%Y')


    #CONTA QUANTOS ACOLHIDOS FORAM RECEPCIONADOS POR DIA DO MES
        qtd_dias = len(df[(df['MÊS DE REF.'] == mes_ref)&
                    (df['DATA DO ACOLHIMENTO ATUAL DD/MM/AAAA'] == data_tx)
                    ])
        coluna = 2

        df_dias.iloc[i, coluna] = qtd_dias


    #CONTA QUANTOS ACOLHIDOS FORAM TRANSFERIDOS POR DIA NO MÊS

        qtd_dias = len(df[(df['MÊS DE REF.'] == mes_ref)&
                    (df['DATA DO DESLIGAMENTO DD/MM/AAAA'] == data_tx) &
                    (df['MOTIVO DO DESLIGAMENTO DO ACOLHIMENTO ATUAL'] == 'DESLIGAMENTO POR TRANSFERÊNCIA PARA OUTRA UNIDADE DE ACOLHIMENTO')
                    ])
        coluna = 3
    
        df_dias.iloc[i, coluna] = qtd_dias

    
    #CONTA QUNTOS ACOLHIDOS FORAM REINSERIDOS POR DIA NO MÊS

        qtd_dias = len(df[(df['MÊS DE REF.'] == mes_ref)&
                    (df['DATA DO DESLIGAMENTO DD/MM/AAAA'] == data_tx) &
                    (df['MOTIVO DO DESLIGAMENTO DO ACOLHIMENTO ATUAL'].isin(['DESLIGAMENTO POR REINSERÇÃO COMUNITÁRIA',
                                                                         'REINSERÇÃO ATRAVÉS DO PROJETO DE VOLTA À TERRA NATAL']))
                    ])
        coluna = 4

        df_dias.iloc[i, coluna] = qtd_dias


    #CONTA QUANDOS ACOLHIDOS FORAM DESLIGADOS POR DIA NO MÊS

        qtd_dias = len(df[(df['MÊS DE REF.'] == mes_ref)&
                    (df['DATA DO DESLIGAMENTO DD/MM/AAAA'] == data_tx) &
                    (df['MOTIVO DO DESLIGAMENTO DO ACOLHIMENTO ATUAL'].isin(['DESLIGAMENTO POR OUTRO MOTIVO',
                                                                             'DESLIGAMENTO POR DECISÃO DA DIREÇÃO E /OU EQUIPE TÉCNICA POR  POR NÃO ACEITAÇÃO DAS REGRAS DA INSTITUIÇÃO',
                                                                             'DESLIGAMENTO VOLUNTÁRIO  POR CONFLITO COM OUTRO ACOLHIDO',
                                                                             'DESLIGAMENTO POR DECISÃO DA DIREÇÃO E /OU EQUIPE TÉCNICA POR CONFLITO COM OUTRO ACOLHIDO',
                                                                             'DESLIGAMENTO VOLUNTÁRIO SEM MOTIVO IDENTIFICADO',
                                                                             'DESLIGAMENTO POR DECISÃO DA DIREÇÃO E /OU EQUIPE TÉCNICA POR CONFLITO COM PROFISSIONAL DA UNIDADE DE ACOLHIMENTO'
                                                                             ]))
                    ])

        coluna = 5

        df_dias.iloc[i, coluna] = qtd_dias

        df_dias = df_dias.fillna(0)
            
        valor_inicial   = df_dias.iloc[i, 1]
        recepcionados   = df_dias.iloc[i, 2]
        transferidos    = df_dias.iloc[i, 3]
        reinseridos     = df_dias.iloc[i, 4]
        desligados      = df_dias.iloc[i, 5]

        resultado       = valor_inicial + recepcionados - transferidos - reinseridos - desligados

        df_dias.iloc[i, 6]       = resultado

        if i + 1 < len(df_dias):
            
            df_dias.iloc[(i+1), 1]   = resultado
        
        coluna = 0

    return df_dias
