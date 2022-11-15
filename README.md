# audio_to_video_sample

>**Note**
>only tested on Linux and hardcoded, this is an rough

## inputs: 
- audio file .m4a
- json file containing
   - time stamps for when speakers talk

## output: 
- video file

maps audio timestamps to images to create a video that is combined for an output

## how to run
```
python -m venv venv
pip install -U pip
pip install -r requirements.txt
python main.py audio_path timestamp_json
```

