import wave
import os
import math
import argparse

def split_wav(name_prefix, file_path, output_dir, chunk_length_minutes):
    try:
        with wave.open(file_path, 'rb') as wf:
            if wf.getcomptype() != 'NONE':
                print(f"Skipping '{file_path}' (unsupported compression type: {wf.getcomptype()})")
                return

            n_channels = wf.getnchannels()
            sample_width = wf.getsampwidth()
            frame_rate = wf.getframerate()
            n_frames = wf.getnframes()

            chunk_frames = int(chunk_length_minutes * 60 * frame_rate)
            num_chunks = math.ceil(n_frames / chunk_frames)

            os.makedirs(output_dir, exist_ok=True)

            for i in range(num_chunks):
                wf.setpos(i * chunk_frames)
                frames = wf.readframes(min(chunk_frames, n_frames - i * chunk_frames))

                chunk_name = os.path.join(output_dir, f"{name_prefix}_chunk_{i+1:03}.wav")
                with wave.open(chunk_name, 'wb') as out_wf:
                    out_wf.setnchannels(n_channels)
                    out_wf.setsampwidth(sample_width)
                    out_wf.setframerate(frame_rate)
                    out_wf.writeframes(frames)

                print(f"Exported: {chunk_name}")

            print(f"Finished processing {file_path}, {num_chunks} chunks saved to {output_dir}\n")

    except (wave.Error, EOFError) as e:
        print(f"Error processing '{file_path}': {e}\n")

parser = argparse.ArgumentParser()
parser.add_argument("--chunk-length", type=int, default=5)
args = parser.parse_args()

input_folder = "./audio/"
output_folder = "output_chunks"

for filename in os.listdir(input_folder):
    if filename.lower().endswith(".wav"):
        input_wav = os.path.join(input_folder, filename)
        name_prefix = os.path.splitext(filename)[0]
        print(f"Processing {input_wav}...")
        split_wav(name_prefix, input_wav, output_folder, chunk_length_minutes=args.chunk_length)
    else:
        print(f"Skipping non-WAV file: {filename}")

print("All files processed.")
