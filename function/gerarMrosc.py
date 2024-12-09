import pandas as pd


def gerar_mrosc ():

    textos = {
        'DESCRIÇÃO': [
                        'TOTAL DE ACOLHIDOS RECEPCIONADOS',
                        'TOTAL DE ACOLHIDOS TRANSFERIDOS PARA OUTRA UNIDADE',
                        'TOTAL DE ACOLHIDOS DESLIGADOS',
                        'TOTAL DE ACOLHIDOS REINSERIDOS – FAMILIAR',
                        'TOTAL DE ACOLHIDOS REINSERIDOS - COMUNITÁRIA/AUTONOMIA',
                        'TOTAL DE ACOLHIDOS REINSERIDOS COMUNITÁRIA OU FAMILIAR VIA PVTN',
                        'TOTAL DE ACOLHIDOS REINSERIDOS COMUNITÁRIA OU FAMILIAR VIA De volta ao lar.',
                        'TOTAL GERAL DE ACOLHIDOS REINSERIDOS',
                        'TOTAL GERAL DE ACOLHIDOS HOSPEDADOS NA UNIDADE NO ÚLTIMO DIA DO MÊS',
                        'MÉDIA MODERADA DO NÚMERO DE USUÁRIOS NO MÊS EM EXERCÍCIO',
                        'DESCRIÇÃO',
                        'ATENDIMENTO TÉCNICO',
                        'TOTAL DE ATENDIMENTOS TÉCNICOS INDIVIDUALIZADOS REALIZADOS PELA EQUIPE TÉCNICA DA UNIDADE',
                        'TOTAL DE ESTUDOS DE CASO REALIZADOS PELA EQUIPE TÉCNICA DA UNIDADE',
                        'SAÚDE',
                        'TOTAL DE ATENDIMENTOS NA SAÚDE REALIZADOS',
                        'TOTAL DE USUÁRIOS QUE FIZERAM TESTE COVID-19',
                        'TOTAL DE USUÁRIOS EM ACOMPANHAMENTO COM DOENÇAS INFECTOCONTAGIOSAS NA UNIDADE',
                        'TOTAL DE USUÁRIOS QUE CUMPRIRAM PERÍODO DE QUARENTENA NO QUARTO DO ISOLAMENTO SOCIAL NA UNIDADE',
                        'DOCUMENTAÇÃO',
                        'TOTAL DE ENCAMINHAMENTOS PARA 2A VIA DO DOCUMENTO DE IDENTIDADE',
                        'TOTAL DE ENCAMINHAMENTOS PARA 2A VIA DA CERTIDÃO DE NASCIMENTO',
                        'TOTAL DE ENCAMINHAMENTOS PARA 2A VIA DA CERTIDÃO DE CASAMENTO',
                        'TOTAL DE ENCAMINHAMENTOS PARA 2A VIA DO CPF',
                        'TOTAL DE ENCAMINHAMENTOS PARA 2A VIA DA CTPS (digital)',
                        'TOTAL DE ENCAMINHAMENTOS PARA OBTENÇÃO DO RIOCARD ESPECIAL',
                        'TOTAL DE ENCAMINHAMENTOS PARA OBTENÇÃO DO CERTIFICADO DE RESERVISTA',
                        'CADASTRO ÚNICO',
                        'TOTAL DE ACOLHIDOS INSCRITOS NO CADÚNICO',
                        'TOTAL DE ACOLHIDOS QUE NÃO TEM INSCRIÇÃO NO CADÚNICO',
                        'TOTAL DE ENTREVISTAS PARA CADÚNICO REALIZADAS FEITOS OU ARTICULADOS PELA UNIDADE.',
                        'TRABALHO E RENDA',
                        'TOTAL DE ACOLHIDOS ENCAMINHADOS PARA VAGA SOCIAL',
                        'TOTAL DE ACOLHIDOS QUE POSSUEM TRABALHO FORMAL',
                        'TOTAL DE ACOLHIDOS QUE POSSUEM TRABALHO INFORMAL',
                        'TOTAL DE ACOLHIDOS QUE FORAM BENEFICIADOS COM O AUXÍLIO SAQUE EMERGENCIAL',
                        'TOTAL DE ACOLHIDOS QUE RECEBEM O BPC',
                        'TOTAL DE ACOLHIDOS QUE RECEBEM O BENEFÍCIO DO PROGRAMA BOLSA FAMÍLIA',
                        'TOTAL DE ACOLHIDOS QUE NÃO RECEBEM NENHUM TIPO DE BENEFÍCIO SOCIAL (BPC / BOLSA FAMÍLIA / AUXÍLIO EMERGENCIIAL)',
                        'OUTRAS AÇÕES',
                        'ENCAMINHAMENTO MERCADO DE TRABALHO (PROJETO RESGATE)',
                        'ENCAMINHAMENTO MERCADO DE TRABALHO (REVISTA TRAÇOS)'
                        
                     ]
        
        }

    df_mrosc = pd.DataFrame(textos)

    return df_mrosc
