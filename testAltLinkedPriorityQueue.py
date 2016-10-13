"""
File: queue2.py

Circular-Array Queue implementation
"""

from arrays import Array
from queue import AltLinkedPriorityQueue

def testQueue():
    queue = AltLinkedPriorityQueue()
    while True:
        print "Test Queue Menu:"
        print "1 - Enqueue"
        print "2 - Dequeue"
        print "3 - Peek"
        print "4 - len()"
        print "5 - isEmpty"
        print "6 - str"
        print "7 - exit testing"
        response = raw_input("Choice (1 - 6)? ")
        if response == '1':
            item = raw_input("Enter the new item to enqueue")
            queue.enqueue(item)
        elif response == '2':
            if len(queue) >= 1:
                item = queue.dequeue()
                print "The item dequeued was:",item
            else:
                print "Cannot dequeue from an empty queue!"
        elif response == '3':
            if len(queue) >= 1:
                item = queue.peek()
                print "The fron item in the queue is:",item
            else:
                print "Cannot peek at an empty queue!"
        elif response == '4':
            print "The number of elements in the queue is",len(queue)
        elif response == '5':
            print "queue.isEmpty() ==",queue.isEmpty()
        elif response == '6':
            print "The queueu is:",str(queue)
        elif response == '7':
            break
        else:
            print "Invalid Menu Choice!"         

testQueue()