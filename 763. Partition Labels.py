class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        # Get new character
        # Move forward until found all of the new character
        # While moving forward keep track of new characters
        # Move forward until found all of the tracked characters
        # Stop once all tracked characters are found
        # Repeat
        if len(S) == 1:
            return [1]
        index = 0
        counter = 0
        new_chars_seen = []
        current_char = S[index]
        partitions = []
        flag = True

        while flag:
            last_index_of_char = S.rfind(current_char)
            substring = S[index: last_index_of_char + 1]
            if last_index_of_char + 1 == len(S):
                partitions.append(len(substring))
                break
            new_chars_seen += list(set(substring))

            for new_char in new_chars_seen[:]:
                if new_char in S[last_index_of_char + 1:]:
                    new_chars_seen.remove(new_char)
                    current_char = new_char
                    break
            else:
                partitions.append(len(substring))
                if last_index_of_char + 1 == len(S):
                    flag = False
                else:
                    index = last_index_of_char + 1
                    current_char = S[index]

        return partitions
