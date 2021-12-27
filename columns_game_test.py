import columns_game
import unittest

class ColumnsGameTest(unittest.TestCase):
    def setUp(self):
        self._game_state = self._create_game_state()
        self._game_state.initiate_game_board_to_empty(4,3)
        
    def test_create_game_state(self)->None:
        self._game_state


    def test_game_state_has_board_in_it(self)->None:
        self._game_state.get_board()

    def test_game_state_could_have_different_size(self)->None:
        row = 8
        col = 9
        
        self._game_state.initiate_game_board_to_empty(8,9)
        board = self._game_state.get_board()
        for col_number in range(0,col):
            for row_number in range(0,row):
                self.assertTrue(board[col_number][row_number].check_empty)
                

    def test_initiate_state_could_set_all_jewels_to_correct_list(self)->None:
        board = self._game_state.get_board()

        for pos_list in board:
            for pos in pos_list:
                self.assertEqual(pos.check_empty(),True)


    def test_position_could_add_jewel(self):
        board = self._game_state.get_board()
        board[0][0].add_jewel(self._create_jewel())


    def test_board_could_add_jewel_in_different_position(self):
        jewel = self._create_jewel()

        row = 1

        col = 2
        
        self._game_state.add_jewel(jewel,row,col)

        self.assertTrue(self._game_state.get_jewel(row,col) , jewel)


    def test_jewel_could_have_color(self):
        jewel = self._create_jewel_with_color()
        self.assertEqual(jewel.get_color() ,'S')


    def test_jewel_could_be_add_to_board_with_correct_color(self):
        jewel = self._create_jewel_with_color()

        self._game_state.add_jewel(jewel,2,1)

        self.assertEqual(self._game_state.get_jewel(2,1).get_color(),'S')

    def test_jewel_has_attribute_called_status(self):
        jewel = self._create_jewel_with_status()

        self.assertEqual(jewel.get_status(), 'moving')


    def test_jewel_could_move_down(self):
        board = self._game_state.get_board()
        
        jewel = self._create_jewel_with_position(1,2)

        jewel.move_down(board)

        self.assertEqual(jewel.get_row(),0)

    def test_faller_class_exist(self):
        jewel1 = self._create_jewel()
        jewel2 = self._create_jewel()
        jewel3 = self._create_jewel()

        
        faller = columns_game.Faller(jewel1,jewel2,jewel3)


    def test_faller_has_jewel_faller_artribute(self):
        jewel1 = self._create_jewel()
        jewel2 = self._create_jewel()
        jewel3 = self._create_jewel()
        
        faller = columns_game.Faller(jewel1,jewel2,jewel3)

        jewel_in_faller = faller.get_jewel_in_faller()

        jewel_in_faller[0] = jewel1
        jewel_in_faller[1] = jewel2
        jewel_in_faller[2] = jewel3

        


    def test_faller_could_be_set_up(self):
        

        jewel1 = self._create_jewel()
        jewel2 = self._create_jewel()
        jewel3 = self._create_jewel()

        faller = columns_game.Faller(jewel1,jewel2,jewel3)




    def test_game_state_could_check_whether_a_jewel_is_on_board(self):
        jewel = self._create_jewel_with_position(1,2)

        board = self._game_state.get_board()

        self.assertEqual(self._game_state.check_if_jewel_on_board(jewel,board),True)

        jewel = self._create_jewel_with_position(5,6)

        self.assertEqual(self._game_state.check_if_jewel_on_board(jewel,board),False)
        

    def test_jewel_could_check_if_a_jewel_is_on_baord(self):
        board = self._game_state.get_board()

        jewel = self._create_jewel_with_position(1,2)

        self.assertTrue(jewel.check_if_jewel_on_board(board))

        jewel = self._create_jewel_with_position(4,5)

        self.assertFalse(jewel.check_if_jewel_on_board(board))

    
    def test_jewel_could_check_if_it_could_move_down(self):
        board = self._game_state.get_board()

        jewel = self._create_jewel_with_position(1,1)

        self._game_state.add_jewel(jewel,1,1)

        jewel = self._create_jewel_with_position(2,1)

        self.assertEqual(jewel.check_if_jewel_could_move_down(board),False)


    def test_jewel_could_check_if_it_could_move_up(self):
        board = self._game_state.get_board()

        jewel = self._create_jewel_with_position(1,1)

        self._game_state.add_jewel(jewel,1,1)

        jewel = self._create_jewel_with_position(0,1)

        self.assertEqual(jewel.check_if_jewel_could_move_up(board),False)


    def test_jewel_could_check_if_it_could_move_left(self):
        board = self._game_state.get_board()

        jewel = self._create_jewel_with_position(1,1)

        self._game_state.add_jewel(jewel,1,1)

        jewel = self._create_jewel_with_position(2,2)

        self.assertEqual(jewel.check_if_jewel_could_move_left(board),True)

    def test_jewel_could_check_if_it_could_move_left(self):
        board = self._game_state.get_board()

        jewel = self._create_jewel_with_position(1,1)

        self._game_state.add_jewel(jewel,1,1)

        jewel = self._create_jewel_with_position(1,0)

        self.assertEqual(jewel.check_if_jewel_could_move_right(board),False)

    def test_jewel_could_check_if_it_could_move_right(self):
        board = self._game_state.get_board()

        jewel = self._create_jewel_with_position(1,1)

        self._game_state.add_jewel(jewel,1,1)

        jewel = self._create_jewel_with_position(2,2)

        self.assertEqual(jewel.check_if_jewel_could_move_left(board),True)


    def test_faller_could_move_jewel_in_faller_to_right(self):
        jewel1 = self._create_jewel_with_color_and_position_and_status(1,0,'S','moving')
        jewel2 = self._create_jewel_with_color_and_position_and_status(2,0,'T','moving')
        jewel3 = self._create_jewel_with_color_and_position_and_status(3,0,'V','moving')
        
        faller = columns_game.Faller(jewel1,jewel2,jewel3)

        self._game_state.add_jewel(jewel1,1,0)
        self._game_state.add_jewel(jewel2,2,0)
        self._game_state.add_jewel(jewel3,3,0)

        for jewel in faller.get_jewel_in_faller():
            jewel.move_right(self._game_state.get_board())

        self.assertEqual(self._game_state.get_jewel(1,1),jewel1)
        self.assertEqual(self._game_state.get_jewel(2,1),jewel2)
        self.assertEqual(self._game_state.get_jewel(3,1),jewel3)

        
    def test_jewel_could_move_right_on_board(self):
        board = self._game_state.get_board()
        jewel1 = self._create_jewel_with_color_and_position_and_status(1,0,'S','moving')
        jewel2 = self._create_jewel_with_color_and_position_and_status(2,0,'T','moving')
        jewel3 = self._create_jewel_with_color_and_position_and_status(3,0,'V','moving')

        self._game_state.add_jewel(jewel1,1,0)
        self._game_state.add_jewel(jewel2,2,0)
        self._game_state.add_jewel(jewel3,3,0)
        
        faller = columns_game.Faller(jewel1,jewel2,jewel3)

        faller.move_right(board)

        self.assertEqual(self._game_state.get_jewel(1,1),jewel1)
        self.assertEqual(self._game_state.get_jewel(2,1),jewel2)
        self.assertEqual(self._game_state.get_jewel(3,1),jewel3)
        
        
    def test_jewel_stop_move_right_when_blocked(self):
        
        board = self._game_state.get_board()
        jewel1 = self._create_jewel_with_color_and_position_and_status(1,0,'S','moving')
        jewel2 = self._create_jewel_with_color_and_position_and_status(2,0,'T','moving')
        jewel3 = self._create_jewel_with_color_and_position_and_status(3,0,'V','moving')

        jewel4 = self._create_jewel_with_color_and_position_and_status(2,1,'V','moving')

        self._game_state.add_jewel(jewel1,1,0)
        self._game_state.add_jewel(jewel2,2,0)
        self._game_state.add_jewel(jewel3,3,0)
        self._game_state.add_jewel(jewel4,2,1)
        

        faller = columns_game.Faller(jewel1,jewel2,jewel3)

        faller.move_right(board)

        self.assertEqual(self._game_state.get_jewel(1,0),jewel1)
        self.assertEqual(self._game_state.get_jewel(2,0),jewel2)
        self.assertEqual(self._game_state.get_jewel(3,0),jewel3)

    def test_check_horizontal_match(self):
        board = self._game_state.get_board()
        jewel1 = self._create_jewel_with_color_and_position_and_status(1,0,'S','freeze')
        jewel2 = self._create_jewel_with_color_and_position_and_status(1,1,'S','freeze')
        jewel3 = self._create_jewel_with_color_and_position_and_status(1,2,'S','freeze')

        jewel4 = self._create_jewel_with_color_and_position_and_status(2,1,'S','freeze')

        self._game_state.add_jewel(jewel1,1,0)
        self._game_state.add_jewel(jewel2,1,1)
        self._game_state.add_jewel(jewel3,1,2)

        horizontal_match_list = match_list = self._game_state.check_horizontal_match()

        self.assertEqual(match_list[0], jewel1)
        self.assertEqual(match_list[1], jewel2)
        self.assertEqual(match_list[2], jewel3)

    def test_check_vertical_match(self):
        board = self._game_state.get_board()
        jewel1 = self._create_jewel_with_color_and_position_and_status(0,0,'S','freeze')
        jewel2 = self._create_jewel_with_color_and_position_and_status(1,0,'S','freeze')
        jewel3 = self._create_jewel_with_color_and_position_and_status(2,0,'S','freeze')
        jewel4 = self._create_jewel_with_color_and_position_and_status(3,0,'S','freeze')

        self._game_state.add_jewel(jewel1,0,0)
        self._game_state.add_jewel(jewel2,1,0)
        self._game_state.add_jewel(jewel3,2,0)
        self._game_state.add_jewel(jewel4,3,0)

        vertical_match_list = match_list = self._game_state.check_vertical_match()

        self.assertEqual(match_list[0], jewel1)
        self.assertEqual(match_list[1], jewel2)
        self.assertEqual(match_list[2], jewel3)
        self.assertEqual(match_list[3], jewel4)

    def test_check_diagonal_up_match(self):
        game_state = columns_game.GameState()
        game_state.initiate_game_board_to_empty(5,6)
        board = game_state.get_board()
        
        jewel1 = self._create_jewel_with_color_and_position_and_status(0,0,'S','freeze')
        jewel2 = self._create_jewel_with_color_and_position_and_status(1,1,'S','freeze')
        jewel3 = self._create_jewel_with_color_and_position_and_status(2,2,'S','freeze')
        jewel4 = self._create_jewel_with_color_and_position_and_status(3,3,'S','freeze')

        game_state.add_jewel(jewel1,0,0)
        game_state.add_jewel(jewel2,1,1)
        game_state.add_jewel(jewel3,2,2)
        game_state.add_jewel(jewel4,3,3)

        match_list = match_list = game_state.check_diagonal_up_match()

        self.assertEqual(match_list[0], jewel1)
        self.assertEqual(match_list[1], jewel2)
        self.assertEqual(match_list[2], jewel3)
        self.assertEqual(match_list[3], jewel4)

    def test_check_diagonal_down_match(self):
        game_state = columns_game.GameState()
        game_state.initiate_game_board_to_empty(5,6)
        board = game_state.get_board()
        
        jewel1 = self._create_jewel_with_color_and_position_and_status(2,0,'S','freeze')
        jewel2 = self._create_jewel_with_color_and_position_and_status(1,1,'S','freeze')
        jewel3 = self._create_jewel_with_color_and_position_and_status(0,2,'S','freeze')

        game_state.add_jewel(jewel1,2,0)
        game_state.add_jewel(jewel2,1,1)
        game_state.add_jewel(jewel3,0,2)

        match_list = match_list = game_state.check_diagonal_down_match()
        
        self.assertEqual(match_list[0].get_color(), jewel1.get_color())
        self.assertEqual(match_list[1].get_color(), jewel2.get_color())
        self.assertEqual(match_list[2].get_color(), jewel3.get_color())

    def test_faller_could_rotate(self):
        board = self._game_state.get_board()
        jewel1 = self._create_jewel()
        jewel2 = self._create_jewel()
        jewel3 = self._create_jewel()
        
        faller = columns_game.Faller(jewel1,jewel2,jewel3)

        faller.rotate(self._game_state)

        jewel_list = faller.get_jewel_in_faller()

        self.assertEqual(jewel_list[0].get_color() , jewel3.get_color())

        self.assertEqual(jewel_list[1].get_color() , jewel1.get_color())

        self.assertEqual(jewel_list[2].get_color() , jewel2.get_color())

    def test_jewel_could_check_whether_on_board_after_move(self):

        board = self._game_state.get_board()

        jewel1 = columns_game.Jewel(4,0,'X','faller')
        jewel2 = columns_game.Jewel(5,0,'X','faller')

        self.assertEqual(jewel1.check_if_jewel_on_board_after_move_down(board),True)

        self.assertEqual(jewel2.check_if_jewel_on_board_after_move_down(board),False)


    def test_game_state_could_move(self):
        
        jewel1 = self._create_jewel_with_color_and_position_and_status(0,2,'S','faller_land')
        jewel2 = self._create_jewel_with_color_and_position_and_status(1,1,'S','faller')
        jewel3 = self._create_jewel_with_color_and_position_and_status(2,0,'S','faller')

        self._game_state.add_jewel(jewel1,0,2)
        self._game_state.add_jewel(jewel2,1,1)
        self._game_state.add_jewel(jewel3,2,0)

        self._game_state.move() 

        self.assertEqual(self._game_state.get_jewel(0,2) , jewel1)
        self.assertEqual(self._game_state.get_jewel(0,2).get_status() , 'freeze')
        self.assertEqual(self._game_state.get_jewel(0,1) , jewel2)
        self.assertEqual(self._game_state.get_jewel(0,1).get_status() , 'faller_land')
        self.assertEqual(self._game_state.get_jewel(1,0) , jewel3)
        self.assertEqual(self._game_state.get_jewel(1,0).get_status() , 'faller')


    def test_faller_could_be_moved_correctly_on_game_state(self):
        game_state = columns_game.GameState()
        game_state.initiate_game_board_to_empty(4,3)
        board = game_state.get_board()

        start_row = len(board[0])+1
        command_list = 'F 3 X Y Z '.split()
        col_number = int(command_list[1])-1

        jewel1 = columns_game.Jewel(5,col_number,command_list[2],'faller')
        jewel2 = columns_game.Jewel(4,col_number,command_list[3],'faller')
        jewel3 = columns_game.Jewel(3,col_number,command_list[4],'faller')

##        game_state.add_jewel(jewel3,start_row-2,col_number)
##
##        game_state.add_jewel_to_off_board_jewel(jewel1)
##        game_state.add_jewel_to_off_board_jewel(jewel2)

##        self.assertTrue(jewel1 in game_state.get_off_board_jewel())
##        self.assertTrue(jewel2 in game_state.get_off_board_jewel())
        game_state.add_jewel(jewel3,3,2)
        
        self.assertTrue(game_state.get_jewel(3,2), jewel3)
        self.assertTrue(game_state.get_jewel(3,2).get_status(), 'faller')
        faller = columns_game.Faller(jewel1,jewel2,jewel3)

        faller.move_down(game_state.get_board())

        self.assertEqual(game_state.get_jewel(3,2),jewel2)
        self.assertEqual(game_state.get_jewel(2,2),jewel3)

        faller.move_down(game_state.get_board())
        self.assertEqual(game_state.get_jewel(1,2),jewel3)
        self.assertEqual(game_state.get_jewel(2,2),jewel2)
        self.assertEqual(game_state.get_jewel(3,2),jewel1)

        faller.move_down(game_state.get_board())
        self.assertEqual(game_state.get_jewel(0,2),jewel3)
        self.assertEqual(game_state.get_jewel(1,2),jewel2)
        self.assertEqual(game_state.get_jewel(2,2),jewel1)

        self.assertEqual(game_state.get_jewel(0,2).get_status(),'faller_land')
        self.assertEqual(game_state.get_jewel(1,2).get_status(),'faller_land')
        self.assertEqual(game_state.get_jewel(2,2).get_status(),'faller_land')

        faller.move_down(game_state.get_board())

        self.assertEqual(game_state.get_jewel(0,2),jewel3)
        self.assertEqual(game_state.get_jewel(1,2),jewel2)
        self.assertEqual(game_state.get_jewel(2,2),jewel1)

        self.assertEqual(game_state.get_jewel(0,2).get_status(),'freeze')
        self.assertEqual(game_state.get_jewel(1,2).get_status(),'freeze')
        self.assertEqual(game_state.get_jewel(2,2).get_status(),'freeze')

    

        
        

        



        

        

        

        
                
        
    def _create_game_state(self)->columns_game.GameState:
        test_game_state = columns_game.GameState()

        return test_game_state



    def _create_jewel(self)->'Jewel':
            jewel = columns_game.Jewel(0,0,' ','moving')
            return jewel


    def _create_jewel_with_position(self,row_position:int,col_position:int):
        jewel = columns_game.Jewel(row_position,col_position,' ','moving')
        return jewel

    
    def _create_jewel_with_color(self):
        jewel = columns_game.Jewel(0,0,'S','moving')
        return jewel

    def _create_jewel_with_status(self):
        jewel = columns_game.Jewel(0,0,' ','moving')
        return jewel

    def _create_jewel_with_color_and_position_and_status(self,row_position:int,
                                                         col_position:int,
                                                         color:str,status:str)->'Jewel':

        jewel = columns_game.Jewel(row_position,col_position,color,status)

        return jewel

    
if __name__ == '__main__':
    unittest.main()
