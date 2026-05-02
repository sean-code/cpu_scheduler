def sjf(processes):
    processes.sort(key=lambda x: x.arrival_time)

    current_time = 0
    completed = []
    ready_queue = []
    gantt = []

    n = len(processes)
    i = 0  # index for incoming processes

    while len(completed) < n:
        # Add all processes that have arrived
        while i < n and processes[i].arrival_time <= current_time:
            ready_queue.append(processes[i])
            i += 1

        if not ready_queue:
            current_time += 1
            continue

        # Pick process with shortest burst time
        ready_queue.sort(key=lambda x: x.burst_time)
        p = ready_queue.pop(0)

        start = current_time
        current_time += p.burst_time
        end = current_time

        p.completion_time = end
        p.turnaround_time = end - p.arrival_time
        p.waiting_time = p.turnaround_time - p.burst_time

        gantt.append((p.pid, start, end))
        completed.append(p)

    return completed, gantt