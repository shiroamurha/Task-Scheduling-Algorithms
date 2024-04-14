from taskgen import Tasks
from time import sleep



def sjf(tasks: Tasks, preemp: bool) -> True:
    
    # task queue
    tasks_waiting: list[dict[str:int]] = []

    # flags
    has_task: bool = True
    new_arrived: bool = True
    last_task = -1

    time = 1
    while has_task:

        sleep(.1) # delay for debugging

        # tasks_waiting becomes a queue of tasks where a task only enters when the time
        # reaches its arrival time and only gets out when its timeleft reaches zero
        for task in tasks:
            if task.get('arrival') <= time and task not in tasks_waiting and task.get('timeleft') != 0:
                tasks_waiting.append(task)

        # gets the smallest task index of the waiting tasks if it's preemptive
        smallest = 0
        if preemp:
            for task_index in range(len(tasks_waiting)):
                if tasks_waiting[task_index].get('timeleft') < tasks_waiting[smallest].get('timeleft'):
                    smallest = task_index

        # if it's not preemptive, sort by task arrival time
        # and run the first of the queue
        else:    
            for task_num in range(len(tasks_waiting)):
                for _ in range(len(tasks_waiting) - task_num - 1):

                    if tasks_waiting[task_num].get('arrival') < tasks_waiting[task_num+1].get('arrival'):

                        temp = tasks_waiting[task_num]
                        tasks_waiting[task_num] = tasks_waiting[task_num+1]
                        tasks_waiting[task_num+1] = temp


        # only if there is at least one task in the queue
        
        if len(tasks_waiting) > 0:

            if new_arrived or last_task != tasks_waiting[smallest].get("num"):
                # if the flag of a new task arrival is raised show that the task has arrived,
                # downs the flag and registers the time it has waited
                print('-------------------------')
                print(f'Task {tasks_waiting[smallest].get("num")} arrived: ')

                tasks_waiting[smallest]['waiting'] = time - tasks_waiting[smallest]['arrival'] - (tasks_waiting[smallest].get('runtime') - tasks_waiting[smallest].get('timeleft'))
                new_arrived = False

            if tasks_waiting[smallest].get('timeleft') != 0:

                print(f"    Time [ {time} ] -  Timeleft: {tasks_waiting[smallest].get('timeleft')}")
                tasks_waiting[smallest]['timeleft'] -= 1
                last_task = tasks_waiting[smallest].get('num')
                
                if tasks_waiting[smallest].get('timeleft') == 0:
                    # if the task's timeleft reaches 0 after the time tick, then erase it (only the pointer)
                    # from the queue and raises a flag that another task is required
                    new_arrived = True
                    del tasks_waiting[smallest] 

            
        else:
            print(f"    Time [ {time} ] - no task ")

        time += 1
        has_task = False

        for task in tasks:
            if task.get('timeleft') > 0:
                has_task = True
        # if any task is above 0 timeleft, raises the flag
        # that there is a task yet to run, else breaks the loop
    
    tasks.show_waiting_time()
    return True



if __name__ == "__main__":
    sjf(Tasks(), preemp = True) 
    sjf(Tasks(), preemp = False) 