# HoK400 and CFM400

#### The Datasets Consisting of *PROFESSIONALLY Edited* Short Videos Accompanied with Background Music and Voice-Overs collected from public video platforms. 

## 1. Introduction

*HoK400* and *CFM400* are two datasets consisting of short videos edited by *professional teams* collected from *public video platforms*. *HoK400* and *CFM400* contain 427 and 401 short videos related to the globally popular games "King of Honors" (alias "Arena of Valor") and "CrossFire Mobile" respectively. Because the main components of a game video are only those stylized 3D models with some transformations and variations generated by the 3D engines, the videos are fine-grained. The *HoK400* dataset is split into 265 and 162 videos for training and testing respectively, while the *CFM400* dataset is split into 270 and 131 videos for training and testing respectively. The data augmentation can be implemented by randomly clipping the videos in the training datasets. As the video lengths are different, we use the beginning 32s clips of the videos in the test datasets for performance evaluation. If the video length is less than 32s, we simply repeat the video until it is longer than 32s.  

The datasets can evaluate the music retrieval performance for short fine-grained videos with or without the popular voice-over modality. By releasing *HoK400* and *CFM400*, we hope the datasets can promote the progress of the video-music retrieval task in the research community.



## 2. How to download

The urls of the datasets are stored in the following txt files.

* HoK400: 'training_part_HoK400.txt'  and  'test_part_HoK400.txt'

* CFM400: 'training_part_CFM400.txt' and 'test_part_CFM400.txt' 

Convenient download.

```
python video_download_script.py --url_list txt_file --saving_path ./saving_dir
```

You may install you-get before the download starts. 

FFmpeg can separate the video and the audio tracks, and the source separator *Spleeter* [[link](https://github.com/deezer/spleeter)] can separate the BGM and the voice-overs.
```
python separating_script --video_path ./video_dir --temporary_audio_saving_path ./temporary_audio_dir --spleeter_res_path  ./separation_dir
```

## 3. Citation

```
{
  author     = {Tingtian Li, Zixun Sun, Haoruo Zhang, Jin Li, Ziming Wu, Hui Zhan, Yipeng Yu, Hengcan Shi},
  title      = {Deep Music Retrieval for Fine-Grained Videos by Exploiting Cross-Modal-Encoded Voice-Overs},
  conference = {ACM SIGIR},
  year       = {2021},
}
```

## 4. The implementation of the video-music retrieval algorithm MRCMV

Codes are coming soon..








