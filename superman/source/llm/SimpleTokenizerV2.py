import re
# Listing 2.3 Implementing a simple text tokenizer
class SimpleTokenizerV2:
    def __init__(self, vocab):
        self.str_to_int = vocab                                                   
        self.int_to_str = {i: s for s, i in vocab.items()}                        

    def encode(self, text):                                                       
        preprocessed = re.split(r'([,.?_!"()\']|--|\s)', text)
        preprocessed = [item.strip() for item in preprocessed if item.strip()]
        preprocessed = [item if item in self.str_to_int                           #A
                        else "<|unk|>" for item in preprocessed]
        ids = [self.str_to_int[s] for s in preprocessed]
        return ids

    def decode(self, ids):                                                        
        text = " ".join([self.int_to_str[i] for i in ids])

        text = re.sub(r'\s+([,.?!"()\'])', r'\1', text)                           #B                       
        return text


#A 用 <|unk|> tokens替换未知词汇
#B 在指定标点符号前替换空格