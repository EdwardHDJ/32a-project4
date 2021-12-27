class InvalidSizeError(Exception):
    pass
class InvalidPositionError(Exception):
    pass

class GameState:
    def __init__(self):
        self._board = self._create_board()


    def get_board(self)->[['Position']]:
        return self._board


    def del_jewel_in_matched_list_from_game_state(jewel_list:['Jewel'],
                                                  game_state):
        for jewel in jewel_list:
            row = jewel.get_row()
            col = jewel.get_rol()

            game_state.del_
    def append_matched_jewel_in_a_list(self):
        for position_list in self.get_board():
            for position in position_list:
                if position.get_jewel()!= None:
                    if position.get_jewel().get_status() != 'freeze':
                        return True
        return False
    
    def move(self)->None:
        for position_list in self.get_board():
            for position in position_list:
                if position.get_jewel() != None:
                    if position.get_jewel().get_status() == 'faller':
                        position.get_jewel().move_down(self.get_board())
                    elif position.get_jewel().get_status() == 'faller_land':
                        position.get_jewel().change_status('freeze')

    def move_faller(self,faller:'Faller')->None:
        faller.move_down(self.get_board())

        if_check_match = True

        for jewel in faller.get_jewel_in_faller():
            if jewel.get_status() != 'freeze':
                if_check_match == False

        if if_check_match == True:
            game_matched_list = self.check_match()
            for jewel in game_matched_list:
                jewel.change_status('matched')

    def check_game_over(self,faller:'Faller'):
        if faller != None:
            for jewel in faller.get_jewel_in_faller():
                if jewel != None:
                    if jewel.get_status() == 'freeze':
                        if jewel.check_if_jewel_on_board(self.get_board()) == False:
                            return True
        return False
            
            
            
            
                        
    def initiate_game_board_to_empty(self,row:int,col:int)->None:
        board = []
        if row < 4 or col < 3:
            raise InvalidSizeError
        for col_number in range(0,col):
            board_sublist = []
            for row_number in range(0,row):
                board_sublist.append(Position())
            board.append(board_sublist)

        self._board = board
        
    
        
    def check_horizontal_match(self)->['Jewel']:
        row_number = len(self._board[0])
        col_number = len(self._board)
        board = self.get_board()
        match_list = []

        for i in range(0,col_number):
            for j in range(0,row_number):
                color = None
                jewel = board[i][j].get_jewel()
                if jewel != None and jewel.get_status() == 'freeze':
                    color = jewel.get_color()
                    count = 1
                    col = i
                    row = j
                    while True:
                        if col >= col_number-1:
                            break
                        if board[col+1][row].get_jewel()!= None:
                            if board[col+1][row].get_jewel().get_color() == color  and board[col+1][row].get_jewel().get_status() == 'freeze':
                                count += 1
                            if board[col+1][row].get_jewel().get_color() != color:
                                break
                        col +=1
                    if count >=3:
                        for col_num in range(i,i+count):
                            match_list.append(board[col_num][j].get_jewel())

        return match_list

    
    def check_vertical_match(self)->['Jewel']:
        row_number = len(self._board[0])
        col_number = len(self._board)
        board = self.get_board()
        match_list = []
        for i in range(0,col_number):
            for j in range(0,row_number):
                color = None
                jewel = board[i][j].get_jewel()
                if jewel != None and jewel.get_status() == 'freeze':
                    color = jewel.get_color()
                    count = 1
                    col = i
                    row = j
                    while True:
                        if row >= row_number-1:
                            break
                        if board[col][row+1].get_jewel()!= None:
                            if board[col][row+1].get_jewel().get_color() == color and board[col][row+1].get_jewel().get_status() == 'freeze':
                                count += 1
                            if board[col][row+1].get_jewel().get_color() != color:
                                break
                        row +=1
                    if count >=3:
                        for row_num in range(j,j+count):
                            match_list.append(board[i][row_num].get_jewel())

        return match_list

    def check_diagonal_up_match(self)->['Jewel']:
        row_number = len(self._board[0])
        col_number = len(self._board)
        board = self.get_board()
        match_list = []
        for i in range(0,col_number):
            for j in range(0,row_number):
                color = None
                jewel = board[i][j].get_jewel()
                if jewel != None and jewel.get_status() == 'freeze':
                    color = jewel.get_color()
                    
                    count = 1
                    col = i
                    row = j
                    while True:
                        if row >= row_number-1 or col >= col_number - 1:
                            break
                        if board[col+1][row+1].get_jewel()!= None:
                            if board[col+1][row+1].get_jewel().get_color() == color and board[col+1][row+1].get_jewel().get_status() == 'freeze':
                                count += 1
                            if board[col+1][row+1].get_jewel().get_color() != color:
                                break
                        row +=1
                        col += 1
                        
                    if count >=3:
                        for count_num in range(0,count):
                            match_list.append(board[i+count_num][j+count_num].get_jewel())

        return match_list

    def check_diagonal_down_match(self)->['Jewel']:
        row_number = len(self._board[0])
        col_number = len(self._board)
        board = self.get_board()
        match_list = []
        for i in range(0,col_number):
            for j in range(0,row_number):
                color = None
                jewel = board[i][j].get_jewel()
                if jewel != None and jewel.get_status() == 'freeze':
                    color = jewel.get_color()
                    count = 1
                    col = i
                    row = j
                    while True:
                        if row < 1 or col >= col_number - 1:
                            break
                        if board[col+1][row-1].get_jewel()!= None:
                            if board[col+1][row-1].get_jewel().get_color() == color and board[col+1][row-1].get_jewel().get_status() == 'freeze':
                                count += 1
                            if board[col+1][row-1].get_jewel().get_color() != color:
                                break
                        row -= 1
                        col += 1
                    if count >=3:
                        for count_num in range(0,count):
                            match_list.append(board[i+count_num][j-count_num].get_jewel())

        return match_list


    
    def check_match(self)->['Jewel']:
        match_list = []

        horizontal_match_list = self.check_horizontal_match()
        vertical_match_list = self.check_vertical_match()
        diagonal_up_match_list = self.check_diagonal_up_match()
        diagonal_down_match_list = self.check_diagonal_down_match()
        
        for jewel in horizontal_match_list:
            if jewel not in match_list:
                match_list.append(jewel)
        for jewel in vertical_match_list:
            if jewel not in match_list:
                match_list.append(jewel)
        for jewel in diagonal_up_match_list:
            if jewel not in match_list:
                match_list.append(jewel)
        for jewel in diagonal_down_match_list:
            if jewel not in match_list:
                match_list.append(jewel)
        
     
        return match_list

                    
                            
    def get_jewel(self,row:int,col:int)->'Jewel': 
        return self.get_board()[col][row].get_jewel()

    def add_jewel(self,jewel:'Jewel',row:int,col:int)->None:
        if row < 0 or row >= len(self.get_board()[0]):
            raise InvalidPositionError
        if col < 0 or col >= len(self.get_board()):
            raise InvalidPositionError
        position = self._board[col][row]
        position.add_jewel(jewel)

    def check_if_jewel_on_board(self,jewel,board)->bool:
        row_position = jewel.get_row()
        col_position = jewel.get_col()

        if row_position >= 0 and row_position < len(self._board) \
           and col_position >= 0 and col_position < len(self._board[0]):
            return True

        return False
        
    def _create_board(self)->[]:
        board = self.initiate_game_board_to_empty(4,3)

        return board


class Position:
    def __init__(self):
        self._is_empty = True
        self._jewel_in_position = None
        
    def check_empty(self)->bool:
        return self._is_empty


    def get_jewel(self)->'Jewel':
        return self._jewel_in_position
    
    def add_jewel(self,jewel:'Jewel')->None:
        self._add_jewel(jewel)


    def _add_jewel(self,jewel:'Jewel')->None:
        self._is_empty = False
        self._jewel_in_position = jewel


        return jewel
    
        
        

class Jewel:
    def __init__(self,row_position:int,col_position:int,color_information:str,
                 status:str):
        self._col_position = col_position
        self._row_position = row_position
        self._color_information = color_information
        self._status = status

    def move(self)->None:
        self._col_position += 1

    def change_status(self,status:str):
        self._status = status
            
        
    def get_color(self)->str:
        return self._color_information

    def get_col(self)->int:
        return self._col_position

    def get_row(self)->int:
        return self._row_position
    
    def get_status(self)->str:
        return self._status
        
    def move_down(self,board:[['Position']])->None:
##        print(self.check_if_jewel_could_move_down(board))
        if self.get_status() != 'match':
            if self.check_if_jewel_could_move_down(board) == True:
                if self.check_if_jewel_on_board_after_move_down(board) == True:
    ##                print('jewel_is_added')
                    board[self._col_position][self._row_position-1].add_jewel(self)
    ##                print('if jewel_could_be reset' ,self.check_if_jewel_on_board(board))
                    if self.check_if_jewel_on_board(board) == True:
    ##                    print('jewel_position_is_reset')
                        board[self._col_position][self._row_position] = Position()
                self._row_position -= 1
            if self.check_if_jewel_could_move_down(board) == False:
                self.change_status('faller_land')

    def move_up(self,board:[['Position']])->None:
        if self.check_if_jewel_could_move_up(board) == True:
            board[self._col_position][self._row_position+1].add_jewel(self)
            board[self._col_position][self._row_position] = Position()
            self._row_position += 1
    
    def move_left(self,board:[['Position']])->None:
        if self.check_if_jewel_could_move_left(board) == True:
            if self.check_if_jewel_on_board(board) == True:
                board[self._col_position-1][self._row_position].add_jewel(self)
                board[self._col_position][self._row_position] = Position()
            self._col_position -= 1
            self.change_status('faller')
            if self.check_if_jewel_could_move_down(board) == False:
                self.change_status('faller_land')

    def move_right(self,board:[['Position']])->None:
        if self.check_if_jewel_could_move_right(board) == True:
            if self.check_if_jewel_on_board(board) == True:
                board[self._col_position+1][self._row_position].add_jewel(self)
                board[self._col_position][self._row_position] = Position()
            self._col_position += 1
            self.change_status('faller')
            if self.check_if_jewel_could_move_down(board) == False:
                self.change_status('faller_land')

    def check_if_jewel_on_board(self,board:[['Position']]):
        row_position = self._row_position
        col_position = self._col_position
##        print('row' ,row_position)
##        print('col' ,col_position)
##        print('len(board[0])', len(board[0]))
##        print('len(board)' , len(board))
        
        if row_position >= 0 and row_position < len(board[0]) \
           and col_position >= 0 and col_position < len(board):
            return True

        return False

    def check_if_jewel_could_move_down(self,board:[['Position']]):
        jewel_row_position = self._row_position
        jewel_col_position = self._col_position

        if jewel_row_position > len(board[0]):
            return True
        
        if jewel_row_position < 1:
            return False

##        print(board[jewel_col_position][jewel_row_position-1].check_empty())
        if board[jewel_col_position][jewel_row_position-1].check_empty() == True:
            return True
        return False

    def check_if_jewel_on_board_after_move_down(self,board:[['Position']]):
        jewel_row_position = self._row_position
        jewel_col_position = self._col_position
        jewel_row_position_after_move = jewel_row_position-1

##        print(jewel_row_position_after_move)
##        print(len(board[0]))

##        print(jewel_row_position_after_move < len(board[0]))
        if jewel_row_position_after_move >= 0 and jewel_row_position_after_move < len(board[0]) \
        and  jewel_col_position >= 0 and  jewel_col_position < len(board):
            return True

        return False
    def check_if_jewel_could_move_up(self,board:[['Position']]):
        jewel_row_position = self._row_position
        jewel_col_position = self._col_position

        if jewel_row_position >= len(board[0])-1:
            return False
        if board[jewel_col_position][jewel_row_position+1].check_empty() == True:
            return True

        return False

    def check_if_jewel_could_move_left(self,board:[['Position']]):
        jewel_row_position = self._row_position
        jewel_col_position = self._col_position

        if self.check_if_jewel_on_board(board) == False:
            return True
        if jewel_col_position < 1:
            return False
        
        if board[jewel_col_position-1][jewel_row_position].check_empty() == True:
            return True

        return False

    def check_if_jewel_could_move_right(self,board:[['Position']]):
        jewel_row_position = self._row_position
        jewel_col_position = self._col_position

        if self.check_if_jewel_on_board(board) == False:
            return True

        if jewel_col_position >= len(board)-1:
            return False
        
        if board[jewel_col_position+1][jewel_row_position].check_empty() == True:
            return True

        return False
    
    
class Faller:
    def __init__(self,jewel1,jewel2,jewel3):
        self._jewel_in_faller = [jewel1,jewel2,jewel3]
    
    def rotate(self,game_state)->'Faller':

        if self._jewel_in_faller[2].get_status() != 'freeze':
            
        
            t_jewel = Jewel(self._jewel_in_faller[2].get_row()+2,self._jewel_in_faller[2].get_col(),self._jewel_in_faller[2].get_color(),
                                self._jewel_in_faller[2].get_status())
            
            self._jewel_in_faller[2] = Jewel(self._jewel_in_faller[1].get_row()-1,self._jewel_in_faller[1].get_col(),self._jewel_in_faller[1].get_color(),
                                self._jewel_in_faller[1].get_status())

            self._jewel_in_faller[1] = Jewel(self._jewel_in_faller[0].get_row()-1,self._jewel_in_faller[0].get_col(),self._jewel_in_faller[0].get_color(),
                                self._jewel_in_faller[0].get_status())

            self._jewel_in_faller[0] = t_jewel

            for jewel in self.get_jewel_in_faller():
                if jewel.check_if_jewel_on_board(game_state.get_board()) == True:
                    game_state.add_jewel(jewel,jewel.get_row(),jewel.get_col())
            
        
        
    def get_jewel_in_faller(self):
        return self._jewel_in_faller
    
    def move_right(self,board:[['Position']]):
        if self._jewel_in_faller[2].get_status() != 'freeze':
            jewel_list = self.get_jewel_in_faller()

            for jewel in jewel_list:
                if jewel.check_if_jewel_could_move_right(board) == False:
                    return None

            for jewel in jewel_list:
                jewel.move_right(board)

    def move_down(self,board:[['Position']]):
        jewel_list = self.get_jewel_in_faller()

        if jewel_list[2].check_if_jewel_could_move_down(board) == False:
            for jewel in jewel_list:
                jewel.change_status('freeze')
            return None

        for jewel_index in reversed(range(0,len(jewel_list))):


##            print(jewel_index)
            jewel_list[jewel_index].move_down(board)

    def move_left(self,board:[['Position']]):
        if self._jewel_in_faller[2].get_status() != 'freeze':
            jewel_list = self.get_jewel_in_faller()

            for jewel in jewel_list:
                if jewel.check_if_jewel_could_move_left(board) == False:
                    return None

            for jewel in jewel_list:
                jewel.move_left(board)
        
    def move_up(self,board:[['Position']]):
        jewel_list = self.get_jewel_in_faller()

        for jewel in jewel_list:
            if jewel.check_if_jewel_could_move_up(board) == False:
                return None

        for jewel in jewel_list:
            jewel.move_up(board)



def time_tick(game_state:'GameState',game_faller:'Faller')->None:
        match_flag = False
        count = 0
        for position_list in game_state.get_board():
            for position in position_list:
                if position.get_jewel()!= None:
                    if position.get_jewel().get_status() == 'matched':
                        count += 1
                        match_flag = True
                        col_number = position.get_jewel().get_col()
                        row_number = position.get_jewel().get_row()
                        empty_position = Position()
                        game_state.get_board()[col_number][row_number] = empty_position

        if match_flag == True:
            for num in range(0,count):
                for position_list in game_state.get_board():
                    for position in position_list:
                        if position.get_jewel()!= None:
                            position.get_jewel().move_down(game_state.get_board())
                        if position.get_jewel() != None:
                            position.get_jewel().change_status('freeze')
                match_list  = game_state.check_match()

                for match_jewel in match_list:
                    match_jewel.change_status('matched')
        
            
                        
                        
        if match_flag == False:
            game_state.move_faller(game_faller)
            game_faller_list = game_faller.get_jewel_in_faller()
            game_faller_status = game_faller_list[2].get_status()
            if game_faller_status != 'matched':
                if game_faller_list[1].get_status() != 'matched':
                    game_faller_list[1].change_status(game_faller_status)
                if game_faller_list[0].get_status() != 'matched':
                    game_faller_list[0].change_status(game_faller_status)
                
def faller_move_left(game_state:'GameState',game_faller:'Faller')->None:
    if game_faller != None:
        if game_faller.get_jewel_in_faller()[0] != 'freeze':
            game_faller_list = game_faller.get_jewel_in_faller()
            game_faller.move_left(game_state.get_board())
            game_faller_status = game_faller_list[2].get_status()
            game_faller_list[1].change_status(game_faller_status)
            game_faller_list[0].change_status(game_faller_status)
            game_faller_status = game_faller_list[2].get_status()


def faller_move_right(game_state:'GameState',game_faller:'Faller')->None:
    if game_faller != None:
        if game_faller.get_jewel_in_faller()[0] != 'freeze':
            game_faller_list = game_faller.get_jewel_in_faller()
            game_faller.move_right(game_state.get_board())
            game_faller_status = game_faller_list[2].get_status()
            game_faller_list[1].change_status(game_faller_status)
            game_faller_list[0].change_status(game_faller_status)
            game_faller_status = game_faller_list[2].get_status()

                
def move_content(game_state)->None:
    row_number = len(game_state.get_board()[0])
    for i in range(0,row_number):
            for position_list in game_state.get_board():
                    for position in position_list:
                        if position.get_jewel()!= None:
                            position.get_jewel().move_down(game_state.get_board())
                        if position.get_jewel() != None:
                            position.get_jewel().change_status('freeze')
                            
def change_content_according_to_input(game_state:'GameState')->None:
    for row_number in reversed(range(0,len(game_state.get_board()[0]))):
        user_input = input()
        for col_number in range(0,len(game_state.get_board())):
            if user_input[col_number] != ' ':
                jewel = Jewel(row_number,col_number,
                                           user_input[col_number],'faller')
                game_state.add_jewel(jewel,row_number,col_number)

def rotate_faller(game_state:'GameState',game_faller:'Faller')->None:
    if game_faller != None:
                if game_faller.get_jewel_in_faller()[0] != 'freeze':
                    game_faller.rotate(game_state)
