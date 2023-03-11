import time
import os



class action_set():
    def __init__(self):
        print("8 Action Set: UP, DOWN, LEFT, RIGHT, Top_Right, Top_Left, Bottom_Right, Bottom_Left")

    #Actions Set = {(1,0), (-1,0), (0,1), (0,-1), (1,1), (-1,1), (1,-1), (-1,-1)}
    def up(self, node): #(0,1)
        node_op = (node[0], node[1]+1)
        return node_op

    def down(self, node): #(0,-1)
        node_op = (node[0], node[1]-1)
        return node_op

    def left(self, node): #(-1,0)
        node_op = (node[0]-1, node[1])
        return node_op

    def right(self, node): #(1,0)
        node_op = (node[0]+1, node[1])
        return node_op

    def up_right(self, node): #(1,1)
        node_op = (node[0]+1, node[1]+1)
        return node_op

    def up_left(self, node): #(-1,1)
        node_op = (node[0]-1, node[1]+1)
        return node_op

    def down_right(self, node): #(1,-1)
        node_op = (node[0]+1, node[1]-1)
        return node_op

    def down_left(self, node): #(-1,-1)
        node_op = (node[0]-1, node[1]-1)
        return node_op


p1 = action_set()
class dijkstra_algo():
    def __init__(self):
    
    def check_if_obstacle(self, node):
        return 1
        return 0

    def check_if_goal_node(self, node):
        return True
        return False
    
    def graph_search(self):

    def backtrack(self):
        return path #start to goal
    

class visualization():
    def __init__(self):

    def GUI_opencv(self): #node exploration & optimal path

    

p2 = dijkstra_algo()
p3 = visualization()
def main():
    start_time = time.time()

    print("Enter Start Node: ")
    start_node = input()

    print("Enter Goal Node: ")
    goal_node = input()

    if p2.check_if_obstacle(start_node):
        print("\nInvalid Start Node.. Re-Enter the Start node: ")

    if p2.check_if_obstacle(goal_node):
        print("\nInvalid Goal Node.. Re-Enter the Goal node: ")
        


    end_time = time.time()
    processing_time = end_time - start_time
    print("\nTime taken to find Optimal Path: ", processing_time)

    



if __name__ == '__main__':
    main()