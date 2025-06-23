import os
import re

from SimpleTokenizerV1 import SimpleTokenizerV1

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "the-verdict.txt")

with open(file_path, 'r', encoding="utf-8") as file:
    raw_text = file.read()

print("Total number of characters in the file:", len(raw_text))
print(raw_text[:99])

preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
preprocessed = [item.strip() for item in preprocessed if item.strip()]
print(len(preprocessed))
print(preprocessed[:30])

all_words = sorted(set(preprocessed))
vocab_size = len(all_words)
print("Vocabulary size:", vocab_size)

vocab = {token:integer for integer, token in enumerate(all_words)}
for i, item in enumerate(vocab.items()):
    print(item)
    if i > 50:
        break

tokenizer = SimpleTokenizerV1(vocab)
text = """"It's the last he painted, you know," Mrs. Gisburn said with pardonable pride."""
ids = tokenizer.encode(text)
print("Encoded IDs:", ids)
print("Decoded text:", tokenizer.decode(ids))


from importlib.metadata import version
import tiktoken

print("tiktoken version:", version("tiktoken"))
enc = tiktoken.get_encoding("gpt2")