def priority_scheduling(processes, preemptive=False):

    if preemptive:
        return priority_preemptive(processes)
    else:
        return priority_non_preemptive(processes)


def priority_non_preemptive(processes):

    remaining = list(processes)

    current_time = 0
    gantt = []

    total_waiting = 0
    total_turnaround = 0

    completed = []

    while remaining:

        available = [
            p for p in remaining
            if p.arrival <= current_time
        ]
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

        # Pick the process with the highest priority
        # Lower number = higher priority
        # Ties broken by arrival time (earliest first)
        process = min(
            available,
            key=lambda p: (p.priority, p.arrival)
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


def priority_preemptive(processes):

    # Track remaining burst time for each process
    remaining_burst = {p.pid: p.burst for p in processes}

    current_time = 0
    gantt = []

    total_waiting = 0
    total_turnaround = 0

    completed = []
    done = set()

    last_pid = None
    last_start = 0

    while len(done) < len(processes):

        # Get all processes that have arrived and not completed
        available = [
            p for p in processes
            if p.arrival <= current_time
            and p.pid not in done
        ]

        if not available:

            next_arrival = min(
                p.arrival for p in processes
                if p.pid not in done
            )

            if last_pid is not None:
                gantt.append(
                    (
                        last_pid,
                        last_start,
                        current_time
                    )
                )
                last_pid = None

            gantt.append(
                (
                    "IDLE",
                    current_time,
                    next_arrival
                )
            )

            current_time = next_arrival
            last_start = current_time
            continue

        # Pick process with highest priority (lowest number)
        # Ties broken by arrival time
        process = min(
            available,
            key=lambda p: (p.priority, p.arrival)
        )

        # If a different process is now running, save previous to gantt
        if last_pid != process.pid:

            if last_pid is not None:
                gantt.append(
                    (
                        last_pid,
                        last_start,
                        current_time
                    )
                )

            last_pid = process.pid
            last_start = current_time

        # Execute for 1 unit of time
        remaining_burst[process.pid] -= 1
        current_time += 1
        if remaining_burst[process.pid] == 0:
            gantt.append(
                (
                    process.pid,
                    last_start,
                    current_time
                )
            )

            last_pid = None
            last_start = current_time

            process.completion_time = current_time

            process.turnaround_time = (
                process.completion_time -
                process.arrival
            )

            process.waiting_time = (
                process.turnaround_time -
                process.burst
            )

            total_waiting += process.waiting_time
            total_turnaround += process.turnaround_time

            completed.append(process)
            done.add(process.pid)

    avg_waiting = total_waiting / len(completed)
    avg_turnaround = total_turnaround / len(completed)

    return {
        "processes": completed,
        "avg_waiting": avg_waiting,
        "avg_turnaround": avg_turnaround,
        "gantt": gantt
    }