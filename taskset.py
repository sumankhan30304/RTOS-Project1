import csv
import random

def generate_task_set(num_tasks, target_utilization):
    task_set = []
    for i in range(num_tasks):
        Ci = random.randint(1, 100)  # Generating random computation time
        Ui = random.uniform(0.1, target_utilization)  # Generating random utilization within target
        Ti = int(Ci / Ui)  # Calculating period Ti = Ci / Ui
        Di = random.randint(Ci, Ti)  # Generating deadline within the range of Ci to Ti

        task = [0, Ci, Di, Ti]
        task_set.append(task)

    return task_set

def write_task_set_to_csv(task_set, file_name):
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(task_set)

def generate_task_set_files(num_sets, min_tasks, max_tasks, target_utilization, file_prefix):
    for i in range(num_sets):
        num_tasks = random.randint(min_tasks, max_tasks)
        task_set = generate_task_set(num_tasks, target_utilization)
        file_name = f"{file_prefix}_taskset_{i+1}.csv"
        write_task_set_to_csv(task_set, file_name)
        print(f"Generated {file_name} with {num_tasks} tasks.")

# Example Usage:
num_sets_to_generate = 10
min_tasks_per_set = 5
max_tasks_per_set = 15
target_utilization = 0.8  # Change this value as needed
file_prefix = "generated"

generate_task_set_files(num_sets_to_generate, min_tasks_per_set, max_tasks_per_set, target_utilization, file_prefix)
