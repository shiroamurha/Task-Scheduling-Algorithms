from taskgen import Tasks
from time import sleep



def sjf(tasks: Tasks, **preemp: bool) -> print:
    
    time = 1

    if preemp:

        tasks_waiting: list[dict[str:int]] = []
        has_task: bool
        new_arrived: bool = True

        while True:
            sleep(.1)
            # appends all the tasks that passes of their arrival time
            for task in tasks:
                if task.get('arrival') <= time and task not in tasks_waiting and task.get('timeleft') != 0:
                    tasks_waiting.append(task)

            # gets the smallest task index of the waiting tasks
            smallest = 0

            for task_index in range(len(tasks_waiting)):
                if tasks_waiting[task_index].get('timeleft') < tasks_waiting[smallest].get('timeleft'):
                    smallest = task_index


            if len(tasks_waiting) > 0:

                if new_arrived:
                    print(f'Task {tasks_waiting[smallest].get("num")} arrived: ')
                    tasks_waiting[smallest]['waiting'] = time - tasks_waiting[smallest]['arrival']
                    new_arrived = False

                if tasks_waiting[smallest].get('timeleft') != 0:
                    print(f"    Time [ {time} ] -  Timeleft: {tasks_waiting[smallest].get('timeleft')}")
                    tasks_waiting[smallest]['timeleft'] -= 1

                    if tasks_waiting[smallest].get('timeleft') == 0:
                        print('-----------------------')
                        new_arrived = True
                        del tasks_waiting[smallest]


            else:
                print(f"    Time [ {time} ] - no task ")

            time += 1
            has_task = False

            for task in tasks:
                if task.get('timeleft') > 0:
                    has_task = True
            
            if has_task:
                continue
            break

        tasks.show_waiting_time()



if __name__ == "__main__":
    sjf(Tasks(), preemp = True) 
    