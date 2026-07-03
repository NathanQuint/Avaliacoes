Sistema de Gestão de Pacientes

Sistema desenvolvido em Python para gerenciar diferentes tipos de pacientes em uma clínica médica, utilizando os conceitos de Orientação a Objetos como herança, encapsulamento e polimorfismo.

``Caminho do Projeto ``
1. main.py = Local para testar o sistema
2. paciente.py = Arquivo contendo a SUPERCLASS Paciente
3. pacienteconvenio.py = Arquivo contendo a SUBCLASS pacienteconvenio
4. pacienteparticular.py = Arquivo contendo a SUBCLASS pacienteparticular"


``Explicação das Classes ``
# SUPERCLASS Paciente #

Classe base do sistema

    # Atributos #

1. nome | tipo = string | Nome completo do paciente
2. data_nascimento | tipo = string | Data de nascimento do paciente
3. cpf | tipo = string | Cpf do paciente (Dado Privado)
4. telefone | tipo = string | telefone do paciente (Dado Privado)
5. tipo_sanguineo | tipo = string | Tipo sanguíneo do paciente
6. numero_prontuario | tipo = string | Número de prontuário do paciente (Dado Privado)

    # Métodos #

1. registrar_atendimento(tipo, custo) — Exibe o tipo e custo do atendimento realizado
2. exibir_informacoes(detalhado) — Se True, exibe todos os atributos. Se False, exibe apenas nome, prontuário e tipo sanguíneo

# SUBCLASS pacienteconvenio #

SUBCLASS herda todos os atributos da SUPERCLASS Paciente

    # Atributos #

1. forma_pagamentos | tipo = string | Formas de pagamento possíveis de um paciente
2. desconto_fidelidade | tipo = float | Desconto fidelidade de acordo com a quantidade de vezes que um paciente ja foi ao mesmo hospital ou clínica

    # Métodos #

1. calcular_valor_final(valor_consulta, taxa_urgencia) — Aplica taxa de urgência (30%) se necessário e desconto de fidelidade, retornando o valor final
2. exibir_informacoes(detalhado) — Sobrescreve o método da superclasse, acrescentando forma de pagamento e desconto de fidelidade


# SUBCLASS pacienteparticular #

SUBCLASS herda todos os atributos da SUPERCLASS Paciente

    # Atributos #

1. nome_convenio | tipo = string | Nome do convenio do paciente
2. _numero_carteirinha | tipo = string | Número da carteirinha do convênio do paciente (Dado Privado)

    # Método #

1. registrar_autorizacao(procedimento, valor_glosa) — Exibe o procedimento autorizado e o valor da glosa (0 caso não haja glosa)
2. exibir_informacoes(detalhado) — Sobrescreve o método da superclasse, acrescentando nome do convênio e número da carteirinha

``Conceitos utilizados``


1. Herança — pacienteparticular e pacienteconvenio herdam de Paciente
2. Encapsulamento — Atributos sensíveis prefixados com _
3. Polimorfismo — exibir_informacoes sobrescrito nas SUBCLASS
4. super() — Utilizado para reaproveitar o __init__ e métodos da SUPERCLASS


``Exemplos de Execução``

Paciente comum (Paciente)
[
pythonpaciente1 = Paciente("Ana Carolina", "01/02/2009", "154-088-774-42", "(21) 98234622", "O+", "2A2FE5")
print(paciente1.exibir_informacoes())
print(paciente1.exibir_informacoes(False))
paciente1.registro_tipo("100", "Quimioterapia")
]


Saída Esperada:


Paciente: 😷 Ana Carolina 😷
====================================================
Data de Nascimento: 01/02/2009 🗓️
CPF: 154-088-774-42
Tipo Sanguíneo: O+ 🩸
Número de Prontuário: 2A2FE5

Paciente: 😷 Ana Carolina 😷
====================================================
Número de Prontuário: 2A2FE5
Tipo Sanguíneo: O+ 🩸
====================================================

HISTÓRICO DO PACIENTE
====================================================
[{'Tipo': 'Quimioterapia', 'Custo': 100}]
====================================================




Paciente convênio (PacienteConvenio)
[
pythonpaciente2 = pacienteconvenio("Carlos Miguel", "12/09/1990", "876-014-991-85", "(52) 98529081", "A-", "2BCCE3", "Amil", "290522578")
print(paciente2.exibir_informacoes())
print(paciente2.exibir_informacoes(False))
paciente2.registrar_autorizacao("1500", "Ortodontia")
paciente2.registrar_autorizacao("0", "Fisioterapia")
]


Saída Esperada:


Paciente: 😷 Carlos Miguel 😷
====================================================
Data de Nascimento: 12/09/1990 🗓️
CPF: 876-014-991-85
Tipo Sanguíneo: A- 🩸
Número de Prontuário: 2BCCE3

Convênio do Paciente: Amil 📋
Número da Carteirinha do Convênio: 290522578 🪪
====================================================

Paciente: 😷 Carlos Miguel 😷
====================================================
Número de Prontuário: 2BCCE3
Tipo Sanguíneo: A- 🩸
====================================================

Procedimento + Glosa
====================================================
Procedimento: Ortodontia ⚕️
Valor da glosa: R$1500.0 💵
====================================================

Procedimento + Glosa
====================================================
Procedimento: Fisioterapia ⚕️
Valor da glosa: R$0 💵
====================================================




Paciente particular (PacienteParticular)
[
pythonpaciente3 = pacienteparticular("Eduarda Fonseca", "27/11/2023", "412-543-012-67", "(34) 98159017", "B+", "7H255A", "Pix", "0.20")
print(paciente3.exibir_informacoes())
print(paciente3.exibir_informacoes(False))
paciente3.calcular_valor_final("1000", True)
paciente3.calcular_valor_final("1000")
]


Saída Esperada:


Paciente: 😷 Eduarda Fonseca 😷
====================================================
Data de Nascimento: 27/11/2023 🗓️
CPF: 412-543-012-67
Tipo Sanguíneo: B+ 🩸
Número de Prontuário: 7H255A

Forma de Pagamento: Pix 💳
Desconto de Fidelidade: 20.0% 🔖
====================================================

Paciente: 😷 Eduarda Fonseca 😷
====================================================
Número de Prontuário: 7H255A
Tipo Sanguíneo: B+ 🩸
====================================================

O valor total a ser pago:
====================================================
R$ 💵 1040.0 💵
====================================================

O valor total a ser pago:
====================================================
R$ 💵 800.0 💵
====================================================


