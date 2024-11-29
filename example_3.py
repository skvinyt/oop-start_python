class Cell:
    def __init__(self, number):
        self.number = number
        self.symbol = ' '
        self.is_occupied = False

    def __str__(self):
        return self.symbol

class Board:
    def __init__(self):
        self.cells = [Cell(i) for i in range(1, 10)]

    def display_board(self):
        for i in range(0, 9, 3):
            print(f"{self.cells[i]} | {self.cells[i+1]} | {self.cells[i+2]}")
            if i < 6:
                print("---------")

    def change_cell_state(self, cell_number, symbol):
        cell = self.cells[cell_number - 1]
        if not cell.is_occupied:
            cell.symbol = symbol
            cell.is_occupied = True
            return True
        return False

    def check_game_over(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
            (0, 4, 8), (2, 4, 6)             # Diagonals
        ]
        for combo in winning_combinations:
            if (self.cells[combo[0]].symbol == self.cells[combo[1]].symbol == self.cells[combo[2]].symbol != ' '):
                return True
        return False

    def reset_board(self):
        for cell in self.cells:
            cell.symbol = ' '
            cell.is_occupied = False

class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.wins = 0

    def make_move(self):
        while True:
            try:
                move = int(input(f"{self.name}, введите номер клетки (1-9): "))
                if 1 <= move <= 9:
                    return move
                else:
                    print("Неверный номер клетки. Попробуйте снова.")
            except ValueError:
                print("Неверный ввод. Попробуйте снова.")

class Game:
    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.board = Board()
        self.current_player_index = 0

    def play_turn(self):
        player = self.players[self.current_player_index]
        move = player.make_move()
        if self.board.change_cell_state(move, player.symbol):
            self.board.display_board()
            if self.board.check_game_over():
                player.wins += 1
                print(f"{player.name} победил!")
                return True
            self.current_player_index = 1 - self.current_player_index
        else:
            print("Клетка уже занята. Попробуйте снова.")
        return False

    def play_one_game(self):
        self.board.reset_board()
        self.current_player_index = 0
        for _ in range(9):
            self.board.display_board()
            if self.play_turn():
                return True
        print("Ничья!")
        return False

    def start_games(self):
        while True:
            self.play_one_game()
            print(f"Счёт: {self.players[0].name} - {self.players[0].wins}, {self.players[1].name} - {self.players[1].wins}")
            play_again = input("Хотите сыграть ещё раз? (да/нет): ").strip().lower()
            if play_again != 'да':
                break

# Пример использования
player1 = Player("Игрок 1", "X")
player2 = Player("Игрок 2", "O")
game = Game(player1, player2)
game.start_games()
