import rubik
from collections import deque

def positions_at_level(level):
    """
    Using BFS, returns the number of cube configurations that are
    exactly a given number of levels away from the starting position
    (rubik.I), using the rubik.quarter_twists move set.
    """

    # Angel Avelar-Bonilla
    # Collaborators: Ryan, Karen, Paige
    # PSET4, Problem 3a

    current_config = rubik.I    # starting position
    visited_configs = {}  # used to keep track of visited configs and their level
    queue = deque()  # queue for BFS

    visited_configs[current_config] = 0  # add current config to visited configs along with its level
    queue.append(current_config)  # add current config to queue

    while len(queue) > 0:
        current_config = queue.popleft()  # dequeue config

        for move in rubik.quarter_twists:  # trying every quarter twist move
            next_config = rubik.perm_apply(move, current_config)  # applying the move, it is now next config
            config_level = visited_configs[current_config] + 1  # the level of our next config
            if next_config not in visited_configs and config_level <= level:  # making sure our next config is unvisited
                visited_configs[next_config] = config_level  # marking config as visited, tracking its level
                queue.append(next_config)  # queue up next_config, it becomes our current_config when it gets popped

    count = 0  # count of configs we will return
    for lvl in visited_configs.values():  # going thru the levels of each visited config
        if lvl == level:  # if the level matches consider it in our count
            count += 1

    return count
