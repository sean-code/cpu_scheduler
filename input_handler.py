from process import Process

def get_processes():
    n = int(input("Enter number of processes: "))
    processes = []

    for i in range(n):
        at = int(input(f"Enter arrival time for P{i+1}: "))
        bt = int(input(f"Enter burst time for P{i+1}: "))
        processes.append(Process(i+1, at, bt))

    return processes