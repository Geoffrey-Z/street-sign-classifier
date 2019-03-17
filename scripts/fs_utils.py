from os import listdir, scandir
from os.path import isdir, isfile, join, abspath, splitext

SCRIPT_PATH = abspath(__file__)
PROJ_ROOT = abspath(join(SCRIPT_PATH, join('..', '..')))


def file_ext(file): return splitext(file)[1]


def list_subdirs(d):
    subdirs = [subdir for subdir in listdir(d) if isdir(join(d, subdir))]
    subdirs.sort()
    return subdirs


def list_files(d, ext=None):
    files = [file for file in listdir(d) if isfile(join(d, file))]
    if ext != None:
        files = [file for file in files if file_ext(file) == ext]
    files.sort()
    return files
