#!/usr/bin/env python
from dataclasses import dataclass, field

from platform import python_version_tuple


@dataclass
class Point:
    x: int = field(default=0)
    y: int = field(default=0)
    direction: int = field(default=0)

    def __repr__(self):
        str_direction = ["N", "E", "S", "W"]
        return f"{self.x} {self.y} {str_direction[self.direction]}"


class Board(Point):
    _max = 5
    _min = 0
    waypoints = 4

    def change_position(self):
        if self.direction in [0, 2]:
            self._change_y()
        else:
            self._change_x()

    def _change_x(self):
        if self.direction == 1:
            if self.x < self._max:
                self.x += 1
        else:
            if self.x > self._min:
                self.x -= 1

    def _change_y(self):
        if self.direction == 0:
            if self.y < self._max:
                self.y += 1
        else:
            if self.y > self._min:
                self.y -= 1

    def switch_direction(self, rotate_direction):
        self.direction += rotate_direction
        if self.direction >= self.waypoints:
            self.direction %= self.waypoints


class Player:
    def __init__(self, board: Board):
        self.position = board

    def move(self):
        self.position.change_position()

    def rotate(self, direction):
        pos = 1 if direction == 'r' else -1
        self.position.switch_direction(pos)


def play(instr: str):
    board = Board()
    player = Player(board)

    for action in instr:
        if action == 'm':
            player.move()
        elif action in ['l', 'r']:
            player.rotate(action)
        else:
            msg = "Unknown action issued %s"
            raise AttributeError(msg, action)
    return player.position


def check_python_version():
    major, minor, _ = python_version_tuple()
    msg = "Not possible to use with python version below 3.7"
    if major < "3":
        raise RuntimeError(msg)
    if minor < "7":
        raise RuntimeError(msg)

def main():
    check_python_version()
    prompt = "Play the game.\nInput M to move, R to rotate right, L to rotate left: "
    print(play(input(prompt)))

if __name__ == '__main__':
    main()