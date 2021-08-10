import unittest
from unittest.mock import Mock

from board_game.main import Board, Player


class TestBoard(unittest.TestCase):
    def setUp(self) -> None:
        self.board = Board()

    def test_initial_values(self):
        self.assertEqual(self.board.x, 0)
        self.assertEqual(self.board.y, 0)
        self.assertEqual(self.board.direction, 0)

    def test_rotate_right(self):
        rotate = 1
        self.board.switch_direction(rotate)
        self.assertEqual(self.board.direction, rotate)

    def test_rotate_left(self):
        rotate = -1
        self.board.switch_direction(rotate)
        self.assertEqual(self.board.direction, rotate)

    def test_rotate_left_above4(self):
        rotate = -5
        self.board.switch_direction(rotate)
        self.assertEqual(self.board.direction, rotate)

    def test_rotate_right_above4_fails(self):
        rotate = 5
        self.board.switch_direction(rotate)
        self.assertNotEqual(self.board.direction, rotate)

    def test_move_one(self):
        self.board.change_position()
        self.assertEqual(self.board.direction, 0)
        self.assertEqual(self.board.y, 1)

    def test_try_move_above_max_limit(self):
        max_limit = 5
        self.board.y = max_limit
        self.board.change_position()
        self.assertEqual(self.board.direction, 0)
        self.assertEqual(self.board.y, max_limit)

    def test_try_move_below_min_limit(self):
        min_limit = 0
        self.board.y = min_limit
        self.board.direction = 2
        self.board.change_position()
        self.assertEqual(self.board.direction, 2)
        self.assertEqual(self.board.y, min_limit)


class TestPlayer(unittest.TestCase):
    def setUp(self) -> None:
        self.board = Mock()
        self.player = Player(self.board)

    def test_initial_position(self):
        self.player.position.x = 0
        self.player.position.y = 0
        self.player.position.direction = 0
        self.assertEqual(self.player.position.x, 0)
        self.assertEqual(self.player.position.y, 0)
        self.assertEqual(self.player.position.direction, 0)

    def test_move_from_default_position(self):
        self.player.position.change_position = Mock()
        self.player.move()
        self.player.position.change_position.assert_called_once_with()

    def test_rotate_left(self):
        self.player.position.switch_direction = Mock()
        direction = 'l'
        direction_int = -1
        self.player.rotate(direction)
        self.player.position.switch_direction.assert_called_once_with(direction_int)

    def test_rotate_right(self):
        self.player.position.switch_direction = Mock()
        direction = 'r'
        direction_int = 1
        self.player.rotate(direction)
        self.player.position.switch_direction.assert_called_once_with(direction_int)


if __name__ == '__main__':
    unittest.main()
