# CPU Scheduling Simulator

## Project Overview

CPU Scheduling Simulator is a desktop application developed in Python to simulate and visualize different CPU scheduling algorithms used in operating systems. The simulator allows users to input processes, execute scheduling algorithms, calculate performance metrics, and display execution order using a Gantt Chart.

The project aims to help students understand how CPU scheduling algorithms work and how they affect process execution, waiting time, and turnaround time.

---

## Objectives

* Simulate CPU scheduling algorithms.
* Calculate process scheduling metrics.
* Visualize process execution using a Gantt Chart.
* Compare the performance of different scheduling algorithms.
* Provide an interactive graphical user interface for users.

---

## Features

### Process Management

* Add processes dynamically.
* Delete selected processes.
* Display process information in a table.

### Scheduling Algorithms

* First Come First Serve (FCFS)
* Shortest Job First (SJF)
* Priority Scheduling
* Round Robin (RR)

### Performance Metrics

* Waiting Time (WT)
* Turnaround Time (TAT)
* Completion Time (CT)
* Average Waiting Time
* Average Turnaround Time

### Visualization

* Embedded Gantt Chart
* Execution Order Display
* CPU Idle Time Visualization

---

## System Requirements

### Hardware Requirements

* Processor: Dual-Core CPU or higher
* RAM: 4 GB minimum
* Storage: 100 MB free space

### Software Requirements

* Python 3.10 or later
* Tkinter
* Matplotlib

---

## Required Python Libraries

Install the required libraries using:

```bash
pip install matplotlib
```

Tkinter is included with most Python installations.

---

## Project Structure

```text
cpu_scheduler/
│
├── algorithms/
│   ├── fcfs.py
│   ├── sjf.py
│   ├── priority.py
│   └── rr.py
│
├── models/
│   └── process.py
│
├── gui/
│   └── interface.py
│
├── main.py
│
└── README.md
```

---

## Scheduling Metrics

### Waiting Time (WT)

Waiting Time is the amount of time a process spends waiting in the ready queue.

Formula:

WT = Start Time − Arrival Time

### Turnaround Time (TAT)

Turnaround Time is the total time taken from process arrival until completion.

Formula:

TAT = Completion Time − Arrival Time

### Completion Time (CT)

Completion Time is the time at which a process finishes execution.

---

## Example Input

| PID | Arrival Time | Burst Time | Priority |
| --- | ------------ | ---------- | -------- |
| P1  | 0            | 5          | 2        |
| P2  | 1            | 3          | 1        |
| P3  | 2            | 8          | 3        |

---

## Expected Output

* Process execution order
* Waiting Time for each process
* Turnaround Time for each process
* Completion Time for each process
* Average Waiting Time
* Average Turnaround Time
* Gantt Chart Visualization

---

## Technologies Used

* Python
* Tkinter
* Matplotlib
* Object-Oriented Programming (OOP)

---

## Authors

Developed as an Operating Systems Final Project.

* Mamy Jean
* Jovan
