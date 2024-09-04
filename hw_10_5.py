import multiprocessing
from datetime import datetime

def read_info(name):
    all_data = []
    with open(name, 'r') as file_open:
        while True:
            line = file_open.readline()
            if line == '':
                break
            all_data.append(line)


# start = datetime.now()
filenames = [f'./file {number}.txt' for number in range(1, 5)]
# for name in filenames:
#     read_info(name)
# end = datetime.now()
# print(end - start)

if __name__ == '__main__':
    start = datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)

    end = datetime.now()
    print(end - start)



