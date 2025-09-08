# FCFS (First-Come, First-Served) CPU Scheduling Algorithm Implementation in Python

# Sample process data: (Process ID, Arrival Time, Burst Time)
processes = [
    {'pid': 'P1', 'arrival': 0, 'burst': 4},
    {'pid': 'P2', 'arrival': 1, 'burst': 3},
    {'pid': 'P3', 'arrival': 2, 'burst': 1},
    {'pid': 'P4', 'arrival': 3, 'burst': 2},
]

# Sort processes by arrival time (FCFS)
processes.sort(key=lambda x: x['arrival'])

current_time = 0
gantt_chart = []
waiting_times = []
turnaround_times = []

print("PID\tArrival\tBurst\tStart\tFinish\tWaiting\tTurnaround")
for p in processes:
    start_time = max(current_time, p['arrival'])
    finish_time = start_time + p['burst']
    waiting_time = start_time - p['arrival']
    turnaround_time = finish_time - p['arrival']
    gantt_chart.append((p['pid'], start_time, finish_time))
    waiting_times.append(waiting_time)
    turnaround_times.append(turnaround_time)
    print(f"{p['pid']}\t{p['arrival']}\t{p['burst']}\t{start_time}\t{finish_time}\t{waiting_time}\t{turnaround_time}")
    current_time = finish_time

avg_waiting = sum(waiting_times) / len(waiting_times)
avg_turnaround = sum(turnaround_times) / len(turnaround_times)

print(f"\nAverage Waiting Time: {avg_waiting:.2f}")
print(f"Average Turnaround Time: {avg_turnaround:.2f}")

# Simple Gantt Chart Visualization
print("\nGantt Chart:")
for pid, start, finish in gantt_chart:
    print(f"| {pid} ({start}-{finish}) ", end="")
print("|")