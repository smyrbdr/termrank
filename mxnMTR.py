##...................compute D_tr; minimum term rank distance...........
import numpy as np
import networkx as nx
from networkx.algorithms import bipartite
import itertools
from networkx.convert import _prep_create_using
from networkx.convert_matrix import _generate_weighted_edges
import scipy
from scipy import linalg
n = 7; m = 3
fname = "C:\Magma\smyr3x7a.txt"
fhand = open(fname)
L = list()
S = str()
for line in fhand:
    line = line.strip()
    if "a^2" in line:
        line = line.replace("a^2","1")
    elif "a" in line:
        line = line.replace("a","1")
    S = S + line
M = S.strip().split("@")
for s in M:
    s = s.split("$")
    L.append(s)
for l in L:
    if len(l) < m+1 :
        L.remove(l)
    else:
        l.remove("")

K = list()
for item in L:
    M = list()
    for i in range(m):
        M.append([int(r) for r in item[i]])
   
    A = scipy.sparse.csr_matrix(M)
    G = nx.bipartite.from_biadjacency_matrix(A)
    D = nx.bipartite.maximum_matching(G)
    termrank = int(len(D.items())/2)
    if termrank != 0:
        K.append(termrank)
print "D_tr = ", min(K)
