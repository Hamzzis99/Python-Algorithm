from data_unsorted import numbers
from random import randint, seed
from pyvisalgo import BubbleSortVisualizer as Visualizer

def main():
  print('before:', array)
  count = len(array)
  for end in range(count - 1, 0, -1):
    for i in range(end):
      vis.compare(i, i+1)
      if array[i] > array[i+1]:
        vis.swap(i, i+1)        
        array[i], array[i+1] = array[i+1], array[i]
    #visualize
    vis.bubble_end(end)
  vis.bubble_end(0)
  print('after :', array)

before: [71, 30, 18, 51, 77, 37, 3, 93, 90, 48]
after : [3, 18, 30, 37, 48, 51, 71, 77, 90, 93]

if __name__ == '__main__':
  seed('Hello') 
  vis = Visualizer('Bubble Sort')
  while True:
    count = randint(10, 30)
    array = numbers[:count]
    vis.setup(vis.get_main_module())
    main()
    vis.draw()

    again = vis.end()
    if not again: break