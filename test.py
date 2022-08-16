import multiprocessing


def sender(conn, flg):
    print("child_flg:{}".format(flg.value))
    if flg.value == 0:
        flg.value = 1
        # conn.send(flg)
        print("send flag:{}".format(flg.value))
    testdata = 0
    conn.send(testdata)
    testdata2 = conn.recv()
    print("testdata2:{}".format(testdata2))
    conn.close()


def receiver(conn, flg):
    # flag = 0
    # while 1:
    testdata = conn.recv()
    print("testdata:{}".format(testdata))
    testdata2 = 2
    conn.send(testdata2)
    if flg.value == 1:
        print("got it")
        flg.value = 2
    elif flg.value == 0:
        print("i dont receive it")
    conn.close()


if __name__ == "__main__":
    # messages to be sent 
    flag = multiprocessing.Value('i', 0)
    print("parent process flag:{}".format(flag.value))

    # creating a pipe 
    parent_conn, child_conn = multiprocessing.Pipe()

    # creating new processes 
    p1 = multiprocessing.Process(target=sender, args=(parent_conn, flag))
    p2 = multiprocessing.Process(target=receiver, args=(child_conn, flag))

    # running processes 
    p1.start()
    p2.start()

    # wait until processes finish 
    p1.join()
    p2.join()
    print("after flag:{}".format(flag.value))
