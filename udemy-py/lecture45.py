import os
import datetime

def merge_files(all_files):
    today = datetime.datetime.now()
    file_name = "{}.txt".format(today.strftime("%Y-%m-%d-%H-%M-%S-%f"))
    with open(file_name, 'wt') as output_file:
        for a_file in all_files:
            tmp = open("./" + a_file, 'r')
            output_file.writelines(tmp.readlines())
            output_file.write("\n")
            tmp.close()


if __name__ == '__main__':
    all_files = os.listdir(".")
    merge_files(all_files)
