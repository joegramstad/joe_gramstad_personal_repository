import pandas as pd
import matplotlib.pyplot as plt

comments = pd.read_csv('attack_annotated_comments.tsv', sep='\t', index_col=0)
annotations = pd.read_csv('attack_annotations.tsv', sep='\t')

labels = annotations.groupby('rev_id')['attack'].mean() > 0.5
comments['attack'] = labels

comments.groupby("year")["attack"].value_counts(normalize=True).unstack(level=1).plot.bar(stacked=True)
comments.groupby("logged_in")["attack"].value_counts(normalize=True).unstack(level=1).plot.bar(stacked=True)
comments.groupby("ns")["attack"].value_counts(normalize=True).unstack(level=1).plot.bar(stacked=True)
comments.groupby("sample")["attack"].value_counts(normalize=True).unstack(level=1).plot.bar(stacked=True)
plt.show()
