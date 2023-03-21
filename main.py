import visualize as vis
import a_star_ankur_aditya as astr
import time

if __name__ == "__main__":
    start_time = time.time()
    print("-----------------------")
    print("Path Planning: A star") 
    print("-----------------------")
    x, y, th = [int(x) for x in input("Enter the Start Coordinates: ").split()] 
    
    if not (0 <= x < 600) or not (0 <= y < 250) or not (0 <= th < 360 and th % 30 == 0):
        raise ValueError("Start coordinates are not acceptable")
    
    y = 250 - y

    start = (x,y, th)

    x, y, th = [int(x) for x in input("Enter the Goal Coordinates: ").split()] 
    if not (0 <= x < 600) or not (0 <= y < 250) or not (0 <= th < 360 and th % 30 == 0):
        raise ValueError("Goal coordinates are not acceptable")
    
    y = 250 - y
    goal = (x,y, th)

    cl,rad = [int(x) for x in input("Enter the Clearance and Robot Radius: ").split()] 
    
    step = int(input("Enter step size for robot movement: "))
    if not (0 <= step <= 10):
        raise ValueError("Step Size is not acceptable")
    
    root, canvas = vis.main(start,goal,cl,rad)
    astr.main(root, canvas, start, goal, rad, step)

    end_time = time.time()
    runtime = end_time - start_time
    print("Runtime: {:.4f} seconds".format(runtime),"\n\n")
    root.mainloop()
