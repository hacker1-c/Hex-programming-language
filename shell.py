import os
import socket

st_file = open('setting-clear first screen.txt')
if st_file.read() == 'True':
    os.system('clear')
st_file.close()
while True:
    command = input('>>> ')
    if command[0:4] == 'hex ':
        last_let = len(command)
        files = command[4:last_let]
        exec(open(f'{files}').read())
    elif command == 'exit':
        file = open('setting-clear last screen.txt')
        if file.read() == 'True':
            os.system('clear')
        exit()
    elif command[0:10] == 'newFolder ':
        last_let = len(command)
        files = command[10:last_let]
        os.mkdir(files)
        print('Create Sucessful\n')
    elif command[0:13] == 'deleteFolder ':
        last_let = len(command)
        files = command[13:last_let]
        os.rmdir(files)
        print('Delete sucessful\n')
    elif command[0:7] == 'delete ':
        last_let = len(command)
        files = command[7:last_let]
        os.remove(files)
        print('Delete sucessful\n')
    elif command == 'rename':
        filename = input('File or Folder name: ')
        rename = input('Rename: ')
        os.rename(filename, rename)
        print('Remane sucessful\n')
    elif command == 'all files':
        files = os.listdir()
        for file in files:
            print(file)
        print()
    elif command[0:8] == 'setting ':
        if command[8:10] == 'y ':
            st_file = open('setting-clear first screen.txt', 'w')
            st_file.write('True')
            st_file.close()
        else:
            st_file = open('setting-clear first screen.txt', 'w')
            st_file.write('False')
            st_file.close()
        if command[10:11] == 'y':
            nd_file = open('setting-clear last screen.txt', 'w')
            nd_file.write('True')
            nd_file.close()
        else:
            nd_file = open('setting-clear last screen.txt', 'w')
            nd_file.write('False')
            nd_file.close()

    elif command == 'ip':
        hn = socket.gethostname()
        ip = socket.gethostbyname(hn)
        print(ip)
    elif command == 'hostname':
        hn = socket.gethostname()
        print(hn)
    elif command == 'clear':
        os.system('clear')
    elif command == 'help':
        print("""hex: Run hex file
newFolder: Create new folder
deleteFolder: Remove folder
delete: Remove normal file
rename: Rename file or folder
hostname: Tell the hostname
ip: Tell the IP address
clear: Clear the screen
setting: Setting the shell
all files: Show all files in this project
help: Help for shell
exit: Exit the shell
""")
    else:
        print('Error')
