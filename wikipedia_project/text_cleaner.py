import pandas as pd
comments = pd.read_csv('attack_annotated_comments.tsv', sep='\t', index_col=0)
comments['comment'] = comments['comment'].apply(lambda x: x.replace("NEWLINE_TOKEN", " "))
comments['comment'] = comments['comment'].apply(lambda x: x.replace("TAB_TOKEN", " "))

print(list(comments['comment'].iloc[:1]))
