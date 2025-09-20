from data_unsorted import numbers
# from data_unsorted_a_lot import numbers
from pyvisalgo import ShellSortVisualizer as Visualizer
# from pyvisalgo import Dummy as Visualizer

from random import randint, seed, shuffle
from time import time

def main():
  print('before:', array)
  count = len(array)

  print('after :', array)

if __name__ == '__main__':
  seed('Hello')
  vis = Visualizer('Selection Sort')

  while True:
    count = randint(10, 30)
    array = numbers[:count]
    vis.setup(vis.get_main_module())
    main()
    # vis.set_gap(1)
    vis.mark_end(0)
    # vis.draw()

    again = vis.end()
    if not again: break