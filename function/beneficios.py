import pandas as pd

def cont_beneficio(df, mes_ref):
    benef_bf                = len(df[(df['MÊS DE REF.'] == mes_ref)
                              & (df['TIPO DE REGISTRO'].isin(['PERMANÊNCIA', 'ENTRADA']))
                              & (df['RECEBE ALGUM BENEFÍCIO? QUAL?'] == 'AUXÍLIO BRASIL (ANTIGO PROGRAMA BOLSA FAMÍLIA)')])

    benef_bpc               = len(df[(df['MÊS DE REF.'] == mes_ref)
                              & (df['TIPO DE REGISTRO'].isin(['PERMANÊNCIA', 'ENTRADA']))
                              & (df['RECEBE ALGUM BENEFÍCIO? QUAL?'] == 'BPC')])

    benef_n_recebe          = len(df[(df['MÊS DE REF.'] == mes_ref)
                              & (df['TIPO DE REGISTRO'].isin(['PERMANÊNCIA', 'ENTRADA']))
                              & (df['RECEBE ALGUM BENEFÍCIO? QUAL?'] == 'NÃO RECEBE BENEFÍCIO')])

    benef_outro             = len(df[(df['MÊS DE REF.'] == mes_ref)
                              & (df['TIPO DE REGISTRO'].isin(['PERMANÊNCIA', 'ENTRADA']))
                              & (df['RECEBE ALGUM BENEFÍCIO? QUAL?'] == 'OUTRO BENEFÍCIO')])

    inscr_cad               = benef_bf+benef_bpc+benef_outro

    return{
            "bf":           benef_bf,
            "bpc":          benef_bpc,
            "n_benef":      benef_n_recebe,
            "outro_benef":  benef_outro,
            "inscr_cad":    inscr_cad
        }
