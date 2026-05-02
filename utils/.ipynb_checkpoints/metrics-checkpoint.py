def calculate_averages(processes):
    total_wt = sum(p.waiting_time for p in processes)
    total_tat = sum(p.turnaround_time for p in processes)

    n = len(processes)

    return {
        "avg_waiting_time": total_wt / n,
        "avg_turnaround_time": total_tat / n
    }


def comparison_table(results):
    print("\n=== Algorithm Comparison ===")
    print(f"{'Algorithm':<15}{'Avg WT':<10}{'Avg TAT':<10}")
    print("-" * 35)

    for name, metrics in results.items():
        print(f"{name:<15}{metrics['avg_waiting_time']:<10.2f}{metrics['avg_turnaround_time']:<10.2f}")