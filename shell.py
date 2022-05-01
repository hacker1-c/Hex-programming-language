import os
import socket
try:
    st_file = open('setting-clear first screen.txt')
    if st_file.read() == 'True':
        os.system('cls')
    st_file.close()
except FileNotFoundError:
    ask = input('Do you want to clear the screen? (y/n): ')
    if ask == 'y':
        os.system('cls')

while True:
    command = input('>>> ')
    if command[0:4] == 'hex ':
        last_let = len(command)
        files = command[4:last_let]
        exec(open(f'{files}').read())
    elif command == 'exit':
        try:
            file = open('setting-clear last screen.txt')
            if file.read() == 'True':
                os.system('cls')
            exit()
        except FileNotFoundError:
            ask1 = input('Do you want to clear screen before exit? (y/n): ')
            if ask1 == 'y':
                os.system('cls')
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
        print()
        files = os.listdir()
        for file in files:
            print(file)
        print()
    elif command[0:8] == 'setting ':
        last_let1 = len(command)
        num = 0
        if command[11:last_let1] == '' and command[8:10] == 'y ':
            st_file = open('setting-clear first screen.txt', 'w')
            st_file.write('True')
            st_file.close()
        elif command[11:last_let1] == '' and command[8:10] == 'n ':
            st_file = open('setting-clear first screen.txt', 'w')
            st_file.write('False')
            st_file.close()
        else:
            num += 1
        if command[11:last_let1] == '' and command[10:11] == 'y':
            nd_file = open('setting-clear last screen.txt', 'w')
            nd_file.write('True')
            nd_file.close()
        elif command[11:last_let1] == '' and command[10:11] == 'n':
            nd_file = open('setting-clear last screen.txt', 'w')
            nd_file.write('False')
            nd_file.close()
        else:
            num += 1
        if num > 0:
            print('Error')
        else:
            print('Setting sucessful')

    elif command == 'ip':
        hn = socket.gethostname()
        ip = socket.gethostbyname(hn)
        print(ip)
    elif command == 'hostname':
        hn = socket.gethostname()
        print(hn)
    elif command == 'clear':
        os.system('cls')
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
