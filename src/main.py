import os
import argparse
from modules import transcribe, summarize
from dotenv import load_dotenv
load_dotenv()

PODCAST_ROOT_DIR =  os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tmp_podcasts")
TRANSCRIPT_ROOT_DIR =  os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tmp_transcripts")
SUMMARY_ROOT_DIR =  os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tmp_summaries")

FILENAME = "000_welcome"
TRANSCRIPT_MODEL = "base.en"
SUMMARY_RATIO = 0.5


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument( "-m", "--mode", type=str, choices=['t', 's'], help="mode flag (t or s)", required=True)
    args = parser.parse_args()

    if args.mode == "t":
        print("=== BEGINNING TRANSCRIPTION ===")
        transcribe(PODCAST_ROOT_DIR, TRANSCRIPT_ROOT_DIR, FILENAME, TRANSCRIPT_MODEL)
    else:
        print("=== BEGINNING SUMMARIZATION ===")
        summarize(TRANSCRIPT_ROOT_DIR, SUMMARY_ROOT_DIR, FILENAME, SUMMARY_RATIO)
