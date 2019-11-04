import sys
from shutil import copyfile

def batch_copy_file() :
    first_source = r"E:\test\logo.svg"
    second_source = r"E:\test\logo.png"

    first_target = r"E:\test\logo"
    second_target = r"E:\test\logo"
    # adding exception handling
    file_number = 0
    while file_number < 300:
        first_target = r"E:\test\logo"
        second_target = r"E:\test\logo"
        first_target = first_target + str(file_number) + str(".svg")
        second_target = second_target + str(file_number) + str(".png")
        try:
            copyfile(first_source, first_target)
            copyfile(second_source, second_target)
        except IOError as e:
            print("Unable to copy file. %s" % e)
            exit(1)
        except:
            print("Unexpected error:", sys.exc_info())
            exit(1)
        file_number += 1
    print("\nFile copy done!\n")


if __name__ == '__main__':
    batch_copy_file()