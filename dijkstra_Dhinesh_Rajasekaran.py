import time
import numpy as np
from visualization import visualization
import cv2


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



                
# p2 = action_set()
# class dijkstra_algo():
#     def __init__(self):
    
#     def check_if_obstacle(self, node):
#         return True
#         return False

#     def check_if_goal_node(self, node):
#         return True
#         return False
    
#     def graph_search(self, start_node, goal_node):
#         path = []

#         return path

#     def backtrack(self):
#         return path #start to goal
    



    
p1 = visualization()
# p3 = dijkstra_algo()
def main():
    start_time = time.time()

    image = p1.map_half_plane()
    image = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
    cv2.imshow("Map", image)
    cv2.waitKey(0)

    print("Enter Start Node: ")
    start_x, start_y = input().split(',')
    start_node = (int(start_x.strip()), int(start_y.strip()))


    print("Enter Goal Node: ")
    goal_x, goal_y = input().split(',')
    goal_node = (int(goal_x.strip()), int(goal_y.strip()))

    # if p3.check_if_obstacle(start_node):
    #     print("\nInvalid Start Node.. Re-Enter the Start node: ")
    #     start_node = input()

    # if p3.check_if_obstacle(goal_node):
    #     print("\nInvalid Goal Node.. Re-Enter the Goal node: ")
    #     goal_node = input()
        
    # path = p3.graph_search(start_node, goal_node)



    end_time = time.time()
    processing_time = end_time - start_time
    print("\nTime taken to find Optimal Path: ", processing_time)

    



if __name__ == '__main__':
    main()