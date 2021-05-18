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
        #The keys are tuples of the (row, column) coordinates, and the values will be the number at that coordinate, currently set to None.    
        row = 1
        column = 1
        while (row <= 9):
            self.board[(row, column)] = None
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



        #for row, column in self.board:
            #if (row >= 1 and row <= 3) and (column >= 1 and column <= 3):
                #pass
                




    def populate_board(self, difficulty):
        pass



test_board = Board('hard')
test_board.create_board()
test_board.generate_sublists()

#print(test_board)