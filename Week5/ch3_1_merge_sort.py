from pyvisalgo import MergeSortVisualizer as Visualizer
from time import time
from random import randint, seed, shuffle

def main():
  print('before:', array)
  count = len(array)
  mergeSort(0, count-1)
  print('after :', array)

def insertionSort(left, right):
  for i in range(left + 1, right + 1):
    v = array[i]
    vis.mark_end(i, v)
    j = i - 1
    while j >= left and array[j] > v:
      vis.shift(j)      
      array[j+1] = array[j]
      print(f'-:{array[left:right+1]=}')
      j -= 1
    print(f'{i=} {j=} {v=}')
    vis.insert(i, j+1)
    array[j+1] = v

def mergeSort(left, right):
  if right <= left: return
  if right < left + 8:
    insertionSort(left, right)
    return
  mid = (left + right) // 2
  vis.push(left, mid, right)
  mergeSort(left, mid)
  mergeSort(mid+1, right)
  merge(left, mid+1, right)
  vis.pop()

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
  array[left:end+1] = merged

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
