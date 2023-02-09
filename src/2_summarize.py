from summarizer import Summarizer
from summarizer.text_processors.coreference_handler import CoreferenceHandler


handler = CoreferenceHandler(spacy_model='en_core_web_md', greedyness=.4)

body = ""

model = Summarizer(sentence_handler=handler)
result = model(body, ratio=0.5)
full = ''.join(result)


print("\n\n\n\n\n")
print(full)