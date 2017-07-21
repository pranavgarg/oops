class MaxSizeList(object):
    def __init__(self, limit):
        self.innerlist = []
        self.max_size = limit

    def get_list(self):
        return self.innerlist

    def push(self, value):
        if self.max_size <= len(self.innerlist):
            self.innerlist.pop(0)
        self.innerlist.append(value)
