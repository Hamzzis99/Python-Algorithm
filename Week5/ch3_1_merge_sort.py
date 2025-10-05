# from pyvisalgo import MergeSortVisualizer as Visualizer
# from pyvisalgo import Dummy as Visualizer
from time import time
from random import randint, seed, shuffle
# from data_unsorted import numbers
from data_unsorted_a_lot import numbers

def main():
  # print('before:', array)
  count = len(array)
  mergeSort(0, count-1)
  # print('after :', array)

def mergeSort(left, right):
  if right <= left: return
  if right == left + 1:
    # vis.compare(left, right)
    if array[left] > array[right]:
      # vis.swap(left, right)
      array[left], array[right] = array[right], array[left]
      return
  mid = (left + right) // 2
  # vis.push(left, mid, right)
  mergeSort(left, mid)
  mergeSort(mid+1, right)
  merge(left, mid+1, right)
  # vis.pop()

def merge(left, right, end):
  merged = []
  # vis.start_merge(merged, False, left)
  l, r = left, right
  while l < right and r <= end:
    # vis.compare(l, r)
    if array[l] <= array[r]:
      merged.append(array[l])
      # vis.add_to_merged(l, True)
      l += 1
    else:
      merged.append(array[r])
      # vis.add_to_merged(r, False)
      r += 1

  while l < right:
    merged.append(array[l])
    # vis.add_to_merged(l, True)
    l += 1
  while r <= end:
    merged.append(array[r])
    # vis.add_to_merged(r, False)
    r += 1

  # vis.end_merge()

  array[left:end+1] = merged
  # l = left
  # for n in merged:
  #   array[l] = n
  #   l += 1

    # vis.erase_merged()

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
    # array = numbers[:count]
    # shuffle(array)
    mmm = count * 10 + randint(1, 1000)
    array = [ randint(1, mmm) for _ in range(count) ]
    # print('before:', array)
    startedOn = time()
    main()
    elapsed = time() - startedOn
    # print('after: ', array)
    print(f'{count=:<6d} {elapsed=:.3f}')
  exit() 

  vis = Visualizer('Merge Sort')
  while True:
    count = randint(20, 40)
    array = [ randint(1, 99) for _ in range(count) ]
    vis.setup(vis.get_main_module())
    main()
    vis.draw()
    again = vis.end()
    if not again: break