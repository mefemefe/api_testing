"""
Test module used to verify that an user can work with Boards

Classes:
    TestBoards
"""

from main.trello.api.members_manager import MembersManager
from main.trello.api.boards_manager import BoardsManager


class TestBoards():
    
    @classmethod
    def setup_class(cls):
        """ Initialze the managers used to interact with the API """
        cls.boards_manager = BoardsManager()
        cls.members_manager = MembersManager()

    def test_create_board(self):
        """Test to verify boards can be created, listed and deleted
        
        STEPS:
        1. Create a new Board
        2. Verify the API response comes with the status code 200 an Board's data
        3. Verify the new Board exists
        4. Verify the board can be deleted
        """
        name = "TestBoard"
        description = "Test the creation of a board"
        status_code, created_board = self.boards_manager.create_board(name, description=description)
        # 1. verify status code
        assert status_code == 200, f"Couldn't create a board with name '{name}' and description '{description}'"
        # 2. verify can new board exists
        status_code, board = self.boards_manager.get_board(created_board['id'])
        assert created_board['name'] == name, f"Board name is {created_board['name']} but it was expected {name}"
        assert created_board['desc'] == description, f"Board name is {created_board['desc']} " \
                                                     f"but it was expected {description}"
        # 3. verify member can see it in the list
        status_code, board_list = self.members_manager.get_boards(fields='name')
        for member_board in board_list:
            if member_board['id'] == created_board['id']:
                break
        else:
            raise AssertionError("Member cannot see listed the board {} " \
                                 "with name '{}'".format(created_board['id'], created_board['name']))
        # 4. Delete created board
        status_code, _ = self.boards_manager.delete_board(created_board['id'])
        assert status_code == 200, f"Board {created_board['id']} with '{name}' couldn't be deleted"
