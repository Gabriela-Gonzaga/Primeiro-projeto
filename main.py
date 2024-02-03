import csv 
#meu aquivo csv esta no mesmo diretorio do Main por isso apenas importei o csv.

class Arquivo:
    def __init__(self, grammy):
        self.grammy = grammy
#chamando o arquivo csv para minha classe e atribuindo ele. 
    
    def ler_csv (self):
        with open (self.grammy, 'r', newline='', encoding='utf-8') as arquivo_csv:
        #aqui eu criei a função para ler o csv 
            leitor = csv.reader(arquivo_csv)
            
            # printando/imprimindo os ganhadores funcionara quando eu chamar minha classe la em baixo
            for linha in leitor:
                print(linha[1]) 


nome_do_arquivo = 'grammy.csv' #criando uma variavel com o caminho do csv
arquivo = Arquivo(nome_do_arquivo) #aqui eu estou criando uma variavel "arquivo" para chamar minha classe e dei o parametro como a variavel criada anteriormente

# Imprimindo os ganhadores do Grammy de 2013
print("Os ganhadores do Grammy de 2013 foram:")
arquivo.ler_csv()


           
    





    
    
    
