# Audio Splitting Script

A simple Python script to split large `.wav` audio files into smaller chunks (default: 5 minutes).

---

## Quick Start

- Ensure you have python installed ([instructions here](https://realpython.com/installing-python))
- Download the script by clicking the green `<> Code` button and selecting 'Download ZIP'
- Extract the .zip
- In the same folder you extracted the zip to, create a new folder called `audio`
- Place the audio files (`.wav` only) that you want to split up in the `audio` folder
- Your folder structure should look like:

```
example_folder/
  |-splitter.py
  |-audio/
    |-my_audio_example.wav
    |-another_audio_example.wav
```

- Open a terminal window and use `cd` to navigate to the folder you extracted the script in (`example_folder` in the above example)
  - Learn how to do this [here](https://tutorials.codebar.io/command-line/introduction/tutorial.html)
- Run the script with `python3 splitter.py`
  - Your command to run python may be `python3` or it may just be `python`
- This will break up any audio files in the `audio` folder and put the chunks in a new folder called `output_chunks`
- You can optionally specify the length of the chunks with the argument `--chunk-length`
  - for example `python3 splitter.py --chunk-length=3` will do 3 minute chunks instead of 5
