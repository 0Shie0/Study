#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
    i = 27
    k = 5
    while i > 0:
        move_right()
        fill_cell()
        i = i-1
    i = 26
    move_down()
    fill_cell()
    while k > 0:        
        while i > 0:
            move_left()
            fill_cell()
            i = i-1
        i = 26
        move_down()
        fill_cell()
        while i > 0:
            move_right()
            fill_cell()
            i = i-1
        move_down()
        fill_cell()
        i = 26
        k = k-1
    while i > 0:
        move_left()
        fill_cell()
        i = i-1
    move_down()
    pass


if __name__ == '__main__':
    run_tasks()
