class Pessoa():
    def __init__(self, nome, CPF, turno, idade, frequencia):
        self.nome = nome
        self.CPF = CPF
        self.turno = turno
        self.idade = idade
        self.frequencia = frequencia
        
    
class Aluno(Pessoa):
    def __init__(self, nome, CPF, turno, idade, frequencia, materia, matricula):
        super().__init__(nome, CPF, turno, idade, frequencia)
        self.materia = materia
        self.matricula = matricula
       
        
           
        
class Professores(Pessoa):
    def __init__(self, nome, CPF, turno, idade, frequencia, lancar_notas, lancar_faltas, salario):
        super().__init__(nome, CPF, turno, idade, frequencia)
        self.lancar_notas = lancar_notas
        self.lancar_faltas = lancar_faltas
        self.salario = salario
        
        
class Secretariado(Pessoa):
    def __init__(self, nome, CPF, turno, idade, frequencia, faz_matricula, salario):
        super().__init__(nome, CPF, turno, idade, frequencia)
        self.faz_matricula = faz_matricula
        self.salario = salario
        
        
class Terceirizados(Pessoa):
    def __init__(self, nome, CPF, turno, idade, frequencia):
        super().__init__(nome, CPF, turno, idade, frequencia)     
        self.salario = salario  
        