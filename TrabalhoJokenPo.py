from random import randint

modalidade = int(input("Boa noite! Seja bem vindo ao Joken Pô do coringão. Essas são as modalidades de jogo:"
      "\n1 - Homem x Máquina"
      "\n2 - Homem x Homem"
      "\n3 - Máquina x Máquina"
      "\nPor favor informe a modalidade de jogo que deseja: "))



if modalidade == 1:
      rodadas = 1
      rodadasBot = 0
      rodadasPlayer = 0
      empate = 0
      while rodadas < 2:
            jogadaPLayer1 = int(input("\nPara jogar digite:"
            "\n1 - Pedra"
            "\n2 - Papel"
            "\n3 - Tesoura: "))
            jogadaBot = randint(1,3)

            #player1 joga pedra
            if jogadaPLayer1 == 1:

                  if jogadaBot == 1:
                        print("\nPlayer: pedra x Computador: pedra. O resultado da rodada foi empate!")
                        empate = empate + 1

                  elif jogadaBot == 2:
                        print("\nPlayer: pedra x Computador: papel. O Computador venceu a rodada!")
                        rodadasBot = rodadasBot + 1

                  elif jogadaBot == 3:
                        print("\nPlayer: pedra x Computador: tesoura. Parabéns você venceu a rodada!")
                        rodadasPlayer = rodadasPlayer + 1

            #player1 joga papel
            if jogadaPLayer1 == 2:

                  if jogadaBot == 1:
                        print("\nPlayer: papel x Computador: pedra. Parabéns você venceu a rodada!")
                        rodadasPlayer = rodadasPlayer + 1

                  elif jogadaBot == 2:
                        print("\nPlayer: papel x Computador: papel. O resultado da rodada foi empate!")
                        empate = empate + 1

                  elif jogadaBot == 3:
                        print("\nPlayer: papel x Computador: tesoura. O computador venceu a rodada!")
                        rodadasBot = rodadasBot + 1

            #player1 joga tesoura
            if jogadaPLayer1 == 3:

                  if jogadaBot == 1:
                        print("\nPlayer: tesoura x Computador: pedra. O computador venceu a rodada!")
                        rodadasBot = rodadasBot + 1

                  elif jogadaBot == 2:
                        print("\nPlayer: tesoura x Computador: papel. Parabéns você venceu a rodada!")
                        rodadasPlayer = rodadasPlayer + 1

                  elif jogadaBot == 3:
                        print("\nPlayer: tesoura x Computador: tesoura. O resultado da rodada foi empate!")
                        empate = empate + 1

            if jogadaPLayer1 > 0 and jogadaPLayer1 < 4:
                  jogarNovamente = int(input("\n Deseja jogar novamente? "
                                             "\n 1 - Sim"
                                             "\n 2 - Não: "))

                  if jogarNovamente == 2:
                        rodadas = rodadas + 1
                        totalRodadas = empate + rodadasBot + rodadasPlayer


                        print("\nEstatísticas da partida:"
                              "\n Rodadas: ", totalRodadas,
                              "\n Empates: ", empate,
                              "\n Percentual de vitórias do Player: ", (rodadasPlayer / totalRodadas) * 100, "%",
                              "\n Percentual de vitórias do Computador: ", (rodadasBot / totalRodadas) * 100,"%",)

                  elif jogarNovamente < 1 or jogarNovamente > 2:
                        print("\nValor Inválido.")
                        rodadas = rodadas + 1
            else:
                  print("\nValor Inválido.")



elif modalidade == 2:
      rodadas = 1
      rodadasPlayer = 0
      rodadasPlayer2 = 0
      empate = 0
      while (rodadas < 2):
            jogadaPLayer1 = int(input("\nPlayer 1, por favor digite para jogar:"
                                      "\n1 - Pedra"
                                      "\n2 - Papel"
                                      "\n3 - Tesoura: "))

            jogadaPLayer2 = int(input("\nPlayer 2, por favor digite para jogar:"
                                      "\n1 - Pedra"
                                      "\n2 - Papel"
                                      "\n3 - Tesoura: "))

            # player1 joga pedra
            if jogadaPLayer1 == 1:

                  if jogadaPLayer2 == 1:
                        print("\nPlayer 1: pedra x Player 2: pedra. O resultado da rodada foi empate!")
                        empate = empate + 1

                  elif jogadaPLayer2 == 2:
                        print("\nPlayer 1: pedra x Player 2: papel. Player 2 venceu a rodada!")
                        rodadasPlayer2 = rodadasPlayer2 + 1

                  elif jogadaPLayer2 == 3:
                        print("\nPlayer 1: pedra x Player 2: tesoura. Player 1  venceu a rodada!")
                        rodadasPlayer = rodadasPlayer + 1

            # player1 joga papel
            if jogadaPLayer1 == 2:

                  if jogadaPLayer2 == 1:
                        print("\nPlayer 1: papel x Player 2: pedra. Player 1 venceu a rodada!")
                        rodadasPlayer = rodadasPlayer + 1

                  elif jogadaPLayer2 == 2:
                        print("\nPlayer 1: papel x Player 2: papel. O resultado da rodada foi empate!")
                        empate = empate + 1

                  elif jogadaPLayer2 == 3:
                        print("\nPlayer 1: papel x Player 2: tesoura. Player 2 venceu a rodada!")
                        rodadasPlayer2 = rodadasPlayer2 + 1

            # player1 joga tesoura
            if jogadaPLayer1 == 3:

                  if jogadaPLayer2 == 1:
                        print("\nPlayer 1: tesoura x Player 2: pedra. Player 2 venceu a rodada!")
                        rodadasPlayer2 = rodadasPlayer2 + 1

                  elif jogadaPLayer2 == 2:
                        print("\nPlayer 1: tesoura x Player 2: papel. Player 1 venceu a rodada!")
                        rodadasPlayer = rodadasPlayer + 1

                  elif jogadaPLayer2 == 3:
                        print("\nPlayer 1: tesoura x Player 2: tesoura. O resultado da rodada foi empate!")
                        empate = empate + 1



            if (jogadaPLayer1 > 0 and jogadaPLayer1 < 4) and (jogadaPLayer2 > 0 and jogadaPLayer2 < 4):
                  jogarNovamente = int(input("\n Desejam jogar novamente? "
                                             "\n 1 - Sim"
                                             "\n 2 - Não: "))

                  if jogarNovamente == 2:
                        rodadas = rodadas + 1
                        totalRodadas = empate + rodadasPlayer2 + rodadasPlayer

                        print("\nEstatísticas da partida:"
                              "\n Rodadas: ", totalRodadas,
                              "\n Empates: ", empate,
                              "\n Percentual de vitórias do Player 1: ", (rodadasPlayer / totalRodadas) * 100, "%",
                              "\n Percentual de vitórias do Player 2: ", (rodadasPlayer2 / totalRodadas) * 100, "%", )

                  elif jogarNovamente < 1 or jogarNovamente > 2:
                        print("\nValor Inválido.")
                        rodadas = rodadas + 1
            else:
                  print("\nValor Inválido.")



elif(modalidade == 3):


      rodadas = 1
      rodadasBot = 0
      rodadasBot2 = 0
      empate = 0
      while rodadas < 2:
            jogadaBot = randint(1, 3)
            jogadaBot2 = randint(1, 3)
            #bot2 joga pedra
            if jogadaBot2 == 1:
                  if jogadaBot == 1:
                        print("\nComputador 1: pedra x Computador 2: pedra. O resultado da rodada foi empate!")
                        empate = empate + 1

                  elif jogadaBot == 2:
                        print("\nComputador 1: papel x Computador 2: pedra. O computador 1 venceu a rodada!")
                        rodadasBot = rodadasBot + 1

                  elif jogadaBot == 3:
                        print("\nComputador 1: tesoura x Computador 2: pedra. O computador 2 venceu a rodada!")
                        rodadasBot2 = rodadasBot2 + 1

            #bot2 joga papel
            if jogadaBot2 == 2:
                  if jogadaBot == 1:
                        print("\nComputador 1: pedra x Computador 2: papel. O computador 2 venceu a rodada!")
                        rodadasBot2 = rodadasBot2 + 1

                  elif jogadaBot == 2:
                        print("\nComputador 1: papel x Computador 2: papel. O resultado da rodada foi empate!")
                        empate = empate + 1

                  elif jogadaBot == 3:
                        print("\nComputador 1: tesoura x Computador 2: papel. O computador 1 venceu a rodada!")
                        rodadasBot = rodadasBot + 1

            #bot2 joga tesoura
            if jogadaBot2 == 3:
                  if jogadaBot == 1:
                        print("\nComputador 1: pedra x Computador 2: tesoura. O computador 1 venceu a rodada!")
                        rodadasBot = rodadasBot + 1

                  elif jogadaBot == 2:
                        print("\nComputador 1: papel x Computador 2: tesoura. O computador 2 venceu a rodada!")
                        rodadasBot2 = rodadasBot2 + 1

                  elif jogadaBot == 3:
                        print("\nComputador 1: tesoura x Computador 2: tesoura. O resultado da rodada foi empate!")
                        empate = empate + 1

            jogarNovamente = int(input("\n Deseja jogar novamente? "
                                       "\n 1 - Sim"
                                       "\n 2 - Não: "))

            if jogarNovamente == 2:
                  rodadas = rodadas + 1
                  totalRodadas = empate + rodadasBot + rodadasBot2

                  print("\nEstatísticas da partida:"
                        "\n Rodadas: ", totalRodadas,
                        "\n Empates: ", empate,
                        "\n Percentual de vitórias do Computador 1: ", (rodadasBot / totalRodadas) * 100, "%",
                        "\n Percentual de vitórias do Computador 2: ", (rodadasBot2 / totalRodadas) * 100, "%", )

            elif jogarNovamente < 1 or jogarNovamente > 2:
                  print("\nValor Inválido.")
                  rodadas = rodadas + 1
else:
      print("\nModalidade inválida.")
