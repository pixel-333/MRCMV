#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import glob
from cup import shell
import argparse


def list_files(folder, pattern='*.mp4'):
    filenames = sorted(glob.glob(folder + pattern))
    return filenames


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--video_path',
                        type=str,
                        default='./videos',
                        help='Path to video files')
    parser.add_argument('--temporary_audio_saving_path', type=str,
                        default='./temporary_audio_path',
                        help='Path to save temporary audio tracks')
    parser.add_argument('--spleeter_res_path', type=str,
                        default='./spleeter_res',
                        help='Path to save splited BGMs and voice-overs')
    opt = parser.parse_args()
    shellexec = shell.ShellExec()

    video_path_list = list_files(opt.video_path + '/')

    for video_idx in range(0, len(video_path_list)):

        input_vidio_name = video_path_list[video_idx]
        output_audio_name = input_vidio_name.split('/')[-1].split('.')[0]
        if not os.path.exists(opt.temporary_audio_saving_path + '/' + output_audio_name + '.aac'):
            video_audio_separate_cmd = 'ffmpeg -i ' + input_vidio_name + ' -vn -acodec copy ' + \
                opt.temporary_audio_saving_path + '/' + output_audio_name + '.aac'
            voice_accompaniment_seprate_cmd = 'spleeter separate -i ' + opt.temporary_audio_saving_path + \
                '/' + output_audio_name + '.aac' + \
                ' -p spleeter:2stems -o ' + opt.spleeter_res_path + '/'

            shellexec.run(video_audio_separate_cmd, timeout=60)
            shellexec.run(voice_accompaniment_seprate_cmd, timeout=60)