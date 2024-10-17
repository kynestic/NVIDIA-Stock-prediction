from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import ast

df = pd.read_csv(r'data\processed\stock_news_price.csv')

tfidf_results = pd.DataFrame()

# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    print(index)
    events_list = eval(row['events']) 

    tfidf_vectorizer = TfidfVectorizer()
    
    events_matrix = tfidf_vectorizer.fit_transform(events_list)

    tfidf_df = pd.DataFrame(events_matrix.toarray(), columns=tfidf_vectorizer.get_feature_names_out())
    tfidf_results = pd.concat([tfidf_results, tfidf_df], ignore_index=True)

# Save the resulting DataFrame to a CSV file

tfidf_results.fillna(0, inplace=True)
if len(df['events']) != len(tfidf_results):
    df['events'] = tfidf_results
else:
    print(len(df['events']))
    print(len(tfidf_results))
    tfidf_results.to_csv(r'D:\CODING\Project\NVIDIA Stock prediction\data\raw\IF-IDF_EmbeddingText.csv', index=False)
print("TF-IDF features extracted and saved to news_vector.csv")