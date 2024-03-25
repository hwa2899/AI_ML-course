# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 16:45:14 2019

@author: Ching
"""
class Problem():
    def __init__(self,init,goal):
        self.init = init
        self.goal = goal
    def goal_test(self, state):
        if state == self.goal:
            return True
        else:
            return False
    def find_zero(self, state):
        for i in range(9):
            if state[i] == 0:
                return i 
    def actions(self, state):
        acts = ['up', 'down', 'left', 'right']
        i = self.find_zero(state)
        if i < 3:
            acts.remove('up')
        if i > 5:
            acts.remove('down')
        if i%3 == 0:
            acts.remove('left')
        if i%3 == 2:
            acts.remove('right')
        return acts
            
class Node():
    def __init__(self, state, parent, action, cost):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.next = None

def Solution(node, statelist, actslist):
    if node.parent == None:
        statelist.append(node.state)
    else:
        Solution(node.parent, statelist, actslist)
        statelist.append(node.state)
        actslist.append(node.action)

def childnode(problem, node, action):
    new = []
    for i in range(len(node.state)):
        new.append(node.state[i])
    n_node = Node(new, node, action, node.cost+1)
    zero = problem.find_zero(node.state)
    if action == 'up':
        n_node.state[zero], n_node.state[zero-3] = n_node.state[zero-3], n_node.state[zero]
    elif action == 'down':
        n_node.state[zero], n_node.state[zero+3] = n_node.state[zero+3], n_node.state[zero]
    elif action == 'right':
        n_node.state[zero], n_node.state[zero+1] = n_node.state[zero+1], n_node.state[zero]
    elif action == 'left':
        n_node.state[zero], n_node.state[zero-1] = n_node.state[zero-1], n_node.state[zero]
    return n_node
#-------------------------------------------------------------

def BFS(problem, r_state, r_action):
    node = Node(problem.init, None, None, 0)
    if problem.goal_test(node.state):
        return Solution(node, r_state, r_action)
    frontier = [node]
    explored = []
    while True:
        if frontier == []:
            return False
        node = frontier[0]
        frontier.remove(frontier[0])
        explored.append(node.state)
        explored.sort()
        for action in problem.actions(node.state):
            child = childnode(problem, node, action)
            if child.state not in explored:
                not_in_frontier = True
                for i in range(len(frontier)):
                    if child.state == frontier[i].state:
                        not_in_frontier = False
                        break
                if not_in_frontier:
                    if problem.goal_test(child.state):
                        return Solution(child, r_state, r_action)
                    frontier.append(child)

#-------------------------------------------------------------

def UCS(problem, r_state, r_action):
    node = Node(problem.init, None, None, 0)
    frontier = [node]
    cost = [node.cost]
    explored = []
    while True:
        if frontier == []:
            return False
        node = frontier[0]
        frontier.remove(frontier[0])
        cost.remove(cost[0])
        if problem.goal_test(node.state):
            return Solution(node,r_state,r_action)
        
        explored.append(node.state)
        explored.sort()
        for action in problem.actions(node.state):
            child = childnode(problem, node, action)
            if child.state not in explored:
                not_in_frontier = True
                for i in range(len(frontier)):
                    if child.state == frontier[i].state:
                        not_in_frontier = False
                        if child.cost < cost[i]:
                            frontier[i] = child
                            cost[i] = child.cost
                        break
                if not_in_frontier:
                    if frontier == []:
                        frontier.append(child)
                        cost.append(child.cost)
                    else:
                        for i in range(len(frontier)):
                            if child.cost < cost[i]:
                                frontier.insert(i,child)
                                cost.insert(i,child.cost)
                                break
                            elif i == len(frontier)-1 :
                                frontier.append(child)
                                cost.append(child.cost)
                                
#-------------------------------------------------------------

def DFS(problem, r_state, r_action):
    node = Node(problem.init, None, None, 0)
    for deep in range(50):
        result = RDLS(node, problem, r_state, r_action, deep)
        if result != "cutoff":
            return "found"
    
def RDLS(node, problem, r_state, r_action, limit):
    if problem.goal_test(node.state):
        return Solution(node, r_state, r_action)
    elif limit == 0:
        return "cutoff"
    else:
        cutoff = False
        for action in problem.actions(node.state):
            child = childnode(problem, node, action)
            result = RDLS(child, problem, r_state, r_action, limit-1)
            if result == "cutoff" :
                cutoff = True
            elif result != "failure":
                return "found"
        if cutoff:
            return "cutoff" 
        else:
            return "failure"
    
#-------------------------------------------------------------
# Main
init = [int(e) for e in input("請輸入初始狀態 (如:7 2 4 5 0 6 8 3 1): ").split()]
goal = [0, 1, 2, 3, 4, 5, 6, 7, 8]
r_state = []
r_action = []

algorithm = input("請輸入 1寬度優先 或 2成本一致 或 3深度優先: ")

problem = Problem(init, goal)
if algorithm == '1':
    BFS(problem, r_state, r_action)
elif algorithm == '2':
    UCS(problem, r_state, r_action)
else:
    DFS(problem, r_state, r_action)
    
if r_state == []:
    print("Fail")
else:
    for i in range(len(r_action)):
        for j in range(3):
            print(r_state[i][0 + 3 * j], 
                  r_state[i][1 + 3 * j], 
                  r_state[i][2 + 3 * j])        
        print("Move:",r_action[i])
    for i in range(3):
        print(goal[0 + 3 * i], 
              goal[1 + 3 * i], 
              goal[2 + 3 * i]) 
