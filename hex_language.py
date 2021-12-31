import socket
import os
import tkinter as gui


class console:
    def writeline(lines, text):
        for i in range(lines):
            print()
        print(text)

    def nextline(lines):
        for i in range(lines):
            print()

    def write(text):
        print(text)

    def clear():
        os.system('clear')


class user:
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)


def IFc(condition, code):
    exec("""if {}:(
      {})""".format(condition, code))


class command:
    def newFolder(folder_name):
        os.mkdir(folder_name)

    def deleteFolder(folder_name):
        os.rmdir(folder_name)

    def delete(filename):
        os.remove(filename)

    def rename(filename):
        os.rename(filename)


def forever(code):
    while True:
        exec(code)
