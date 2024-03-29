from random import randint



class Tasks():


    def __init__(self, random: bool = True, size: int = 3):
        
        self.tasks: list[dict[str: int]] = []
        self.size: int = size

        if random:
            for _ in range(size):
                
                rand = randint(1, 10)
                
                self.tasks.append({
                    'num': 0 if len(self.tasks) == 0 else len(self.tasks),
                    'runtime': rand,
                    'timeleft': rand,
                    'arrival': randint(1, 10),
                    'prio': randint(1, 15),
                    'waiting': 0
                })
                
        else:
            
            for task_num in range(size):
                
                self.tasks.append({
                    
                    'runtime': int(input(f'Task {task_num} runtime: ')),
                    'timeleft': None,
                    'arrival': int(input(f'Task {task_num} arrival: ')),
                    'prio': int(input(f'Task {task_num} priority: ')),
                    'waiting': 0 
                })
                
                # timeleft equals runtime at the begining
                self.tasks[task_num]['timeleft'] = self.tasks[task_num].get('runtime')
                print()
        
        self.show_tasks()
        
    
    
    def show_tasks(self) -> print:

        task_num: int

        try:

            print()
            for task_num in range(0, len(self.tasks), 3):
                print(f"""Task {self.tasks[task_num].get('num')}:           Task {self.tasks[task_num+1].get('num')}:           Task {self.tasks[task_num+2].get('num')}:     
    Runtime  - {self.tasks[task_num].get('runtime')}     Runtime  - {self.tasks[task_num+1].get('runtime')}     Runtime  - {self.tasks[task_num+2].get('runtime')}
    Timeleft - {self.tasks[task_num].get('timeleft')}     Timeleft - {self.tasks[task_num+1].get('timeleft')}     Timeleft - {self.tasks[task_num+2].get('timeleft')}
    Arrival - {self.tasks[task_num].get('arrival')}     Arrival - {self.tasks[task_num+1].get('arrival')}     Arrival - {self.tasks[task_num+2].get('arrival')}
    Priority - {self.tasks[task_num].get('prio')}     Priority - {self.tasks[task_num+1].get('prio')}     Priority - {self.tasks[task_num+2].get('prio')}\n"""
                )

        except IndexError:

            if self.size % 3 == 2:

                print(
f"""Task {self.tasks[task_num].get('num')}:           Task {self.tasks[task_num+1].get('num')}:
    Runtime  - {self.tasks[task_num].get('runtime')}     Runtime  - {self.tasks[task_num+1].get('runtime')}
    Timeleft - {self.tasks[task_num].get('timeleft')}     Timeleft - {self.tasks[task_num+1].get('timeleft')}
    Arrival - {self.tasks[task_num].get('arrival')}     Arrival - {self.tasks[task_num+1].get('arrival')}
    Priority - {self.tasks[task_num].get('prio')}     Priority - {self.tasks[task_num+1].get('prio')}\n"""
                )

            #
            elif self.size % 3 == 1:
                
                print(
f"""Task {self.tasks[task_num].get('num')}:     
    Runtime  - {self.tasks[task_num].get('runtime')}
    Timeleft - {self.tasks[task_num].get('timeleft')}
    Arrival - {self.tasks[task_num].get('arrival')}
    Priority - {self.tasks[task_num].get('prio')}\n"""
                )
            #

        print('-'*60)
            

        
    def show_waiting_time(self) -> print:
        
        average_time = 0
        
        for task in self.tasks:
            print(f'Task {task.get("num")} - waiting time: {task.get("waiting")}')
            average_time += task.get('waiting')
        
        average_time /= len(self.tasks)
        
        print(f'[ Average waiting time: {average_time:.1f} ]')    
        
    
    
    def __getitem__(self, slicer: slice):
        return self.tasks[slicer] 
    
    def __setitem__(self, index: int, new_task: dict[str:int]):

        if type(new_task) is dict:
            self.tasks[index] = new_task

        else:
            raise TypeError('inserted task type is not dict[str:int]')

    def __iter__(self):
        return iter(self.tasks)

    def __len__(self):
        return len(self.tasks)




if __name__ == "__main__":
    a = Tasks()
    print(a[0])