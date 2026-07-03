from paciente import Paciente
from pacienteconvenio import pacienteconvenio
from pacienteparticular import pacienteparticular



paciente1 = Paciente("Ana Carolina", "01/02/2009", "154-088-774-42", "(21) 98234622", "O+", "2A2FE5")
print(paciente1.exibir_informacoes())
print(paciente1.exibir_informacoes(False))
paciente1.registrar_atendimento("100", "Quimioterapia")


paciente2 = pacienteconvenio("Carlos Miguel", "12/09/1990", "876-014-991-85", "(52) 98529081", "A-", "2BCCE3", "Amil","290522578")
print(paciente2.exibir_informacoes())
print(paciente2.exibir_informacoes(False))
paciente2.registrar_autorização("1500", "Ortodontia")
paciente2.registrar_autorização("0", "Fisioterapia")


paciente3 = pacienteparticular("Eduarda Fonseca", "27/11/2023", "412-543-012-67", "(34) 98159017", "B+","7H255A","Pix", "0.20")
print(paciente3.exibir_informacoes())
print(paciente3.exibir_informacoes(False))
paciente3.calcular_valor_final("1000", True)
paciente3.calcular_valor_final("1000")














