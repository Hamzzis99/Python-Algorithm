from pyvisalgo import VertexCoverVisualizer as Visualizer
from copy import deepcopy
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