# Audio_to_video_sample

>**Note**
>only tested on Linux and hardcoded, this is early stages of the product

## inputs:
- json file
   - containing : **time stamps for when speakers talk**

## output: 
- video file

maps audio timestamps to images to create a video that is combined for an output

>**Note**
>for this early version use images, json and audio provided in repository, next version will allow more flexibility 

## how to run
```
python -m venv venv
pip install -U pip
pip install -r requirements.txt
python main.py timestamp_json
```

## default test paths
```
python main.py timestamp.json
```
- 25 seconds average runtime for a 10 seconds long video
