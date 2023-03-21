# Obstacle Space with Clearance
# Ankur Chavan and Aditya Chaugule

import numpy as np
import tkinter as tk
import math

def points(node):
    x,y,th = node
    r = 5
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    pts = [x0,y0,x1,y1]
    return pts

def triangle(base, height, xc,yc, angle=0):

    x1, y1 = xc+height, yc
    x2, y2 = xc, yc + base/2
    x3, y3 = xc, yc - base/2
    pts = [(x1, y1), (x2, y2), (x3, y3)]
    return pts

def triangle_inflated(base, height, xc, yc, angle=0, dist=0):

    x1, y1 = xc + height + dist, yc
    x2, y2 = xc - 0.8*dist, yc + base/2 + 2.5*dist
    x3, y3 = xc - 0.8*dist, yc - base/2 - 2.5*dist
    pts = [(x1, y1), (x2, y2), (x3, y3)]
    return pts

def polygon_original(sides, length, xc, yc,orient=np.pi/2):
    n = sides
    theta = 2*np.pi/n
    p = length*0.5/np.sin(theta/2)
    pts = []
    for i in range(n):
        x = xc + p*np.cos(theta*i + orient)
        y = yc + p*np.sin(theta*i + orient)
        pts.append((x,y))
    return pts, p

def polygon_inflated(sides, length, xc, yc,orient=np.pi/2, dist=0):
    n = sides
    theta = 2*np.pi/n
    p = length*0.5/np.sin(theta/2)
    pts = []
    for i in range(n):
        x = xc + p*np.cos(theta*i + orient)
        y = yc + p*np.sin(theta*i + orient)
        pts.append((x,y))
    return pts, p

def squircles(canvas, points, corner_radius, **kwargs):
    num_points = len(points)

    angles = []
    for i in range(num_points):
        x1, y1 = points[i]
        x2, y2 = points[(i+1)%num_points]
        dx, dy = x2-x1, y2-y1
        angles.append(math.atan2(dy, dx))
    
    poly_points = []
    for i in range(num_points):
        x, y = points[i]
        angle1 = angles[i-1]
        angle2 = angles[i]
        dx1, dy1 = corner_radius*math.cos(angle1), corner_radius*math.sin(angle1)
        dx2, dy2 = corner_radius*math.cos(angle2), corner_radius*math.sin(angle2)
        x1, y1 = x-dx1, y-dy1
        x2, y2 = x+dx2, y+dy2
        poly_points.extend([x1, y1, x, y, x2, y2])
    
    return canvas.create_polygon(poly_points, **kwargs, smooth=True)
    
def main(start, goal, clearance, robot_radius):
    clearance = clearance
    radius = robot_radius
    distance = clearance + radius

    cr = 10

    root = tk.Tk()

    global wd, ht, canvas
    wd = 600
    ht = 250

    canvas = tk.Canvas(root, width=wd, height=ht,background='white')
    canvas.pack()

    left_wall = [0, 250, 0, 0, distance, 0, distance, 250]
    right_wall = [600 - distance, 250, 600 - distance, 0, 600, 0, 600, 250]
    upper_wall = [0, distance, 0, 0, 600, 0, 600, distance]
    bottom_wall = [0, 250, 0, 250 - distance, 600, 250 - distance, 600, 250]

    canvas.create_polygon(left_wall, fill='orange')    # left wall
    canvas.create_polygon(right_wall, fill='orange')   # right wall
    canvas.create_polygon(upper_wall, fill='orange')   # upper wall
    canvas.create_polygon(bottom_wall, fill='orange')  # bottom wall

    rect_obs1_c = [(100 - distance, 100 + distance), (100 - distance, 0 - distance), (150 + distance, 0 - distance), (150 + distance, 100 + distance)]
    rect_obs2_c = [(100 - distance, 250 + distance), (100 - distance, 150 - distance), (150 + distance, 150 - distance), (150 + distance, 250 + distance)]
    rect_obs2 = [100, 250, 100, 150, 150, 150, 150, 250]
    rect_obs1 = [100 , 100 , 100 , 0 , 150 , 0 , 150 , 100 ]

    squircles(canvas,rect_obs1_c,cr,fill='orange') # Inflated Obs 1
    squircles(canvas,rect_obs2_c,cr,fill='orange') # Inflated Obs 2

    canvas.create_polygon(rect_obs1, fill='blue')  # original rect 1
    canvas.create_polygon(rect_obs2, fill='blue')  # original rect 2

    _, p = polygon_original(6, 75, 300, 125)  # original hexagon

    length = ((distance + p)/p)*75
    pts , p0 = polygon_inflated(6, length, 300, 125)  # inlated hexagon
    squircles(canvas,pts,cr,fill='orange')

    pts, p = polygon_original(6, 75, 300, 125)  # original hexagon
    canvas.create_polygon(pts, fill='blue')

    pts = triangle_inflated(200, 50, 460, 125, angle=0, dist = distance )   # Inflated triangle
    squircles(canvas, pts, cr*2.5, fill='orange')

    pts = triangle(200,50, 460, 125)  # original triangle
    canvas.create_polygon(pts, fill='blue')


    pts = points(start)
    canvas.create_oval(pts, fill='green')
    pts = points(goal)
    canvas.create_oval(pts, fill='green')
    return root, canvas

if __name__ == "__main__":
    main()
