import nltk
import pandas as pd


text_df = pd.read_csv('/Users/KristinDay/Dropbox/LEGAL-DOMAIN-WORK/Pragmatics-paper/IN-case-paragraphs.csv', header=0, encoding="ISO-8859-1")

label_df = pd.read_csv('/Users/KristinDay/Dropbox/LEGAL-DOMAIN-WORK/Pragmatics-paper/IN.Case.Spreadsheet.csv', header=0, encoding="ISO-8859-1")

tagged_df = pd.DataFrame()

#pos-tag the text in text_df
for (idx, row) in text_df.iterrows():
    index = 1
    while True and index <=30:
        if row[index].values not None:
        text = nltk.word_tokenize(row[index].values)
        text_pos = nltk.pos_tag(text)
        tagged_df.iloc[idx][index] = text_pos
        index += 1
    else:
        False




