import random
import turtle
import numpy as np

grid_x = 20
grid_y = 20


def backtrack(move_list, board_p, number_p):
    for i in range(2, len(move_list)):
        x = move_list[-i][0]
        y = move_list[-i][1]
        available_0 = False

        try:
            if board_p[y + 1][x] == 0:
                available_0 = True
                new_x = x
                new_y = y + 1
        except IndexError: # this index error is for going above 20 need to include for below 0 eg -1
            available_0 = False

        if not available_0:
            if y-1 != -1:
                if board_p[y - 1][x] == 0:
                    available_0 = True
                    new_x = x
                    new_y = y-1
            else:
                available_0 = False

        if not available_0:
            try:
                if board_p[y][x + 1] == 0:
                    available_0 = True
                    new_x = x + 1
                    new_y = y
            except IndexError:
                available_0 = False

        if not available_0:
            if x-1 != -1:
                if board_p[y][x - 1] == 0:
                    available_0 = True
                    new_x = x - 1
                    new_y = y
            else:
                available_0 = False

        if available_0:
            # set all moves after chosen one back to 0 in board - tick
            # return new board - tick
            # pop all useless moves - tick
            # return new move list - tick
            # have to send back new cell number based on how many deleted
            index = move_list.index((x, y))
            counter = 0
            for g in range(len(move_list) - 1, index, -1):
                board_p[move_list[g][1]][move_list[g][0]] = 0
                del move_list[g]
                counter += 1
            number_p -= counter-1
            return new_x, new_y, board_p, move_list


def make_hamiltonian_cycle(x, y):
    start_block_x, start_block_y = random.randint(0, x - 1), random.randint(0, y - 1)

    board = [[0 for a in range(x)] for b in range(y)]

    number = 1

    board[start_block_y][start_block_x] = number

    last_block_x = start_block_x
    last_block_y = start_block_y

    finished = False
    moves = [(start_block_x, start_block_y)]
    options = ["up", "down", "left", "right"]
    while not finished:
        try:
            direction = random.choice(options)

            if direction == "up":
                new_block_x = last_block_x
                new_block_y = last_block_y + 1
            elif direction == "down":
                new_block_x = last_block_x
                new_block_y = last_block_y - 1
                if new_block_y == -1:
                    options.remove(direction)
                    continue
            elif direction == "left":
                new_block_x = last_block_x - 1
                new_block_y = last_block_y
                if new_block_x == -1:
                    options.remove(direction)
                    continue
            elif direction == "right":
                new_block_x = last_block_x + 1
                new_block_y = last_block_y

        except IndexError:
            # print_board(board)
            new_block_x, new_block_y, board, moves = backtrack(moves, board, number)
            options = ["up", "down", "left", "right"]
            continue

        try:
            if board[new_block_y][new_block_x] == 0:
                number += 1
                board[new_block_y][new_block_x] = number
                print_board(board)
                last_block_x = new_block_x
                last_block_y = new_block_y
                options = ["up", "down", "left", "right"]
                moves.append((new_block_x, new_block_y))
            else:
                options.remove(direction)
        except IndexError:
            options.remove(direction)



def print_board(board_t):
    col_width = max(len(str(word)) for row in board_t for word in row) + 2  # padding
    for row in board_t:
        print("".join(str(word).ljust(col_width) for word in row))
    print("\n")


make_hamiltonian_cycle(grid_x, grid_y)
print("done")

##########################

# block size 30px
# gap size 10 px

screen_width = (grid_x * 40) + 10
screen_height = (grid_y * 40) + 10

screen = turtle.Screen()
screen.setup(screen_width, screen_height)

screen.addshape("block", ((-15, -15), (15, -15), (15, 15), (-15, 15)))
t1 = turtle.Turtle()
t1.shape("block")

snake_length = 1

turtle.mainloop()
