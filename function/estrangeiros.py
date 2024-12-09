import pandas as pd

def cont_estrangeiros(df, mes_ref):
    
    estrangeiros = len(df[
        (df["NACIONALIDADE"] != "BRASIL") & 
        (df["MÊS DE REF."] == mes_ref) & 
        (df["TIPO DE REGISTRO"].isin(['PERMANÊNCIA', 'ENTRADA']))
    ])

    refugiados = len(df[
        (df["MÊS DE REF."] == mes_ref) &
        (df["CASO POSSUA OUTRA DOCUMENTAÇÃO, INFORME AQUI O Nº:"].notna())
    ])

    imigrantes = estrangeiros - refugiados
    
    return {
       'estrangeiros': estrangeiros,
       'refugiados':   refugiados,
       'imigrantes':   imigrantes
    }
