import os
import time
from summarizer import Summarizer
from summarizer.text_processors.coreference_handler import CoreferenceHandler


TRANSCRIPT_ROOT_DIR =  os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tmp_transcripts")
SUMMARY_ROOT_DIR =  os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tmp_summaries")
FILENAME = "000_welcome"
RATIO = 0.5

if __name__ == "__main__":
    text_in = ""
    with open(os.path.join(TRANSCRIPT_ROOT_DIR, FILENAME+".txt")) as f:
        text_in = f.read()


    model = Summarizer(
        sentence_handler=CoreferenceHandler(spacy_model='en_core_web_md', greedyness=.4)
    )

    # TIME BLOCK
    print("SUMMARIZING...")
    start_time = time.time()

    result = model(text_in, ratio=RATIO)
    text_out = ''.join(result)

    stop_time = time.time()
    print("DONE SUMMARIZING")
    # TIME BLOCK

    print("\n*** STATS ***")
    print("Time (s): \t", stop_time - start_time)
    print("WordCount:\t", len(text_out.split()))


    with open(os.path.join(SUMMARY_ROOT_DIR, FILENAME+".txt"), 'w') as f:
        f.write(text_out)