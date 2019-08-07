#!/usr/env/bin python3

import time
import os
import subprocess

# See parse_args for supported arguments
configs = [
    dict(tag='train',
         num_img=100,
         img_width=256,
         length=length)
    for length in range(10,11)
] + [
    dict(tag='val',
         num_img=10,
         img_width=256,
         length=length)
    for length in range(10,11)
]




def dict_to_args(config: dict):
    args = []
    for k, v in config.items():
        if v is False:
            continue
        args.append('--%s' % k)
        args.append('%s' % v)

    return args


if __name__ == "__main__":
    main_func = './main.py'
    start = time.time()

    for config in configs:
        args = dict_to_args(config)
        print("Run with args: %s" % args)
        subprocess.run(['python3', main_func] + args)
    print(time.time()-start)

