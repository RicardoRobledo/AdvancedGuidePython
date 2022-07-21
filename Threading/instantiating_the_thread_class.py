'''
Created on 30 may. 2021

@author: RSSpe

The class Thread defines a single constructor that takes up
to six optional arguments:

class threading.Thread(group=None,
                       target=None,
                       name=None,
                       args=(),
                       kwargs={},
                       daemon=None)
                       
themeaning of these arguments is:
• group should be None; reserved for future extension when
a ThreadGroup class is implemented.
• target is the callable object to be invoked by the run() method. Defaults
to None, meaning nothing is called.
• name is the thread name. By default, a unique name is constructed of the form
“Thread-N” where N is an integer.
• args is the argument tuple for the target invocation. Defaults to (). If a single
argument is provided the tuple is not required. If multiple arguments are provided then each argument is an element within the tuple.
• kwargs is a dictionary of keyword arguments for the target invocation.
Defaults to {}.
• daemon indicates whether this thread runs as a daemon thread or not. If
not None, daemon explicitly sets whether the thread is daemonic. If None (the
default), the daemonic property is inherited from the current thread.
'''

from threading import Thread, local, currentThread
from random import randint
from time import sleep
import threading


def simple_worker():
    print('hello')
    
# Create a new thread and start it
# The thread will run the function simple_worker
#t1 = Thread(target=simple_worker)
#t1.start()

'''
The Thread Class

The key methods are:
• start() Start the thread’s activity. It must be called at most once per thread
object. It arranges for the object’s run() method to be invoked in a separate
thread of control. This method will raise a RuntimeError if called more than
once on the same thread object.
• run() Method representing the thread’s activity. You may override this
method in a subclass. The standard run() method invokes the callable object
passed to the object’s constructor as the target argument, if any, with positional
and keyword arguments taken from the args and kwargs arguments,
respectively. You should not call this method directly.
• join(timeout = None) Wait until the thread sent this message terminates.
This blocks the calling thread until the thread whose join()method is called
terminates. When the timeout argument is present and not None, it should be a
floating-point number specifying a timeout for the operation in seconds (or
fractions thereof). A thread can be join()ed many times.
• name A string used for identification purposes only. It has no semantics.
Multiple threads may be given the same name. The initial name is set by the
constructor. Giving a thread a name can be useful for debugging purposes.
• ident The ‘thread identifier’ of this thread or None if the thread has not been
started. This is a nonzero integer.
'''

def simple_worker2():
    print('hello')

#t1 = Thread(target=simple_worker2)
#t1.start()
#print(f"---->{t1.getName()}")
#print(f"---->{t1.ident}")
#print(f"---->{t1.is_alive()}") 


def worker():
    for i in range(0, 10):
        print('.', end='', flush=True)
        sleep(1)

print('Starting')
# Create read object with reference to worker function
#t = Thread(target=worker)
# Start the thread object
#t.start()
# Wait for the thread to complete
#t.join()

print('\nDone')


'''
The Threading Module Functions

There are a set of threading module functions which support working with
threads; these functions include:
• threading.active_count() Return the number of Thread objects currently alive. The returned count is equal to the length of the list returned
by enumerate().
• threading.current_thread() Return the current Thread object, corresponding to the caller’s thread of control. If the caller’s thread of control was
not created through the threading module, a dummy thread object with
limited functionality is returned.
• threading.get_ident() Return the ‘thread identifier’ of the current
thread. This is a nonzero integer. Thread identifiers may be recycled when a
thread exits and another thread is created.
• threading.enumerate()Return a list of all Thread objects currently
alive. The list includes daemon threads, dummy thread objects created
by current_thread() and the main thread. It excludes terminated threads
and threads that have not yet been started.
• threading.main_thread()Return the main Thread object
'''

print(threading.active_count())
print(threading.current_thread())
print(threading.get_ident())
print(threading.enumerate())
print(threading.main_thread())



def worker2(msg):
    
    for i in range(0, 10):
        print(msg, end='', flush=True)
        sleep(1)


print('Starting')
#t1 = Thread(target=worker2, args='A')
#t2 = Thread(target=worker2, args='B')
#t3 = Thread(target=worker2, args='C')
#t1.start()
#t2.start()
#t3.start()
#t1.join()
#t2.join()
#t3.join()
print('Done')

'''
Extending the Thread Class
The second approach to creating a Thread mentioned earlier was to subclass the
Thread class. To do this you must
1. Define a new subclass of Thread.
2. Override the run() method.
3. Define a new __init__() method that calls the parent class __init__()
method to pass the required parameters up to the Thread class constructor.
'''

class WorkerThread(Thread):
    def __init__(self, daemon=None, target=None, name=None):
        super().__init__(daemon=daemon, target=target, name=name)
    
    def run(self):
        for i in range(0, 10):
            print('.', end='', flush=True)
            sleep(1)


print('Starting')
#t = WorkerThread()
#t.start()
print('\nDone')


'''
Daemon Threads

A thread can be marked as a daemon thread by setting the daemon property to true
either in the constructor or later via the accessor property.
For example:
'''

def worker3(msg):
    for i in range(0, 10):
        print(msg, end='', flush=True)
        sleep(1)

print('Starting')
# Create a daemon thread
#d = Thread(daemon=True, target=worker3, args='C')
#d.start()
#sleep(5)
print('Done\n\n')

'''
Naming Threads
Threads can be named; which can be very useful when debugging an application
with multiple threads.
In the following example, three threads have been created; two have been
explicitly given a name related to what they are doing while the middle one has
been left with the default name. We then start all three threads and use the
threading.enumerate() function to loop through all the currently live
threads printing out their names:
'''

def worker4(msg):
    for i in range(0,10):
        print(msg, end='', flush=True)
        sleep(1)


t1 = Thread(name='worker', target=worker4, args='A')
t2 = Thread(target=worker4, args='B') # use default name e.g. Thread-1
d = Thread(daemon=True, name='daemon', target=worker4, args='C')

#t1.start()
#t2.start()
#d.start()

print()
#for t in threading.enumerate():
#    print(t.getName())


'''
Thread Local Data

In some situations each Thread requires its own copy of the data it is working
with; this means that the shared (heap) memory is difficult to use as it is inherently
shared between all threads
'''

def show_value(data):
    try:
        val = data.value
    except AttributeError:
        print(currentThread().name, ' - No value yet')
    else:
        print(currentThread().name, ' - value =', val)

def worker5(data):
    show_value(data)
    data.value = randint(1, 100)
    show_value(data)

print(currentThread().name, ' - Starting')
local_data = local()
show_value(local_data)

t=None
print("-----")
for i in range(2):
    t = Thread(name='W' + str(i),
               target=worker5, args=[local_data])
    
    t.start()
t.join()
print("-----")

show_value(local_data)
print(currentThread().name, ' - Done')

'''
On the above example the first function attempts to access a value in the thread local data object. If the
value is not present an exception is raised (AttributeError). The
show_value() function catches the exception or successfully processes the
data.
• The worker function calls show_value() twice, once before it sets a value in
the local data object and once after. As this function will be run by separate
threads the currentThread name is printed by the show_value()
function.'''


'''
Timer

The signature of the Timer class constructor is:
Timer(interval, function, args = None, kwargs = None)
'''

from threading import Timer


def hello():
    print('hello')

print('Starting')
t = Timer(5, hello)
t.start()

print('Done')







