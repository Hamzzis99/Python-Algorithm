# from pyvisalgo import QuickSortVisualizer as Visualizer
# from pyvisalgo import Dummy as Visualizer
from time import time
from random import randint, seed, shuffle

def main():
  # print('before:', array)
  count = len(array)
  quickSort(0, count-1)

  # print('after :', array)

def quickSort(left, right): #q=inclusive
  # if left == right: vis.fix(left)
  if left >= right: return
  if right == left + 1:
    # vis.compare(left, right)
    if array[left] > array[right]:
      # vis.swap(left, right)
      array[left], array[right] = array[right], array[left]
    return  
  # vis.push(left, right)
  pivot = partition(left, right)
  # vis.set_pivot(pivot)
  quickSort(left, pivot-1)
  quickSort(pivot+1, right)
  # vis.pop()

def partition(left, right):

  pi = left
  pivot = array[pi]

  p, q = left, right + 1

  while True:
    while True:
      p += 1
      # vis.set_p(p)
      if q < p: break
      # if p <= right: vis.compare(pi, p)
      if p > right or array[p] > pivot: break 

      # if p <= right: vis.set_left(p)

    while True:
      q -= 1
      # vis.set_q(q)
      if q < p: break
      # if q >= left: vis.compare(pi, q)
      if q < left or array[q] < pivot: break

      # if q >= left: vis.set_right(q)

    if p >= q: break

    # vis.set_left(p)
    # vis.set_right(q)

    # vis.swap(p, q)
    array[p], array[q] = array[q], array[p] 

  if left != q:
    # vis.swap(left, q, True)
    array[left], array[q] = array[q], array[left]

  return q

if __name__ == '__main__':
  seed('Hello')

  counts = [ 
  # 10,20,30,50,100
    100, 1000, 2000, 3000, 4000, 5000, 
    6000, 7000, 8000, 9000, 10000, 15000, 
    20000, 30000, 40000, 50000,
    100000, 200000, 300000, 400000, 500000,
    1000000, 2000000, 3000000, 4000000, 5000000,
  ]
  for count in counts:
    startedOn = time()
    array = [ randint(1, count) for _ in range(count) ]
    creation = time() - startedOn
    # shuffle(array)
    # print('before:', array)
    startedOn = time()
    main()
    elapsed = time() - startedOn
    # print('after: ', array)
    print(f'{count=:<7d} {elapsed=:6.3f} {creation=:5.2f}')    
  exit() 

  # vis = Visualizer('Quick Sort')
  while True:
    count = randint(20, 40)
    array = [ randint(1, 99) for _ in range(count) ]
    vis.setup(vis.get_main_module())
    main()
    vis.draw()
    again = vis.end()
    if not again: break