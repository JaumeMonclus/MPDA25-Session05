#r: networkx
#r: matplotlib

from typing import cast, Any
import networkx as nx # type: ignore
import matplotlib.pyplot as plt # type: ignore
import Rhino.Geometry as rg # type: ignore beaause using stubs
import ghpythonlib.treehelpers as th # type: ignore
import ghpythonlib.components as comps # type: ignore


import graph_helpers as graph 


# DECLARE INPUT VARIABLES OF PYTHON COMPONENT
# DECLARE INPUT VARIABLES OF PYTHON COMPONENT
m = cast(rg.Mesh, m)  # type: ignore
s = cast(int, s)  # type: ignore
# p = cast(rg.Point3d,p)



strips=[]
allindexes=[]
slen=[]

G, dv, de = graph.DualGraphFromMesh(m)

#pick starting point
startPoint = s

# iterate through SP and get all shorest paths
all_sp_indexes  = []
all_sp_points  = []
nodes = []
for i in range(len(G.nodes)):
    if nx.has_path(G, s, i):
        sp = graph.shortestPath(G, s, i)
        all_sp_points.append(sp[0])
        all_sp_indexes.append(sp[1])

        OL = nx.onion_layers(G)
        nodes.append(OL)




#convert all shortest paths to polylines
all_sp_polylines = []


#evaluate polylines for straightness and max length


#select shortest path based on crieteria


# repeat the process




a = th.list_to_tree(all_sp_indexes)
b = th.list_to_tree(all_sp_points)
# c = all_sp_polylines
d = nodes
    







# a= strips
# b = allindexes
# c = slen

