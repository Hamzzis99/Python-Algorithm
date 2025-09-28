from data_unsorted_a_lot import numbers
from pyvisalgo import RadixSortLsdVisualizer as Visualizer
from time import time
from random import randint, seed, shuffle
from math import log10, ceil

def main():
  print('before:', array)
  count = len(array)

  global counts
  max_value = max(array)
  radix_count = ceil(log10(max_value))
  print(f'{max_value=} {log10(max_value)=} {radix_count=}')
  counts = [0] * 10

  div = 1
  for pos in range(1):
    for i in range(count):
      v = array[i] // div % 10
      counts[v] += 1
      vis.set_inc_index(div, i)

    print(f'{counts=}') 
  # print('after :', array)

if __name__ == '__main__':
  seed('HelloCountSort')
  vis = Visualizer('Radix Sort: LSD')
  while True:
    kind = 1000
    count = randint(30, 150)
    print(f'Creating data: {kind=} {count=}')
    begin = 500 + randint(1, 1000)
    array = list(map(lambda x: x%kind, numbers[begin:begin+count]))
    vis.setup(vis.get_main_module())
    main()
    vis.draw()
    again = vis.end()
    if not again: break