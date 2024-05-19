class SortedQueue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        if self.is_empty():
            self.items.append(item)
        else:
            inserted = False
            for index, current in enumerate(self.items):
                if item.num_id < current.num_id:
                    self.items.insert(index, item)
                    inserted = True
                    break
            if not inserted:
                self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def search(self, numid):
        for item in self.items:
            if item.num_id == numid:
                return item
        return None

    def delete(self, numid):
        for index, item in enumerate(self.items):
            if item.num_id == numid:
                return self.items.pop(index)
        return None

    def __repr__(self):
        return repr(self.items)
