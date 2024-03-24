class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.front = new_node
        else:
            self.rear.next = new_node
        self.rear = new_node
        self.rear.next = self.front

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        elif self.front == self.rear:
            temp = self.front
            self.front = None
            self.rear = None
            return temp.data
        else:
            temp = self.front
            self.front = self.front.next
            self.rear.next = self.front
            return temp.data

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        temp = self.front
        while temp.next != self.front:
            print(temp.data, end=" ")
            temp = temp.next
        print(temp.data)

# Example usage:
cq = CircularQueue()

cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)

print("Queue elements:")
cq.display()  # Output: 1 2 3

print("Dequeueing elements:")
print(cq.dequeue())  # Output: 1
print(cq.dequeue())  # Output: 2

print("Queue elements after dequeue:")
cq.display()  # Output: 3
