# from data_unsorted import numbers
# from data_unsorted_a_lot import numbers
from pyvisalgo import QuickSortVisualizer as Visualizer
# from pyvisalgo import Dummy as Visualizer
from time import time
from random import randint, seed, shuffle

def main():
  print('before:', array)
  count = len(array)

  vis.push(0, count-1)
  pivot = partition(0, count-1)
  vis.set_pivot(pivot)

  print('after :', array)

def partition(left, right):

  pi = left
  pivot = array[pi]

  p, q = left, right + 1

  while True:
    while True:
      p += 1
      vis.set_p(p)
      if q < p: break
      if p <= right: vis.compare(pi, p)
      if p > right or array[p] > pivot: break 

      if p <= right: vis.set_left(p)

    while True:
      q -= 1
      vis.set_q(q)
      if q < p: break
      if q >= left: vis.compare(pi, q)
      if q < left or array[q] < pivot: break

      if q >= left: vis.set_right(q)

    if p >= q: break

    vis.set_left(p)
    vis.set_right(q)

    vis.swap(p, q)
    array[p], array[q] = array[q], array[p] 

  if left != q:
    vis.swap(left, q, True)
    array[left], array[q] = array[q], array[left]
  return q

if __name__ == '__main__':
  seed('Hello')
  vis = Visualizer('Quick Sort')
  while True:
    count = randint(20, 40)
    array = [ randint(1, 99) for _ in range(count) ]
    vis.setup(vis.get_main_module())
    main()
    vis.draw()
    again = vis.end()
    if not again: break