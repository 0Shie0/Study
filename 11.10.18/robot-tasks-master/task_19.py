#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_29():
    i = 0
    while  wall_is_above() and i <16:
        while wall_is_on_the_right() == False and wall_is_above():
                move_right()
                i = i+1
        while wall_is_on_the_left() == False and wall_is_above():
                move_left()
                i = i + 1
        if i>=16:
            while wall_is_on_the_right() == False:
                move_right()
    while wall_is_above() == False and i<16:
            move_up()
    while wall_is_on_the_left() == False and i<16:
            move_left()
    pass


if __name__ == '__main__':
    run_tasks()
