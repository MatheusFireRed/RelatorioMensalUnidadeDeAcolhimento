import pandas as pd

def cont_juridico(df, mes_ref):

    df['RESPONDE ALGUM PROCESSO JUDICIAL?']         = df['RESPONDE ALGUM PROCESSO JUDICIAL?'].fillna('')
    df['ESTÁ EM LIBERDADE CONDICIONAL?']            = df['ESTÁ EM LIBERDADE CONDICIONAL?'].fillna('')
    df['QUANTO TEMPO DE CUMPRIMENTO JUDICIAL?']     = df['QUANTO TEMPO DE CUMPRIMENTO JUDICIAL?'].fillna('')
    
    proc            = len(df[
                     (df["RESPONDE ALGUM PROCESSO JUDICIAL?"] == "SIM")&
                     (df["MÊS DE REF."] == mes_ref)&
                     (df["TIPO DE REGISTRO"].isin(["PERMANÊNCIA", "ENTRADA"]))
                      ])

    proc_andamento  = len(df[
                     (df["ESTÁ EM LIBERDADE CONDICIONAL?"] == "SIM")&
                     (df["MÊS DE REF."] == mes_ref)&
                     (df["TIPO DE REGISTRO"].isin(["PERMANÊNCIA", "ENTRADA"]))
                      ])

    egressos        = len(df[
                    (df["QUANTO TEMPO DE CUMPRIMENTO JUDICIAL?"].notna()) &  # Verifica se não é nulo
                    (df["QUANTO TEMPO DE CUMPRIMENTO JUDICIAL?"] != "") &    # Verifica se não é vazio
                    (df["QUANTO TEMPO DE CUMPRIMENTO JUDICIAL?"] != "NÃO") & # Verifica se não é "NÃO"
                    (df["MÊS DE REF."] == mes_ref) &                          # Verifica o mês de referência
                    (df["TIPO DE REGISTRO"].isin(["PERMANÊNCIA", "ENTRADA"]))  # Verifica os tipos de registro
                     ])

    return{
        "processo":         proc,
        "lib_condicional":  proc_andamento,
        "egressos":         egressos
        }
