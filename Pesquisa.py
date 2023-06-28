
from test_var import test_var
import csv
from datetime import datetime

class Pesquisa:
    def __init__(self):
        self.dados_respostas = []  # Inicializa a lista que irá armazenar as respostas dos participantes

    def coletar_respostas(self):
        while True:
            print('-' * 100)
            print('\033[33mOlá! Está é uma pesquisa sobre equilíbrio entre vida pessoal, trabalho e saúde mental.')

        
            idade = int(input("\033[0;0mInforme sua idade (ou '00' para sair): "))
                
            if idade == 0:  # Verifica se o usuário deseja sair da pesquisa
                break
            # verificacao idade    
            idade_ok = test_var(idade) 

            print('-' * 100)

            genero = input("Informe seu Gênero\n1 - Feminino\n2 - Masculino\n3 - Transgênero\n4 - Outro\n ")
            # verificacao genero
            genero_ok = test_var(genero)
            print('-' * 100)

            genero_opcao = {'1': 'Feminino', '2': 'Masculino', '3': 'Transgênero', '4': 'Outro'}.get(genero_ok)  # Mapeia a escolha do gênero para a opção correspondente
            
            resposta1 = self.obter_resposta("A sua empresa oferece suporte adequado à saúde mental dos funcionários?\n1 - Sim\n2 - Não\n3 - Não sei responder\n ")
            resposta2 = self.obter_resposta("Você já passou por situações de sobrecarga no seu trabalho?\n1 - Sim\n2 - Não\n3 - Não sei responder\n ")
            resposta3 = self.obter_resposta("Na empresa em que você trabalha, existem políticas para promover equilíbrio entre vida pessoal e trabalho?\n1 - Sim\n2 - Não\n3 - Não sei responder\n ")
            resposta4 = self.obter_resposta("Você acha importante que as empresas adotem políticas/programas de bem-estar para cuidar da saúde mental dos seus funcionários?\n1 - Sim\n2 - Não\n3 - Não sei responder\n ")

            print('-' * 100)
            print('\033[36mObrigado por responder nossa pesquisa!')
            print('-' * 100)

            data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Obtém a data e hora atual

            respostas = {
                'idade': idade_ok,
                'genero': genero_ok,
                'lista_respostas': [resposta1, resposta2, resposta3, resposta4],
                'data_hora': data_hora
            }

            self.dados_respostas.append(respostas)  # Adiciona as respostas à lista de dados de respostas

    def obter_resposta(self, mensagem):
        while True:
            try:
                resposta = int(input(mensagem))
                if resposta not in [1, 2, 3]:  # Verifica se a resposta está dentro das opções válidas
                    print("Opção inválida. Por favor, selecione uma opção válida.")
                else:
                    return resposta
            except ValueError:  # Captura o erro caso o usuário não digite um número
                print("Opção inválida. Por favor, selecione uma opção válida.")

    def salvar_csv(self):
        try:
            nome_arquivo = 'pesquisa_saude_trabalho'

            if not nome_arquivo.endswith('.csv'):  # Verifica se o nome do arquivo termina com ".csv"
                nome_arquivo += '.csv'
            # trocar "w" (escrever) para "a" (append)    
            with open(nome_arquivo, 'a', newline='') as arquivo_csv:  # Abre o arquivo CSV para escrita
                campos = ['Idade', 'Gênero', 'Resposta_1', 'Resposta_2', 'Resposta_3', 'Resposta_4', 'data_hora_resposta']
                escritor = csv.DictWriter(arquivo_csv, fieldnames=campos)
                escritor.writeheader()  # Escreve o cabeçalho no arquivo CSV

                for resposta in self.dados_respostas:
                    escritor.writerow({
                        'Idade': resposta['idade'],
                        'Gênero': resposta['genero'],
                        'Resposta_1': resposta['lista_respostas'][0],
                        'Resposta_2': resposta['lista_respostas'][1],
                        'Resposta_3': resposta['lista_respostas'][2],
                        'Resposta_4': resposta['lista_respostas'][3],
                        'data_hora_resposta': resposta['data_hora']
                    })  # Escreve as respostas no arquivo CSV

            print('\033[32mOs dados foram salvos no arquivo .CSV com sucesso!')
        except IOError:  # Captura o erro caso ocorra um problema ao salvar o arquivo
            print('\033[41mErro ao salvar o arquivo. Verifique o nome e a permissão do diretório.')
        except Exception as e:  # Captura erros inesperados
            print(f'\033[41mOcorreu um erro inesperado: {str(e)}')

# Cria uma instância da classe Pesquisa e executa o fluxo do programa
pesquisa = Pesquisa()
pesquisa.coletar_respostas()
pesquisa.salvar_csv()

