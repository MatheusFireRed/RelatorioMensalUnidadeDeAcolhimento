import pandas as pd


def cont_movimentacoes(df, mes_ref, mes, ano):
    

    reinseridos_pvtn        = len(df[(df['MÊS DE REF.'] == mes_ref)
                              &
                              (df['MOTIVO DO DESLIGAMENTO DO ACOLHIMENTO ATUAL'] == 'REINSERÇÃO ATRAVÉS DO PROJETO DE VOLTA À TERRA NATAL')])


    reinseridos_comunitario = len(df[(df['MÊS DE REF.'] == mes_ref)
                              &
                              (df['MOTIVO DO DESLIGAMENTO DO ACOLHIMENTO ATUAL'] == 'DESLIGAMENTO POR REINSERÇÃO COMUNITÁRIA')])

    reinseridos_familiar    = len(df[(df['MÊS DE REF.'] == mes_ref)
                              &
                              (df['MOTIVO DO DESLIGAMENTO DO ACOLHIMENTO ATUAL'] == 'DESLIGAMENTO POR REINSERÇÃO EM FAMÍLIA DE ORIGEM OU FAMÍLIA EXTENSA')])

    reinsercoes_ref_creas   = reinseridos_pvtn+reinseridos_comunitario+reinseridos_familiar

    tranferidos             = len(df[(df['MÊS DE REF.'] == mes_ref)
                              &
                              (df['MOTIVO DO DESLIGAMENTO DO ACOLHIMENTO ATUAL'] == 'DESLIGAMENTO POR TRANSFERÊNCIA PARA OUTRA UNIDADE DE ACOLHIMENTO')])

    desligados_mes          = len(df[(df['MÊS DE REF.'] == mes_ref)
                              &
                              (df['TIPO DE REGISTRO'] == "DESLIGAMENTO")])

    total_acolh_mes         = len(df[(df['MÊS DE REF.'] == mes_ref)])


    obitos                  = len(df[(df['MÊS DE REF.'] == mes_ref)
                              &
                              (df['MOTIVO DO DESLIGAMENTO DO ACOLHIMENTO ATUAL'] == 'ÓBITO')])

    total_accolh_mes_final  = len(df[
                            (df['MÊS DE REF.'] == mes_ref)&
                            (df['TIPO DE REGISTRO'].isin(["PERMANÊNCIA", "ENTRADA"]))
                            ])

    recepcionados           =len(df[
                             (df["DATA DO ACOLHIMENTO ATUAL DD/MM/AAAA"].dt.month == mes)&
                             (df["DATA DO ACOLHIMENTO ATUAL DD/MM/AAAA"].dt.year == ano) &
                             (df["DATA DO ACOLHIMENTO ATUAL DD/MM/AAAA"].notna())&
                             (df['MÊS DE REF.'] == mes_ref)
                             ])
                              

    return{
        "pvtn":             reinseridos_pvtn,
        "comunitario":      reinseridos_comunitario,
        "familiar":         reinseridos_familiar,
        "ref_creas":        reinsercoes_ref_creas,
        "transferidos":     tranferidos,
        "desligados":       desligados_mes,
        "total_acolhidos":  total_acolh_mes,
        "obitos":           obitos,
        "total_acolh_final":total_accolh_mes_final,
        "recepcionados":    recepcionados
        }
