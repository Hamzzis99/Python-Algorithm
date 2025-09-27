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
  print('after :', array)
  vis.build_tree()

  last_parent_index = count // 2 - 1
  if True:
    n = last_parent_index
    vis.set_root(n)
    heapify(n, count)

  print('after :', array)


if __name__ == '__main__':
  seed('Hello')