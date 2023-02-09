import os
import time
import whisper

PODCAST_ROOT_DIR =  os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tmp_podcasts")
TRANSCRIPT_ROOT_DIR =  os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tmp_transcripts")
FILENAME = "000_welcome"
MODEL = "base.en"


if __name__ == "__main__":
    model = whisper.load_model(MODEL, device="cuda")

    # TIME BLOCK
    print("TRANSCRIBING...")
    start_time = time.time()

    result = model.transcribe(os.path.join(PODCAST_ROOT_DIR, FILENAME+".mp3"))
    text = str.strip(result["text"])
    
    stop_time = time.time()
    print("DONE TRANSCRIBING")
    # TIME BLOCK


    print("\n*** STATS ***")
    print("Time (s): \t", stop_time - start_time)
    print("WordCount:\t", len(text.split()))

    with open(os.path.join(TRANSCRIPT_ROOT_DIR, FILENAME+".txt"), 'w') as f:
        f.write(text)