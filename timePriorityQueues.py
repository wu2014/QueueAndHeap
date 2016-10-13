# timePriorityQueues.py
# Tests the list implementations using two stack implementations based on lists.
# See if we can infer the list implementation.

import queue
import priorityqueue
from os import times
import random

numberOfItems = 10000
myPriorityQueue = queue.LinkedPriorityQueue()
start = times()
print "TIMING LINKED PRIORITY QUEUE"
for i in xrange(numberOfItems):
    item = random.randint(1,numberOfItems)
    myPriorityQueue.enqueue(item)
#end for
end = times()
userTime = end[0] - start[0]
systemTime = end[1] - start[1]
totalTime = userTime + systemTime
print "Time to enqueue", numberOfItems, "items: total =", totalTime, \
      "user =", userTime, "system =", systemTime

start = times()
for i in xrange(numberOfItems):
    value = myPriorityQueue.dequeue()
#end for
end = times()
userTime = end[0] - start[0]
systemTime = end[1] - start[1]
totalTime = userTime + systemTime
print "Time to dequeue", numberOfItems, "items: total =", totalTime, \
      "user =", userTime, "system =", systemTime

print "="*35

myPriorityQueue = priorityqueue.HeapPriorityQueue()
start = times()
print "TIMING HEAP PRIORITY QUEUE"
for i in xrange(numberOfItems):
    item = random.randint(1,numberOfItems)
    myPriorityQueue.enqueue(item)
#end for
end = times()
userTime = end[0] - start[0]
systemTime = end[1] - start[1]
totalTime = userTime + systemTime
print "Time to enqueue", numberOfItems, "items: total =", totalTime, \
      "user =", userTime, "system =", systemTime

start = times()
for i in xrange(numberOfItems):
    value = myPriorityQueue.dequeue()
#end for
end = times()
userTime = end[0] - start[0]
systemTime = end[1] - start[1]
totalTime = userTime + systemTime
print "Time to dequeue", numberOfItems, "items: total =", totalTime, \
      "user =", userTime, "system =", systemTime

print "="*35
