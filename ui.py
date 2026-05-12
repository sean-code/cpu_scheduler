import tkinter as tk
from tkinter import ttk
import copy
from process import Process
from scheduler.fcfs import fcfs
from scheduler.sjf import sjf
from scheduler.round_robin import round_robin
from utils.metrics import calculate_averages
import matplotlib.pyplot as plt
import csv
import os
from datetime import datetime


process_entries = []


def add_process_row():
    row = len(process_entries)

    at_entry = tk.Entry(frame_inputs, width=5)
    bt_entry = tk.Entry(frame_inputs, width=5)

    at_entry.grid(row=row, column=1)
    bt_entry.grid(row=row, column=2)

    tk.Label(frame_inputs, text=f"P{row+1}").grid(row=row, column=0)

    process_entries.append((at_entry, bt_entry))


def run_simulation():
    processes = []

    for i, (at_entry, bt_entry) in enumerate(process_entries):
        at_val = at_entry.get().strip()
        bt_val = bt_entry.get().strip()

        # Validate empty fields
        if not at_val or not bt_val:
            output_text.delete(1.0, tk.END)
            output_text.insert(tk.END, "Error: Please fill all fields.\n")
            return

        # Validate numeric input
        if not at_val.isdigit() or not bt_val.isdigit():
            output_text.delete(1.0, tk.END)
            output_text.insert(tk.END, "Error: Only numeric values allowed.\n")
            return

        at = int(at_val)
        bt = int(bt_val)

        processes.append(Process(i+1, at, bt))

    # Extra safety check
    if len(processes) == 0:
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "No processes entered.\n")
        return

    algo = algo_var.get()
    proc_copy = copy.deepcopy(processes)

    if algo == "FCFS":
        result, gantt = fcfs(proc_copy)
    elif algo == "SJF":
        result, gantt = sjf(proc_copy)
    else:
        result, gantt = round_robin(proc_copy, 2)

    averages = calculate_averages(result)

    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, f"Averages: {averages}\n")

    for p in result:
        output_text.insert(
            tk.END,
            f"P{p.pid} -> WT: {p.waiting_time}, "
            f"TAT: {p.turnaround_time}\n"
        )

    # SAVE RESULTS TO CSV
    file_exists = os.path.isfile("results.csv")

    with open("results.csv", "a", newline="") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow(["Algorithm", "Process", "WT", "TAT"])

        for p in result:
            writer.writerow([
                algo,
                f"P{p.pid}",
                p.waiting_time,
                p.turnaround_time
            ])

    plot_gantt(gantt, algo)


# Save Results in CSV file

        


def plot_gantt(gantt, algo):
    fig, ax = plt.subplots()

    for pid, start, end in gantt:
        ax.barh(y=f"P{pid}", width=end-start, left=start)

    ax.set_xlabel("Time")
    ax.set_title(f"Gantt Chart - {algo}")

    # Create folder if it doesn't exist
    os.makedirs("charts", exist_ok=True)

    # Create unique filename using timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"charts/{algo.replace(' ', '_')}_{timestamp}.png"

    # Save the figure
    plt.savefig(filename)

    print(f"Gantt chart saved as {filename}")

    plt.show()


root = tk.Tk()
root.title("CPU Scheduling Simulator")

frame_inputs = tk.Frame(root)
frame_inputs.pack()

tk.Button(root, text="Add Process", command=add_process_row).pack()

algo_var = tk.StringVar(value="FCFS")
ttk.Combobox(root, textvariable=algo_var, values=["FCFS", "SJF", "Round Robin"]).pack()

tk.Button(root, text="Run Simulation", command=run_simulation).pack()

output_text = tk.Text(root, height=10, width=50)
output_text.pack()

root.mainloop()