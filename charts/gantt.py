import matplotlib.pyplot as plt


def draw_gantt(gantt_data):

    fig, ax = plt.subplots(figsize=(8, 2))

    for process in gantt_data:

        pid = process[0]
        start = process[1]
        end = process[2]

        duration = end - start

        ax.barh(
            y=0,
            width=duration,
            left=start,
            height=0.5
        )

        ax.text(
            start + duration / 2,
            0,
            pid,
            ha="center",
            va="center"
        )

        ax.text(
            start,
            -0.3,
            str(start)
        )

    ax.text(
        gantt_data[-1][2],
        -0.3,
        str(gantt_data[-1][2])
    )

    ax.set_title("FCFS Gantt Chart")

    ax.set_yticks([])

    plt.tight_layout()

    plt.show()