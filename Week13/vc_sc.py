edges=[
    (0, 2, 267), (0, 10, 292), (0, 14, 162), (0, 17, 311), (0, 23, 281),
    (1, 11, 331), (1, 19, 307), (1, 22, 395), (2, 6, 256), (2, 10, 319),
    (2, 14, 111), (2, 16, 316), (2, 18, 405), (2, 20, 451), (2, 21, 415),
    (2, 24, 488), (3, 8, 249), (3, 12, 438), (3, 15, 84), (4, 7, 445),
    (4, 10, 53), (4, 16, 320), (4, 17, 135), (4, 20, 229), (4, 24, 298),
    (5, 9, 367), (5, 13, 483), (5, 15, 261), (5, 19, 358), (6, 7, 109),
    (6, 12, 358), (6, 14, 319), (6, 16, 456), (6, 18, 153), (6, 21, 465),
    (7, 12, 440), (7, 13, 465), (7, 14, 210), (7, 23, 236), (8, 9, 106),
    (10, 16, 285), (11, 13, 371), (11, 19, 53), (12, 13, 243), (12, 18, 364),
    (12, 21, 395), (12, 22, 442), (13, 21, 170), (14, 18, 451), (14, 23, 318),
    (16, 17, 287), (16, 23, 325), (17, 24, 392), (19, 22, 146), (20, 24, 76)
]

num_vertex = 25

## Set Cover

# u,f
n_edges = len(edges)
u = set(range(n_edges))
print(u)
f = [ set() for i in range(num_vertex)]
printf(f)

for i in range(n_edges):
  u,v,w = edges[i]
  f[u].add(i)
  f[v].add(i)
#print(f)

# n x  n x n
C = []
while U:
  max_i = f.index(max(f, key=lambda s: len(s & U)))
  S = f[max_i]
  C.append(S)
  U -= S
  f[max_i] = set()
  print('Selecting {S}, Now u = {U}')
  f.pop(max_i)

print('Selected vertices:', sorted(C))

## Max Matching

# graph build
adjs = [ set() for _ in range(num_vertex)]
for u,v,w in edges:
  adjs[u].add(v)
  adjs[v].add(u)
  print('Adj List:', adjs)
# search matching

vc = []
edge_count = 0

from random import randrange
vertices = list(range(num_vertex))

while edge_count < n_edges:
  rand_index = randrange(Len(vertices))
  u = vertices.pop(rand_index)
  if not adjs[u]: continue
  #v = adjs[u].pop()
  v = list(adjs[u])[0]
  #v = next(iter(adjs[u]))


  #print('{(u,v)=}')
  for n in (u, v):
    #print('------{n=} -------{adjs[n]=}')
    vc.append(n)

    while adjs[n]:
      k = adjs[n].pop()
      print('{k=} {adjs[k]=}')
      adjs[k].remove(n)
      edge_count += 1

print('VC List', vc)
