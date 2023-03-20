import heapq as hq
import tkinter as tk
import numpy as np
######################
# Thresholds
eu = 20
goal_thr = 10

# Initializations
def points(node):
    x,y,th = node
    r = 5
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvas.create_oval(x0, y0, x1, y1, fill='green')

def eu_dist(p1, p2):
    return np.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

start = (200,200,0)
s_pos,s_ori = start[:2],start[-1]

goal = (500,10,0)
g_pos,g_ori = goal[:2],goal[-1]

nodes = {}
s_c2c = 0
s_c2g = eu_dist(s_pos,g_pos)
s_tc = s_c2c + s_c2g
nodes[s_pos] = (s_ori,s_c2c,s_c2g,s_tc,None)
ol = []

def vec0(node,th):
    x,y = node
    u0 = eu*np.cos(np.deg2rad(th))
    v0 = eu*np.sin(np.deg2rad(th))
    xu = x+u0
    yu = y-v0
    tu = th
    new_node = (xu,yu)
    return new_node,tu

def vec30(node,th):
    x,y = node
    u0 = eu*np.cos(np.deg2rad(th+30))
    v0 = eu*np.sin(np.deg2rad(th+30))
    xu = x+u0
    yu = y-v0
    tu = th+30
    new_node = (xu,yu)
    return new_node,tu

def vecm30(node,th):
    x,y = node
    u0 = eu*np.cos(np.deg2rad(th-30))
    v0 = eu*np.sin(np.deg2rad(th-30))
    xu = x+u0
    yu = y-v0
    tu = th-30
    new_node = (xu,yu)
    return new_node, tu

def explore(node):
    parent = node
    exp = nodes[parent]
    th = exp[0]
    for act in [vec0,vec30,vecm30]:
        
        new_node,new_th = act(node,th)
        pos, ori = new_node, new_th
        if pos[0] >= 0 and pos[0]<wd and pos[1]>=0 and pos[1]<ht:
            items = canvas.find_closest(pos[0],pos[1])
            color = root.winfo_rgb(canvas.itemcget(items[0], "fill"))
            if color == (0,0,65535):
                continue
            if pos not in nodes:
                c2c = nodes[parent[0:2]][1] + eu_dist(parent[0:2], pos)
                c2g = eu_dist(pos,g_pos)
                h = eu_dist(pos, g_pos)  
                tc = c2c + c2g + h  
                nodes[pos] = (ori,c2c,c2g,tc,parent) 
                hq.heappush(ol, (tc,new_node))
                canvas.create_line(parent[0], parent[1], new_node[0],new_node[1], arrow=tk.LAST, fill='red', width=1)

                if eu_dist(pos,s_pos)<=goal_thr:
                    break
            else:
                c2c = nodes[parent[0:2]][1] + eu_dist(parent[0:2], pos)
                c2g = eu_dist(pos,g_pos)
                h = eu_dist(pos, g_pos)  
                tc = c2c + c2g + h  
                if tc < nodes[pos][3]:
                    nodes[pos] = (ori,c2c,c2g,tc,parent)
                    hq.heapify(ol)

root = tk.Tk()

wd = 600
ht = 250
canvas = tk.Canvas(root, width=wd, height=ht)
canvas.pack()

points(start)
points(goal)
hq.heappush(ol,(eu_dist(s_pos,g_pos),s_pos))

rect = canvas.create_rectangle(250, 250, 300, 50, fill="blue")
rect = canvas.create_rectangle(350, 0, 400, 150, fill="blue")
while ol:
    _, node = hq.heappop(ol)
    if eu_dist(node, g_pos) > goal_thr:
        explore(node)
    else:
        break

root.mainloop()

# print(len(nodes))
