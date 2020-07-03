import random
import collections


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.index_to_val = {}
        self.val_to_index = {}
        self.current_index = 0
        self.indexes = set()
        self.removed_indexes = collections.deque([])

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.val_to_index:
            if len(self.removed_indexes) != 0:
                index = self.removed_indexes.popleft()
                self.indexes.add(index)
                self.val_to_index.update({val: index})
                self.index_to_val.update({index: val})
            else:
                self.val_to_index.update({val: self.current_index})
                self.index_to_val.update({self.current_index: val})
                self.indexes.add(self.current_index)
                self.current_index += 1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.val_to_index:
            index = self.val_to_index.pop(val)
            self.index_to_val.pop(index)
            self.removed_indexes.append(index)
            self.indexes.remove(index)
            return True
        else:
            return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.index_to_val[random.sample(self.indexes, 1)[0]]


if __name__ == "__main__":
    a = RandomizedSet()
    for command in [a.remove(1), a.insert(1), a.insert(2), a.getRandom()]:
        print(command)
