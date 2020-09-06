from collections import deque


def kill_process(pid, ppid, kill):
    ppid_to_pid = {}
    for i, p in enumerate(ppid):
        if p not in ppid_to_pid:
            ppid_to_pid[p] = set()
        ppid_to_pid[p].add(pid[i])

    to_kill = []
    q = deque([kill])
    visited = set(to_kill)
    while q:
        process = q.popleft()
        to_kill.append(process)
        if process in ppid_to_pid:
            for p in ppid_to_pid[process]:
                if p not in visited:
                    q.append(p)
                    visited.add(p)
    return to_kill


if __name__ == "__main__":
    print(kill_process([1, 3, 10, 5], [3, 0, 5, 3], 3))  # [3, 1, 5, 10]
