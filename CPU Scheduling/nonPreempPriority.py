def processData(n):
    process_data = []
    for i in range(n):
        temporary = []
        process_id = int(input("Enter Process ID: "))
        arrival_time = int(input(f"Enter Arrival Time for Process {process_id}: "))
        burst_time = int(input(f"Enter Burst Time for Process {process_id}: "))
        priority = int(input(f"Enter Priority for Process {process_id}: "))
        temporary.extend([process_id, arrival_time, burst_time, priority, 0])
        process_data.append(temporary)
    schedulingProcess(process_data)

def schedulingProcess(process_data):
    start_time = []
    exit_time = []
    s_time = 0
    process_data.sort(key=lambda x: x[1])
    for i in range(len(process_data)):
        ready_queue = []
        temp = []
        normal_queue = []
        for j in range(len(process_data)):
            if (process_data[j][1] <= s_time) and (process_data[j][4] == 0):
                temp.extend([process_data[j][0], process_data[j][1], process_data[j][2], process_data[j][3]])
                ready_queue.append(temp)
                temp = []
            elif process_data[j][4] == 0:
                temp.extend([process_data[j][0], process_data[j][1], process_data[j][2], process_data[j][3]])
                normal_queue.append(temp)
                temp = []
        if len(ready_queue) != 0:
            ready_queue.sort(key=lambda x: x[3], reverse=True)
            start_time.append(s_time)
            s_time = s_time + ready_queue[0][2]
            e_time = s_time
            exit_time.append(e_time)
            for k in range(len(process_data)):
                if process_data[k][0] == ready_queue[0][0]:
                    break
            process_data[k][4] = 1
            process_data[k].append(e_time)
        elif len(ready_queue) == 0:
            if s_time < normal_queue[0][1]:
                s_time = normal_queue[0][1]
            start_time.append(s_time)
            s_time = s_time + normal_queue[0][2]
            e_time = s_time
            exit_time.append(e_time)
            for k in range(len(process_data)):
                if process_data[k][0] == normal_queue[0][0]:
                    break
            process_data[k][4] = 1
            process_data[k].append(e_time)
    t_time = turnaroundTime(process_data)
    w_time = waitingTime(process_data)
    print("Waiting time is :",w_time)
    print("Turnaround Time is :",t_time)

def waitingTime(process_data):
    total_waiting_time = 0
    for i in range(len(process_data)):
        waiting_time = process_data[i][6] - process_data[i][2]
        total_waiting_time = total_waiting_time + waiting_time
        process_data[i].append(waiting_time)
    average_waiting_time = total_waiting_time / len(process_data)
    return average_waiting_time

def turnaroundTime(process_data):
    total_turnaround_time = 0
    for i in range(len(process_data)):
        turnaround_time = process_data[i][5] - process_data[i][1]
        total_turnaround_time = total_turnaround_time + turnaround_time
        process_data[i].append(turnaround_time)
    average_turnaround_time = total_turnaround_time / len(process_data)
    return average_turnaround_time

n = int(input("Enter number of processes: "))
processData(n)