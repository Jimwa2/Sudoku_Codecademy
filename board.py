class Board:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.board = {}
        self.row_list = {}
        self.column_list = {}
        self.three_by_three_list = {}


    def __repr__(self):
        return str(self.board)


    def create_board(self):
        #This function creates an empty board by adding key:value pairs to the self.board dictionary.
        #The keys are tuples of the (row, column, section) coordinates, and the values will be the number at that coordinate, currently set to None.
        #The section is determined by checking the row and column using if statements, to see what three by three section they fit into.    
        row = 1
        column = 1
        section = 1

        while (row <= 9):
            
            if row in range(1, 4):
                if column in range(1, 4):
                    section = 1
                if column in range(4, 7):
                    section = 2
                if column in range(7, 10):
                    section = 3
            if row in range(4, 7):
                if column in range(1, 4):
                    section = 4
                if column in range(4, 7):
                    section = 5
                if column in range(7, 10):
                    section = 6
            if row in range(7, 10):
                if column in range(1, 4):
                    section = 7
                if column in range(4, 7):
                    section = 8
                if column in range(7, 10):
                    section = 9


            self.board[(row, column, section)] = None
            if column == 9:
                column = 1
                row += 1
            else:
                column += 1

                
    def generate_sublists(self):
        #This function adds key:value pairs to the self.row_list dictionary.
        #The keys are the numbers 1 through 9, and each key has a value that is a list of digits from 1 to 9.
        #This row_list dictionary is then copied to the column and three by three dictionaries at the end.
        #These dictionaries will be used by the populate_board() function to adhere to the rules of Sudoku.
        key_pointer = 1
        while key_pointer < 10:
            self.row_list[key_pointer] = []
            for i in range(1, 10):
                self.row_list[key_pointer].append(i)
            key_pointer += 1
        self.column_list = self.row_list
        self.three_by_three_list = self.row_list                


    def populate_board(self, difficulty):
        pass



test_board = Board('hard')
test_board.create_board()
test_board.generate_sublists()

print(test_board)