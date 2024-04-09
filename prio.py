from taskgen import Tasks
from time import sleep



def prio(tasks: Tasks, preemp: bool) -> True:
    
    # task queue
    tasks_waiting: list[dict[str:int]] = []

    # flags
    has_task: bool
    new_arrived: bool = True
    last_task = -1
    highest_prio = 0

    time = 1
    while True:

        sleep(.1) # delay for debugging

        # tasks_waiting becomes a queue of tasks where a task only enters when the time
        # reaches its arrival time and only gets out when its timeleft reaches zero
        for task in tasks:
            if task.get('arrival') <= time and task not in tasks_waiting and task.get('timeleft') != 0:
                tasks_waiting.append(task)

        # gets the highest priority task index of the waiting tasks if it's preemptive
        if preemp:
            highest_prio = 0
            for task_index in range(len(tasks_waiting)):
                if tasks_waiting[task_index].get('prio') > tasks_waiting[highest_prio].get('prio'):
                    highest_prio = task_index

        # if it's not preemptive, sort by task arrival time
        # and run the first of the queue
        else:    
            for i in range(len(tasks_waiting)):
                for task_num in range(len(tasks_waiting) - i - 1):

                    if tasks_waiting[task_num].get('arrival') > tasks_waiting[task_num+1].get('arrival'):

                        temp = tasks_waiting[task_num]
                        tasks_waiting[task_num] = tasks_waiting[task_num+1]
                        tasks_waiting[task_num+1] = temp

            # switches places of tasks with same arrival time but less priority 
            for n in range(len(tasks_waiting)):
                for i in range(len(tasks_waiting) - n - 1):

                    if tasks_waiting[i].get('arrival') == tasks_waiting[i+1].get('arrival') and tasks_waiting[i].get('prio') < tasks_waiting[i+1].get('prio'):

                        temp = tasks_waiting[i]
                        tasks_waiting[i] = tasks_waiting[i+1]
                        tasks_waiting[i+1] = temp

        # only if there is at least one task in the queue
        if len(tasks_waiting) > 0:

            if new_arrived or last_task != tasks_waiting[highest_prio].get("num"):
                # if the flag of a new task arrival is raised show that the task has arrived,
                # downs the flag and registers the time it has waited
                print('-------------------------')
                print(f'Task {tasks_waiting[highest_prio].get("num")} arrived: ')

                tasks_waiting[highest_prio]['waiting'] = time - tasks_waiting[highest_prio]['arrival'] - (tasks_waiting[highest_prio].get('runtime') - tasks_waiting[highest_prio].get('timeleft'))

                new_arrived = False

            if tasks_waiting[highest_prio].get('timeleft') != 0:

                print(f"    Time [ {time} ] -  Timeleft: {tasks_waiting[highest_prio].get('timeleft')}")
                tasks_waiting[highest_prio]['timeleft'] -= 1
                last_task = tasks_waiting[highest_prio].get('num')
                
                if tasks_waiting[highest_prio].get('timeleft') == 0:
                    # if the task's timeleft reaches 0 after the time tick, then erase it (only the pointer)
                    # from the queue and raises a flag that another task is required
                    new_arrived = True
                    del tasks_waiting[highest_prio] 
        
        else:
            print(f"    Time [ {time} ] - no task ")

        time += 1
        has_task = False

        for task in tasks:
            if task.get('timeleft') > 0:
                has_task = True
        # if any task is above 0 timeleft, raises the flag
        # that there is a task yet to run, else breaks the loop

        if not has_task:
            break

    tasks.show_waiting_time()
    return True


if __name__ == "__main__":
    prio(Tasks(), preemp = True) 
    