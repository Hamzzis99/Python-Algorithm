from pyvisalgo import QuickSortVisualizer as Visualizer
# from pyvisalgo import Dummy as Visualizer
from time import time
from random import randint, seed, shuffle

def main():
  # print('before:', array)
  count = len(array)
  quickSort(0, count-1)
  # insertionSort(0, count-1)

  # print('after :', array)

def quickSort(left, right): #q=inclusive
  if left == right: vis.fix(left)  # 정렬 대상이 하나뿐이라면 확정해도 좋다
  if left >= right: return         # 정렬할 것이 없으면 할 일이 없다
  # if right < left + 4:
  #   # insertionSort(left, right)
  #   return
  vis.push(left, right)
  pivot = partition(left, right)   # pivot 위치를 결정해 온다
  vis.set_pivot(pivot)
  quickSort(left, pivot-1)  # pivot 보다 왼쪽 그룹을 다시 quickSort 한다
  quickSort(pivot+1, right) # pivot 보다 오른쪽 그룹을 다시 quickSort 한다
  vis.pop()

def insertionSort(left, right): #right=inclusive
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

  pi = left               # pi = Pivot Index
  pivot = array[pi]       # pivot = Pivot Value

  p, q = left, right + 1  # 후보선수들 출전준비

  while True:             # p < q 인 동안 하게 된다. 하지만 중간에 break 하므로 while True 를 쓰자
    while True:           # 왼쪽에서 pivot 보다 큰 값을 찾을때까지
      p += 1
      vis.set_p(p)
      if q < p: break
      if p <= right: vis.compare(pi, p)
      if p > right or array[p] > pivot: break 
      # 왼쪽에서 pivot 보다 큰 값을 찾았다

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