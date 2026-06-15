from models.process import Process
from algorithms.fcfs import fcfs

processes = [

    Process("P1", 0, 5, 2),

    Process("P2", 1, 3, 1),

    Process("P3", 2, 8, 3)

]

result = fcfs(processes)

print("\nFCFS RESULTS\n")

for p in result["processes"]:

    print(
        f"{p.pid}"
        f" | WT={p.waiting_time}"
        f" | TAT={p.turnaround_time}"
        f" | CT={p.completion_time}"
    )

print()

print(
    "Average Waiting Time:",
    round(result["avg_waiting"], 2)
)

print(
    "Average Turnaround Time:",
    round(result["avg_turnaround"], 2)
)

print("\nGantt Data:")

for g in result["gantt"]:
    print(g)