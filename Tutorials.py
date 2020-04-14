from time import sleep

matrix = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
board = f'\n1 {matrix[0][0]} | {matrix[0][1]} | {matrix[0][2]} \n ---+---+---\n2 {matrix[1][0]} | {matrix[1][1]} | {matrix[1][2]} \n ---+---+---\n3 {matrix[2][0]} | {matrix[2][1]} | {matrix[2][2]} '


def matrix_win(checklist):

    winner = 0

    for i in range(0, 3):
        if checklist[i][0] == checklist[i][1] == checklist[i][2]:
            if checklist[i][0] == 'X':
                winner = 1
            elif checklist[i][0] == 'O':
                winner = 2

        elif checklist[0][i] == checklist[1][i] == checklist[2][i]:
            if checklist[0][i] == 'X':
                winner = 1
            elif checklist[0][i] == 'O':
                winner = 2

    if checklist[0][0] == checklist[1][1] == checklist[2][2]:
            if checklist[0][0] == 'X':
                winner = 1
            elif checklist[0][0] == 'O':
                winner = 2

    elif checklist[0][2] == checklist[1][1] == checklist[2][0]:
            if checklist[0][2] == 'X':
                winner = 1
            elif checklist[0][2] == 'O':
                winner = 2

    return winner


def cpu_move(current_build):
    best_move = [0, 0]
    best_score = -100
    for a in range(0, 3):
        for b in range(0, 3):
            if current_build[a][b] == ' ':
                current_build[a][b] == 'O'
                if minimize(current_build) >= best_score:
                    best_score = minimize(current_build)
                    best_move = [a, b]
                current_build[a][b] == ' '
    matrix[best_move[0]][best_move[1]] = 'O'
    return


def minimize(matrix):
    score = 0
    for i in range(0, 3):
        for k in range(0, 3):
            if matrix[i][k] == ' ':
                matrix[i][k] == 'X'

                # Horizontal

                for x in range(0, 3):
                    empty = [0]
                    x_score = 0
                    o_score = 0
                    for y in range(0, 3):
                        if matrix[x][y] == 'X':
                            x_score += 1
                        elif matrix[x][y] == 'O':
                            o_score += 1
                        elif matrix[x][y] == ' ':
                            empty = [1]
                    if x_score >= 2 and empty[0] == 1:
                        if x_score == 2:
                            score -= 1
                        else:
                            score -= 2
                    elif o_score >= 2 and empty[0] == 1:
                        if o_score == 2:
                            score += 1
                        else:
                            score += 2

                # Vertical

                for x in range(0, 3):
                    empty = [0]
                    x_score = 0
                    o_score = 0
                    for y in range(0, 3):
                        if matrix[y][x] == 'X':
                            x_score += 1
                        elif matrix[y][x] == 'O':
                            o_score += 1
                        elif matrix[y][x] == ' ':
                            empty = [1]
                    if x_score >= 2 and empty[0] == 1:
                        if x_score == 2:
                            score -= 1
                        else:
                            score -= 2
                    elif o_score >= 2 and empty[0] == 1:
                        if o_score == 2:
                            score += 1
                        else:
                            score += 2

                # Diagonal 1

                if matrix[0][0] == matrix[1][1] and matrix[2][2] == ' ':
                    if matrix[0][0] == 'X':
                        score -= 1
                    elif matrix[0][0] == 'O':
                        score += 1
                elif matrix[2][2] == matrix[1][1] and matrix[0][0] == ' ':
                    if matrix[2][2] == 'X':
                        score -= 1
                    elif matrix[2][2] == 'O':
                        score += 1
                elif matrix[0][0] == matrix[2][2] and matrix[1][1] == ' ':
                    if matrix[0][0] == 'X':
                        score -= 1
                    elif matrix[0][0] == 'O':
                        score += 1

                # Diagonal 1 Wins

                if matrix[0][0] == matrix[1][1] == matrix[2][2]:
                    if matrix[0][0] == 'X':
                        score -= 2
                    elif matrix[0][0] == 'O':
                        score += 2

                # Diagonal 2

                if matrix[0][2] == matrix[1][1] and matrix[2][0] == ' ':
                    if matrix[0][2] == 'X':
                        score -= 1
                    elif matrix[0][2] == 'O':
                        score += 1
                elif matrix[1][1] == matrix[2][0] and matrix[0][2] == ' ':
                    if matrix[2][0] == 'X':
                        score -= 1
                    elif matrix[2][0] == 'O':
                        score += 1
                elif matrix[2][0] == matrix[0][2] and matrix[1][1] == ' ':
                    if matrix[2][0] == 'X':
                        score -= 1
                    elif matrix[2][0] == 'O':
                        score += 1

                # Diagonal 2 Wins

                if matrix[0][2] == matrix[1][1] == matrix[2][0]:
                    if matrix[0][2] == 'X':
                        score -= 2
                    elif matrix[0][2] == 'O':
                        score += 2

                # RESET MOVE

                matrix[i][k] == ' '
    print(score)
    return score

# ORIGINAL CODE


def take_turn(player, num):

    turn_taken = False

    while not turn_taken:
                try:
                    sleep(1)
                    x, y = input(f"{player}, please enter the coordinates of your move: ").split(' ')
                    x = int(x)
                    y = int(y)
                    if num % 2 == 1:
                        matrix[x-1][y-1] = 'O'
                        turn_taken = True
                    elif ' ' in (matrix[x-1][y-1]):
                        matrix[x-1][y-1] = 'X'
                        turn_taken = True
                    else:
                        sleep(1)
                        print("There's already something there!")
                except ValueError:
                    sleep(1)
                    print("Try not to add any additional spaces or characters.")
                # print(board)
    return


print("Welcome to tic-tac toe!")
play_again = 'Y'
Player_1 = input("Player 1 please enter your name: ")
sleep(.5)
print("Awesome!")
Player_2 = input("Player 2 please enter your name: ")
sleep(.5)
print("Thankyou! Now you can play on, but don't forget folks... It's just a game <3")
sleep(0.5)
print("Also, you will be asked to enter coordinates-- enter the row number first then the column")
rounds = 0


while play_again.upper() == 'Y':
    matrix = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    while matrix_win(matrix) == 0 and rounds <= 8:
        board = f'  1   2   3\n1 {matrix[0][0]} | {matrix[0][1]} | {matrix[0][2]} \n ---+---+---\n2 {matrix[1][0]} | {matrix[1][1]} | {matrix[1][2]} \n ---+---+---\n3 {matrix[2][0]} | {matrix[2][1]} | {matrix[2][2]} '
        print(board)

        if rounds % 2 == 0:
            take_turn(Player_1, rounds)
        else:
            if Player_2.upper() != 'CPU':
                take_turn(Player_2, rounds)
            else:
                cpu_move(matrix)

        matrix_win(matrix)
        rounds += 1

        if matrix_win(matrix) == 1:
            sleep(1)
            print(f'\n{Player_1} wins!')
            play_again = input("Would you like to play again? (Y or N) ")
            break
        elif matrix_win(matrix) == 2:
            sleep(1)
            print(f'\n{Player_2} wins!')
            play_again = input("Would you like to play again? (Y or N) ")
            break

    if matrix_win(matrix) == 0:
        print("\nRETARDS! SUCH A SIMPLE GAME AND YET NO ONE WON?? I DEMAND THAT YOU PLAY AGAIN")
        play_again = 'Y'

print("ok, goodbye!")
