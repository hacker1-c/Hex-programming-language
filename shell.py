import os
import socket

ask = input('Do you want to clear the screen? (y/n): ')
if ask == 'y':
    os.system('clear')
while True:
    command = input('>>> ')
    if command[0:4] == 'hex ':
        last_let = len(command)
        files = command[4:last_let]
        exec(open(f'{files}').read())
    elif command == 'exit':
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
help: Help for shell
exit: Exit the shell
""")
    else:
        print('Error')
