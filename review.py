# Review 1

def add_to_list(value, my_list=[]):
    my_list.append(value)

    return my_list

"""
mutable object should not be used as default argument, 
otherwise the second time you call the function the my_list argument will contain the value from the first call,
as shown below.
"""

def add_to_list_fix(value, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(value)

    return my_list


# Review 2

def format_greeting(name, age):
    return "Hello, my name is {name} and I am {age} years old."

"""
improper usage of format string
"""

def format_greeting_fix(name, age):
    return f"Hello, my name is {name} and I am {age} years old."


# Review 3

class Counter:
    count = 0

    def __init__(self):
        self.count += 1

    def get_count(self):
        return self.count

class CounterFix:
    count = 0

    def __init__(self):
        self.__class__.count += 1

    @classmethod
    def get_count(cls):
        return cls.count


"""
The problem is that the author confused the usage of class attribute and instance attribute
In the __init__ method the += operator will get the initial value of self.count from cls.count because self.count are not defined before, 
add 1 and then assign to self.count.
Therefore, cls.count is left unchanged, while self.count is created with value 1 every time a object is instantiated. 
"""

# Review 4

import threading


class SafeCounter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

class SafeCounterFix:
    def __init__(self):
        self.count = 0
        self.lock = threading.Lock()

    def increment(self):
        with self.lock:
            self.count += 1


def worker(counter):
    for _ in range(1000):
        counter.increment()


counter = SafeCounter()

threads = []

for _ in range(10):
    t = threading.Thread(target=worker, args=(counter,))

    t.start()

    threads.append(t)

for t in threads:
    t.join()

"""
The problem is that raise condition is not considered. 
the increment method is not a atomic operation, and not thread-safe, but called in multiple threads,
"""


# Review 5
def count_occurrences(lst):
    counts = {}
    for item in lst:
        if item in counts:
            counts[item] =+ 1
        else:
            counts[item] = 1
    return counts

def count_occurrences_fix(lst):
    counts = {}
    for item in lst:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts

import collections
def count_occurrences_fast(lst):
    return collections.Counter(lst)

"""
'+=' should be used, not '=+'. 
What's more, Counter from collections is a better tool for this job
"""



if __name__ == "__main__":
    print("==================== review 1")
    print(add_to_list(4))
    print(add_to_list(5))

    print(add_to_list_fix(4))
    print(add_to_list_fix(5))

    print("==================== review 3")
    c1 = Counter()
    print(c1.get_count())
    c2 = Counter()
    print(c1.get_count())

    cf1 = CounterFix()
    print(cf1.get_count())
    cf2 = CounterFix()
    print(cf2.get_count())

    print("==================== review 4")
    counter = SafeCounter()

    threads = []
    for _ in range(10):
        t = threading.Thread(target=worker, args=(counter,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print(counter.count)

    counter_fix = SafeCounterFix()

    threads = []
    for _ in range(10):
        t = threading.Thread(target=worker, args=(counter_fix,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print(counter_fix.count)

    print("==================== review 5")
    l = [1,2,3,3,4,5,5,5]
    print(count_occurrences(l))
    print(count_occurrences_fix(l))
    print(count_occurrences_fast(l))
