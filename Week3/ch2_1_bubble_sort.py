from random import randint, seed
from pyvisalgo import BubbleSortVisualizer as Visualizer

def main():
  print(array)

if __name__ == '__main__':
  seed('Hello') # 시드 설정, 이로부터 똑같은 수가 나오게 됨
  vis = Visualizer('Bubble Sort')
  while True:
    count = randint(10, 30)
    array = numbers[:count]
    vis.setup(vis.get_main_module())
    main()
    vis.draw()

    # R key 를 누르면 다음 case 가 실행된다
    again = vis.end()
    if not again: break