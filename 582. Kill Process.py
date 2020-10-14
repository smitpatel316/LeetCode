from collections import deque, defaultdict


def kill_process(pid, ppid, kill):
    ppid_to_pid = defaultdict(set)
    for i, p in enumerate(ppid):
        ppid_to_pid[p].add(pid[i])

    to_kill = []
    q = deque([kill])
    while q:
        process = q.popleft()
        to_kill.append(process)
        if process in ppid_to_pid:
            for p in ppid_to_pid[process]:
                q.append(p)
    return to_kill


if __name__ == "__main__":
    print(kill_process([1, 3, 10, 5], [3, 0, 5, 3], 3))  # [3, 1, 5, 10]
