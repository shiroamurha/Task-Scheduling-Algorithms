from random import randint




def set_tasks(random: bool = True, size: int = 3) -> list[dict[str: int]]:
    
    tasks: list[dict[str: int]] = []
    
    if random:
        for _ in range(size):
            
            rand = randint(1, 10)
            
            tasks.append({
                'runtime': rand,
                'timeleft': rand,
                'arriving': randint(1, 10),
                'prio': randint(1, 15),
                'waiting': 0
            })
            
    else:
        
        for task_num in range(size):
            
            tasks.append({
                
                'runtime': int(input(f'Task {task_num} runtime: ')),
                'timeleft': None,
                'arriving': int(input(f'Task {task_num} arriving: ')),
                'prio': int(input(f'Task {task_num} priority: ')),
                'waiting': 0 
            })
            
            # timeleft equals runtime at the begining
            tasks[task_num]['timeleft'] = tasks[task_num].get('runtime')
            print()
    
    for task_num in range(0, len(tasks)):        
        print(f"""
    Task {task_num}:
        Runtime - {tasks[task_num].get('runtime')}
        Timeleft - {tasks[task_num].get('timeleft')}
        Arriving - {tasks[task_num].get('arriving')}
        Priority - {tasks[task_num].get('prio')}""")
        
    return tasks
    
    
    
def show_waiting_time(tasks: list[dict[str: int]]) -> None:
    
    average_time = 0
    
    for task_num in range(0, len(tasks)):
        print(f'Task {task_num} - waiting time: {tasks[task_num].get('waiting')}')
        average_time += tasks[task_num].get('waiting')
    
    average_time /= len(tasks)
    
    print(f'[ Average waiting time: {average_time:.1f} ]')            
            
    

if __name__ == "__main__":
    pass