# A star implementation for Path Planning
# Ankur Chavan and Aditya Chaugule

import heapq as hq
import tkinter as tk
import numpy as np

######################
# Thresholds

wd = 600
ht = 250

shape =(2, 3, 2)

def eu_dist(p1, p2):
    return np.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def plot_vec(canvas, px,py,x,y,color='red'):
    canvas.create_line(px, py, x,y, arrow=tk.LAST, arrowshape=shape, fill=color, width=1)

def color_space(root, canvas, x,y):
    items = canvas.find_closest(x,y)
    color = root.winfo_rgb(canvas.itemcget(items[0], "fill"))
    return color

nodes = {}

ol = []
visited = set()

def vec0(node,th,step):
    x,y = node
    eu = step
    u0 = eu*np.cos(np.deg2rad(th))
    v0 = eu*np.sin(np.deg2rad(th))
    xu = x+u0
    yu = y-v0
    tu = th
    new_node = (xu,yu)
    return new_node,tu

def vec30(node,th, step):
    x,y = node
    eu = step
    u0 = eu*np.cos(np.deg2rad(th+30))
    v0 = eu*np.sin(np.deg2rad(th+30))
    xu = x+u0
    yu = y-v0
    tu = th+30
    new_node = (xu,yu)
    return new_node,tu

def vecm30(node,th,step):
    x,y = node
    eu = step
    u0 = eu*np.cos(np.deg2rad(th-30))
    v0 = eu*np.sin(np.deg2rad(th-30))
    xu = x+u0
    yu = y-v0
    tu = th-30
    new_node = (xu,yu)
    return new_node, tu

def vec60(node,th,step):
    x,y = node
    eu = step

    u0 = eu*np.cos(np.deg2rad(th+60))
    v0 = eu*np.sin(np.deg2rad(th+60))
    xu = x+u0
    yu = y-v0
    tu = th+60
    new_node = (xu,yu)
    return new_node,tu

def vecm60(node,th, step):
    x,y = node
    eu = step

    u0 = eu*np.cos(np.deg2rad(th-60))
    v0 = eu*np.sin(np.deg2rad(th-60))
    xu = x+u0
    yu = y-v0
    tu = th-60
    new_node = (xu,yu)
    return new_node, tu

def explore(root, canvas, node,step):
    eu = step
    if node in visited:
        return
    visited.add(node)
    parent = node
    exp = nodes[parent]
    th = exp[0]
    for act in [vec0, vec30, vecm30, vec60, vecm60]:
        new_node, new_th = act(node, th,eu)
        pos, ori = new_node, new_th
        if pos[0] >= 0 and pos[0] < wd and pos[1] >= 0 and pos[1] < ht:
            color = color_space(root, canvas, pos[0], pos[1])
            if color == (0, 0, 65535) or color == (65535, 42405, 0):
                continue
            c2c = exp[1] + eu_dist(parent, pos)
            if pos in nodes.keys() and c2c >= nodes[pos][1]:
                continue
            c2g = eu_dist(pos, g_pos)
            tc = c2c + c2g 
            if pos not in nodes.keys() or tc < nodes[pos][3]:
                nodes[pos] = (ori, c2c, c2g, tc, parent)
                if pos not in [n[1] for n in ol]:
                    hq.heappush(ol, (tc, new_node))
                    plot_vec(canvas, parent[0], parent[1], new_node[0], new_node[1], color='white')

def animate(canvas, nodes):
    batch = 100 
    node_list = list(nodes.items())
    num_batch = len(node_list) // batch + 1
    for i in range(num_batch):
        chunk = node_list[i*batch:(i+1)*batch]
        for pos, (ori, c2c, c2g, tc, parent) in chunk:
            if parent is not None:
                px, py = parent[0], parent[1]
                x, y = pos[0], pos[1]
                plot_vec(canvas, px, py, x, y, color='red')
        canvas.after(10)
        canvas.update()

def tracking(nodes, start, end_node):
    track = []
    node = end_node
    while node is not None:
        track.append(node)
        node = nodes[node][4]
    track.reverse()
    return track

def track_animate(canvas,track):
    for i in range(len(track)-1):
        node1 = track[i]
        node2 = track[i+1]
        plot_vec(canvas, node1[0], node1[1], node2[0], node2[1],color='green')

def robot_animate(canvas,track,robot_radius):
    radius = robot_radius
    global robot

    for i, pos in enumerate(track):
        if i == 0:
            x = pos[0]
            y = pos[1]
            robot = canvas.create_oval(x - radius, y - radius, x + radius, y + radius)
            canvas.itemconfig(robot, outline="black")
            canvas.update()
        else:
            prev_pos = track[i-1]
            x_diff = pos[0] - prev_pos[0]
            y_diff = pos[1] - prev_pos[1]
            canvas.move(robot, x_diff, y_diff)
            canvas.after(100)
            canvas.update()

def main(root, canvas, start, goal, robot_radius, step):
    eu =  step
    goal_thr = 10
    thr = 0.5
    global s_pos, s_ori, g_pos, g_ori

    s_pos,s_ori = start[:2],start[-1]
    g_pos,g_ori = goal[:2],goal[-1]
    s_c2c = 0
    s_c2g = eu_dist(s_pos,g_pos)
    s_tc = s_c2c + s_c2g
    nodes[s_pos] = (s_ori,s_c2c,s_c2g,s_tc,None)

    end_node = None
    hq.heappush(ol,(eu_dist(s_pos,g_pos),s_pos))

    while ol:
        _, node = hq.heappop(ol)
        if eu_dist(node, g_pos) > goal_thr:
            explore(root,canvas,node,eu)
        else:
            print("Goal Reached")
            end_node = node
            animate(canvas,nodes)
            if end_node is not None:
                track = tracking(nodes,start,end_node)
                print(len(track))
                track_animate(canvas,track)
                robot_animate(canvas,track,robot_radius)
            break

if __name__ == "__main__":
    main()
