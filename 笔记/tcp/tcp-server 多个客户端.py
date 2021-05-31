import socket


def main():
    # 1.买个手机（创建套接字）
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2.插上手机卡（绑定本地信息）
    tcp_server_socket.bind(("", 7891))

    # 3.将手机设置成正常的响铃模式（让默认的套接字由主动变成被动）
    tcp_server_socket.listen(128)

    # 4.等待别人的电话到来（等待客户端的链接 accept）
    while True:
        print('----等待一个新的客服端到来----')
        client_socket, clientAddr = tcp_server_socket.accept()
        print('----一个新的客服端已经到来-----\n---%s---' % str(clientAddr))
        while True:# 多次服务，等待客户端
            # recv默认会堵塞
            recv_data = client_socket.recv(1024)
            if recv_data:
                print("客服端收到的请求是：%s" % recv_data.decode("gbk"))
            else:
                break
            # 如果recv解堵塞，那么有两种方式：
            # 1.客户端发送过来数据
            # 2.客户端调用close导致
            if recv_data:
                client_socket.send('服务端已处理'.encode('gbk'))
            # if none:  if false: 都不成立
            else:
                break
        # 关闭套接字
        client_socket.close()
        print("已经为此客户服务完毕")

    tcp_server_socket.close()


if __name__ == "__main__":
    main()
