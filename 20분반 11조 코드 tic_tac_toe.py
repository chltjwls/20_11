def print_board(board): # 출력 함수
    print()
    print(board[0][0], '|',  board[0][1], '|', board[0][2])
    print('---------')
    print(board[1][0], '|', board[1][1], '|', board[1][2])
    print('---------')
    print(board[2][0], '|', board[2][1], '|', board[2][2])

def empty(board, rows, cols): # 공백 함수
    if board[rows][cols] != ' ':
        print('이미 선택된 자리입니다. ') 
    else:
        return board[rows][cols] == ' '

def board_full(board): # 포화 함수
     if board[0][0] != ' ' and \
    board[0][1] != ' ' and \
    board[0][2] != ' ' and \
    board[1][0] != ' ' and \
    board[1][1] != ' ' and \
    board[1][2] != ' ' and \
    board[2][0] != ' ' and \
    board[2][1] != ' ' and \
    board[2][2] != ' ':
        return True
     else:
        return False

def win(board, mark): # 우승 함수
    if (board[0][0] == mark and board[0][1] == mark and board[0][2] == mark) or\
    (board[1][0] == mark and board[1][1] == mark and board[1][2] == mark) or\
    (board[2][0] == mark and board[2][1] == mark and board[2][2] == mark) or\
    (board[0][0] == mark and board[1][0] == mark and board[2][0] == mark) or\
    (board[0][1] == mark and board[1][1] == mark and board[2][1] == mark) or\
    (board[0][2] == mark and board[1][2] == mark and board[2][2] == mark) or\
    (board[0][0] == mark and board[1][1] == mark and board[2][2] == mark) or\
    (board[2][0] == mark and board[1][1] == mark and board[0][2] == mark):
        return True
    else:
        return False

print('\n <틱택토 게임> \n')
print('* O 또는 X를 먼저 연속으로 세 개 놓으면 이기는 게임입니다. \n  (가로, 세로, 대각선 모두 가능)')

board = [['1', '2', '3'], 
        ['4', '5', '6'], 
        ['7', '8', '9']]

print_board(board)

turn = 0

while True:
    restart=str(input("\n게임을 플레이 하시겠습니까?(y/n) : "))
    if restart == 'y':
        
        board = [[' ', ' ', ' '], 
                [' ', ' ', ' '], 
                [' ', ' ', ' ']]
        while True:
            if turn == 0:
                number = int(input('\nX를 놓을 자리를 선택하세요 (1 ~ 9): '))
                if number >= 1 and number <= 3:
                    cols = number - 1
                    rows = 0
                elif number >= 4 and number <= 6:
                    cols = number - 4
                    rows = 1
                elif number >= 7 and number <= 9:
                    cols = number - 7
                    rows = 2

                if empty(board, rows, cols):
                    board[rows][cols] = 'X'

                    print_board(board)

                    if win(board, 'X'):
                        print('\nX가 이겼습니다.')
                        break
                    elif board_full(board):
                        print('\n무승부')
                        break
                    turn += 1
                    turn %= 2

            elif turn == 1:     
                number = int(input('\nO를 놓을 자리를 선택하세요. (1 ~ 9): '))
                if number >= 1 and number <= 3:
                    cols = number - 1
                    rows = 0
                elif number >= 4 and number <= 6:
                    cols = number - 4
                    rows = 1
                elif number >= 7 and number <= 9:
                    cols = number - 7
                    rows = 2

                if empty(board, rows, cols):
                    board[rows][cols] = 'O'

                    print_board(board)

                    if win(board, 'O'):
                        print('\nO가 이겼습니다.')
                        break
                    elif board_full(board):
                        print('\n무승부')
                        break
                    turn += 1
                    turn %= 2
    else:
        print('게임을 종료합니다.')
        break
                 
   
