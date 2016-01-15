"""
prioqueue.py
author: Vinay More
"""
class Node:

    __slots__ = "value", "link"

    def __init__( self, value, link = None ):
        """ Creating new node.
            param value: value to be stored in the new node
            param link: the node linked
        """
        self.value = value
        self.link = link

    def __str__( self ):
        """ Return a string representation of the contents of this node.
        """
        return str( self.value )

class PriorityQueue():

    __slots__ = "front", "back","after"

    def __init__(self,after):
        """ Initialize a new empty priority queue.
            param after: an ordering function. See definition of dequeue method.
            return: None (constructor)
        """
        self.after=after
        self.front = None
        self.back = None

    def __str__( self ):
        """ Return a string representation of the contents of this queue, front value first.
        """
        result = "Queue["
        p = self.front
        while p != None:
            result += " " + str( p.value )
            p = p.link
        result += " ]"
        return result

    def isEmpty( self ):
        """ return: True iff there are no elements in the queue.
        """
        return self.front == None

    def enqueue( self, newValue ):
        """ Enter a new value into the queue.
            param newValue: the value to be entered into the queue
            return: None
        """
        newNode = Node( newValue )
        if self.front == None:
            self.front = newNode
        else:
            self.back.link = newNode
        self.back = newNode

    insert = enqueue

    def dequeue( self ):
        """ Remove one of the values v from the queue such that, for all values u in the queue, after(v,u) is False.
            If more than one value satisfies the requirement, the value chosen should be the one that has been in the queue the longest.
            :pre: not isEmpty()
            return: None
        """
        if self.isEmpty():
            print("Empty queue")
        else:
            self.front = self.front.link
            if self.front == None:
                self.back = None

    remove = dequeue

    def peek( self ):
        """ Find in the queue the value that would be removed were the dequeue method to be called at this time.
            :pre: not isEmpty()
            :return: the value described above
        """
        if self.isEmpty():
            "Empty queue"
        else:
            np =self.front
            nv= np
            while np!=None:
                nv=self.front
                nvr=nv.link
                while nvr != None:
                    if self.after(nv.value,nvr.value):
                        tmp=np.value
                        np.value=nv.value
                        nv.value=tmp
                    nvr=nvr.link
                np=np.link
            return self.front.value

def afterFunction(v,u):
        """ Method to determine v object should be removed before u object or not.
        return: true if value v should be removed after u otherwise false
        """
        return v > u

def test():
    """ Main Function """
    q = PriorityQueue(afterFunction)
    print( q )
    for value in 3, 1,2, 3,4,3,:
        q.enqueue( value )
        print( q )
    for value in 17, 20,15,2:
        q.insert( value )
        print( q )
    print( "Removing:", q.peek())
    q.remove()
    print( q )
    while not q.isEmpty():
        print( "Dequeueing:", q.peek())
        q.dequeue()
        print( q )
    try:
        q.dequeue()
    except Exception as e:
        print(str( e ))

if __name__ == "__main__":
    test()
