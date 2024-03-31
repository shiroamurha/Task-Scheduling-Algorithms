from taskgen import Tasks
from fcfs import fcfs
from sjf import sjf



cases = {
    '1': lambda t: bool(bool(fcfs(t))+1),
    '2': lambda t: bool(bool(sjf(t, preemp=True))+1),
    '3': lambda t: bool(bool(sjf(t, preemp=False))+1),
    '4': lambda t: ...,
    '5': lambda t: ...,
    '6': lambda t: ...,
    '0': lambda t: False  
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
    0 - Exit
NPE = not preemptive
{"-"*27}
> """



def select_mode() -> None:

    random = input('Random? [any char = Y / empty = N]  ')

    if random:
        tasks = Tasks()

    else:
        size = int(input('no. of tasks: '))
        tasks(random = False, size=size)
    
    run_again = True

    while run_again:

        opt = input(menu)
        run_again = bool(cases.get(opt)(tasks)) # if 0 returns False

        tasks.reset()
        


if __name__ == "__main__":
    select_mode()