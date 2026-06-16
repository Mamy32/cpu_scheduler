def round_robin(processes, quantum):

    processes.sort(key=lambda p: p.arrival)

    current_time = 0
    gantt = []

    total_waiting = 0
    total_turnaround = 0

    remaining = {p.pid: p.burst for p in processes}

    queue = []
    arrived = set()
    completed = []
    index = 0

    # Enqueue first process
    while index < len(processes) and processes[index].arrival <= current_time:
        queue.append(processes[index])
        arrived.add(processes[index].pid)
        index += 1

    while queue or index < len(processes):

        # CPU Idle Case — queue is empty but processes still pending
        if not queue:

            current_time = processes[index].arrival

            while index < len(processes) and processes[index].arrival <= current_time:
                queue.append(processes[index])
                arrived.add(processes[index].pid)
                index += 1

        process = queue.pop(0)

        start_time = current_time

        # Run for quantum or remaining time, whichever is smaller
        run_time = min(quantum, remaining[process.pid])

        current_time += run_time
        remaining[process.pid] -= run_time

        gantt.append(
            (
                process.pid,
                start_time,
                current_time
            )
        )

        while index < len(processes) and processes[index].arrival <= current_time:
            queue.append(processes[index])
            arrived.add(processes[index].pid)
            index += 1

        if remaining[process.pid] == 0:

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

        else:
            queue.append(process)

    avg_waiting = total_waiting / len(completed)
    avg_turnaround = total_turnaround / len(completed)

    return {
        "processes": completed,
        "avg_waiting": avg_waiting,
        "avg_turnaround": avg_turnaround,
        "gantt": gantt
    }