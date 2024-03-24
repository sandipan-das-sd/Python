from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        else:
            print("Queue is empty")
            return None

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            print("Queue is empty")
            return None

    def size(self):
        return len(self.queue)

# Example usage:
queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Queue size:", queue.size())  # Output: 3
print("Front element:", queue.peek())  # Output: 1

print("Dequeueing elements:")
while not queue.is_empty():
    print(queue.dequeue())  # Output: 1, 2, 3
