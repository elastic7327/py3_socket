import socket
import colors
import traceback



def main(argv):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect(("localhost", 8800))

    while True:

        try:
            # str_recv = s.recv(1024)

            # print(str_recv + b"\n")

            str_send = input(colors.G +"Input Exit: Exit" + colors.W)

            if str_send == "Exit":
                break

            s.send(bytes(str_send, "utf-8"))

            str_recv = s.recv(1024)

            print("\n" + str(str_recv))

        except:
            print(colors.R +"system error occured " + colors.W)
            print(traceback.print_exc())
            s.close()
            break

    s.close()
