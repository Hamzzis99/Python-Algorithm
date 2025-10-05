from pyvisalgo import QuickSortVisualizer as Visualizer
# from pyvisalgo import Dummy as Visualizer
from time import time
from random import randint, seed, shuffle

def main():
  # print('before:', array)
  count = len(array)
  quickSort(0, count-1)
  insertionSort(0, count-1)

  # print('after :', array)

def quickSort(left, right):
  if left == right: vis.fix(left)
  if left >= right: return
  if right < left + 4:
    #insertionSort(left, right)
    return

def insertionSort(left, right):
  for i in range(left + 1, right + 1):
    v = array[i]
    vis.mark_end(i, v)
    j = i - 1
    while j >= left and array[j] > v:
      vis.shift(j)
      array[j+1] = array[j]
      j -= 1
    vis.insert(i, j+1)
    array[j+1] = v

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