from pyvisalgo import VertexCoverVisualizer as Visualizer
from copy import deepcopy
from random import randrange
import data_sample_cities as dsc


class VertexCover:
  def __init__(self, cities, edges, usingSetCover=True):
    self.cities = cities
    self.edges = edges
    self.usingSetCover = usingSetCover
    self.main = self.setCoverMain if usingSetCover else self.maxMatchMain

  def setCoverMain(self):
    print('Using Set Cover')
    n_cities = len(self.cities)
    n_edges = len(self.edges)
    self.u = { i for i in range(n_edges) }
    self.f = [ set() for _ in range(n_cities) ]
    for i in range(n_edges):
      u,v,w = self.edges[i]
      self.f[u].add(i)
      self.f[v].add(i)
    print(self.u, self.f)
    self.U = deepcopy(self.u)
    self.F = deepcopy(self.f)

    self.C = []
    while self.U:
      max_i = self.F.index(max(self.F, key=lambda s: len(s & self.U)))
      vis.fix(max_i)
      print(f'fixing {max_i}')
      S = self.F[max_i]
      self.U -= S
      print(S, self.U, self.F)
      self.F[max_i] = set()
      self.C.append(S)

    vis.draw()

  def maxMatchMain(self):
    print('Using Maximul Matching')
    n_cities = len(self.cities)
    n_edges = len(self.edges)
    self.adjs = [ set() for _ in range(n_cities) ]
    print(self.adjs)
    for i in range(n_edges):
      u,v,w = self.edges[i]
      self.adjs[u].add(v)
      self.adjs[v].add(u)
    print(self.adjs)
    self.vc = set()
    edge_count = 0

    vertices = list(range(n_cities))
    while edge_count < n_edges:
      print(f'{self.adjs=}, {vertices=}')
      vi = randrange(len(vertices))
      u = vertices.pop(vi)
      print(f'{vi=} {u=} {self.adjs[u]=}')
      if not self.adjs[u]: continue
      v = self.adjs[u].pop()
      print(f'{u=} {v=}')
      vis.matching(u,v)

      for n in (u, v):
        self.vc.add(n)
        print(f'{self.vc=}')

        for k in range(n_cities):
          if k in self.adjs[n]:
            print(f'<{n=} {k=} {self.adjs[n]=} {self.adjs[k]=}')
            self.adjs[n].remove(k)
            if n in self.adjs[k]:
              self.adjs[k].remove(n)
            print(f'>{n=} {k=} {self.adjs[n]=} {self.adjs[k]=}')
            edge_count += 1

      print(f'vc={self.vc} {edge_count=} {n_edges=}')

    vis.draw()

vis = Visualizer('Vertex Cover')
usingSetCover = False
while True:
  vc = VertexCover(dsc.cities, dsc.edges, usingSetCover)
  vis.setup(vc)
  vc.main()
  again = vis.end()
  if not again: break
  if vis.restart_lshift:
    dsc.next()
  elif vis.restart_rshift:
    dsc.random()
  else:
    usingSetCover = not usingSetCover