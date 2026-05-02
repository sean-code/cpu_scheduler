def print_gantt_chart(gantt):
    print("\nGantt Chart:")
    for pid, start, end in gantt:
        print(f"| P{pid} ({start}-{end}) ", end="")
    print("|")