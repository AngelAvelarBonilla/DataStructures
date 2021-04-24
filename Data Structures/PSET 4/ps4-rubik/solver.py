import rubik
from collections import deque

def shortest_path(start, end):
    """
    Using 2-way BFS, finds the shortest path from start_position to
    end_position. Returns a list of moves. 
    Assumes the rubik.quarter_twists move set.
    """

    # Angel Avelar-Bonilla
    # Collaborators: Ryan, Karen, Paige
    # PSET4, Problem 3b

    # dictionaries with state of cube as key and moves it took to get to state as values
    fParents = {}
    bParents = {}
    # state of cube going forward/backward
    fState = start
    bState = end
    # initial states of the cubes going forward/backwards
    fParents[fState] = []
    bParents[bState] = []
    # queue for walking forward/backward
    fQueue = deque()
    bQueue = deque()
    # adding our initial node/states to respective queues
    fQueue.append(fState)
    bQueue.append(bState)

    # catches when the cube is given solved
    if fState in bParents:
        return fParents[fState] + bParents[fState]

    while len(fQueue) > 0 and len(bQueue) > 0:
        # deque our cube states
        fState = fQueue.popleft()
        bState = bQueue.popleft()
        # for every quarter twist possible
        for move in rubik.quarter_twists:
            # apply the move to the current state, store it as "next state"
            next_fState = rubik.perm_apply(move, fState)
            # add the moves it took to get to previous state + move we just did
            fParents[next_fState] = fParents[fState] + [move]
            # if our next state already exists in our walking backward dictionary
            if next_fState in bParents:
                return fParents[next_fState] + bParents[next_fState]  # combine the move lists
            fQueue.append(next_fState)  # queue up next state
            # apply the INVERSE of the move to the current state, store it as "next state"
            #  important to apply inverse since we are walking backwards
            next_bState = rubik.perm_apply(rubik.perm_inverse(move), bState)
            # add the move we just did + previous moves, we add regular move not inverse since our final
            # move list will be walking forward
            bParents[next_bState] = [move] + bParents[bState]
            # if our next state already exists in our walking forward dictionary
            if next_bState in fParents:
                return fParents[next_bState] + bParents[next_bState] # combine move lists
            bQueue.append(next_bState)  # queue up next state
        # if a move list goes over 7 moves, we can say there is no solution since the bi-directional BFS
        # did not meet in the middle
        if len(fParents[fState]) >= 7 or len(bParents[bState]) >= 7:
            return None


