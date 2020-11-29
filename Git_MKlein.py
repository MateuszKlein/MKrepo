import os
import random


def get_model_record():
    model_labels = ['A', 'B', 'C']
    label = model_labels[random.randint(0, 2)]
    output = random.randint(0, 1000)
    time = random.randint(0, 1000)

    return f'{label} ; {output} ; {time}s; \n'


def task_a():
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    times_of_day = ['morning', 'evening']
    file_header = ' Model; Output value; Time of computation; \n'

    for day in days:
        if not os.path.exists(day):
            os.mkdir(day)

        for time in times_of_day:
            dir_r_path = os.path.join(day, time)
            if not os.path.exists(dir_r_path):
                os.mkdir(dir_r_path)

            with open(os.path.join(dir_r_path, 'Solutions.csv'), 'w+') as file:
                file.writelines([
                    file_header,
                    get_model_record()
                ])


def task_b():
    sum_time = 0
    for d in os.listdir(os.getcwd()):
        if os.path.isdir(d):
            for subdir in os.listdir(d):
                sdir_path = os.path.join(d, subdir)
                if os.path.isdir(sdir_path):
                    for file in os.listdir(sdir_path):
                        with open(os.path.join(sdir_path, file), 'r') as file:
                            lines = file.readlines()
                            sum_time += sum([float(x.split(';')[2].strip()[:-1]) for x in lines[1:]])
    return sum_time
