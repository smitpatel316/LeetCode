class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []

        for log in logs:
            log_list = log.split(" ")
            if log_list[1].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append(log)

        def sort_key(log):
            log_list = log.split(" ")
            return (" ".join(log_list[1:]), log_list[0])

        letter_logs.sort(key=lambda log: sort_key(log))
        return letter_logs + digit_logs
