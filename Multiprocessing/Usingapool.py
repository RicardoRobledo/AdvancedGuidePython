'''
Created on 2 jun. 2021

@author: RSSpe

Creating Processes is expensive in terms of computer resources. It would therefore
be useful to be able to reuse processes within an application. The Pool class
provides such reusable processes.
The Pool class represents a pool of worker processes that can be used to
perform a set of concurrent, parallel operations. The Pool provides methods which
allow tasks to be offloaded to these worker processes.
The Pool class provides a constructor which takes a number of arguments:

class multiprocessing.pool.Pool(processes,
                                initializer, initargs,
                                maxtasksperchild,
                                context)

These represent:
• processes is the number of worker processes to use. If processes is None then the number returned by os.cpu_count() is used.
• initializer If initializer is not None then each worker process will
call initializer(*initargs) when it starts.
• maxtasksperchild is the number of tasks a worker process can complete
before it will exit and be replaced with a fresh worker process, to enable unused
resources to be freed. The default maxtasksperchild is None, which
means worker processes will live as long as the pool.
• context can be used to specify the context used for starting the worker
processes. Usually a pool is created using the function multiprocessing.
Pool(). Alternatively the pool can be created using the Pool() method of a
context object.


The simplest of the methods provided by the Pool for work submission is the map
method:

pool.map(func, iterable, chunksize=None)

This method returns a list of the results obtained by executing the function in
parallel against each of the items in the iterable parameter.
• The func parameter is the callable object to be executed (such as a function or
a method).
• The iteratable is used to pass in any parameters to the function.
• This method chops the iterable into a number of chunks which it submits to the
process pool as separate tasks. The (approximate) size of these chunks can be
specified by setting chunksize to a positive integer. The method blocks until
the result is ready.
'''

# ¿Porque usar    if __name__ == '__main__'?:

'''
Asegúrese de que un nuevo intérprete de Python pueda importar de forma segura el módulo principal sin causar efectos secundarios no deseados (como comenzar un nuevo proceso).
Por ejemplo, usando el método de inicio spawn o forkserver ejecutando este módulo fallaría produciendo RuntimeError

En su lugar, se debe proteger el «punto de entrada» («entry point») del programa utilizando como sigue if __name__ == '__main__':
'''


from multiprocessing import Process, Pool
import os

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def f(name):
    info('function f')
    print('hello', name)

if __name__ == '__main__':
    info('main line')
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()
    


def collect_results(result):
    print('In collect_results: ', result)

def worker(x):
    print('In worker with: ', x)
    return x * x

def main():
    with Pool(processes=2) as pool:
    # get based example
        res = pool.apply_async(worker, [6])
        print('Result from async: ', res.get(timeout=1))

    with Pool(processes=2) as pool:
        # callback based example
        pool.apply_async(worker, args=[4],
                        callback=collect_results)

if __name__ == '__main__':
    main()





















