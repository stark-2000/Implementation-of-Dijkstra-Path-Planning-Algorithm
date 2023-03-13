from visualization import visualization
import heapq as hq
import time
import cv2


class action_set():
    def __init__(self):
        print("\n***************Point Robot Path Planning using Dijkstra Algorithm********************")
        print("\nRobot Action Set: UP, DOWN, LEFT, RIGHT, Top_Right, Top_Left, Bottom_Right, Bottom_Left")

    #Actions Set = {(1,0), (-1,0), (0,1), (0,-1), (1,1), (-1,1), (1,-1), (-1,-1)}
    def up(self, node): #(0,1) #Get the node in the up direction
        node_op = (node[0], node[1]+1)
        cost = 1
        return (cost, node_op)

    def down(self, node): #(0,-1) #Get the node in the down direction
        node_op = (node[0], node[1]-1)
        cost = 1
        return (cost, node_op)

    def left(self, node): #(-1,0) #Get the node in the left direction
        node_op = (node[0]-1, node[1])
        cost = 1
        return (cost, node_op)

    def right(self, node): #(1,0) #Get the node in the right direction
        node_op = (node[0]+1, node[1])
        cost = 1
        return (cost, node_op)

    def up_right(self, node): #(1,1) #Get the node in the up_right direction
        node_op = (node[0]+1, node[1]+1)
        cost = 1.414
        return (cost, node_op)

    def up_left(self, node): #(-1,1) #Get the node in the up_left direction
        node_op = (node[0]-1, node[1]+1)
        cost = 1.414
        return (cost, node_op)

    def down_right(self, node): #(1,-1) #Get the node in the down_right direction
        node_op = (node[0]+1, node[1]-1)
        cost = 1.414
        return (cost, node_op)

    def down_left(self, node): #(-1,-1) #Get the node in the down_left direction
        node_op = (node[0]-1, node[1]-1)
        cost = 1.414
        return (cost, node_op)


p1 = visualization()       
p2 = action_set()

class dijkstra_algo():
    def __init__(self):
        self.image = p1.map_half_plane() #get the map for the path planning and obstacle detection

    #check if the node is an obstacle
    def check_if_obstacle(self, node): 
        if (not(self.image[node[0], node[1]][0] == 0 and \
                self.image[node[0], node[1]][1] == 0 and \
                self.image[node[0], node[1]][2] == 0)): #if the node is not black
            return True
    
    #check if the node is the goal node
    def check_if_goal_node(self, node, goal_node): 
        if node == goal_node: 
            return True
        
    #check if the node is outside the map
    def check_if_outside_map(self, node): 
        if node[0] > 595 or node[1] > 245 or node[0] < 0 or node[1] < 0: #if the node is outside the map
            return True
    
    #check if the node is valid - combining the 2 functions above
    def validate_node(self, node): 
        if self.check_if_outside_map(node):
            return False
        elif self.check_if_obstacle(node):
            return False
        else:
            return True

    #Generate the list of nodes to be explored
    def generate_nodes(self, node):
        nodes = [] #list of nodes to be explored

        _node = p2.up(node) #get node from the action set up
        if self.validate_node(_node[1]): #if the node is valid
            nodes.append(_node) #append the node to the list of nodes
        
        _node = p2.down(node) #get node from the action set down
        if self.validate_node(_node[1]):
            nodes.append(_node) 
        
        _node = p2.left(node) #get node from the action set left
        if self.validate_node(_node[1]):
            nodes.append(_node)

        _node = p2.right(node) #get node from the action set right
        if self.validate_node(_node[1]):
            nodes.append(_node)

        _node = p2.up_right(node) #get node from the action set up_right
        if self.validate_node(_node[1]):
            nodes.append(_node)

        _node = p2.up_left(node) #get node from the action set up_left
        if self.validate_node(_node[1]):
            nodes.append(_node)

        _node = p2.down_right(node) #get node from the action set down_right
        if self.validate_node(_node[1]):
            nodes.append(_node)

        _node = p2.down_left(node) #get node from the action set down_left
        if self.validate_node(_node[1]):
            nodes.append(_node)

        return nodes #return the list of nodes to be explored
    
    #Graph search algorithm - Dijkstra
    def graph_search(self, start_node, goal_node):
        Q = [] #open_list
        explored_nodes = [] #list of visited nodes/ explored nodes
        Q_keys = {} #open_list_keys - stores the pixel values of the nodes in the open list
        Closed_keys = {} #closed_list_keys - stores the pixel values of the nodes in the closed list
        Parent_keys = {} #parent_list_keys - stores the pixel values of the nodes in the parent list

        d1 = (0, start_node, (0,0)) #cost, node, parent
        hq.heappush(Q, d1) #pushing the start node into the open list
        Q_keys[start_node] = None #adding the start node to the open list keys

        while len(Q) > 0: #while the open list is not empty
            d1 = hq.heappop(Q) #pop the node with the least cost from the open list
            del Q_keys[d1[1]] #delete the node from the open list keys

            cost = d1[0] #cost = d1[0]
            node = d1[1] #node = d1[1]
            parent = d1[2] #parent = d1[2]
            Closed_keys[node] = None #add the node to the closed list keys 
            Parent_keys[node] = parent #add the closed list nodes with their parents in a dictionary for backtracking


            if self.check_if_goal_node(node, goal_node): #if the node is the goal node
                return Parent_keys,explored_nodes #return the dict of the closed list nodes with their parents
            
            nodes = self.generate_nodes(node) #generate the nodes from the current node
            
            for i in range(len(nodes)): #for each node in the generated nodes
                explored_nodes.append(nodes[i][1])

                if nodes[i][1] not in Closed_keys: #if the node is not in the closed list - check if the node is in the closed list keys for faster search
                    if nodes[i][1] not in Q_keys: #if the node is not in the open list - check if the node is in the open list keys for faster search
                        _d1 = (cost + nodes[i][0], nodes[i][1], node) #cost = cost + nodes[i][0], node = nodes[i][1], parent = node
                        Q_keys[_d1[1]] = _d1 #add the node to the open list keys
                        hq.heappush(Q, Q_keys[_d1[1]]) #push the node into the open list
                        
                    elif nodes[i][1] in Q_keys: #if the node is in the open list
                        if Q_keys[nodes[i][1]][0] > cost + nodes[i][0]: #if the cost of the node in the open list is greater than the cost of the node in the generated nodes
                            Q_keys[nodes[i][1]] = (cost + nodes[i][0], nodes[i][1], node) #update the cost, node and parent of the node in the open list
                            hq.heapify(Q) #heapify the open list
                             
        return None
        
    #Backtrack from the goal node to the start node
    def backtrack(self, _Parent_keys, start_node, goal_node):
        backtrack_list = [] 
        backtrack_list.append(goal_node) #append the goal node to the backtrack list
        node = goal_node  #node = goal node - start backtracking from the goal node

        while (node is not start_node): #while the node is not the start node
            backtrack_list.append(_Parent_keys[node]) #append the parent of the node to the backtrack list
            node = _Parent_keys[node] #node = parent of the node
        
        backtrack_list.reverse() #reverse the backtrack list
        return backtrack_list
            
    
p3 = dijkstra_algo()
def main():
    #Getting start node from the user:
    print("\nEnter Start Node: ") 
    start_x, start_y = input().split(',')
    start_node = (int(start_x.strip()), int(start_y.strip()))
    
    while(p3.check_if_outside_map(start_node)): #check if the start node is outside the map
        print("\nStart Node is out of the Map.. Re-Enter the Start node: ")
        start_x, start_y = input().split(',')
        start_node = (int(start_x.strip()), int(start_y.strip()))

    while(p3.check_if_obstacle(start_node)): #check if the start node is on an obstacle
        print("\nStart Node on Obstacle.. Re-Enter the Start node: ")
        start_x, start_y = input().split(',')
        start_node = (int(start_x.strip()), int(start_y.strip()))
    
    
    #Getting goal node from the user:
    print("Enter Goal Node: ")
    goal_x, goal_y = input().split(',')
    goal_node = (int(goal_x.strip()), int(goal_y.strip()))

    while(p3.check_if_outside_map(goal_node)): #check if the goal node is outside the map
        print("\nGoal Node is out of the Map.. Re-Enter the Goal node: ")
        goal_x, goal_y = input().split(',')
        goal_node = (int(goal_x.strip()), int(goal_y.strip()))

    while(p3.check_if_obstacle(goal_node)): #check if the goal node is on an obstacle
        print("\nGoal Node on Obstacle.. Re-Enter the Goal node: ")
        goal_x, goal_y = input().split(',')
        goal_node = (int(goal_x.strip()), int(goal_y.strip()))
    
    
    #check if the start node and goal node are the same
    while(p3.check_if_goal_node(start_node, goal_node)):
        print("\nStart Node and Goal Node are same.. Re-Enter the Start node: ")
        start_x, start_y = input().split(',')
        start_node = (int(start_x.strip()), int(start_y.strip()))

        print("Re-Enter the Goal node: ")
        goal_x, goal_y = input().split(',')
        goal_node = (int(goal_x.strip()), int(goal_y.strip()))
    

    start_time = time.time() #start timer

    #Finding the optimal path - Invoking defined Dijkstra's Algorithm
    path_node_parent_dict = p3.graph_search(start_node = start_node, goal_node = goal_node) 

    if path_node_parent_dict[0] is not None: #if the path is found
        print("Path Found :)")
        final_path = p3.backtrack(path_node_parent_dict[0], start_node, goal_node) #Calling backdrop function to get the optimal path

    elif path_node_parent_dict is None: #if the path is not found
        print("Path Not Found :(")

    end_time = time.time() #end timer
    processing_time = end_time - start_time
    print("\nTime taken to find Optimal Path: ", processing_time)

    #Plotting the explored nodes on the map - Green
    for i in range(len(path_node_parent_dict[1])): #path_node_parent_dict[1] = explored nodes
        p1.highLight_node(path_node_parent_dict[1][i], (102,255,178)) #plot the explored nodes on the map
        op_image = cv2.rotate(p1.image, cv2.ROTATE_90_COUNTERCLOCKWISE) #rotate the image
        if (i%800 == 0): #plot the image every 800 nodes
            cv2.imshow("Map with Shortest Path", op_image)
            cv2.waitKey(1) #wait for 1ms

    #Plotting the optimal path on the map - Blue
    for i in range(len(final_path)): #final_path = optimal path
        p1.highLight_node(final_path[i], (51,51,255)) #plot the optimal path on the map
        op_image = cv2.rotate(p1.image, cv2.ROTATE_90_COUNTERCLOCKWISE)
        cv2.imshow("Map with Shortest Path", op_image)

    #Plotting the movement of point robot on the map - Blue
    for i in range(len(final_path)): #final_path = optimal path
        plot = p1.highLight_position(final_path[i], (255,0,0)) #plot the movement of point robot on the map
        op_image = cv2.rotate(plot, cv2.ROTATE_90_COUNTERCLOCKWISE)
        cv2.imshow("Map with Shortest Path", op_image)
        cv2.waitKey(1) #wait for 1ms
        
        
    cv2.waitKey(0) #wait for any key to be pressed


if __name__ == '__main__':
    main()