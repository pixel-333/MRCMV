#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from cup import shell
import argparse




if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--url_list',
                        type=str,
                        default='./training_part_HoK400.txt',
                        help='Path to url list file')
    parser.add_argument('--saving_path', type=str,
                        default='./',
                        help='Path to save video files')

    opt = parser.parse_args()
    shellexec = shell.ShellExec()
    
    with open(opt.url_list) as f:
        html_list= f.readlines()
        html_list = [line.rstrip() for line in html_list]
    
    for idx in range(0, len(html_list)):

        video_download_cmd = 'you-get -o '+ opt.saving_path + ' -O '+ str(idx) + ' ' + html_list[idx]
        shellexec.run(video_download_cmd, timeout=60)
        time.sleep(3)
