from copy import deepcopy

from models.process import Process

from algorithms.fcfs import fcfs
from algorithms.sjf import sjf
from algorithms.priority import priority_scheduling
from algorithms.rr import round_robin

import matplotlib.pyplot as plt
import numpy as np


# ==================================
# SAME PROCESS SET FOR ALL ALGORITHMS
# ==================================

processes = [
    Process("P1", 0, 7, 2),
    Process("P2", 2, 4, 1),
    Process("P3", 4, 1, 3),
    Process("P4", 5, 4, 2)
]


# ==================================
# RUN ALL ALGORITHMS
# ==================================

fcfs_result = fcfs(
    deepcopy(processes)
)

sjf_np_result = sjf(
    deepcopy(processes),
    preemptive=False
)

srtf_result = sjf(
    deepcopy(processes),
    preemptive=True
)

priority_np_result = priority_scheduling(
    deepcopy(processes),
    preemptive=False
)

priority_p_result = priority_scheduling(
    deepcopy(processes),
    preemptive=True
)

rr_result = round_robin(
    deepcopy(processes),
    quantum=2
)


# ==================================
# PRINT RESULTS
# ==================================

print("\nALGORITHM COMPARISON\n")

print(
    f"{'Algorithm':<15}"
    f"{'Avg WT':<15}"
    f"{'Avg TAT':<15}"
)

print("-" * 45)

results = [
    ("FCFS", fcfs_result),
    ("SJF NP", sjf_np_result),
    ("SRTF", srtf_result),
    ("Priority NP", priority_np_result),
    ("Priority P", priority_p_result),
    ("Round Robin", rr_result)
]

for name, result in results:

    print(
        f"{name:<15}"
        f"{result['avg_waiting']:<15.2f}"
        f"{result['avg_turnaround']:<15.2f}"
    )


# ==================================
# GRAPH DATA
# ==================================

algorithms = [
    "FCFS",
    "SJF NP",
    "SRTF",
    "Priority NP",
    "Priority P",
    "RR"
]

avg_waiting = [
    fcfs_result["avg_waiting"],
    sjf_np_result["avg_waiting"],
    srtf_result["avg_waiting"],
    priority_np_result["avg_waiting"],
    priority_p_result["avg_waiting"],
    rr_result["avg_waiting"]
]

avg_turnaround = [
    fcfs_result["avg_turnaround"],
    sjf_np_result["avg_turnaround"],
    srtf_result["avg_turnaround"],
    priority_np_result["avg_turnaround"],
    priority_p_result["avg_turnaround"],
    rr_result["avg_turnaround"]
]


# ==================================
# CREATE COMPARISON CHART
# ==================================

x = np.arange(len(algorithms))
width = 0.35

plt.figure(figsize=(10, 5))

plt.bar(
    x - width / 2,
    avg_waiting,
    width,
    label="Average Waiting Time"
)

plt.bar(
    x + width / 2,
    avg_turnaround,
    width,
    label="Average Turnaround Time"
)

plt.xticks(
    x,
    algorithms
)

plt.ylabel("Time")

plt.xlabel(
    "Scheduling Algorithms"
)

plt.title(
    "CPU Scheduling Algorithm Performance Comparison"
)

plt.legend()

plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.5
)

plt.tight_layout()

plt.show()