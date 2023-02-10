import os
import time
import whisper

def transcribe(podcast_root_dir: str, transcript_root_dir: str, filename: str, model: str) -> None:
    model = whisper.load_model(model, device="cuda")

    # TIME BLOCK
    print("TRANSCRIBING...")
    start_time = time.time()

    result = model.transcribe(os.path.join(podcast_root_dir, filename+".mp3"))
    text = str.strip(result["text"])
    
    stop_time = time.time()
    print("DONE TRANSCRIBING")
    # TIME BLOCK


    print("\n*** STATS ***")
    print("Time (s): \t", stop_time - start_time)
    print("WordCount:\t", len(text.split()))

    with open(os.path.join(transcript_root_dir, filename+".txt"), 'w') as f:
        f.write(text)