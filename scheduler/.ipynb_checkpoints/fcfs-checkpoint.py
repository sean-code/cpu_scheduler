def fcfs(processes):
    processes.sort(key=lambda x: x.arrival_time)

    current_time = 0
    gantt = []

    for p in processes:
        if current_time < p.arrival_time:
            current_time = p.arrival_time

        start = current_time
        current_time += p.burst_time
        end = current_time

        p.completion_time = end
        p.turnaround_time = end - p.arrival_time
        p.waiting_time = p.turnaround_time - p.burst_time

        gantt.append((p.pid, start, end))

    return processes, gantt