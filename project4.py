import columns_game

class ColumnsGame:
    def __init__(self):
        pass

    def run(self):
        game_row,game_col = self._ask_user_for_board_size()

        game_state = self._create_game_state(game_row,game_col)

        board = game_state.get_board()

        game_faller = None

        third_line = input()

        if third_line == 'EMPTY':
            pass

        elif third_line == 'CONTENTS':

            columns_game.change_content_according_to_input(game_state)

            columns_game.move_content(game_state)

            match_list  = game_state.check_match()

            for match_jewel in match_list:
                match_jewel.change_status('matched')
            

        self._display_board(game_state)

        while True:
            user_input = input()

            if user_input == '':
                columns_game.time_tick(game_state,game_faller)
                
                self._display_board(game_state)
                    
                
                if game_state.check_game_over(game_faller) == True:
                    print('GAME OVER')
                    return None
                        
            if user_input == 'Q': 
                return None
            
            if user_input.startswith('F'):
                check_faller = game_state.if_there_is_faller_on_board()

                if check_faller == True:
                    continue
                
                command_list = user_input.split()
                    
                
                start_row = len(board[0])+1
                col_number = int(command_list[1])-1
                
                jewel1 = columns_game.Jewel(start_row , col_number,command_list[2],'faller')
                jewel2 = columns_game.Jewel(start_row-1,col_number,command_list[3],'faller')
                jewel3 = columns_game.Jewel(start_row-2,col_number,command_list[4],'faller')

                if game_state.get_board()[jewel3.get_col()][jewel3.get_row()].get_jewel() != None:
                    print('GAME OVER')
                    return None
                
                game_state.add_jewel(jewel3,start_row-2,col_number)
                
                game_faller = columns_game.Faller(jewel1,jewel2,jewel3)

                check_jewel = game_faller.get_jewel_in_faller()[2]

                if check_jewel.check_if_jewel_could_move_down(game_state.get_board()) == False:
                    for jewel in game_faller.get_jewel_in_faller():
                        jewel.change_status('faller_land')
                self._display_board(game_state)


                
            if user_input == 'R':
                columns_game.rotate_faller(game_state,game_faller)
                
                self._display_board(game_state)
                
            if user_input == '<':
                columns_game.faller_move_left(game_state,game_faller)
                    
                self._display_board(game_state)
            if user_input == '>':
                columns_game.faller_move_right(game_state,game_faller)

                self._display_board(game_state)
                
                
        
                    

    def _create_game_state(self,row:int,col:int)->columns_game.GameState:
        game_state = columns_game.GameState()
        game_state.initiate_game_board_to_empty(row,col)

        return game_state

    def _ask_user_for_board_size(self)->tuple:
        input_row_number = int(input())
        input_column_number = int(input())        
##        input_row_number = 4
##        input_column_number = 3
        row_number =  input_row_number 
        column_number = input_column_number

        return row_number,column_number





                
    def _display_board(self,game_state:'GameState')->None:
        board = game_state.get_board()
        for row_number in reversed(range(0,len(board[0]))):
            if row_number != len(board[0])-1:
                print()
            print('|',end = '')
            for col_number in range(0,len(board)):
                if board[col_number][row_number].get_jewel() == None:
                    print('   ',end = '')
                if board[col_number][row_number].get_jewel() != None:
                    if board[col_number][row_number].get_jewel().get_status() == 'freeze':
                        print(' ' +board[col_number][row_number].get_jewel().get_color()+ ' ',end = '')
                    if board[col_number][row_number].get_jewel().get_status() == 'faller':
                        print('[' +board[col_number][row_number].get_jewel().get_color()+ ']',end = '')
                    if board[col_number][row_number].get_jewel().get_status() == 'faller_land':
                        print('|' +board[col_number][row_number].get_jewel().get_color()+ '|',end = '')
                    if board[col_number][row_number].get_jewel().get_status() == 'matched':
                        print('*' +board[col_number][row_number].get_jewel().get_color()+ '*',end = '')
            print('|',end = '')
        print()
        print(' '+ '---'* len(board)+' ')
    
if __name__ =='__main__':
    game = ColumnsGame()
    game.run()
