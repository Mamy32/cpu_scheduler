# gui/interface.py
from models.process import Process
from algorithms.fcfs import fcfs
from algorithms.sjf import sjf
from algorithms.rr import round_robin
from algorithms.priority import priority_scheduling
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import tkinter as tk

from tkinter import ttk


class CPUSchedulerGUI:
    def __init__(self, root):
        self.root = root

        self.root.title("CPU Scheduling Simulator")
        self.root.geometry("1200x700")
        self.root.resizable(False, False)

        self.setup_ui()

    def setup_ui(self):

        title = tk.Label(
            self.root,
            text="CPU Scheduling Simulator",
            font=("Arial", 20, "bold")
        )
        title.pack(pady=10)

        # ==========================
        # TOP SECTION
        # ==========================

        top_frame = tk.Frame(self.root)
        top_frame.pack(fill="x", padx=10)

        left_top = tk.Frame(top_frame)
        left_top.pack(side="left", padx=10)

        right_top = tk.Frame(top_frame)
        right_top.pack(side="right", padx=10)

        # ==========================
        # PROCESS INPUT
        # ==========================

        input_frame = tk.LabelFrame(
            left_top,
            text="Process Input"
        )
        input_frame.pack()

        tk.Label(input_frame, text="PID").grid(row=0, column=0, padx=5, pady=5)

        self.pid_entry = tk.Entry(input_frame)
        self.pid_entry.grid(row=0, column=1)

        tk.Label(input_frame, text="Arrival Time").grid(row=1, column=0)

        self.arrival_entry = tk.Entry(input_frame)
        self.arrival_entry.grid(row=1, column=1)

        tk.Label(input_frame, text="Burst Time").grid(row=2, column=0)

        self.burst_entry = tk.Entry(input_frame)
        self.burst_entry.grid(row=2, column=1)

        tk.Label(input_frame, text="Priority").grid(row=3, column=0)

        self.priority_entry = tk.Entry(input_frame)
        self.priority_entry.grid(row=3, column=1)

        tk.Button(
            input_frame,
            text="Add Process",
            command=self.add_process
        ).grid(
            row=4,
            column=0,
            columnspan=2,
            pady=10
        )

        # ==========================
        # ALGORITHM SECTION
        # ==========================

        algorithm_frame = tk.LabelFrame(
            right_top,
            text="Scheduling Algorithm"
        )

        algorithm_frame.pack()

        self.algorithm = tk.StringVar(value="FCFS")

        tk.Radiobutton(
            algorithm_frame,
            text="FCFS",
            variable=self.algorithm,
            value="FCFS"
        ).pack(anchor="w")

        tk.Radiobutton(
            algorithm_frame,
            text="SJF",
            variable=self.algorithm,
            value="SJF"
        ).pack(anchor="w")

        tk.Radiobutton(
            algorithm_frame,
            text="Round Robin",
            variable=self.algorithm,
            value="RR"
        ).pack(anchor="w")

        tk.Radiobutton(
            algorithm_frame,
            text="Priority",
            variable=self.algorithm,
            value="Priority"
        ).pack(anchor="w")

        tk.Label(
            algorithm_frame,
            text="Quantum"
        ).pack(anchor="w")

        self.quantum_entry = tk.Entry(
            algorithm_frame,
            width=10
        )

        self.quantum_entry.insert(0, "2")
        self.quantum_entry.pack(anchor="w")

        tk.Button(
            algorithm_frame,
            text="Run Simulation",
            command=self.run_simulation
        ).pack(pady=10)

        # ==========================
        # GANTT CHART
        # ==========================

        self.gantt_frame = tk.LabelFrame(
            self.root,
            text="Gantt Chart"
        )
        self.gantt_frame.config(height=120)
        self.gantt_frame.pack_propagate(False)
        self.gantt_frame.pack(
            fill="x",
            padx=10,
            pady=5
        )

        self.gantt_placeholder = tk.Label(
            self.gantt_frame,
            text="Run Simulation to Generate Gantt Chart",
            font=("Arial", 12)
        )

        self.gantt_placeholder.pack(
            pady=5
        )

        # ==========================
        # BOTTOM SECTION
        # ==========================

        bottom_frame = tk.Frame(self.root)
        bottom_frame.pack(
            fill="both",
            expand=True,
            padx=10
        )

        # ==========================
        # PROCESS TABLE
        # ==========================

        table_frame = tk.LabelFrame(
            bottom_frame,
            text="Process List"
        )

        table_frame.pack(
            side="left",
            fill="both",
            expand=True,
            padx=5
        )

        self.process_table = ttk.Treeview(
            table_frame,
            columns=("PID", "Arrival", "Burst", "Priority"),
            show="headings"
        )

        self.process_table.heading("PID", text="PID")
        self.process_table.heading("Arrival", text="Arrival")
        self.process_table.heading("Burst", text="Burst")
        self.process_table.heading("Priority", text="Priority")

        self.process_table.column("PID", width=80, anchor="center")
        self.process_table.column("Arrival", width=100, anchor="center")
        self.process_table.column("Burst", width=100, anchor="center")
        self.process_table.column("Priority", width=100, anchor="center")
        
        self.process_table.pack(
            fill="both",
            expand=True
        )

        tk.Button(
            table_frame,
            text="Delete Selected",
            command=self.delete_process
        ).pack(pady=5)

        # ==========================
        # RESULTS
        # ==========================

        results_frame = tk.LabelFrame(
            bottom_frame,
            text="Results"
        )

        results_frame.pack(
            side="right",
            fill="both",
            expand=True,
            padx=5
        )

        self.results_text = tk.Text(
            results_frame,
            height=20
        )

        self.results_text.pack(
            fill="both",
            expand=True
        )
    def draw_gantt_in_gui(self, gantt_data):

        for widget in self.gantt_frame.winfo_children():
            widget.destroy()

        fig, ax = plt.subplots(figsize=(10, 1))

        for process in gantt_data:

            pid = process[0]
            start = process[1]
            end = process[2]

            duration = end - start

            ax.barh(
                0,
                duration,
                left=start,
                height=0.5,
                edgecolor="black"
            )

            ax.text(
                start + duration / 2,
                0,
                pid,
                ha="center",
                va="center"
            )

            ax.set_xticks(
                [g[1] for g in gantt_data] + [gantt_data[-1][2]]
            )

        

        ax.set_title("CPU Scheduling Gantt Chart")

        ax.set_yticks([])

        ax.grid(
            axis="x",
            linestyle="--",
            alpha=0.5
        )

        plt.tight_layout()

        canvas = FigureCanvasTkAgg(
            fig,
            master=self.gantt_frame
        )

        canvas.draw()

        canvas.get_tk_widget().pack(
            fill="both",
            expand=True
        )
    def add_process(self):

        pid = self.pid_entry.get()
        arrival = self.arrival_entry.get()
        burst = self.burst_entry.get()
        priority = self.priority_entry.get()

        self.process_table.insert(
            "",
            "end",
            values=(pid, arrival, burst, priority)
        )

        self.pid_entry.delete(0, tk.END)
        self.arrival_entry.delete(0, tk.END)
        self.burst_entry.delete(0, tk.END)
        self.priority_entry.delete(0, tk.END)
        
    def delete_process(self):

        selected = self.process_table.selection()

        for item in selected:
            self.process_table.delete(item)
            
    def run_simulation(self):

        processes = []

        for row in self.process_table.get_children():

            values = self.process_table.item(row)["values"]

            process = Process(
                str(values[0]),  # PID
                int(values[1]),  # Arrival
                int(values[2]),  # Burst
                int(values[3])   # Priority
            )

            processes.append(process)

        if len(processes) == 0:
            return

        selected_algorithm = self.algorithm.get()

        if selected_algorithm == "FCFS":
            result = fcfs(processes)
            self.display_results(result, "FCFS")
            self.draw_gantt_in_gui(result["gantt"])
        elif selected_algorithm == "SJF":
            result = sjf(processes)
            self.display_results(result, "SJF")
            self.draw_gantt_in_gui(result["gantt"])
        elif selected_algorithm == "RR":
            quantum = int(self.quantum_entry.get())
            result = round_robin(processes, quantum)
            self.display_results(result, "Round Robin")
            self.draw_gantt_in_gui(result["gantt"])
        elif selected_algorithm == "Priority":
            result = priority_scheduling(processes)
            self.display_results(result, "Priority")
            self.draw_gantt_in_gui(result["gantt"])

    
    def display_results(self, result,algorithm_name=""):

        self.results_text.delete("1.0", tk.END)

        self.results_text.insert(
            tk.END,
            f"{algorithm_name} RESULTS\n\n"
    )

        self.results_text.insert(
            tk.END,
            f"{'PID':<8}{'WT':<8}{'TAT':<8}{'CT':<8}\n"
        )

        self.results_text.insert(
            tk.END,
            "-" * 35 + "\n"
        )

        for process in result["processes"]:

            self.results_text.insert(
                tk.END,
                f"{process.pid:<8}"
                f"{process.waiting_time:<8}"
                f"{process.turnaround_time:<8}"
                f"{process.completion_time:<8}\n"
            )

        self.results_text.insert(
            tk.END,
            "\n"
        )

        self.results_text.insert(
            tk.END,
            f"Average Waiting Time: "
            f"{result['avg_waiting']:.2f}\n"
        )

        self.results_text.insert(
            tk.END,
            f"Average Turnaround Time: "
            f"{result['avg_turnaround']:.2f}\n"
        )

        self.results_text.insert(
            tk.END,
            "\nExecution Order:\n"
        )

        execution_order = " → ".join(
            [g[0] for g in result["gantt"]]
        )

        self.results_text.insert(
            tk.END,
            execution_order
        )