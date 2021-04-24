from heap import *
#  Angel Avelar-Bonilla
#  PSET 3 Problem 1
class heap_delete(heap):
    def delete(self, i):

        self.A[i] = self.A[self.heapsize]  # move index at end of heap up so that it does not get deleted
                                           # also replacing element at index i
        self.heapsize -= 1  # decrement list size, effectively 'disconnecting' the last element from the heap
        self.A.pop()  # delete element at last index of heap
        self.min_heapify(i)  # heapify at index i since the rest of the list should still be a valid min heap

        return None

