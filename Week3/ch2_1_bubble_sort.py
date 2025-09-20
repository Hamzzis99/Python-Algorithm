from data_unsorted import numbers
from random import randint, seed
from pyvisalgo import Dummy as Visualizer

def main():
  print('before:', array)
  count = len(array)
  end = count - 1
  if True: 
    for i in range(end):
      if array[i] > array[i+1]:
        array[i], array[i+1] = array[i+1], array[i]
  print('after :', array)

''' Bubble 을 한 칸 진행해 본 결과, 다음과 같이 출력된다.
before: [71, 30, 18, 51, 77, 37, 3, 93, 90, 48]
after : [30, 18, 51, 71, 37, 3, 77, 90, 48, 93]
'''

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