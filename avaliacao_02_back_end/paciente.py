# registrar_atendimento(tipo, custo)
# Exibe a informação de que o paciente passou por um atendimento do tipo informado, com custo de tanto.

# exibir_informacoes(detalhado)
# Se False → exibe apenas nome, numero_prontuario e tipo_sanguineo
# Se True → exibe todos os 6 atributos

#SUPERCLASSE

class Paciente:
    def __init__ (self, nome:str, data_nascimento:str, cpf:str, telefone:str, tipo_sanguineo:str, numero_prontuario:str ):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self._cpf = cpf
        self._telefone = telefone
        self.tipo_sanguineo = tipo_sanguineo
        self._numero_prontuario = numero_prontuario

    def registrar_atendimento(self, custo: str, tipo_atendimento:str):
        self.historico  = []
        self.tipo_atendimento = tipo_atendimento
        custo = int(custo)
        
        atendimento = {
            "Tipo": tipo_atendimento, 
            "Custo": custo
        }

        self.historico.append(atendimento)
        return print (f'''
                      
            HISTÓRICO DO PACIENTE
            ====================================================  

            {self.historico}

            ====================================================  
        ''')
    

    def exibir_informacoes(self, detalhe = True):
        if detalhe: 
            return f'''






            Paciente: 😷 {self.nome} 😷
            ====================================================             
            Data de Nascimento: {self.data_nascimento} 🗓️
            CPF: {self._cpf}
            Tipo Sanguíneo: {self.tipo_sanguineo} 🩸
            Número de Prontuário: {self._numero_prontuario}

            '''
        else:
            return f'''

            Paciente: 😷 {self.nome} 😷
            ====================================================             
            Número de Prontuário: {self._numero_prontuario}  
            Tipo Sanguíneo: {self.tipo_sanguineo} 🩸
            ====================================================  

            '''
        












