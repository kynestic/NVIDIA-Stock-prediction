import torch
import time
from transformers import BertModel, BertTokenizer
import numpy as np
import pandas as pd

start_time = time.time()
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased", cache_dir='./model_cache')
model = BertModel.from_pretrained("bert-base-uncased", cache_dir='./model_cache')

df = pd.read_csv(r'data\synthesis\data.csv')

embedding_text = []
line = 0
print(df)
for item in df['keyword']:
    line+=1
    print(line)

    inputs = tokenizer(item, return_tensors='pt', padding=True, truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)
    event_embedding = outputs.pooler_output.cpu().numpy().reshape(-1)

    embedding_text.append(event_embedding)

data = pd.DataFrame(embedding_text)
data['timestamp'] = df['date']
data.to_csv(r'data\synthesis\embedding\BERT_EmbeddingText.csv', index=False)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")