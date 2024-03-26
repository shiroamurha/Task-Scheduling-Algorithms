import taskgen



def fcfs(tasks: list[dict[str: int]]) -> None:
    
    time = 1
    
    for task in tasks:
        print(f'Task {tasks.index(task)}:')
        task['waiting'] = time -1
        
        while task.get('timeleft') > 0:
            print(f"    Time [ {time} ] -  Timeleft: {task.get('timeleft')}")
            
            time += 1
            task['timeleft'] -= 1
    print()
    


if __name__ == "__main__":
    tasks = taskgen.set_tasks()
    fcfs(tasks)
    taskgen.show_waiting_time(tasks)