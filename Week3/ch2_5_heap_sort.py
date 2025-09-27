from data_unsorted import numbers
from random import randint, seed, shuffle
from pyvisalgo import HeapSortVisualizer as Visualizer
from time import time

def heapify(root, size):
  lc = root * 2 + 1
  if lc >= size: return
  child = lc
  rc = root * 2 + 2
  if rc < size:
    vis.compare(rc, lc)
    if array[rc] > array[lc]:
      child = rc

  vis.compare(root, child)
  if array[root] < array[child]:
    vis.swap(root, child)
    array[root], array[child] = array[child], array[root]
    heapify(child, size)

def main():
  print('before:', array)
  count = len(array)
  vis.build_tree()

  last_parent_index = count // 2 - 1
  for n in range(last_parent_index, -1, -1):
    vis.set_root(n)
    heapify(n, count)

  last_sort_index = count - 1
  if last_sort_index > 0:
    vis.compare(0, last_sort_index)
    vis.swap(0, last_sort_index)
    array[0], array[last_sort_index] = array[last_sort_index], array[0] 
    vis.set_tree_size(last_sort_index)

  print('after :', array)


if __name__ == '__main__':
  seed('Hello')
  vis = Visualizer('Heap Sort')
  while True:
    array = numbers[:randint(10, 30)]
    vis.setup(vis.get_main_module())
    startedOn = time()
    main()
    elapsed = time() - startedOn
    print(f'Elapsed time = {elapsed:.3f}s')
    again = vis.end()
    if not again: break