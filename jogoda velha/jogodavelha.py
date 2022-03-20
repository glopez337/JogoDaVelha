import os

tabuleiro = [
  [" "," "," "," "," "],
  [" "," "," "," "," "],
  [" "," "," "," "," "],
  [" "," "," "," "," "],
  [" "," "," "," "," "]
]
jogador = 0
jogadas = 0



def main():
  print("------menu------")
  print("Digite 1 para jogar")
  print("Digite 2 para criar novo jogador")
  print("Digite 3 para exibir histórico de jogador")
  print("Digite 4 para excluir jogador")

  opçao = input("Escolha uma das opções:")
  
  if opçao == "1":
        jogadajogador()

  elif opçao == "2":
      criarnovojogador()
     
  elif opçao == "3":
      Lehistorico()

  elif opçao == "4":
      excluirjogador()    
  

def criarnovojogador():
    nome = input("Digite o nome do novo jogador: ")
    if os.path.isfile(nome + ".txt"):
       print("jogador já registrado")
       main()
    
    else:
       arquivo = open(nome + ".txt", "w")
       arquivo.write("0/n")
       arquivo.close()
       main()
  
def excluirjogador():
  nome = input("Digite o nome do jogador a ser excluído: ")
  if os.path.isfile(nome + ".txt"):
    print("exluindo o jogador:", nome )
    os.remove(nome + ".txt")
    main() 
  else:
    print("esse jogador não existe")
    main()

def Lehistorico():
  nome = input("Digite o nome do jogador: ")
  if os.path.isfile(nome + ".txt"):
     arquivo = open(nome + ".txt")
     historico = arquivo.readlines()
     vitorias = int(historico[0])
     print("Vitórias:{}".format(vitorias)) 
  else:
     print("jogador não existe")


def jogo():
 
  print("    0   1   2   3   4")
  print("0:  " + tabuleiro[0][0] + " | " + tabuleiro[0][1] + " | " + tabuleiro[0][2] + " | " + tabuleiro[0][3] + " | " + tabuleiro[0][4])
  print("   -------------------")
  print("1:  " + tabuleiro[1][0] + " | " + tabuleiro[1][1] + " | " + tabuleiro[1][2] + " | " + tabuleiro[1][3] + " | " + tabuleiro[1][4])
  print("   -------------------")
  print("2:  " + tabuleiro[2][0] + " | " + tabuleiro[2][1] + " | " + tabuleiro[2][2] + " | " + tabuleiro[2][3] + " | " + tabuleiro[2][4])
  print("   -------------------")
  print("3:  " + tabuleiro[3][0] + " | " + tabuleiro[3][1] + " | " + tabuleiro[3][2] + " | " + tabuleiro[3][3] + " | " + tabuleiro[3][4])
  print("   -------------------")
  print("4:  " + tabuleiro[4][0] + " | " + tabuleiro[4][1] + " | " + tabuleiro[4][2] + " | " + tabuleiro[4][3] + " | " + tabuleiro[4][4])    


def jogadajogador():
    global jogador
    global tabuleiro
    global jogadas
    jogador1 = input("Digite o nome do primeiro jogador(O): " )
    jogador2 = input("Digite o nome do primeiro jogador(X): " )
    jogo()

    while True:
      if (os.path.isfile(jogador1 + ".txt") and os.path.isfile(jogador2 + ".txt")):
        if jogador == 0:
          print("vez de",jogador1)
          l = int(input("Digite a linha: "))
          c = int(input("Digite a coluna: "))
          try:
             while tabuleiro[l][c] != " ":
                 print("este lugar já está ocupado")
                 l = int(input("Digite a linha: "))
                 c = int(input("Digite a coluna: "))
             tabuleiro[l][c] = "O"
             jogadas += 2
             if(tabuleiro[0][0] == "O" and tabuleiro[0][1] =="O" and tabuleiro[0][2] =="O" and tabuleiro[0][3] =="O"):
               print(jogador1,"venceu")
               main()  
             elif(tabuleiro[0][1] == "O" and tabuleiro[0][2] =="O" and tabuleiro[0][3] =="O" and tabuleiro[0][4] =="O"):
               print(jogador1,"venceu")
               main()
             elif(tabuleiro[1][0] == "O" and tabuleiro[1][1] =="O" and tabuleiro[1][2] =="O" and tabuleiro[1][3] =="O"):
               print(jogador1,"venceu")
               main()
             elif(tabuleiro[1][1] == "O" and tabuleiro[1][2] =="O" and tabuleiro[1][3] =="O" and tabuleiro[1][4] =="O"):
               print(jogador1,"venceu")
               main()
             elif(tabuleiro[2][0] == "O" and tabuleiro[2][1] =="O" and tabuleiro[2][2] =="O" and tabuleiro[2][3] =="O"):
               print(jogador1,"venceu")
               main()
             elif(tabuleiro[2][1] == "O" and tabuleiro[2][2] =="O" and tabuleiro[2][3] =="O" and tabuleiro[2][4] =="O"):
               print(jogador1,"venceu")
               main()
             elif(tabuleiro[3][0] == "O" and tabuleiro[3][1] =="O" and tabuleiro[3][2] =="O" and tabuleiro[3][3] =="O"):
               print(jogador1,"venceu")
               main()
             elif(tabuleiro[3][1] == "O" and tabuleiro[3][2] =="O" and tabuleiro[1][3] =="O" and tabuleiro[1][4] =="O"):
               print(jogador1,"venceu")
               main()
             elif(tabuleiro[4][0] == "O" and tabuleiro[4][1] =="O" and tabuleiro[4][2] =="O" and tabuleiro[4][3] =="O"):
               print(jogador1,"venceu")
               main()    
             elif(tabuleiro[4][1] == "O" and tabuleiro[4][2] =="O" and tabuleiro[4][3] =="O" and tabuleiro[4][4] =="O"):
               print(jogador1,"venceu")
               main()
#coluna
             elif(tabuleiro[0][0] == "O" and tabuleiro[1][0] =="O" and tabuleiro[2][0] =="O" and tabuleiro[3][0] =="O"):
               print(jogador1,"venceu")
               main()
             elif(tabuleiro[1][0] == "O" and tabuleiro[2][0] =="O" and tabuleiro[3][0] =="O" and tabuleiro[4][0] =="O"):
               print(jogador1,"venceu")
               main()
             elif(tabuleiro[0][1] == "O" and tabuleiro[1][1] =="O" and tabuleiro[2][1] =="O" and tabuleiro[3][1] =="O"):
               print(jogador1,"venceu")
               main()
             elif(tabuleiro[1][1] == "O" and tabuleiro[1][2] =="O" and tabuleiro[1][3] =="O" and tabuleiro[1][4] =="O"):
               print(jogador1,"venceu")
               main()
             elif(tabuleiro[0][2] == "O" and tabuleiro[1][2] =="O" and tabuleiro[2][2] =="O" and tabuleiro[3][2] =="O"):
               print(jogador1,"venceu")
               main()
             elif(tabuleiro[1][2] == "O" and tabuleiro[2][2] =="O" and tabuleiro[2][3] =="O" and tabuleiro[2][4] =="O"):
               print(jogador1,"venceu")
               main()
             elif(tabuleiro[0][3] == "O" and tabuleiro[1][3] =="O" and tabuleiro[2][3] =="O" and tabuleiro[3][3] =="O"):
               print(jogador1,"venceu")
               main()
             elif(tabuleiro[1][3] == "O" and tabuleiro[2][3] =="O" and tabuleiro[3][3] =="O" and tabuleiro[4][3] =="O"):
               print(jogador1,"venceu")
               main()
             elif(tabuleiro[0][4] == "O" and tabuleiro[1][4] =="O" and tabuleiro[2][4] =="O" and tabuleiro[3][4] =="O"):
               print(jogador1,"venceu")
               main() 
             elif(tabuleiro[1][4] == "O" and tabuleiro[2][4] =="O" and tabuleiro[3][4] =="O" and tabuleiro[4][4] =="O"):
               print(jogador1,"venceu")
               main()
  #diagonal
             elif(tabuleiro[0][0] == "O" and tabuleiro[1][1] =="O" and tabuleiro[2][2] =="O" and tabuleiro[3][3] =="O"):
               print(jogador1,"venceu")
               main()
             elif(tabuleiro[1][1] == "O" and tabuleiro[2][2] =="O" and tabuleiro[3][3] =="O" and tabuleiro[4][4] =="O"):
               print(jogador1,"venceu")
               main()
             elif(tabuleiro[0][4] == "O" and tabuleiro[1][3] =="O" and tabuleiro[2][2] =="O" and tabuleiro[3][1] =="O"):
               print(jogador1,"venceu")
               main()
             elif(tabuleiro[1][1] == "O" and tabuleiro[1][2] =="O" and tabuleiro[1][3] =="O" and tabuleiro[1][4] =="O"):
               print(jogador1,"venceu")
               main()
             elif(tabuleiro[1][0] == "O" and tabuleiro[2][1] =="O" and tabuleiro[3][2] =="O" and tabuleiro[4][3] =="O"):
               print(jogador1,"venceu")
               main()
             elif(tabuleiro[0][1] == "O" and tabuleiro[1][2] =="O" and tabuleiro[2][3] =="O" and tabuleiro[3][4] =="O"):
               main()
             elif(tabuleiro[1][4] == "O" and tabuleiro[2][3] =="O" and tabuleiro[3][3] =="O" and tabuleiro[4][1] =="O"):
               print(jogador1,"venceu")
               main()
             elif(tabuleiro[0][3] == "O" and tabuleiro[1][2] =="O" and tabuleiro[2][1] =="O" and tabuleiro[3][0] =="O"):
               print(jogador1,"venceu")
               main()
             elif(jogadas >= 25):
               print("empatou")
               main()
             jogador = 1
             jogo()
          except:
            print("Jogada inválida")


      if jogador == 1:

        print("vez de",jogador2)
        l = int(input("Digite a linha: "))
        c = int(input("Digite a coluna: "))
        try:
            while tabuleiro[l][c] != " ":
                print("este lugar já está ocupado")
                l = int(input("Digite a linha: "))
                c = int(input("Digite a coluna: "))
            tabuleiro[l][c] = "X"
            #linha
            if(tabuleiro[0][0] == "X" and tabuleiro[0][1] =="X" and tabuleiro[0][2] =="X" and tabuleiro[0][3] =="X"):
               print(jogador2,"venceu")
               main()
            elif(tabuleiro[0][1] == "X" and tabuleiro[0][2] =="X" and tabuleiro[0][3] =="X" and tabuleiro[0][4] =="X"):
               print(jogador2,"venceu")
               main()
            elif(tabuleiro[1][0] == "X" and tabuleiro[1][1] =="X" and tabuleiro[1][2] =="X" and tabuleiro[1][3] =="X"):
               print(jogador2,"venceu")
               main()
            elif(tabuleiro[1][1] == "X" and tabuleiro[1][2] =="X" and tabuleiro[1][3] =="X" and tabuleiro[1][4] =="X"):
               print(jogador2,"venceu")
               main() 
            elif(tabuleiro[2][0] == "X" and tabuleiro[2][1] =="X" and tabuleiro[2][2] =="X" and tabuleiro[2][3] =="X"):
               print(jogador2,"venceu")
               main()
            elif(tabuleiro[2][1] == "X" and tabuleiro[2][2] =="X" and tabuleiro[2][3] =="X" and tabuleiro[2][4] =="X"):
               print(jogador2,"venceu")
               main()
            elif(tabuleiro[3][0] == "X" and tabuleiro[3][1] =="X" and tabuleiro[3][2] =="X" and tabuleiro[3][3] =="X"):
               print(jogador2,"venceu")
               main()
            elif(tabuleiro[3][1] == "X" and tabuleiro[3][2] =="X" and tabuleiro[1][3] =="X" and tabuleiro[1][4] =="X"):
               print(jogador2,"venceu")
               main()
            elif(tabuleiro[4][0] == "X" and tabuleiro[4][1] =="X" and tabuleiro[4][2] =="X" and tabuleiro[4][3] =="X"):
               print(jogador2,"venceu")
               main()
                
            elif(tabuleiro[4][1] == "X" and tabuleiro[4][2] =="X" and tabuleiro[4][3] =="X" and tabuleiro[4][4] =="X"):
               print(jogador2,"venceu")
               main()   
#coluna
            elif(tabuleiro[0][0] == "X" and tabuleiro[1][0] =="X" and tabuleiro[2][0] =="X" and tabuleiro[3][0] =="X"):
               print(jogador2,"venceu")
               main()
      
            elif(tabuleiro[1][0] == "X" and tabuleiro[2][0] =="X" and tabuleiro[3][0] =="X" and tabuleiro[4][0] =="X"):
               print(jogador2,"venceu")
               main()
               
            elif(tabuleiro[0][1] == "X" and tabuleiro[1][1] =="X" and tabuleiro[2][1] =="X" and tabuleiro[3][1] =="X"):
               print(jogador2,"venceu")
               main()
                  
            elif(tabuleiro[1][1] == "X" and tabuleiro[1][2] =="X" and tabuleiro[1][3] =="X" and tabuleiro[1][4] =="X"):
               print(jogador2,"venceu")
               main()
                
            elif(tabuleiro[0][2] == "X" and tabuleiro[1][2] =="X" and tabuleiro[2][2] =="X" and tabuleiro[3][2] =="X"):
               print(jogador2,"venceu")
               main()
                
            elif(tabuleiro[1][2] == "X" and tabuleiro[2][2] =="X" and tabuleiro[2][3] =="X" and tabuleiro[2][4] =="X"):
               print(jogador2,"venceu")
               main()
            elif(tabuleiro[0][3] == "X" and tabuleiro[1][3] =="X" and tabuleiro[2][3] =="X" and tabuleiro[3][3] =="X"):
               print(jogador2,"venceu")
               main()
               
            elif(tabuleiro[1][3] == "X" and tabuleiro[2][3] =="X" and tabuleiro[3][3] =="X" and tabuleiro[4][3] =="X"):
               print(jogador2,"venceu")
               main()

            elif(tabuleiro[0][4] == "X" and tabuleiro[1][4] =="X" and tabuleiro[2][4] =="X" and tabuleiro[3][4] =="X"):
               print(jogador2,"venceu")
               main()
                    
            elif(tabuleiro[1][4] == "X" and tabuleiro[2][4] =="X" and tabuleiro[3][4] =="X" and tabuleiro[4][4] =="X"):
               print(jogador2,"venceu")
               main()
  #diagonal
            elif(tabuleiro[0][0] == "X" and tabuleiro[1][1] =="X" and tabuleiro[2][2] =="X" and tabuleiro[3][3] =="X"):
               print(jogador2,"venceu")
               main()
               
            elif(tabuleiro[1][1] == "X" and tabuleiro[2][2] =="X" and tabuleiro[3][3] =="X" and tabuleiro[4][4] =="X"):
               print(jogador2,"venceu")
               main()
               
            elif(tabuleiro[0][4] == "X" and tabuleiro[1][3] =="X" and tabuleiro[2][2] =="X" and tabuleiro[3][1] =="X"):
               print(jogador2,"venceu")
               main()
            elif(tabuleiro[1][3] == "X" and tabuleiro[2][2] =="X" and tabuleiro[3][1] =="X" and tabuleiro[4][0] =="X"):
               print(jogador2,"venceu")
               main()
                
            elif(tabuleiro[1][0] == "X" and tabuleiro[2][1] =="X" and tabuleiro[3][1] =="X" and tabuleiro[4][3] =="X"):
               print(jogador2,"venceu")
               main()
                
            elif(tabuleiro[0][1] == "X" and tabuleiro[1][2] =="X" and tabuleiro[2][3] =="X" and tabuleiro[3][4] =="X"):
               print(jogador2,"venceu")
               main()
                
            elif(tabuleiro[1][4] == "X" and tabuleiro[2][3] =="X" and tabuleiro[3][2] =="X" and tabuleiro[4][1] =="X"):
               print(jogador2,"venceu")
               main()
                
            elif(tabuleiro[0][3] == "X" and tabuleiro[1][2] =="X" and tabuleiro[2][1] =="X" and tabuleiro[3][0] =="X"):
               print(jogador2,"venceu")
               main()
                
            elif(jogadas >= 25):
              print("empatou")
              main()
            jogador = 0
            jogo()

        except:
            print("Jogada inválida") 

      else:
        print("jogador não registrado")
        main()


main()