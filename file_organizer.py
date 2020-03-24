import os
import sys
import time
import logging
import re
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import pathlib
import datetime
import os.path

""" 
Program organize file in your dictionary. The job is to copy files to folder with their extension 

How to use program:
    1: chose path to your file
    2: run program
    3: copy some file into your folder
"""

#TODO use one class for all methods
#TODO make universal "create_path" function, use lib path. It will be working with linux to


basic_path = "C:\\Users\\matejko\\Desktop"


class HelperFunctions:
    @staticmethod
    def find_file_extension(filename):
        return re.search('(?<=\.).*', filename).group(0)

    @staticmethod
    def create_path(path, *args):
        for arg in args:
            path += "\\" + arg
        return path


class MyHandler(FileSystemEventHandler):
    def __init__(self, ignored_files=None):
        logging.info('handler initialized')
        if ignored_files is None:
            self.ignored_files = []
        else:
            self.ignored_files = ignored_files

    def on_modified(self, event):
        for filename in os.listdir(basic_path):
            index = 0
            time = datetime.datetime.now()
            try:
                ext = HelperFunctions.find_file_extension(filename)
            except AttributeError:
                continue
            year_path = HelperFunctions.create_path(basic_path, ext, str(time.strftime("%Y-%m")))
            if ext not in os.listdir(basic_path):
                folder_path = HelperFunctions.create_path(basic_path, ext)
                os.mkdir(folder_path)
            try:
                os.mkdir(year_path)
            except:
                print(year_path, 'folder already exist')
            src = HelperFunctions.create_path(basic_path, filename)
            # os.chmod(basic_path, 0o777)
            destination_path = HelperFunctions.create_path(year_path, filename)
            try:
                os.rename(src, destination_path)
            except:
                self._copy_file(src, destination_path, ext=ext)

    def _copy_file(self, src, destination_path, ext, index=0):
        try:
            assert os.path.isfile(destination_path) == True
            assert os.path.isfile(src) == True
        except AssertionError as e:
            return 'file is already copied'
        ext_len = (len(ext) + 1)
        index += 1
        try:
            new_destination_path = destination_path[:-ext_len] + '_' + str(index) + '.' + ext
            print('new destiny:    ', new_destination_path)
            os.rename(src, new_destination_path)
        except FileExistsError as e:
            if index < 20:
                self._copy_file(src, destination_path, ext, index=index)
            else:
                print('too many the same files, i will left it here!')


# basic_path = "C:\\Users\\matejko\\Downloads\\Python\\Download"
print(os.listdir(basic_path))
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, basic_path, recursive=False)
observer.start()
try:
    while True:
        time.sleep(100)
except KeyboardInterrupt:
    observer.stop()
observer.join()
