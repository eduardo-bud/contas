nv = True
while nv == True:
    pj = input("quem começa jogando X ou O: ")
    jogo = [ 
             ["0 0","|","0 2","|","0 4"],
             ["1 0","|","1 2","|","1 4"],
             ["2 0","|","2 2","|","2 4"] 
                                         ]
    cont = 0
    r = 0
    for i in range(9):
        for j in range(len(jogo)):
              print(jogo[j][r],jogo[j][r+1],jogo[j][r+2],jogo[j][r+3],jogo[j][r+4])
        if pj == "X":
           cord1, cord2 = map(int,input("em qual casa deseja jogar(informe conforme apresentado): ").split())
           jogo[cord1][cord2] = " X " 
        elif pj == "O":
           cord1, cord2 = map(int,input("em qual casa deseja jogar(informe conforme apresentado): ").split())
           jogo[cord1][cord2] = " O " 
        if pj == "X":
            pj = "O"
        elif pj == "O":
            pj = "X"
        cont += 1
        if jogo[0][0] == jogo[0][2] == jogo[0][4] == " X " or jogo[0][0] == jogo[1][0] == jogo[2][0] == " X "  or jogo[1][0] == jogo[1][2] == jogo[1][4] == " X "  or jogo[2][0] == jogo[2][2] == jogo[2][4] == " X "  or jogo[0][2] == jogo[1][2] == jogo[2][2] == " X "  or jogo[0][4] == jogo[1][4] == jogo[2][4] == " X "  or  jogo[0][0] == jogo[1][2] == jogo[2][4] == " X " or jogo[2][0] == jogo[1][2] == jogo[0][4] == " X ":
            print("vitoria do X")
            break
        elif jogo[0][0] == jogo[0][2] == jogo[0][4] == " O " or jogo[0][0] == jogo[1][0] == jogo[2][0] == " O "  or jogo[1][0] == jogo[1][2] == jogo[1][4] == " O "  or jogo[2][0] == jogo[2][2] == jogo[2][4] == " O "  or jogo[0][2] == jogo[1][2] == jogo[2][2] == " O "  or jogo[0][4] == jogo[1][4] == jogo[2][4] == " O "  or  jogo[0][0] == jogo[1][2] == jogo[2][4] == " O " or jogo[2][0] == jogo[1][2] == jogo[0][4] == " O ":
            print("vitoria do O")
            break
        elif cont >= 9:
            print("empate")
    nv = input("deseja jogar novamente?(S ou N):" )
    if nv == "N":
     nv = False
    elif nv == "S":
        nv == True
print("fim de jogo")
           







