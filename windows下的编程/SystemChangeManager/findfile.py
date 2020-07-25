import os
import os.path

# os.chdir('/')
#
# print([filename for filename in os.listdir('./')])

my_path = []


def list_dir_depth(directory):
    for filename in os.listdir(directory):
        path = os.path.join(directory, filename)
        if os.path.isfile(path):
            my_path.append('f_'+path)
        elif os.path.isdir(path):
            my_path.append('d_'+path)
            try:
                list_dir_depth(path)
            except PermissionError:
                break
            finally:
                print(path)


if __name__ == '__main__':
    list_dir_depth('/')
    print(my_path)








