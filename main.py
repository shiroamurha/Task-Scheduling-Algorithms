from taskgen import Tasks
from fcfs import fcfs
from sjf import sjf
from prio import prio
from round_robin import roundr



cases = {
    '1': lambda t: fcfs(t),
    '2': lambda t: sjf(t, preemp=True),
    '3': lambda t: sjf(t, preemp=False),
    '4': lambda t: prio(t, preemp=True),
    '5': lambda t: prio(t, preemp=False),
    '6': lambda t: roundr(t),
    '7': lambda t: True,
    '0': lambda t: bool(print('     > Exiting . . . <     \n'))
}

menu = f"""{"-"*27}
    CHOOSE AN ALGORITHM
{"-"*27}
    1 - FCFS
    2 - SJF 
    3 - SJF (NPE)
    4 - Priority
    5 - Priority (NPE)
    6 - Round Robin
    7 - Set new tasks
    0 - Exit
NPE = not preemptive
{"-"*27}
> """



def select_mode() -> None:

    run_again = True
    opt = '7'

    while run_again:
        
        if opt == '7':
            random = input('Random? [any char = Y / empty = N]  ')
            size = int(input('no. of tasks: '))

            if random:
                tasks = Tasks(size=size)
            else:
                tasks = Tasks(random = False, size=size)
                    
        opt = input(menu)
        if opt not in '01234567' or opt == '':
            continue
        run_again = cases.get(opt)(tasks) # if 0 returns False
        tasks.reset()

        
        

if __name__ == "__main__":
    select_mode()