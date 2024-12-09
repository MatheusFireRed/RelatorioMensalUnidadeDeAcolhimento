import pandas as pd

def gerar_devolutiva():

    textos = {
        'CONSOLIDADA EIXO ADULTO': ['SAÚDE',
                                    'Nº DE ATENDIMENTOS NA SAÚDE - ATENÇÃO BÁSICA',
                                    'Nº DE ATENDIMENTOS NA SAÚDE MENTAL – CAPS E CAPSAD',
                                    'Nº DE ATENDIMENTOS EM UNIDADE DE EMERGÊNCIA',
                                    'SAÚDE/COVID19',
                                    'Nº DE USUÁRIOS COM SUSPEITA DE COVID NO MÊS',
                                    'Nº DE USUÁRIOS TESTADOS POSITIVO PARA COVID-19 NO MÊS',
                                    'Nº DE USUÁRIOS INTERNADOS EM DECORRÊNCIA DA COVID-19 NO MÊS',
                                    'Nº DE USUÁRIOS QUE VIERAM A ÓBITO EM DECORRÊNCIA DA COVID -19 NO MÊS',
                                    'Nº DE USUÁRIOS VACINADOS NO MÊS',
                                    'ÓBITOS',
                                    'Nº DE USUÁRIOS QUE VIERAM A ÓBITO  NO MÊS',
                                    'DOCUMENTAÇÃO',
                                    'Nº DE USUÁRIOS QUE OBTIVERAM A EXPEDIÇÃO DA CÉDULA DE IDENTIDADE',
                                    'Nº DE USUÁRIOS QUE OBTIVERAM A EXPEDIÇÃO DA CERTIDÃO DE NASCIMENTO',
                                    'Nº DE USUÁRIOS QUE OBTIVERAM A CARTEIRA DE TRABALHO',
                                    'Nº DE USUÁRIOS QUE OBTIVERAM  CPF (1ª e 2ª via)',
                                    'Nº DE USUÁRIOS QUE OBTIVERAM A EXPEDIÇÃO DO CERTIFICADO DE RESERVISTA',
                                    'ENCAMINHAMENTO PARA A REDE SOCIOASSISTENCIAL',
                                    'TOTAL DE ENCAMINHAMENTOS PARA A REDE SOCIOASSISTENCIAL (TODOS OS ENCAMINHAMENTOS REALIZADOS)',
                                    'REINSERÇÃO/TRANSF PARA OUTRA UNIDADE DE ACOLHIMENTO',
                                    'Nº DE REINSERÇÕES PELO PROGRAMA “DE VOLTA À TERRA NATAL”',
                                    'Nº DE REINSERÇÕES POR AUTONOMIA/ COMUNITÁRIA',
                                    'Nº DE REINSERÇÕES NA FAMÍLIA',
                                    'Nº DE USUÁRIOS REINSERIDOS QUE FORAM REFERENCIADOS AOS CREAS',
                                    'Nº DE USUÁRIOS TRANSFERIDOS PARA OUTRA UNIDADE DE ACOLHIMENTO',
                                    'CADASTRO ÚNICO',
                                    'Nº DE USUÁRIOS INSERIDOS NO CADÚNICO – CADASTRO NOVO E TRANSFERÊNCIA DE MUNICIPIO',
                                    'Nº DE USUÁRIOS REALIZADOS ATUALIZAÇÃO NO CAD ÚNICO',
                                    'Nº DE USUÁRIOS QUE NÃO POSSUEM INSCRIÇÃO NO CADÚNICO POR FALTA DE DOCUMENTOS',
                                    'ACESSO A BENEFÍCIOS',
                                    'Nº DE USUÁRIOS ENCAMINHADOS PARA SMH',
                                    'OUTROS PROJETOS HABITACIONAIS',
                                    'USUÁRIOS EM ACOLHIMENTO',
                                    'TOTAL DE USUÁRIOS ACOLHIDOS NO MÊS',
                                    'TOTAL DE USUÁRIOS QUE ENTRARAM NO MÊS DE REFERÊNCIA (ENCAMINHADOS PELA CRAF TOM JOBIM)',
                                    'TOTAL DE USUÁRIOS QUE ENTRARAM NO MÊS DE REFERÊNCIA (ENCAMINHADOS  PELA ABORDAGEM)',
                                    'TOTAL DE USUÁRIOS DESLIGADOS NO MÊS',
                                    'TOTAL DE USUÁRIOS ACOLHIDOS NO MÊS COM NACIONALIDADE ESTRANGEIRA',
                                    'TOTAL DE USUÁRIOS IMIGRANTES NO MÊS',
                                    'TOTAL DE USUÁRIOS REFUGIADOS NO MÊS']

                }

    df_devolutiva = pd.DataFrame(textos)

    return df_devolutiva
