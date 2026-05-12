from process import Process
from scheduler.fcfs import fcfs
from scheduler.sjf import sjf
from scheduler.round_robin import round_robin
from utils.metrics import calculate_averages, comparison_table
from utils.gantt import print_gantt_chart
from input_handler import get_processes
import copy


def run_and_store(name, func, processes, results_summary, *args):
    proc_copy = copy.deepcopy(processes)

    result, gantt = func(proc_copy, *args) if args else func(proc_copy)

    print(f"\n=== {name} ===")
    print_gantt_chart(gantt)

    for p in result:
        print(f"P{p.pid} -> WT: {p.waiting_time}, TAT: {p.turnaround_time}")

    averages = calculate_averages(result)
    print("Averages:", averages)

    results_summary[name] = averages


def main():
    # THIS is where my user input comes in
    processes = get_processes()

    results_summary = {}

    run_and_store("FCFS", fcfs, processes, results_summary)
    run_and_store("SJF", sjf, processes, results_summary)
    run_and_store("Round Robin (q=2)", round_robin, processes, results_summary, 2)

    # Final comparison output
    comparison_table(results_summary)


if __name__ == "__main__":
    main()