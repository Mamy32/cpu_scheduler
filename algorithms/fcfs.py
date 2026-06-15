def fcfs(processes):

    # Sort by arrival time
    processes.sort(key=lambda p: p.arrival)

    current_time = 0
    gantt = []

    total_waiting = 0
    total_turnaround = 0

    for process in processes:

        # CPU Idle Case
        if current_time < process.arrival:

            gantt.append(
                (
                    "IDLE",
                    current_time,
                    process.arrival
                )
            )

            current_time = process.arrival

        start_time = current_time

        # Waiting Time
        process.waiting_time = (
            start_time - process.arrival
        )

        # Execute Process
        current_time += process.burst

        # Completion Time
        process.completion_time = current_time

        # Turnaround Time
        process.turnaround_time = (
            process.completion_time -
            process.arrival
        )

        total_waiting += process.waiting_time
        total_turnaround += process.turnaround_time

        # Add Process to Gantt Chart
        gantt.append(
            (
                process.pid,
                start_time,
                current_time
            )
        )

    avg_waiting = total_waiting / len(processes)
    avg_turnaround = total_turnaround / len(processes)

    return {
        "processes": processes,
        "avg_waiting": avg_waiting,
        "avg_turnaround": avg_turnaround,
        "gantt": gantt
    }