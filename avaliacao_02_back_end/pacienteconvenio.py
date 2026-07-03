from paciente import Paciente

#SUBCLASSE

# registrar_autorizacao(procedimento, valor_glosa)
# Exibe o procedimento autorizado pelo convênio
# Exibe o valor da glosa (caso não haja glosa, passar 0)


# exibir_informacoes(detalhado)
# Sobrescreve o método da superclasse
# Deve chamar super().exibir_informacoes(detalhado) e acrescentar nome_convenio e numero_carteirinha


class pacienteconvenio(Paciente):
    def __init__(self, nome:str, data_nascimento:str, cpf:str, telefone:str, tipo_sanguineo:str, numero_prontuario:str, nome_convenio:str, numero_carteirinha:str):
        super().__init__(nome, data_nascimento, cpf, telefone, tipo_sanguineo, numero_prontuario,)
        self.nome_convenio = nome_convenio
        self._numero_carteirinha = numero_carteirinha
    
    def registrar_autorização(self,valor_glosa: str, procedimento:str): # Oi WIill! Passando pra avisar que sei que poderia so ter usado o "self.tipo_atendimento" no lugar desse atributo "procedimento", mas como la no site da prova diz que vc quer esses 2 atributos acabou ficando redundante. 
        valor_glosa = float(valor_glosa)
        self.valor_glosa = valor_glosa
        self.tipo_atendimento = procedimento

        if valor_glosa > 0:
            print(f'''
            Procedimento + Glosa
            ====================================================                  
            Procedimento: {self.tipo_atendimento} ⚕️
            Valor da glosa: R${valor_glosa} 💵
            ====================================================

            ''')
        else:
            print(f'''
            Procedimento + Glosa
            ====================================================                  
            Procedimento: {self.tipo_atendimento} ⚕️
            Valor da glosa: R$0 💵
            ====================================================       

                  ''')

    def exibir_informacoes(self, detalhe = True):
        parte1 = super().exibir_informacoes(detalhe)

        if detalhe:
            return parte1 + f'''
     
            Convênio do Paciente: {self.nome_convenio} 📋
            Número da Carteirinha do Convênio: {self._numero_carteirinha} 🪪
            ====================================================  
            







                '''
        else:
            return parte1       







