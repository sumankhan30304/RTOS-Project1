import csv
import sys
import matplotlib.pyplot as plt

# Function to parse a task set file
def parse_task_set(file):
    tasks = []
    with open(file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            tasks.append([int(row[0]), int(row[1]), int(row[2]), int(row[3])])
    return tasks

# Implement the Deadline Monotonic (DM) scheduling algorithm
def deadline_monotonic(tasks):
    tasks.sort(key=lambda x: x[2])  # Sort tasks based on deadlines
    current_time = 0

    schedule = []
    for task in tasks:
        if current_time + task[1] > task[2]:
            return schedule, True  # Deadline missed for the task

        schedule.append((current_time, task[1]))
        current_time += task[1]

    return schedule, False  # No deadline misses

# Implement the Earliest Deadline First (EDF) scheduling algorithm
def earliest_deadline_first(tasks):
    tasks.sort(key=lambda x: x[2])  # Sort tasks based on deadlines
    current_time = 0

    schedule = []
    for task in tasks:
        if current_time + task[1] > task[2]:
            return schedule, True  # Deadline missed for the task

        schedule.append((current_time, task[1]))
        current_time += task[1]

    return schedule, False  # No deadline misses

# Implement the Round Robin (RR) scheduling algorithm
def round_robin(tasks, time_quantum):
    tasks.sort(key=lambda x: x[3])  # Sort tasks based on periods
    current_time = 0

    schedule = []
    for task in tasks:
        remaining_time = task[1]
        while remaining_time > 0:
            schedule.append((current_time, min(remaining_time, time_quantum)))
            remaining_time -= time_quantum
            current_time += time_quantum

            if current_time > task[2]:
                return schedule, True  # Deadline missed for the task

    return schedule, False  # No deadline misses

# Visualization function to plot the schedule
def visualize_schedule(tasks, task_file, algorithm, deadline_miss):
    plt.figure(figsize=(10, 5))
    plt.title(f"Scheduling Simulation - {algorithm}")
    plt.xlabel("Time")
    plt.ylabel("Task")

    for index, task in enumerate(tasks):
        start, comp_time, deadline, period = task
        plt.barh(index, comp_time, left=start, color=plt.cm.viridis(index / len(tasks)), alpha=0.7)
        plt.arrow(start + comp_time, index, deadline - start - comp_time, 0, head_width=0.2, head_length=0.5, fc='black', ec='black')
        plt.text(deadline, index, f'Deadline {index + 1}', verticalalignment='center')

        if isinstance(deadline_miss, list) and deadline_miss[index]:
            plt.text(deadline, index, "Miss", color='red', verticalalignment='center')

    plt.yticks(range(len(tasks)), [f'Task {i + 1}' for i in range(len(tasks))])
    plt.grid(axis='x')
    plt.tight_layout()
    plt.savefig(f"{task_file.split('.')[0]}_{algorithm}.png")

    # Main function
def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py dm|edf|rr <task_file>")
        sys.exit(1)

    algorithm = sys.argv[1]
    task_file = sys.argv[2]

    tasks = parse_task_set(task_file)

    if algorithm == "dm":
        # Deadline Monotonic scheduling
        schedule, deadline_miss = deadline_monotonic(tasks)
    elif algorithm == "edf":
        # Earliest Deadline First scheduling
        schedule, deadline_miss = earliest_deadline_first(tasks)
    elif algorithm == "rr":
        # Round Robin scheduling
        time_quantum = 5  # Set your desired time quantum
        schedule, deadline_miss = round_robin(tasks, time_quantum)
    else:
        print("Invalid algorithm. Please use dm, edf, or rr.")
        sys.exit(1)

    # Visualize the schedule
    visualize_schedule(tasks, task_file, algorithm, deadline_miss)

    if deadline_miss:
        sys.exit(1)  # Deadline missed, exit code 1
    else:
        sys.exit(0)  # Task set is schedulable, exit code 0

if __name__ == "__main__":
    main()
