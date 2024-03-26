import taskgen



def sjf(tasks: list[dict[str: int]], **premp: bool):
        
    time = 1
    task_waiting = True
    
    while task_waiting:
        
        for task in tasks:
            
            if task.get('arriving') == time:
                
                has_smaller = False
                for t in tasks:
                    
                    # if at any point there is a task with less timeleft, doesnt save this task index
                    if t.get('timeleft') < task.get('timeleft'):        
                        has_smaller = True
                        break
                    
                    if not has_smaller:
                        task_num = tasks.index(task)

        
        
        
        
        
        for task in tasks:
            if task.get('timeleft') > 0:
                task_waiting = True
                break
            task_waiting = False
            
            
    
    
    for task in tasks:
        print(f'Task {tasks.index(task)}:')
        task['waiting'] = time -1
        
        
        
        while task.get('timeleft') > 0:
            print(f"    Time [ {time} ] -  Timeleft: {task.get('timeleft')}")
            
            time += 1
            task['timeleft'] -= 1
    print()


if __name__ == "__main__":
    sjf() 
    