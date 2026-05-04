def print_gantt_chart(gantt):
    print("\nGantt Chart:")

    # Top bar
    print(" ", end="")
    for pid, start, end in gantt:
        print("------", end="")
    print()

    # Process row
    print("|", end="")
    for pid, start, end in gantt:
        print(f" P{pid}  |", end="")
    print()

    # Bottom bar
    print(" ", end="")
    for pid, start, end in gantt:
        print("------", end="")
    print()

    # Time markers
    for i, (pid, start, end) in enumerate(gantt):
        if i == 0:
            print(f"{start:<6}", end="")
        print(f"{end:<6}", end="")
    print("\n")