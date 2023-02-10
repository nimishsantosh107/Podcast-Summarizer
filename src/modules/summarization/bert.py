import os
import time
from summarizer import Summarizer
from summarizer.text_processors.coreference_handler import CoreferenceHandler

def summarize(transcript_root_dir: str, summary_root_dir: str, filename: str, ratio: int) -> None:
    text_in = ""
    with open(os.path.join(transcript_root_dir, filename+".txt")) as f:
        text_in = f.read()


    model = Summarizer(
        sentence_handler=CoreferenceHandler(spacy_model='en_core_web_md', greedyness=.4)
    )

    # TIME BLOCK
    print("SUMMARIZING...")
    start_time = time.time()

    result = model(text_in, ratio=ratio)
    text_out = ''.join(result)

    stop_time = time.time()
    print("DONE SUMMARIZING")
    # TIME BLOCK

    print("\n*** STATS ***")
    print("Time (s): \t", stop_time - start_time)
    print("WordCount:\t", len(text_out.split()))


    with open(os.path.join(summary_root_dir, filename+".txt"), 'w') as f:
        f.write(text_out)