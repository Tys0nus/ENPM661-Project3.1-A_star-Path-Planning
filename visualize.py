import numpy as np
import tkinter as tk

def triangle(base, height, xc,yc, angle=0):

    x1, y1 = xc+height, yc
    x2, y2 = xc, yc + base/2
    x3, y3 = xc, yc - base/2
    pts = [x1, y1, x2, y2, x3, y3]
    canvas.create_polygon(pts, fill='blue')
    return pts

def polygon(sides, length, xc, yc,orient=np.pi/2):
    n = sides
    theta = 2*np.pi/n
    p = length*0.5/np.sin(theta/2)
    pts = []
    for i in range(n):
        x = xc + p*np.cos(theta*i + orient)
        pts.append(x)
        y = yc + p*np.sin(theta*i + orient)
        pts.append(y)
    canvas.create_polygon(pts, fill='blue')
    return pts


root = tk.Tk()

wd = 600
ht = 250
canvas = tk.Canvas(root, width=wd, height=ht)
canvas.pack()

rect_obs1 = [100, 100, 100, 0, 150, 0, 150, 100]
rect_obs2 = [100, 250, 100, 150, 150, 150, 150, 250]

canvas.create_polygon(rect_obs1, fill='blue')
canvas.create_polygon(rect_obs2, fill='blue')
tri_obs = triangle(200,50, 460, 125)
hex_obs = polygon(6, 75, 300, 125)

root.mainloop()



    
