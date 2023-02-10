import os
import time
import openai

def summarize(transcript_root_dir: str, summary_root_dir: str, filename: str, ratio: int) -> None:
    openai.api_key = os.environ['OPENAI_API_KEY']

    text_in = ""
    with open(os.path.join(transcript_root_dir, filename+".txt")) as f:
        text_in = f.read()

    # TIME BLOCK
    print("SUMMARIZING...")
    start_time = time.time()

    target_length = int(len(text_in.split(" ")) * ratio)
    response = openai.Completion.create(
        engine="curie",
        prompt=f"summarize: {text_in} ({target_length} words)",
        max_tokens=int(target_length * 1.33),
        n=1,
        stop=None,
        temperature=0.5,
    )
    text_out = response["choices"][0]["text"].strip()
    
    stop_time = time.time()
    print("DONE SUMMARIZING")
    # TIME BLOCK

    print("\n*** STATS ***")
    print("Time (s): \t", stop_time - start_time)
    print("WordCount:\t", len(text_out.split()))

    with open(os.path.join(summary_root_dir, filename+".txt"), 'w') as f:
        f.write(text_out)

