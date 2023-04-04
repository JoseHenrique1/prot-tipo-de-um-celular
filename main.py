
import webbrowser # IMPORTAÇÃO PARA APP NAVEGADOR
import random # GERA NUMEROS ALEATORIOS

# --->  LETRAS CONTROLADORAS, REGISTRO DE ATIVIDADES (APP ESPECIAL)

#letras controladoras:
p = 1
o = 2
e = 3
i = 4
u = 5
y = 6

#registro de atividades:

def regt(z):   
  
  try:
       
    arquivo = open('Controle.txt','x')
    arquivo.close()
    regt(z)# chamamos a funcao denovo, pois quando executamos o celular pela primeira vez o primeiro app não é lido 
    
  except:
    if z == 1:
      
      arquivo = open('Controle.txt','a')#abrimos o arquivo e adicionamos um print, depois fechamos
      print('Você abriu a calculadora\n',file=arquivo)
      arquivo.close()
    
    elif z == 2:
      
      arquivo = open('Controle.txt','a')
      print('Você abriu os contatos\n',file=arquivo)
      arquivo.close()
    
    elif z == 3:
      
      arquivo = open('Controle.txt','a')
      print('Você olhou a hora\n',file=arquivo)
      arquivo.close()
    
    elif z == 4:
      
      arquivo = open('Controle.txt','a')
      print('Você abriu o navegador\n',file=arquivo)
      arquivo.close()
    
    elif z == 5:
      
      arquivo = open('Controle.txt','a')
      print('Você abriu o registro de atividades\n',file=arquivo)
      arquivo.close()
      
      arq = open('Controle.txt','r')
      while True:

        conteudo = arq.readline()# ler o conteudo
    
        print(conteudo)
        if conteudo == '':
          arq.close()
          break
    elif z == 6:
      
      import os #exclui arquivos
      arquivo = "Controle.txt"
      os.remove(arquivo)
       
    else:
      print(' Tecla errada! ')
   
#-----------------------------------------------------
# APPS : CALCULADORA, HORA, CONTATOS, NAVEGADOR

def calculadora(a,b,i):
  #controle de atividade

  if i == 'A':#realiza as quatro operacoes
   return a+b
  elif i == 'B':
    return a-b
  elif i == 'C':
    return a/b
  elif i == 'D':
    return a*b

def hora():
  regt(e)#controle de atividade
  a = random.randint(0,24)
  b = random.randint(0,59)#gera numero aleatorio
  print('Horario de Brasíla ',a,':',b)
  print()
#---------da linha pra baixo eu----------------------
def Navegador():
  regt(i)#controle de atividade
  while True:
    print(10*'>-<','\nEscolha seu site de pesquisa:\n''\ngoogle\n''\nyoutube\n''\nPara sair aperte qualquer tecla\n')
    z = input('')
    
    if z == 'google':
      pesquisa = input('Pesquise:  ')  
      x = ('https://www.google.com.br/search?q='+pesquisa)
      
      webbrowser.open(x) #jutamos o link do site com a pesquisa e executamos com o webbrowser.open()
    
    elif z == 'youtube':
      pesquisa = input('pesquise  ')  
      x = ('https://www.youtube.com/search?q='+pesquisa)

      webbrowser.open(x)
    
    else:
      print('Saindo do navegador\n',10*'>-<')
      break

def contato():
  regt(o)# controle de atividade
  contatos = {}
  while True:

    print('\nEscolha uma opção: \n''1 - Criar contato\n''2 - Excluir contato\n''3 - Lista contato\n''4 - Sair\n')
    x = int(input(''))
    if x == 1:
      nome = input('Digite o nome do contato: ')
      numero = int(input('Digite o numero do contato: '))
      contatos[nome] = numero
    
    elif x == 2:
      excluir = input('Digite o nome do contato que deseja excluir: ')
      if excluir in contatos:
        contatos.pop(excluir)
        print('Contato excluido\n')
      else:
        print('Não foi possivel excluir o contato\n''Verifique se o nome esta certo\n''e tente novamente.\n')
    
    elif x == 3:
      print(contatos)
    
    elif x == 4:
      break
    else:
      print('Tecla errada!')

#-----------------------------------------------------
#]-------------->     CELULAR      <----------------[

#Aqui é onde junta todos os apps à interface do celular

def menu():
  while True:
    print()
    print(' ======>Celular Pirata3.0<======\n',  '| Calculadora       -   1     |\n','| Contato           -   2     |\n','| Hora              -   3     |\n','| Navegadores       -   4     |\n','| R. de atividade   -   5     |\n','| Desligar          -   6     |\n',31*'=')

    escolha = int(input())
    l = True
    
    if escolha == 1:
      regt(p)
      
      while l:
         print(10*'¨¨','\nCALCULADORA\n''\n' '--> Adição          A\n''--> Subtração       B\n''--> Divisão         C\n''--> Multiplicação   D\n''--> Sair do app     E\n')
         i = input('operacao desejada  ')
  
         if i == 'E':
           l = False
         else:
           a = float(input('Digite o primeiro numero:  '))
           b = float(input('Digite o segundo numero:  '))
           x = calculadora(a,b,i)
           print(f'Resultado:{x:.2f} ')
    
    elif escolha == 2:
      contato()
    
    elif escolha == 3:
      hora()
    
    elif escolha == 4:
      Navegador()
    elif escolha == 5:
      regt(u)
    elif escolha == 6:
      regt(6) # apaga o arquivo que estava armazenando o registro
      print(20*'=', '\n|Desligando celular|')
      print(20*'=')
      
      break
        
menu()