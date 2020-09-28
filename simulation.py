#!/usr/bin/env python
# -*- coding: utf-8 -*-

#IS211 Week5  assignment5  Filename simulation.py
#Lang | 9/27/2020 | The basics(step by stepish) are already in the text
# Ch 3.5 Queues: e.g. class Queue was already implemented in text (it is very helpful)
# It is a bit easier, in a sense it gives you confident and comfort but still not easy at all for me.
# I was feeling a bit more confident but then I found out I am very noob in class
import csv
import urllib2
import argparse


class Queue:
    def __init__ (self):
        self.items = []
    def is_empty (self):
        return self.items == []
    def enqueue (self, item):
        self.items.insert (0, item)
    def dequeue (self):
        return self.items.pop ()
    def size (self):
        return len (self.items)

class Server:
    def __init__ (self):
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        if self.current_task ! None:
            self.time_remaining = self.time_remaining - 1
            if self.time_remaining <= 0:
                self.current_task  None

    def busy(self):
        if self.current_task != None:
            return True
        else:
            return False

    def start_next (self, new_task):
        self.current_task = new_task
        self.time_remaining = new_task.get_time()

class Request:
    def __init__ (self,time):
        self.timestamp = time
        self.run_time  = run_time

    def get_stamp (self):
        return self.timestamp

    def get_time (self):
        return self.run_time

    def wait_time (self, current_time):
        return current_time - self.timestamp

def downloadData(url):
    file = urllib2.urlopen(url)
    return file

def simulateOneServer(file):
    data_server  = Server()
    server_queue = Queue()
    waiting_times = []

#Still struggles with iteration and implementing steps from psudocode
    for line in readfile:
        request_time = int(line[0])
        run_time = int(line[2])
        task = Request (request_time,run_time)
        server_queue.enqueue(task)

        if (not data_server.busy()) and (not server_queue.is_empty()):
            next_task = server_queue.dequeue()
            waiting_times.append(next_task.wait_time(request_time))

        data_server.tick()

    average_wait = sum(waiting_times) / len(waiting_times)
    print("Average Wait %6.2f secs %3d tasks remaining."
        % (aavearge_wait, server_queue.size()))

def simulateManyServer(file, server_amount):
    request_time = Queue()
    server_queue = Queue()
    waiting_times = []

    for line in readfile:
        request_time = int(line[0])
        run_time = int(line[2])
        task = Request (request_time,run_time)
        server_queue.enqueue(task)

    latency = 0
    counter = 0

    while counter < server_amount:
        server_queue.enqueue(Server())
        counter += 1

    while not request_time.is_empty():
        #I stuck here with how to process,implement
        #One solutoin was to have another function to be call here
        #but I'm also not 100% clear how to do and complete that also.

#________________________________________________________
#This function is not complete or not sure will be needed.
def Next_Server():
    #get next server from servers (queue)


def main():
    if not args.url:
        raise sys.exit()
    try:
        file = downloadData(args.url)
    except urllib2.URLError:
        print ("You must enter a valid URL.")
        raise

    else:
        if not args.servers:
            simulateOneServer(file)
        else:
            simulateManyServer(file,args.servers)

if __name__ = '__main__':
    main()
