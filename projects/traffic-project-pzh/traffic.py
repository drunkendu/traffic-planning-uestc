# import tkinter as tk
# from tkinter import messagebox
# import networkx as nx
# import random
# import matplotlib.pyplot as plt

# class TrafficNetworkSimulation:
#     def __init__(self, root, n):
#         self.root = root
#         self.root.title("交通网络流分配模拟")
#         self.n = n 
        
#         self.create_widgets()  
#         self.create_network()   

#     def create_widgets(self):
#         self.simulate_button = tk.Button(self.root, text="开始模拟", command=self.simulate_flow)
#         self.simulate_button.pack(pady=10)

#     def create_network(self):

#         self.G = nx.DiGraph()
   
#         for i in range(self.n):
#             for j in range(self.n):
#                 node = f'Node{i*self.n+j+1}'
#                 self.G.add_node(node) 
               
#                 if j < self.n - 1:
#                     self.G.add_edge(node, f'Node{i*self.n+j+2}', capacity=10+random.randint(0,5), weight=1+random.randint(0,2))
#                 if i < self.n - 1:
#                     self.G.add_edge(node, f'Node{(i+1)*self.n+j+1}', capacity=10+random.randint(0,5), weight=1+random.randint(0,2))

#     def simulate_flow(self):
#         # 随机选择起点和终点
#         start_node = random.choice(list(self.G.nodes))
#         end_node = random.choice(list(self.G.nodes))
        
#         # 使用 Dijkstra 算法计算最短路径
#         try:
#             shortest_path = nx.dijkstra_path(self.G, start_node, end_node)
#         except nx.NetworkXNoPath:
#             messagebox.showerror("错误", "网络中没有从起点到终点的路径,请重试!")
#             return
        
#         flow_dict = self.random_flow()  # 初始随机流量分配
#         previous_flow_dict = None         # 用于存储上一次流量分配
        
#         # 迭代调整流量，直到收敛
#         while previous_flow_dict != flow_dict:
#             previous_flow_dict = flow_dict.copy() 
#             for i in range(len(shortest_path) - 1):
#                 u = shortest_path[i]
#                 v = shortest_path[i + 1]
#                 flow_dict[u][v] = min(flow_dict[u][v], self.G[u][v]['capacity'])
        
#         # 计算总流量
#         flow_value = sum(flow_dict[u][v] for u, v in self.G.edges())
        
#         # 显示结果和绘制网络图
#         self.show_result(flow_value, flow_dict)
#         self.draw_abstract_network(flow_dict)

#     def random_flow(self):      
#         flow_dict = {u: {v: random.randint(0, self.G[u][v]['capacity']) for v in self.G[u]} for u in self.G}
#         return flow_dict

#     def show_result(self, flow_value, flow_dict):   # 展示总流量和流量分配细节
#         messagebox.showinfo("模拟结果", f"总流量: {flow_value}\n流量分配: {flow_dict}")

#     def get_line_properties(self, flow_amount):    # 根据流量大小返回边的颜色和宽度
#         if flow_amount < 5:
#             return 'green', 2
#         elif flow_amount < 10:
#             return 'orange', 4
#         else:
#             return 'red', 6

#     def draw_abstract_network(self, flow_dict):     # 使用 Matplotlib 绘制交通网络图
#         plt.figure(figsize=(10, 10))
#         pos = nx.spring_layout(self.G)  # 使用Spring布局

#         for u, v in self.G.edges():
#             flow_amount = flow_dict[u][v]
#             if flow_amount > 0:
#                 color, width = self.get_line_properties(flow_amount)
#                 nx.draw_networkx_edges(self.G, pos, edgelist=[(u, v)], width=width, edge_color=color)
        
#         nx.draw_networkx_nodes(self.G, pos, node_size=500)
#         nx.draw_networkx_labels(self.G, pos, font_size=10)

#         for u, v in self.G.edges():
#             flow_amount = flow_dict[u][v]
#             if flow_amount > 0:
#                 mid_pos = ((pos[u][0] + pos[v][0]) / 2, (pos[u][1] + pos[v][1]) / 2)
#                 plt.text(mid_pos[0], mid_pos[1], str(flow_amount), fontsize=12, ha='center')

#         plt.title("抽象交通网络流分配模型")
#         plt.axis('off')
#         plt.show()

# if __name__ == "__main__":
#     n =  6 # 定义网格的大小
#     root = tk.Tk()
#     app = TrafficNetworkSimulation(root, n)
#     root.mainloop()

import tkinter as tk
from tkinter import messagebox
import networkx as nx
import random
import matplotlib.pyplot as plt

class TrafficNetworkSimulation:
    def __init__(self, root, n):
        self.root = root
        self.root.title("交通网络流分配模拟")
        self.n = n 
        
        self.create_widgets()  
        self.create_network()   

    def create_widgets(self):
        self.simulate_button = tk.Button(self.root, text="开始模拟", command=self.simulate_flow)
        self.simulate_button.pack(pady=10)

    def create_network(self):

        self.G = nx.DiGraph()
   
        for i in range(self.n):
            for j in range(self.n):
                node = f'Node{i*self.n+j+1}'
                self.G.add_node(node) 
               
                if j < self.n - 1:
                    self.G.add_edge(node, f'Node{i*self.n+j+2}', capacity=10+random.randint(0,5), weight=1+random.randint(0,2))
                if i < self.n - 1:
                    self.G.add_edge(node, f'Node{(i+1)*self.n+j+1}', capacity=10+random.randint(0,5), weight=1+random.randint(0,2))

    def simulate_flow(self):
        while True:
            # 随机选择起点和终点
            start_node = random.choice(list(self.G.nodes))
            end_node = random.choice(list(self.G.nodes))
            
            # 使用 Dijkstra 算法计算最短路径
            try:
                shortest_path = nx.dijkstra_path(self.G, start_node, end_node)
                break
            except nx.NetworkXNoPath:
                continue
        
        flow_dict = self.random_flow()  # 初始随机流量分配
        previous_flow_dict = None         # 用于存储上一次流量分配
        
        # 迭代调整流量，直到收敛
        while previous_flow_dict != flow_dict:
            previous_flow_dict = flow_dict.copy() 
            for i in range(len(shortest_path) - 1):
                u = shortest_path[i]
                v = shortest_path[i + 1]
                flow_dict[u][v] = min(flow_dict[u][v], self.G[u][v]['capacity'])
        
        # 计算总流量
        flow_value = sum(flow_dict[u][v] for u, v in self.G.edges())
        
        # 显示结果和绘制网络图
        self.show_result(flow_value, flow_dict)
        self.draw_abstract_network(flow_dict)

    def random_flow(self):      
        flow_dict = {u: {v: random.randint(0, self.G[u][v]['capacity']) for v in self.G[u]} for u in self.G}
        return flow_dict

    def show_result(self, flow_value, flow_dict):   # 展示总流量和流量分配细节
        messagebox.showinfo("模拟结果", f"总流量: {flow_value}\n流量分配: {flow_dict}")

    def get_line_properties(self, flow_amount):    # 根据流量大小返回边的颜色和宽度
        if flow_amount < 5:
            return 'green', 2
        elif flow_amount < 10:
            return 'orange', 4
        else:
            return 'red', 6

    def draw_abstract_network(self, flow_dict):     # 使用 Matplotlib 绘制交通网络图
        plt.figure(figsize=(10, 10))
        pos = nx.spring_layout(self.G)  # 使用Spring布局

        for u, v in self.G.edges():
            flow_amount = flow_dict[u][v]
            if flow_amount > 0:
                color, width = self.get_line_properties(flow_amount)
                nx.draw_networkx_edges(self.G, pos, edgelist=[(u, v)], width=width, edge_color=color)
        
        nx.draw_networkx_nodes(self.G, pos, node_size=500)
        nx.draw_networkx_labels(self.G, pos, font_size=10)

        for u, v in self.G.edges():
            flow_amount = flow_dict[u][v]
            if flow_amount > 0:
                mid_pos = ((pos[u][0] + pos[v][0]) / 2, (pos[u][1] + pos[v][1]) / 2)
                plt.text(mid_pos[0], mid_pos[1], str(flow_amount), fontsize=12, ha='center')

        plt.title("抽象交通网络流分配模型")
        plt.axis('off')
        plt.show()

if __name__ == "__main__":
    n =  6 # 定义网格的大小
    root = tk.Tk()
    app = TrafficNetworkSimulation(root, n)
    root.mainloop()