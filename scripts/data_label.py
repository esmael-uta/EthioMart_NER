 ## labeling data in coNLL format

import pandas as pd
import numpy as np
import re
import os
import sys

def label_to_conll_format(messages, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        for message in messages:
            tokens = message.split()
            for token in tokens:
                # Example labeling logic (replace with actual labeling)
                if token.startswith('በ') and token.endswith('ብር'):
                    label = 'B-PRICE'
                elif token in ['Addis', 'Bole']:
                    label = 'B-LOC'
                else:
                    label = 'O'
                
                f.write(f"{token} {label}\n")
            f.write("\n")


messages = df['text'].dropna().tolist()[:50]
label_to_conll_format(messages, 'amharic_ner_project/data/labeled/ner_data.conll')