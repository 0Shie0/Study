#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_21():
    i = 0
    k = 0
    if wall_is_beneath():
            move_up(9)
            k = 1
    if wall_is_on_the_right():
            move_left(9)
            i = 2
    if wall_is_on_the_left() and i != 2:
            move_right(9)          
    if wall_is_above() and k != 1:
            move_down(9)

    pass


if __name__ == '__main__':
    run_tasks()
