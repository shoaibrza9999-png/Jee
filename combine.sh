#!/bin/bash
mkdir -p final_videos

# Combine
ffmpeg -y -i media/videos/chemistry_scenes_1/720p30/Scene1.mp4 -i audio/audio_1.mp3 -c:v copy -c:a aac -shortest final_videos/Video1.mp4
ffmpeg -y -i media/videos/chemistry_scenes_1/720p30/Scene2.mp4 -i audio/audio_2.mp3 -c:v copy -c:a aac -shortest final_videos/Video2.mp4
ffmpeg -y -i media/videos/chemistry_scenes_1/720p30/Scene3.mp4 -i audio/audio_3.mp3 -c:v copy -c:a aac -shortest final_videos/Video3.mp4
ffmpeg -y -i media/videos/chemistry_scenes_2/720p30/Scene4.mp4 -i audio/audio_4.mp3 -c:v copy -c:a aac -shortest final_videos/Video4.mp4
ffmpeg -y -i media/videos/chemistry_scenes_2/720p30/Scene5.mp4 -i audio/audio_5.mp3 -c:v copy -c:a aac -shortest final_videos/Video5.mp4
ffmpeg -y -i media/videos/chemistry_scenes_2/720p30/Scene6.mp4 -i audio/audio_6.mp3 -c:v copy -c:a aac -shortest final_videos/Video6.mp4
ffmpeg -y -i media/videos/chemistry_scenes_3/720p30/Scene7.mp4 -i audio/audio_7.mp3 -c:v copy -c:a aac -shortest final_videos/Video7.mp4
ffmpeg -y -i media/videos/chemistry_scenes_3/720p30/Scene8.mp4 -i audio/audio_8.mp3 -c:v copy -c:a aac -shortest final_videos/Video8.mp4
ffmpeg -y -i media/videos/chemistry_scenes_3/720p30/Scene9.mp4 -i audio/audio_9.mp3 -c:v copy -c:a aac -shortest final_videos/Video9.mp4
ffmpeg -y -i media/videos/chemistry_scenes_3/720p30/Scene10.mp4 -i audio/audio_10.mp3 -c:v copy -c:a aac -shortest final_videos/Video10.mp4
