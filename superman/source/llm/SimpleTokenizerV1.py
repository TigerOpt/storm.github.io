import re
# Listing 2.3 Implementing a simple text tokenizer
class SimpleTokenizerV1:
    def __init__(self, vocab):
        self.str_to_int = vocab                                                   #A
        self.int_to_str = {i: s for s, i in vocab.items()}                        #B

    def encode(self, text):                                                       #C
        preprocessed = re.split(r'([,.?_!"()\']|--|\s)', text)
        preprocessed = [item.strip() for item in preprocessed if item.strip()]
        ids = [self.str_to_int[s] for s in preprocessed]
        return ids

    def decode(self, ids):                                                        #D
        text = " ".join([self.int_to_str[i] for i in ids])

        text = re.sub(r'\s+([,.?!"()\'])', r'\1', text)                           #E
        return text


#A 将词汇表作为类属性存储，以方便在 encode 和 decode 方法中访问
#B 创建一个反向词汇表，将token ID 映射回原始的文本token
#C 将输入文本转换为token ID
#D 将token ID 还原为文本
#E 在指定的标点符号前去掉空格