# from pyvisalgo import QuickSortVisualizer as Visualizer
# from pyvisalgo import Dummy as Visualizer
from time import time
from random import randint, seed, shuffle

def main():
  count = len(array)
  quickSort(0, count-1)

def quickSort(left, right):
  if left >= right: return
  pivot = partition(left, right)
  quickSort(left, pivot-1)
  quickSort(pivot+1, right)

def partition(left, right):
  pi = left
  pivot = array[pi]
  p, q = left, right + 1

  while True:
    while True:
      p += 1
      if q < p: break
      if p > right or array[p] > pivot: break

    while True:
      q -= 1
      if q < p: break
      if q < left or array[q] < pivot: break

    if p >= q: break
    array[p], array[q] = array[q], array[p]

  if left != q:
    array[left], array[q] = array[q], array[left]

  return q

if __name__ == '__main__':
  seed('Hello')

  counts = [
    100, 1000, 2000, 3000, 4000, 5000,
    6000, 7000, 8000, 9000, 10000, 15000,
    20000, 30000, 40000, 50000,
    100000, 200000, 300000, 400000, 500000,
    1000000, 2000000, 3000000, 4000000, 5000000,
  ]

  for count in counts:
    startedOn = time()
    array = [randint(1, count) for _ in range(count)]
    creation = time() - startedOn
    startedOn = time()
    main()
    elapsed = time() - startedOn
    print(f'{count=:<7d} {elapsed=:6.3f} {creation=:5.2f}')
  exit()

  while True:
    count = randint(20, 40)
    array = [randint(1, 99) for _ in range(count)]
    main()
    again = input("again? (y/n): ")
    if again.lower() != 'y': break