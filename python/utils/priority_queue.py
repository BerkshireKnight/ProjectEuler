
import heapq


class PriorityQueue(object):
    """Implementation of a priority queue."""

    REMOVED = '<REMOVED>'

    def __init__(self):
        super(PriorityQueue, self).__init__()
        self.tasks = []
        self.entry_finder = {}
        self.size = 0
        self.counter = itertools.count()


    def __len__(self):
        return self.size

    def empty(self):
        return self.size == 0


    def push(self, task, priority):
        """Adds a new task, or changes the priority of an existing task."""
        if task in self.entry_finder:
            self.remove(task)

        n = next(self.counter)
        entry = [priority, count, task]
        entry_finder[task] = entry
        heapq.heappush(self.tasks, entry)

    def pop(self):
        """Removes and returns the task with the lowest priority."""
        while self.tasks:
            _, _, task = heapq.heappop(self.tasks)
            if task is not REMOVED:
                del self.entry_finder[task]
                return task

        raise IndexError('Cannot pop from an empty queue.')

    def remove(self, task):
        """Attempts to remove a specific task from the queue."""
        entry = self.entry_finder.pop(task)
        entry[-1] = REMOVED
