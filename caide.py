#!/usr/bin/python3
import argparse
import sys
from os import makedirs
from os.path import abspath, expanduser, join
from pathlib import Path
from shutil import copy2, rmtree
from subprocess import PIPE, Popen
from tempfile import TemporaryDirectory
from remove_comments import remove_comments


def check_exists(docker_image):
    proc = Popen(['docker', 'images'], stdout=PIPE)
    proc.wait()

    if proc.returncode != 0:
        exit(proc.returncode)

    if docker_image not in proc.stdout.read().decode():
        print(f'Image {docker_image} not found.')
        exit(1)


def remove_comment(code):
    return remove_comments(code)


def main():
    check_exists('caide-docker')
    parser = argparse.ArgumentParser(
        'Caide-Docker', description='Inline c++ code from libraries in a single file.')

    parser.add_argument(
        'main_file', help='Path to the .cpp that contains the main function.')
    parser.add_argument('-l', '--libraries', default='',
                        help='List of libraries to be used other than the std. Use comma (,) to separate several libraries.')
    parser.add_argument('-o', '--output', default='',
                        help='Name of file to store final submission. stdout is used by default.')
    parser.add_argument('-p', '--prune-comments', default='', action='store_true',
                        help='Prune comments from source code.')

    args = parser.parse_args()

    main_file = abspath(args.main_file)
    libraries = [abspath(lib) for lib in args.libraries.split(',') if lib]

    target_folder = Path(abspath(expanduser('~/.caide-docker/tmp')))
    rmtree(target_folder, ignore_errors=True)
    makedirs(target_folder, exist_ok=True)

    copy2(main_file, join(target_folder, 'main.cpp'))

    command = ['docker',
               'run',
               f'--volume={target_folder}:/home/io'] +\
        [f'--volume={lib}:/home/cpplib' for lib in libraries] +\
        ['caide-docker']

    proc = Popen(command)
    proc.wait()

    err = target_folder / 'output.err'
    out = target_folder / 'submission.cpp'

    if err.exists():
        with open(err) as f:
            print(f.read(), file=sys.stderr)

    if out.exists():
        with open(out) as f:
            content = f.read()

        if args.prune_comments:
            content = remove_comment(content)

        file = sys.stdout
        should_close = False

        if args.output:
            file = open(args.output, 'w')
            should_close = True

        print(content, file=file)

        if should_close:
            file.close()


if __name__ == '__main__':
    main()
