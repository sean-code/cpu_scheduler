from collections import deque

def round_robin(processes, quantum):
    processes.sort(key=lambda x: x.arrival_time)

    queue = deque()
    current_time = 0
    gantt = []

    i = 0
    n = len(processes)

    while queue or i < n:
        # Add arriving processes
        while i < n and processes[i].arrival_time <= current_time:
            queue.append(processes[i])
            i += 1

        if not queue:
            current_time += 1
            continue

        p = queue.popleft()

        start = current_time
        exec_time = min(quantum, p.remaining_time)
        current_time += exec_time
        end = current_time

        p.remaining_time -= exec_time
        gantt.append((p.pid, start, end))

        # Add newly arrived processes during execution
        while i < n and processes[i].arrival_time <= current_time:
            queue.append(processes[i])
            i += 1

        if p.remaining_time > 0:
            queue.append(p)
        else:
            p.completion_time = current_time
            p.turnaround_time = current_time - p.arrival_time
            p.waiting_time = p.turnaround_time - p.burst_time

    return processes, gantt

    ## Assigns A fixed quantum to each process