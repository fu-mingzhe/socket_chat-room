import threading
import os
import socket
import time
import random
import json


class main():
    def __init__(self,host=""):
        self.directory = (os.path.split(
            os.path.realpath(__file__))[0]).split("\\")
        self.directory = "/".join(self.directory)+"/"
        self.tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.tcp_server.bind((host, 8765))
        except Exception as e:
            print(e)
            exit(0)
        self.client_dict = {}
        self.client_file = {}
        self.tcp_server.listen(128)
        print("服务器已开启,正在等待用户连接...")
        try:
            while True:
                new_tcp_client, client_info = self.tcp_server.accept()
                print("%s进入聊天室" % (str(client_info)))
                t = threading.Thread(target=self.start_client, args=(
                    new_tcp_client, client_info))
                t.start()
        except:
            pass

    def start_client(self, client, client_info):
        try:
            client.send(
                "欢迎来到PythonSocket聊天室,请先输入你在群里的昵称(不能带有空格呦~)\r\n".encode("utf-8"))
            while True:
                user_name = client.recv(1024)
                if user_name.decode("utf-8") in self.client_dict:
                    client.send("1".encode("utf-8"))
                else:
                    client.send(
                        "昵称创建成功,输入/ls可查看所有在线的人,输入/help可以查看帮助(所有首字符为/的消息都不会发送)\r\n".encode("utf-8"))
                    break
            self.client_dict[user_name.decode("utf-8")] = client
            print("%s[%s]" % (str(client_info), user_name.decode("utf-8")))
            for i in self.client_dict:
                self.client_dict[i].send(self.send_msg(user_name="系统",msg="{}进入聊天室".format(user_name.decode("utf-8"))).encode("utf-8"))
            try:
                while True:
                    content = client.recv(1024).decode("utf-8")
                    if content.isspace():
                        client.send(self.send_msg(user_name="系统",msg="输入的不能为空\r\n").encode("utf-8"))
                        continue
                    elif content[0] == "@":
                        if content[1:].split(" ") == ['']:
                            client.send(self.send_msg(user_name="系统",msg="输入的内容有误,你可以输入@对方昵称(注意对方昵称后面的空格)+消息 即可发动单聊").encode("utf-8"))
                        else:
                            content = content[1:].split(" ")
                            if len(content) >= 2:
                                if content[0] in self.client_dict:
                                    content1 = ""
                                    for i in content[1:]:
                                        content1 += i
                                    if content1.isspace() or content1 == '':
                                        client.send(self.send_msg(user_name="系统",msg="发送的不能为空\r\n").encode("utf-8"))
                                    elif content[0] == user_name.decode("utf-8"):
                                        client.send(self.send_msg(user_name="系统",msg="你不能给自己发消息").encode("utf-8"))
                                    else:
                                        print(f"{client_info}[{user_name.decode('utf-8')}]>>>@{content[0]} {content1}")
                                        client.send(self.send_msg(user_name=f"你发送给{content[0]}",msg=content1).encode("utf-8"))
                                        self.client_dict[content[0]].send(self.send_msg(user_name=f"{user_name.decode('utf-8')}发送给你",msg=content1).encode("utf-8"))
                                else:
                                    client.send(f"[ 时间 {time.ctime()} ]\r\n[ 系统 ] : 输入昵称不存在,你可以输入/ls,即可获得所有登录用户信息\r\n".encode("utf-8"))
                            else:
                                client.send(f"[ 时间 {time.ctime()} ]\r\n[ 系统 ] : 输入的内容有误,你可以输入@对方昵称(注意对方昵称后面的空格)+消息 即可发动单聊\r\n".encode("utf-8"))
                        continue
                    elif content[0] == "/":
                        print("%s[%s]>>>%s" % (str(client_info),
                                               user_name.decode("utf-8"), content))
                        if content[1:] == "help" or content[1:] == "h":
                            client.send(f"[ 时间 {time.ctime()} ]\r\n"
                                        "[ 系统 ]\r\n"
                                        "输入/ls,即可获得所有登录用户信息\r\n"
                                        "输入/help或/h,即可获得帮助\r\n"
                                        "输入@对方昵称(注意对方昵称后面的空格)+消息 即可发动单聊\r\n"
                                        "输入/f或/file,即可发送文件(注意发送的文件大小不能超过20MB)\r\n"
                                        "输入/fi(空格)文件id,即可得对方发送的文件\r\n"
                                        "输入/fd,即可获得所有文件id\r\n"
                                        "输入/e或/exit,就会退出\r\n"
                                        "所有首字符为/的信息都不会发送出去\r\n".encode("utf-8"))
                        elif content[1:] == "e" or content[1:] == "exit":
                            client.send("exit".encode("utf-8"))
                            self.client_dict.pop(user_name.decode('utf-8'))
                            client.close()
                            for i in self.client_dict:
                                self.client_dict[i].send(self.send_msg("系统",f"{user_name.decode('utf-8')}已退出").encode("utf-8"))
                            break
                        elif content[1:] == "f" or content[1:] == "file":
                            client.send(self.send_msg(user_name="系统",msg="请输入文件路径,输入exit取消发送文件").encode("utf-8"))
                            file = client.recv(1024).decode("utf-8")
                            if file == "exit":
                                client.send(self.send_msg(user_name="系统",msg="你已经成功退出发送文件").encode("utf-8"))
                                continue
                            try:
                                client.send(f"file[{file}]".encode("utf-8"))
                                file_list = json.loads(client.recv(1024**2*20))
                                s = "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
                                while True:
                                    a = ""
                                    for i in range(10):
                                        a += random.choice(s)
                                    if a not in self.client_dict:
                                        break
                                self.client_file[a] = file_list
                                print(f"{client_info}[{user_name.decode('utf-8')}]>>>文件:{file_list[0]}:{a}")
                                for i in self.client_dict:
                                    self.client_dict[i].send(self.send_msg(user_name=f"{user_name.decode('utf-8')}发送的文件",msg=f"文件id为{a},文件名为:{file_list[0]}").encode("utf-8"))
                                continue
                            except Exception as e:
                                client.send(self.send_msg(user_name="系统",msg="文件发送失败!").encode("utf-8"))
                                continue
                        elif content[1:] == "fd":
                            if self.client_file == {}:
                                client.send(self.send_msg(user_name="系统",msg="现在还没有人发文件哟!").encode("utf-8"))
                            else:
                                content_id = ""
                                for i in self.client_file:
                                    content_id += f"{self.client_file[i][0]}:{i}  "
                                client.send(self.send_msg(user_name="系统",msg="现有文件有:  "+content_id).encode("utf-8"))
                                
                            
                        elif content[1:3]== "fi":
                            file_id = content[4:]
                            if file_id in self.client_file:
                                file_list = self.client_file[file_id]
                                client.send("reception_file".encode("utf-8"))
                                client.send(bytes(json.dumps(file_list).encode("utf-8")))
                                content = client.recv(1024).decode("utf-8")
                                if content == "1":
                                    client.send(self.send_msg("系统",f"你已经成功下载了文件:{file_list[0]}").encode("utf-8"))
                                else:
                                    client.send(self.send_msg("系统",f"文件:{file_list[0]}下载失败").encode("utf-8"))
                            else:
                                client.send(self.send_msg("系统",f"未找到id为{file_id}的文件").encode("utf-8"))
                        elif content[1:] == "ls":
                            client.send(f"[ 时间 {time.ctime()} ]\r\n"
                                        f"[ 系统 ] 全部用户 : {','.join(list(self.client_dict.keys()))}\r\n".encode("utf-8"))
                        continue
                    else:
                        for i in self.client_dict:
                            self.client_dict[i].send(self.send_msg(user_name=user_name.decode("utf-8"),msg=content).encode("utf-8"))
                        print("%s[%s]>>>%s" % (str(client_info),
                                               user_name.decode("utf-8"), content))
            except ConnectionResetError:
                self.client_dict.pop(user_name.decode("utf-8"))
                client.close()
                print("%s[%s]已退出" % (str(client_info),user_name.decode("utf-8")))
                for i in self.client_dict:
                    self.client_dict[i].send(self.send_msg("系统",f"{user_name.decode('utf-8')}已退出").encode("utf-8"))
        except ConnectionResetError:
            print("%s已退出" % (str(client_info)))

    def get_file_content(file_name, directory):
        try:
            with open(directory+file_name, "rb") as f:
                content = f.read()
            return content
        except Exception as e:
            print(e)
            print("没有下载的文件:%s" % file_name)

    def send_msg(self,user_name, msg):
        return "[ 时间 : %s ]\r\n" \
               "[ %s ] : %s\r\n" % (time.ctime(), user_name, msg)


if __name__ == "__main__":
    main(host="")
