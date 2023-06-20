class Aluno():
    def __init__(self, nome):
        self.nome = nome
        self.notas = []
        self.faltas = []
        
    def adicionar_notas(self, notas):
         self.notas.append(notas)
    
    def calcular_media(self):
        total = sum(self.notas)
        media = total / 3
        return media
    
    def verificar_situacao(self):
        media = self.cacular_media()
        
       
        if(media >= 7):
            print("O aluno está aprovado!")
        elif(media < 7):
            print("O aluno está reprovado!")    
        elif(media > 15 or media < 21):
            print("O aluno está de prova final!")
    def calcular_faltas(self):
        faltas = self.calcular_faltas()
        
        if(faltas >= 20):
            print("O aluno está reprovado!")
            
             
       
       
 