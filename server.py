import socket
import traceback
import colors
import sys, getopt


def main(argv):

    flags , port = argv[1].split("=")

    title = """
      __  __         ____             _        _     ____
     |  \/  |_   _  / ___|  ___   ___| | _____| |_  / ___|  ___ _ ____   _____ _ __
     | |\/| | | | | \___ \ / _ \ / __| |/ / _ \ __| \___ \ / _ \ '__\ \ / / _ \ '__|
     | |  | | |_| |  ___) | (_) | (__|   <  __/ |_   ___) |  __/ |   \ V /  __/ |
     |_|  |_|\__, | |____/ \___/ \___|_|\_\___|\__| |____/ \___|_|    \_/ \___|_|
             |___/
    """

    queue = []

    print(colors.B + title + colors.W)

    so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    so.bind(('localhost', int(port)))

    so.listen(100)

    flag = 0

    print(colors.R + "The Server running very soon!!" + colors.W)

    connect, addr = so.accept()

    queue.append(connect)

    while True:
        try:

            print(queue)

            for usr in queue:

                print(colors.G + "Connection Addresses:" + colors.W + colors.O + str(addr) + colors.W)

                str_return = "Welcome to visit my test socket server. Waithing for command"

                usr.sendto(bytes(str_return, 'utf-8'), addr)

                str_recv, temp = connect.recvfrom(1024)

                print(str_recv)

                str_return = str(str_recv)

                usr.sendto(bytes(str_return, 'utf-8'), addr)

        except:
            print(traceback.print_exc())
            connect.close()
            break

    connect.close()

if __name__ == "__main__":
    main(sys.argv)
