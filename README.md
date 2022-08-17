# Python-Pipe
something I learned about Pipe
1. 对于多进程之前的数据传递，可以使用Multiprocessing.Pipe中的conn.send()和conn.recv()进行数据的传输和接受。但是注意，一个子进程中只能有一个conn.send()和conn.recv()，且只能传递一个参数。参数传递是可以双向传递的。
2. 对于不通过Pipe来进行参数改变的情况，可以在父进程中使用Multiprocessing.Value()进行参数的定义，此举类似于定义的全局变量，子进程中可以通过改变.value的值进行参数的修改。
