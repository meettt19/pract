import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules


dataset = [
    ['milk', 'bread', 'nuts'],
    ['milk', 'bread'],
    ['milk', 'eggs', 'nuts'],
    ['milk', 'bread', 'eggs'],
    ['bread', 'nuts']
]


items = sorted(set(item for transaction in dataset for item in transaction))

df = pd.DataFrame([
    [item in transaction for item in items]
    for transaction in dataset
], columns=items)


frequent_itemsets = apriori(
    df,
    min_support=0.4,
    use_colnames=True
)

print("Frequent Itemsets:")
print(frequent_itemsets)


rules = association_rules(
    frequent_itemsets,
    metric="lift",
    min_threshold=1.0
)

print("\nAssociation Rules:")
print(rules[
    ['antecedents', 'consequents', 'support',
     'confidence', 'lift']
])
