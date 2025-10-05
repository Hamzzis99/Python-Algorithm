from pyvisalgo import MergeSortVisualizer as Visualizer
# from pyvisalgo import Dummy as Visualizer
from time import time
from random import randint, seed, shuffle

def main():
  print('before:', array)
  count = len(array)
  mid = count // 2
  array[0:mid] = sorted(array[0:mid])
  array[mid:] = sorted(array[mid:])

  vis.push(0, mid-1, count-1)
  merge(0, mid, count-1)
  print('after :', array)

def merge(left, right, end):
  merged = []
  vis.start_merge(merged, False, left)
  l, r = left, right
  while l < right and r <= end:
    vis.compare(l, r)
    if array[l] <= array[r]:
      merged.append(array[l])
      vis.add_to_merged(l, True)
      l += 1
    else:
      merged.append(array[r])
      vis.add_to_merged(r, False)
      r += 1

  while l < right:
    merged.append(array[l])
    vis.add_to_merged(l, True)
    l += 1
  while r <= end:
    merged.append(array[r])
    vis.add_to_merged(r, False)
    r += 1

  vis.end_merge()

  l = left
  for n in merged:
    array[l] = n
    l += 1
    # vis.erase_merged()

  vis.pop()

if __name__ == '__main__':
  seed('Hello')
  vis = Visualizer('Merge Sort')
  while True:
    count = randint(20, 40)
    array = [ randint(1, 99) for _ in range(count) ]
    vis.setup(vis.get_main_module())
    main()
    vis.draw()
    again = vis.end()
    if not again: break