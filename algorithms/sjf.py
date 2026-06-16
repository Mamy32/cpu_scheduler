def sjf(processes):

    remaining = list(processes)

    current_time = 0
    gantt = []

    total_waiting = 0
    total_turnaround = 0

    completed = []

    while remaining:

        # Get all processes that have arrived by current_time
        available = [
            p for p in remaining
            if p.arrival <= current_time
        ]

        # CPU Idle Case — no process has arrived yet
        if not available:

            next_arrival = min(p.arrival for p in remaining)

            gantt.append(
                (
                    "IDLE",
                    current_time,
                    next_arrival
                )
            )

            current_time = next_arrival
            continue

        # Pick the process with the shortest burst time
        # Ties broken by arrival time (earliest first)
        process = min(
            available,
            key=lambda p: (p.burst, p.arrival)
        )

        remaining.remove(process)

        start_time = current_time
        process.waiting_time = (
            start_time - process.arrival
        )

        current_time += process.burst

        process.completion_time = current_time

        process.turnaround_time = (
            process.completion_time -
            process.arrival
        )

        total_waiting += process.waiting_time
        total_turnaround += process.turnaround_time

        gantt.append(
            (
                process.pid,
                start_time,
                current_time
            )
        )

        completed.append(process)

    avg_waiting = total_waiting / len(completed)
    avg_turnaround = total_turnaround / len(completed)

    return {
        "processes": completed,
        "avg_waiting": avg_waiting,
        "avg_turnaround": avg_turnaround,
        "gantt": gantt
    }