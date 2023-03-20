import visualize as vis
import a_star_ankur_aditya as astr

if __name__ == "__main__":
    print("-----------------------")
    print("Path Planning: A star") 
    print("-----------------------")
    x, y, th = [int(x) for x in input("Enter the Start Coordinates: ").split()] 
    
    if not (0 <= x < 600) or not (0 <= y < 250) or not (th in [0, 30, -30, 60, -60]):
        raise ValueError("Start coordinates are not acceptable")
    
    y = 250 - y

    start = (x,y, th)

    x, y, th = [int(x) for x in input("Enter the Goal Coordinates: ").split()] 
    if not (0 <= x < 600) or not (0 <= y < 250) or not (th in [0, 30, -30, 60, -60]):
        raise ValueError("Goal coordinates are not acceptable")
    
    y = 250 - y
    goal = (x,y, th)

    root, canvas = vis.main(start,goal)
    astr.main(root, canvas, start,goal)

    root.mainloop()

