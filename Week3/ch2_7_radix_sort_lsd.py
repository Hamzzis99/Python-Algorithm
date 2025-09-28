from data_unsorted_a_lot import numbers
from pyvisalgo import RadixSortLsdVisualizer as Visualizer
from time import time
from random import randint, seed, shuffle
from math import log10, ceil

def main():
  global array
  print('before:', array)
  count = len(array)

  global counts
  max_value = max(array)
  radix_count = ceil(log10(max_value))
  print(f'{max_value=} {log10(max_value)=} {radix_count=}')

  global result
  result = []

  div = 1
  for pos in range(radix_count):
    counts = [0] * 10
    for i in range(count):
      v = array[i] // div % 10
      counts[v] += 1
      vis.set_inc_index(div, i)

    print(f'counts= {counts}') 
    vis.set_inc_index(div, -1)
    for i in range(9):
      counts[i+1] += counts[i]
      vis.draw()
      vis.wait(1000)

    print(f'indices={counts}') 

    result = [None] * count

    for i in range(count-1, -1, -1):
      v = array[i] // div % 10
      at = counts[v] - 1
      counts[v] -= 1
      vis.set_inc_index(div, i, False)
      result[at] = array[i]
      # print(f'{i=:2d} {v=:2d} {result=}')

    vis.result_to_array()
    array = result
    result = []
    div *= 10

  # print('after :', array)

if __name__ == '__main__':
  seed('HelloCountSort')
  vis = Visualizer('Radix Sort: LSD')
  while True:
    kind = 100000
    count = randint(30, 80)
    print(f'Creating data: {kind=} {count=}')
    array = list(map(lambda x: randint(1, kind), range(count)))
    vis.setup(vis.get_main_module())
    main()
    vis.draw()
    again = vis.end()
    if not again: break