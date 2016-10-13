"""
File: priorityqueue.py

A heap-based priority queue.
"""

from heap import ArrayHeap


class HeapPriorityQueue(ArrayHeap):
    """Heap-based implementation of a priority queue."""

    def __init__(self):
        ArrayHeap.__init__(self)

    def enqueue(self, item):
        self.add(item)

    def dequeue(self):
        return self.pop()

    def __str__(self):
        result = ""
        for item in self:
            result += str(item) + " "
        return result

    
def main():
    # Test any implementation with same code
    q = HeapPriorityQueue()
    #q = LinkedQueue()
    print "Length:", len(q)
    print "Empty:", q.isEmpty()
    print "Enqueue 1-10"
    for i in xrange(10):
        q.enqueue(i + 1)
    print "Peeking:", q.peek()
    print "Items (front to rear):",  q
    print "Length:", len(q)
    print "Empty:", q.isEmpty()
    print "Enqueue 0"
    q.enqueue(0)
    print "Dequeuing items (front to rear):",
    while not q.isEmpty(): print q.dequeue(),
    print "\nLength:", len(q)
    print "Empty:", q.isEmpty()

