from taskgen import Tasks
from time import sleep



def roundr(tasks: Tasks):

    timeslice = int(input('enter timeslice: ')) 

    time = 1
    has_task = True

    while has_task:

        for task in tasks:

            if task['timeleft'] < 1:
                continue

            sleep(.1) # delay for debugging
            print('-------------------------')
            print(f'NEW SLICE [Task {task.get("num")}]: ')

            for _ in range(timeslice):
                sleep(.1)
                print(f"    Time [ {time} ] -  Timeleft: {task.get('timeleft')}")

                task['timeleft'] -= 1
                time += 1

                if task['timeleft'] < 1:
                    break

        has_task = False

        for task in tasks:
            if task.get('timeleft') > 0:
                has_task = True
    
    return True



if __name__ == "__main__":
    roundr(Tasks())


