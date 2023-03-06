import wntr
import numpy as np
import networkx as nx
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import eigsh
import matplotlib.pyplot as plt

inp_file = './Network/Simple_QDModel.inp'
wn = wntr.network.WaterNetworkModel(inp_file)
G = wn.get_graph()
print(G)

# pos = nx.spring_layout(G, seed=42)  # 确定节点的位置
# nx.draw_networkx_nodes(G, pos, node_size=500)
# nx.draw_networkx_edges(G, pos, arrows=True)
# nx.draw_networkx_edge_labels(G, pos, font_size=14, edge_labels=nx.get_edge_attributes(G, 'label'))
# nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')
# plt.axis('off')
# plt.show()

A = nx.adjacency_matrix(G).astype(float)
degree_dict = dict(G.degree())
degree_values = np.array(list(degree_dict.values())).astype(float)

# 创建度矩阵
D = csr_matrix(np.diag(degree_values))
L = D - A
eigenvalues, eigenvectors = eigsh(A, k=1000, which='SM')
plt.title('Rank eig plot')
plt.plot(np.sort(eigenvalues))
plt.xlabel('k')
plt.ylabel('eig')
plt.show()
