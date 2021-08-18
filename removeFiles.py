
# importing the required modules
import os
import shutil
import time

# main function
def main():

    # initializing the count
    deleted_folders_count = 0
    deleted_files_count = 0
    
    # specify the path
    path = "/PATH_TO_DELETE"

    # specify the days
    days = 30

    # converting days to seconds
    # time.time() returns current time in seconds
    seconds = time.time() - (days * 24 * 60 * 60)

    # checking whether the file is present or not
    if os.path.exists(path):

        # iterating over each and every folder and file in the path
        for root_folder, folders, files in os.walk(path):

            # compairing the days
            if seconds >= get_file_or_folder_age(root_folder):

                # removing the folder
                remove_folder(root_folder)
                deleted_folders_count += 1 # increasing count

                # breaking after removing the root_folder
                break

            else:

                # checking folder from the root_folder
                for folder in folders:

                    # folder path
                    folder_path = os.path.join(root_folder, folder)

                    # compairing with days
                    if seconds >= get_file_or_folder_age(folder_path):

                        # invoking remove folder function
                        remove_folder(folder_path)
                        deleted_folders_count += 1 # increasing count

                # checking the current directory files
                for file in files:

                    # file path
                    file_path = os.path.join(root_folder, file)

                    # compairing the days
                    if seconds >= get_file_or_folder_age(file_path):

                        # invoking the remove file function
                        remove_file(file_path)
                        deleted_files_count += 1 # incrementing count

    else:

        # file/folder is not found
        print(f'"{path}" is not found ')
        deleted_files_count += 1 # incrementing count

    print(f"Total Folders Deleted: {deleted_folders_count}")
    print(f"Total Files Deleted: {deleted_files_count}")

def remove_folders(path):

    # removing the folder
    if not shutil.rmtree(path):

        # success message
        print(f"{path} is removed successfully")

    else:

        # faliure message
        print("Unable to delete the "+path)


def remove_file(path):

    # removing the folder
    if not os.remove(path):

        # success message
        print(f"{path} is removed successfully")

    else:

        # faliure message
        print("Unable to delete the "+path)


def get_file_or_folder_age(path):

    # getting ctime of the file/folder
    # time will be in seconds
    ctime = os.start(path).st_ctime

    # returning the time
    return ctime


if __name__ == '__main__':
    main()
        