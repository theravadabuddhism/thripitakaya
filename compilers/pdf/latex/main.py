#!/usr/bin/env python3
import argparse
import json
import os

import configs
import errors

from compiler_1 import compile


def process_file(path: str):
    content_fpath = os.path.join(os.path.dirname(path), configs.content_filename)
    if not os.path.isfile(content_fpath):
        raise errors.LatexGenError(f"invalid input path '{path}'. contents file {content_fpath} not found")
    with open(content_fpath, 'r') as contents_file:
        contents = json.load(contents_file)
        unit_info = contents[os.path.basename(path)]
    compile(path, unit_info)


def iterate_dir(path: str):
    content_fpath = os.path.join(path, configs.content_filename)
    if not os.path.isfile(content_fpath):
        raise errors.LatexGenError(f"invalid directory '{path}'. CONTENTS.json not found")
    with open(content_fpath, 'r') as contents_file:
        contents = json.load(contents_file)
    for filename in contents.keys():
        process_path(os.path.join(path, filename))


def process_path(path: str):
    if os.path.isdir(path):
        iterate_dir(path)
    else:
        process_file(path)


def arg_parse() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('path')
    return parser.parse_args()


if __name__ == '__main__':
    args = arg_parse()
    process_path(args.path)
