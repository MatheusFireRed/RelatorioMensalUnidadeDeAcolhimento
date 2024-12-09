import pandas as pd

def preencher_devolutiva(df_devolutiva,
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
                         estrangeiros,
                         cont_refugiados,
                         imigrantes,
                         cont_processo,
                         cont_lib_condicional,
                         cont_egressos
                         ):

    dados = {
    'pvtn': pvtn,
    'comunitario': comunitario,
    'familiar': familiar,
    'ref_creas': ref_creas,
    'transferidos': transferidos,
    'desligados': desligados,
    'total_acolhidos': total_acolhidos,
    'obitos': obitos,
    'total_acolhidos_final': total_acolhidos_final,
    'recepcionados': recepcionados,
    'bf': bf,
    'bpc': bpc,
    'n_benef': n_benef,
    'outro_benef': outro_benef,
    'inscr_cad': inscr_cad,
    'formal': formal,
    'informal': informal,
    'estrangeiros': estrangeiros,
    'cont_refugiados': cont_refugiados,
    'imigrantes': imigrantes,
    'cont_processo': cont_processo,
    'cont_lib_condicional': cont_lib_condicional,
    'cont_egressos': cont_egressos
    }

    df_devolutiva['RESULTADOS'] = ['', 0, 0, 0, '', 0, 0, 0, 0, 0, '', dados['obitos'],
                                   '', 0, 0, 0, 0, 0, '', 0, '', dados['pvtn'], dados['comunitario'],
                                    dados['familiar'], dados['ref_creas'], dados['transferidos'], '',
                                    dados['inscr_cad'], 0, 0, '', 0, 0, '', dados['total_acolhidos'],
                                    dados['recepcionados'], 0, dados['desligados'], dados['estrangeiros'],
                                    dados['imigrantes'], dados['cont_refugiados']]
 
    
  

    return df_devolutiva