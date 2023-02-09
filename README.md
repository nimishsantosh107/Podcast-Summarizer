## Prerequisites:

-   conda
-   python=3.7

## Installation:

-   PyTorch (1.9.0) + CUDA (11.1)
    `conda install pytorch==1.9.0 cudatoolkit=11.1 -c pytorch -c conda-forge`

-   Spacy model + (en_core_web_md)

    1. `pip install spacy==2.1.3`
    2. `pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_md-2.1.0/en_core_web_md-2.1.0.tar.gz` (en_code_web_md==2.1.0)

-   `pip install transformers==4.9.1 sentencepiece==0.1.96`

-   `pip install neuralcoref`

-   `pip install bert-extractive-summarizer`
