from taskgen import Tasks



def fcfs(tasks: Tasks) -> None:
    
    time = 1
    
    for task in tasks:
        print(f'Task {task.get("num")}:')
        task['waiting'] = time -1
        
        while task.get('timeleft') > 0:
            print(f"    Time [ {time} ] -  Timeleft: {task.get('timeleft')}")
            
            time += 1
            task['timeleft'] -= 1
    print()
    tasks.show_waiting_time()
    


if __name__ == "__main__":
    tasks = Tasks()
    fcfs(tasks)