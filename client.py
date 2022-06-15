import socket
import threading
import json
import os


class Main():
    def __init__(self,host="192.168.1.5"):
        self.directory = (os.path.split(
            os.path.realpath(__file__))[0]).split("\\")
        self.directory = "/".join(self.directory)+"/"
        self.tcp_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            self.tcp_client.connect((host,8765))
        except ConnectionRefusedError:
            print("[WinError 10061] 由于目标计算机积极拒绝，无法连接。\r\n")
            exit(0)
        self.content = self.tcp_client.recv(1024)
        print(self.content.decode("utf-8"))
        self.start_client()
    def start_client(self):
        while True:
            user_name = input("")
            if len(user_name) > 12:
                print("昵称的长度不能超过12个字符\r\n")
            elif " " in user_name:
                print("昵称中不能带有空格呦\r\n")
            elif user_name == "":
                print("昵称不能为空\r\n")
            else:
                self.tcp_client.send(user_name.encode("utf-8"))
                r = self.tcp_client.recv(1024).decode("utf-8")
                if r == "1":
                    print("昵称已存在,换一个试试吧\r\n")
                else:
                    print(r)
                    break
        r = threading.Thread(target=self.recv)
        s = threading.Thread(target=self.send)
        r.start()
        s.start()
    def recv(self):
        while True:
            try:
                content = self.tcp_client.recv(1024).decode("utf-8")
                if content.split("[")[0] == 'file':
                    try:
                        f = open(content[5:-1],"rb")
                        file_read = f.read()
                        f.close()
                        if "/" in content:
                            file_name = content[5:-1].split("/")[-1]
                        elif "\\" in content:
                            file_name = content[5:-1].split("\\")[-1]
                        else:
                            file_name = content[5:-1]
                        self.tcp_client.send(bytes(json.dumps([file_name,file_read.decode('utf-8')]).encode("utf-8")))
                    except :
                        self.tcp_client.send("失败".encode("utf-8"))
                        continue
                elif content == "reception_file":
                    try:
                        file_list = json.loads(self.tcp_client.recv(1024**2*20))
                        f = open(f"{self.directory}[接收]{file_list[0]}","wb")
                        f.write(file_list[1].encode('utf-8'))
                        f.close()
                        self.tcp_client.send("1".encode("utf-8"))
                    except:
                        self.tcp_client.send("2".encode("utf-8"))
                elif content == "exit":
                    print("你已经成功退出")
                    os._exit(0)
                elif content != "":
                    print(content)
            except ConnectionResetError:
                print("[WinError 10054] 远程主机强迫关闭了一个现有的连接。")
                exit(0)
    def send(self):
        while True:
            try:
                content = input("")
                self.tcp_client.send(content.encode("utf-8"))
            except:
                continue

if __name__ == '__main__':
    Main(host="你的服务器IP地址")
