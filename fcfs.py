from taskgen import Tasks
from time import sleep



def fcfs(tasks: Tasks) -> True:
    
    time = 1
    
    for task in tasks:
        print(f'Task {task.get("num")}:')
        task['waiting'] = time -1
        
        while task.get('timeleft') > 0:
            sleep(.1)
            print(f"    Time [ {time} ] -  Timeleft: {task.get('timeleft')}")
            
            time += 1
            task['timeleft'] -= 1
    print()
    tasks.show_waiting_time()
    sleep(.1)

    return True
    


if __name__ == "__main__":
    tasks = Tasks()
    fcfs(tasks)