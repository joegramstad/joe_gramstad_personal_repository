import pandas as pd
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder

comments = pd.read_csv('attack_annotated_comments.tsv', sep='\t', index_col=0)
annotations = pd.read_csv('attack_annotations.tsv', sep='\t')
labels = annotations.groupby('rev_id')['attack'].mean() > 0.5
comments['attack'] = labels
comments['comment'] = comments['comment'].apply(lambda x: x.replace("NEWLINE_TOKEN", " "))
comments['comment'] = comments['comment'].apply(lambda x: x.replace("TAB_TOKEN", " "))

comments['logged_in'] = comments['logged_in'].apply(lambda x: 1 if x == 'False' else 0)
comments['ns'] = comments['ns'].apply(lambda x: 1 if x == 'user' else 0)
comments['sample'] = comments['sample'].apply(lambda x: 1 if x == 'blocked' else 0)
print(comments.head(10))

encode_elements = ['logged_in', 'ns', 'sample']
comments['composite'] = comments[encode_elements].sum(axis=1) + 1
print(comments.head(10))
