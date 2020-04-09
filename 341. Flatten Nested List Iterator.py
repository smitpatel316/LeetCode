class NestedIterator:
    def __init__(self, nestedList):
        self.nested_list = nestedList
        self.index = 0
        self.flatten_list = []
        self.flatten(self.nested_list)
        self.length = len(self.flatten_list)

    def next(self) -> int:
        if self.hasNext():
            self.index += 1
            return self.flatten_list[self.index - 1]

    def hasNext(self) -> bool:
        return self.index < self.length

    def flatten(self, nested_list):
        for nested_item in nested_list:
            if nested_item.isInteger():
                self.flatten_list.append(nested_item.getInteger())
            else:
                self.flatten(nested_item.getList())
