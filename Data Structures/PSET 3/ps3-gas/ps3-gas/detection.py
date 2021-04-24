import math

def detect_collisions(balls):
    """ 
    Detect any pairs of balls that are colliding.
    Returns a set of ball_pairs.
    """

    # Angel Avelar-Bonilla
    # PSET 3, Problem 2(c)


    def compare_ball_with_bin(b1, bin2balls):
        """
        Compares a ball (b1) every ball of another bin (bin2balls)
        To see if they are colliding
        """
        for b2 in bin2balls:    # For every ball in the bin
            # if they are colliding and we have not already handled this pair
            if gas.colliding(b1, b2) and (b1, b2) not in handled_pairs and (b2, b1) not in handled_pairs:
                set_of_collisions.add(gas.ball_pair(b1, b2))  # add it to our set of collisions
                handled_pairs.add((b1, b2))  # add it to our set of already handled pairs

    set_of_collisions = set()

    bins_dict = dict()  # a dictionary using tuples (x, y) as keys to represent our 'grid' of bins
    for ball in balls:  # for each ball in our set of balls
        x_coord = int(ball.x // 256)    # the x of our tuple
        y_coord = int(ball.y // 256)    # the y of our tuple
        if (x_coord, y_coord) in bins_dict:  # if the tuple is already a key in our dict
            bins_dict[(x_coord, y_coord)].append(ball)  # add the ball to our list of balls in the bin
        else:
            bins_dict[(x_coord, y_coord)] = []  # create an empty list as the value
            bins_dict[(x_coord, y_coord)].append(ball)  # add the ball to our list of balls in the bin

    handled_pairs = set()  # create

    for bin_x, bin_y in bins_dict:  # for each x and y coordinate in each tuple
        bin1balls = bins_dict[(bin_x, bin_y)]  # bin 1 = dict[x, y]
        for b1 in bin1balls:  # for each ball in the bin

            if len(bin1balls) > 1:  # if we have more than 1 ball in the same bin
                for b2 in bin1balls:  # go thru every ball in the bin
                    # using the hash of both balls to make sure they are not the same ball
                    # and if they are colliding and we have not already handled this pair
                    if b1.__hash__() != b2.__hash__() and gas.colliding(b1, b2) and (b1, b2) not in handled_pairs and (b2, b1) not in handled_pairs:
                        set_of_collisions.add(gas.ball_pair(b1, b2))  # add it to our set of collisions
                        handled_pairs.add((b1, b2))  # add it to our set of already handled pairs
            # check if a bin exists ABOVE
            if (bin_x, bin_y + 1) in bins_dict:
                bin2balls = bins_dict[(bin_x, bin_y + 1)]
                compare_ball_with_bin(b1, bin2balls)
            # check if a bin exists BELOW
            if (bin_x, bin_y - 1) in bins_dict:
                bin2balls = bins_dict[(bin_x, bin_y - 1)]
                compare_ball_with_bin(b1, bin2balls)
            # check if a bin exists RIGHT
            if (bin_x + 1, bin_y) in bins_dict:
                bin2balls = bins_dict[(bin_x + 1, bin_y)]
                compare_ball_with_bin(b1, bin2balls)
            # check if a bin exists LEFT
            if (bin_x - 1, bin_y) in bins_dict:
                bin2balls = bins_dict[(bin_x - 1, bin_y)]
                compare_ball_with_bin(b1, bin2balls)
            # check if a bin exists ABOVE RIGHT
            if (bin_x + 1, bin_y + 1) in bins_dict:
                bin2balls = bins_dict[(bin_x + 1, bin_y + 1)]
                compare_ball_with_bin(b1, bin2balls)
            # check if a bin exists ABOVE LEFT
            if (bin_x - 1, bin_y + 1) in bins_dict:
                bin2balls = bins_dict[(bin_x - 1, bin_y + 1)]
                compare_ball_with_bin(b1, bin2balls)
            # check if a bin exists BELOW RIGHT
            if (bin_x + 1, bin_y - 1) in bins_dict:
                bin2balls = bins_dict[(bin_x + 1, bin_y - 1)]
                compare_ball_with_bin(b1, bin2balls)
            # check if a bin exists BELOW LEFT
            if (bin_x - 1, bin_y - 1) in bins_dict:
                bin2balls = bins_dict[(bin_x - 1, bin_y - 1)]
                compare_ball_with_bin(b1, bin2balls)

    return set_of_collisions

import gas

