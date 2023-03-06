import wntr
import pandas as pd

# 读取EPANET输入文件
inp_file = './Network/QDModel.inp'
res = pd.DataFrame()
wn = wntr.network.WaterNetworkModel(inp_file)
n_pipes = len(wn.pipe_name_list)
n_nodes = len(wn.node_name_list)
res_0 = pd.DataFrame([[n_pipes, n_nodes]],
                     index=['before simplify'],
                     columns=['number of pipes', 'number of nodes'])
wn = wntr.morph.skel.skeletonize(wn, pipe_diameter_threshold=300)

n_pipes = len(wn.pipe_name_list)
n_nodes = len(wn.node_name_list)
res_1 = pd.DataFrame([[n_pipes, n_nodes]],
                     index=['after simplify'],
                     columns=['number of pipes', 'number of nodes'])
# 绘制水力网络模型
wntr.graphics.plot_network(wn, title='Water Network Model')
wn.write_inpfile('./Network/Simple_QDModel.inp', version=2.2)
res = pd.concat([res, res_0])
res = pd.concat([res, res_1])
print(res)
