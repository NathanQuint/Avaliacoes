from paciente import Paciente

#SUBCLASSE

# calcular_valor_final(valor_consulta, taxa_urgencia)
# Adiciona taxa_urgencia ao cálculo caso o atendimento seja de urgência
# Aplica desconto_fidelidade * valor_consulta sobre o valor
# Retorna o valor final calculado

# exibir_informacoes(detalhado)
# Sobrescreve o método da superclasse
# Deve chamar super().exibir_informacoes(detalhado) e acrescentar forma_pagamento e desconto_fidelidade



class pacienteparticular(Paciente):
    def __init__(self, nome:str, data_nascimento:str, cpf:str, telefone:str, tipo_sanguineo:str, numero_prontuario:str, forma_pag:str, desconto_fide: float):
        super().__init__(nome, data_nascimento, cpf,telefone, tipo_sanguineo, numero_prontuario)
        self.forma_pag = forma_pag
        desconto_fide = float(desconto_fide)
        self.desconto_fide = desconto_fide
        

    def calcular_valor_final(self,valor_consulta, taxa_urgencia = False):
        valor_consulta = float(valor_consulta)
        self.valor_consulta = valor_consulta
        
        if taxa_urgencia:
           
           self.valor_consulta = valor_consulta * 1.30

        else:
            pass

        valor_total = round (self.valor_consulta - (self.valor_consulta * self.desconto_fide) ,2)

        print(f'''
                        
            O valor total a ser pago:
            ====================================================  
            R$ 💵 {valor_total} 💵
            ====================================================  

            ''')
        return valor_total
    
    def exibir_informacoes(self, detalhe = True):
        parte1 = super().exibir_informacoes(detalhe)
        if detalhe:
            return parte1 + f'''

            Forma de Pagamento: {self.forma_pag} 💳
            Desconto de Fidelidade: {self.desconto_fide * 100}% 🔖
            ====================================================  
                '''
        else:
            return parte1



paciente3 = pacienteparticular("Eduarda Fonseca", "27/11/2023", "412-543-012-67", "(34) 98159017", "B+","7H255A","Pix", "0.20")
paciente3.exibir_informacoes()