import random

class Board:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.board = {}
        self.row_list = {}
        self.column_list = {}
        self.three_by_three_list = {}
        self.poss_choices_row = {}
        self.poss_choices_column = {}
        self.poss_choices_three_by_three = {}
        self.failed_coordinates = {}


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
        #This function generates the lists used to adhere to the rules of Sudoku.

        #Generates row, column, and three_by_three lists of coordinates.
        for num in range(1, 10):
            self.row_list[num] = []
            self.column_list[num] = []
            self.three_by_three_list[num] = []
        for coordinate in self.board:
            self.row_list[coordinate[0]].append(coordinate)
            self.column_list[coordinate[1]].append(coordinate)
            self.three_by_three_list[coordinate[2]].append(coordinate)

        #Generates poss_choices lists of possible choices from 1 to 9.
        key_pointer = 1
        while key_pointer < 10:
            self.poss_choices_row[key_pointer] = []
            self.poss_choices_column[key_pointer] = []
            self.poss_choices_three_by_three[key_pointer] = []
            for i in range(1, 10):
                self.poss_choices_row[key_pointer].append(i)
                self.poss_choices_column[key_pointer].append(i)
                self.poss_choices_three_by_three[key_pointer].append(i)
            key_pointer += 1


    def add_choice_to_coordinate(self, coordinate, choice_to_be_added):
        self.board[coordinate] = choice_to_be_added
        self.poss_choices_row[coordinate[0]].remove(choice_to_be_added)
        self.poss_choices_column[coordinate[1]].remove(choice_to_be_added)
        self.poss_choices_three_by_three[coordinate[2]].remove(choice_to_be_added)
        print(coordinate, "set to:", choice_to_be_added)


    def remove_choice_from_coordinate(self, coordinate):
        choice_to_be_removed = self.board[coordinate]
        self.board[coordinate] = None
        self.poss_choices_row[coordinate[0]].append(choice_to_be_removed)
        self.poss_choices_column[coordinate[1]].append(choice_to_be_removed)
        self.poss_choices_three_by_three[coordinate[2]].append(choice_to_be_removed)
        print(coordinate, "set to: None")


    def swap_coordinate_values(self, coordinate, other_coord):
        coordinate_value = self.board[coordinate]
        other_coord_value = self.board[other_coord]

        self.remove_choice_from_coordinate(coordinate)
        self.add_choice_to_coordinate(coordinate, other_coord_value)

        self.remove_choice_from_coordinate(other_coord)
        self.add_choice_to_coordinate(other_coord, coordinate_value)


    def look_for_possible_swap(self, coordinate):
        choice_to_be_added = 0
        poss_choices_row = self.poss_choices_row[coordinate[0]]
        poss_choices_column = self.poss_choices_column[coordinate[1]]
        poss_choices_three_by_three = self.poss_choices_three_by_three[coordinate[2]]
        
        print("Looking for coordinate to swap with...")

        #Search through other coordinates within the current row for a possible swap.
        for other_coord in self.row_list[coordinate[0]]:
            #For each choice within the current coordinate's poss_choices_row...
            for choice in poss_choices_row:
                #if the choice is in the other_coord's poss_choices_column and poss_choices_three_by_three...
                if choice in self.poss_choices_column[other_coord[1]] and choice in self.poss_choices_three_by_three[other_coord[2]]:
                    #and the other_coord's value is a valid choice for the current coordinate...
                    if self.board[other_coord] in poss_choices_column and self.board[other_coord] in poss_choices_three_by_three:
                        choice_to_be_added = self.board[other_coord]
                        self.remove_choice_from_coordinate(other_coord)
                        self.add_choice_to_coordinate(other_coord, choice)
                        break
        if choice_to_be_added:
            self.add_choice_to_coordinate(coordinate, choice_to_be_added)
            return

        #Search through other coordinates within the current column for a possible swap.
        for other_coord in self.column_list[coordinate[1]]:
            ###
            for choice in poss_choices_column:
                ###
                if choice in self.poss_choices_row[other_coord[0]] and choice in self.poss_choices_three_by_three[other_coord[2]]:
                    ###
                    if self.board[other_coord] in poss_choices_row and self.board[other_coord] in poss_choices_three_by_three:
                        choice_to_be_added = self.board[other_coord]
                        self.remove_choice_from_coordinate(other_coord)
                        self.add_choice_to_coordinate(other_coord, choice)
                        break
        if choice_to_be_added:
            self.add_choice_to_coordinate(coordinate, choice_to_be_added)
            return

        #Search through other coordinates within the current three_by_three for a possible swap.
        for other_coord in self.three_by_three_list[coordinate[2]]:
            ###
            for choice in poss_choices_three_by_three:
                ###
                if choice in self.poss_choices_row[other_coord[0]] and choice in self.poss_choices_column[other_coord[1]]:
                    ###
                    if self.board[other_coord] in poss_choices_row and self.board[other_coord] in poss_choices_column:
                        choice_to_be_added = self.board[other_coord]
                        self.remove_choice_from_coordinate(other_coord)
                        self.add_choice_to_coordinate(other_coord, choice)
                        break
        if choice_to_be_added:
            self.add_choice_to_coordinate(coordinate, choice_to_be_added)
            return

        if not choice_to_be_added:
            print("No valid choice found for coordinate:", coordinate)
            self.failed_coordinates[coordinate] = None
            #for other_coord in self.three_by_three_list[coordinate[2]]:
                #if self.board[other_coord] in 


    def fix_failed_coordinates(self):

        while self.failed_coordinates:        
        
            for coordinate in self.failed_coordinates:
                self.failed_coordinates[coordinate] = [self.poss_choices_row[coordinate[0]][0], self.poss_choices_column[coordinate[1]][0], self.poss_choices_three_by_three[coordinate[2]][0]]

            for coordinate in self.failed_coordinates:

                #To fix coordinates which have only one possible choice in all three of their poss_choice lists.
                if len(set(self.failed_coordinates[coordinate])) == 1:
                    self.add_choice_to_coordinate(coordinate, self.failed_coordinates[coordinate][0])
                    del self.failed_coordinates[coordinate]
                    break          

                #
                if len(set(self.failed_coordinates[coordinate])) == 2:
                    #Find out which number is an option for two sublists...
                    counter_dict = {}
                    for num in self.failed_coordinates[coordinate]:
                        if num not in counter_dict:
                            counter_dict[num] = 1
                        else:
                            counter_dict[num] += 1
                    higher_count = max([(value, key) for key, value in counter_dict.items()])[1]
                    lower_count = min([(value, key) for key, value in counter_dict.items()])[1]
                    #...and which sublist does not have that number (row, column, or three_by_three).
                    sublist_to_change = self.failed_coordinates[coordinate].index(lower_count)
                    #change_queue = [coordinate, sublist_to_change]
                    #del self.failed_coordinates[coordinate]

                    for other_coord in self.failed_coordinates:
                        if self.failed_coordinates[other_coord][sublist_to_change] == higher_count:
                            if sublist_to_change == 0:
                                self.poss_choices_row[coordinate[0]] = [higher_count]
                                self.poss_choices_row[other_coord[0]] = [lower_count]
                            if sublist_to_change == 1:
                                self.poss_choices_column[coordinate[1]] = [higher_count]
                                self.poss_choices_column[other_coord[1]] = [lower_count]
                            if sublist_to_change == 2:
                                self.poss_choices_three_by_three[coordinate[2]] = [higher_count]
                                self.poss_choices_three_by_three[other_coord[2]] = [lower_count]
                            break
                break




                        
                    


            

        


    def min_len_list_index(self, row_list, column_list, three_by_three_list):
        combined_list = [row_list, column_list, three_by_three_list]
        min_len_list = min(combined_list, key = len)
        return combined_list.index(min_len_list)

    def populate_board(self):
        for coordinate in self.board:
            print("\nSetting coordinate ", coordinate)
            choice_list = []
            choice_to_be_added = 0
            poss_choices_row = self.poss_choices_row[coordinate[0]]
            poss_choices_column = self.poss_choices_column[coordinate[1]]
            poss_choices_three_by_three = self.poss_choices_three_by_three[coordinate[2]]
            print("poss_choices_row = " + str(poss_choices_row))
            print("poss_choices_column = " + str(poss_choices_column))
            print("poss_choices_three_by_three = " + str(poss_choices_three_by_three))

            for choice in poss_choices_row:
                if choice in poss_choices_column:
                    if choice in poss_choices_three_by_three:
                        choice_list.append(choice)
            print("choice_list =", choice_list)

            if choice_list:
                choice_to_be_added = random.choice(choice_list)
                self.add_choice_to_coordinate(coordinate, choice_to_be_added)

            else:
                self.look_for_possible_swap(coordinate)

        print(self.poss_choices_row)
        print(self.poss_choices_column)
        print(self.poss_choices_three_by_three)

        if self.failed_coordinates:
            print("\nFixing failed coordinates:", self.failed_coordinates)
            self.fix_failed_coordinates()


            



            
                



test_board = Board('hard')
test_board.create_board()
test_board.generate_sublists()
test_board.populate_board()

print("\n", test_board)