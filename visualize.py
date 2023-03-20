import numpy as np
import tkinter as tk
import math

clearance = int(input("Please give the clearance for the obstacles:"))
radius = int(input("Please give the radius of the robot:"))

def triangle(base, height, xc,yc, angle=0):

    x1, y1 = xc+height, yc
    x2, y2 = xc, yc + base/2
    x3, y3 = xc, yc - base/2
    pts = [x1, y1, x2, y2, x3, y3]
    canvas.create_polygon(pts, fill='blue')
    return pts

def triangle_inflated(base, height, xc, yc, angle=0, dist=0):

    x1, y1 = xc + height + dist, yc
    x2, y2 = xc - dist, yc + base/2 + 3*dist
    x3, y3 = xc - dist, yc - base/2 - 3*dist
    pts = [x1, y1, x2, y2, x3, y3]
    canvas.create_polygon(pts, fill='red')
    return pts


def polygon_original(sides, length, xc, yc,orient=np.pi/2):
    n = sides
    theta = 2*np.pi/n
    p = length*0.5/np.sin(theta/2)
    pts = []
    for i in range(n):
        x = xc + p*np.cos(theta*i + orient)
        pts.append(x)
        y = yc + p*np.sin(theta*i + orient)
        pts.append(y)
    canvas.create_polygon(pts, fill="blue")
    return pts, p

def polygon_inflated(sides, length, xc, yc,orient=np.pi/2):
    n = sides
    theta = 2*np.pi/n
    p = length*0.5/np.sin(theta/2)
    pts = []
    for i in range(n):
        x = xc + p*np.cos(theta*i + orient)
        pts.append(x)
        y = yc + p*np.sin(theta*i + orient)
        pts.append(y)
    canvas.create_polygon(pts, fill="red")
    return pts, p

root = tk.Tk()

wd = 600
ht = 250
canvas = tk.Canvas(root, width=wd, height=ht)
canvas.pack()

# clearance = 5
# radius = 5
distance = clearance + radius
rect_obs1_c = [100 - distance, 100 + distance, 100 - distance, 0 - distance, 150 + distance, 0 - distance, 150 + distance, 100 + distance]
rect_obs2_c = [100 - distance, 250 + distance, 100 - distance, 150 - distance, 150 + distance, 150 - distance, 150 + distance, 250 + distance]
rect_obs2 = [100, 250, 100, 150, 150, 150, 150, 250]
rect_obs1 = [100 , 100 , 100 , 0 , 150 , 0 , 150 , 100 ]

canvas.create_polygon(rect_obs1_c, fill='red')
canvas.create_polygon(rect_obs1, fill='blue')
canvas.create_polygon(rect_obs2_c, fill='red')
canvas.create_polygon(rect_obs2, fill='blue')
tri_obs_inflated = triangle_inflated(200, 50, 460, 125, angle=0, dist = distance )
tri_obs = triangle(200,50, 460, 125)
# hex_obs = polygon_new(6, 75, 300, 125)


_, p = polygon_original(6, 75, 300, 125)  # original hexagon
length = ((distance + p)/p)*75
_, p0 = polygon_inflated(6, length, 300, 125)  # inlated hexagon

_, p = polygon_original(6, 75, 300, 125)  # original hexagon

root.mainloop()



    
 