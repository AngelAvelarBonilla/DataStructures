import heap_id
import math

# Angel Avelar-Bonilla


'''
    Returns a node by city and state
'''
def node_by_name(nodes, city, state):
    for node in nodes:  # goes thru every node
        if node.state == state and city in node.description:  # if state matches and city is in desc
            return node

'''
    Returns the distance between two nodes using pythagorean theorem
'''
def distance(node1, node2):
    a = node1.longitude - node2.longitude
    b = node1.latitude - node2.latitude
    c = math.sqrt(pow(a, 2) + pow(b, 2)) # c = sqrt(a^2 + b^2)
    return c

'''
    Single source single target Djikstra,
    Returns a list of nodes representing the path from s to t
'''
def shortest_path(nodes, edges, weight, s, t):
    G = {}  # Our graph representation, key: node, value: adj nodes
    D = {}  # Our distance table, key: node, value: estimated shortest path length
    for node in nodes:
        G[node] = []
        D[node] = math.inf # set all distance estimates to infinity
    for link in edges:  # store all adjacent nodes in dict[node]
        G[link.begin].append(link.end) # edges are undirected so we must store both
        G[link.end].append(link.begin)  # nodes in eachother's adjacency list

    D[s] = 0  # distance from source is 0

    queue = heap_id.heap_id()  # min heap
    Q = {queue.insert(0): s}  # Q keeps track of which id in the queue belongs to which node

    S = [s]  # list of nodes whose minimum cost has already been found

    pi = {s: -1}  # tracks our predecessors, key: node, value: previous node

    while queue.heapsize > 0 and t not in S:  # while we have nodes in the queue and t hasn't been visited
        min_with_id = queue.extract_min_with_id()  # extract smallest est distance from queue
        u = Q[min_with_id[1]]  # use extracted id to access corresponding node

        for adj_node in G[u]:  # for each adjacent node
            v = adj_node
            dist = weight(u, v)  # get weight of edge between u, v

            if D[u] + dist < D[v] and v not in S: # RELAX
                D[v] = D[u] + dist
                pi[v] = u  # store u as predecessor to v
                Q[queue.insert(D[v])] = v  # queue up v

        S.append(u)  # add u to visited nodes

    shortest_path = [t]  # our shortest path begins with t, we will reverse this later
    while pi[shortest_path[-1]] != -1:  # while our predecessor is not -1
        shortest_path.append(pi[shortest_path[-1]])  # add predecessor of latest node in list

    shortest_path.reverse()  # reverse our path since we started with t
    return shortest_path
