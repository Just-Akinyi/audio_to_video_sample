# audio_to_video_sample

## inputs: 
- audio file 
- json file containing
   - number of speakers
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

