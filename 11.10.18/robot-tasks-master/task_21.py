#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    i = 12
    iall=12
    k = 12
    move_right()
    move_down()
    while i + 1 > 0:
        fill_cell()
        move_down()
        i = i-1
    move_up()
    i = iall
    iall = iall - 1
    while iall > 0:
        move_right()
        while i > 0:
            fill_cell()
            move_up()
            i = i-1
        i = iall
        iall = iall - 1
        move_down(i)
        move_down()
    move_right()
    fill_cell()
    move_down()
    move_left(12)
    
    
    pass


if __name__ == '__main__':
    run_tasks()
