class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.notas = []
        self.faltas = []
        
    def add_nota(self, notas):
         if len(notas) > 3:
             print("3 notas já lançadas")
         self.notas.append(notas)
         
         
    def media_calc(self):
        total = sum(self.notas)
        media = total / 3
        return media
         
         
    def verificar_situacao(self):
        media = self.media_calc()
        
        
        if(media > 7):
            print("Aprovado")
        elif(media > 5 and media <7):
            #nfinal = float(input("Digite a nota final!"))
            print("Recuperação")
        else:
            print("Reprovado")
            
    def calc_faltas(self, faltas):
        f = self.faltas >= 20:
        print("Reprovado")
        
            
        
             
