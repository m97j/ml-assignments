import csv
import math
import argparse

class DecisionTreeClassifier:
    def __init__(self):
        self.tree = None

    def fit(self, filename):
        headers, data = self._read_csv(filename)
        self.tree = self._build_tree(data, headers)

    def print_tree(self):
        self._print_tree(self.tree)

    def _read_csv(self, filename):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            dataset = list(reader)
        headers = dataset[0]
        data = dataset[1:]
        return headers, data

    def _entropy(self, data):
        total = len(data)
        positive = sum(1 for row in data if row[-1] == 'Yes')
        negative = total - positive
        if positive == 0 or negative == 0:
            return 0
        p_pos = positive / total
        p_neg = negative / total
        return -p_pos * math.log2(p_pos) - p_neg * math.log2(p_neg)

    def _information_gain(self, data, feature_index):
        entropy_d = self._entropy(data)
        values = set(row[feature_index] for row in data)
        entropy_dv = 0
        for value in values:
            subset = [row for row in data if row[feature_index] == value]
            entropy_dv += (len(subset) / len(data)) * self._entropy(subset)
        return entropy_d - entropy_dv

    def _best_feature(self, data):
        features = len(data[0]) - 1
        gains = [self._information_gain(data, i) for i in range(features)]
        return gains.index(max(gains))

    def _build_tree(self, data, features):
        if all(row[-1] == 'Yes' for row in data):
            return 'Yes'
        if all(row[-1] == 'No' for row in data):
            return 'No'
        if len(data[0]) == 1:
            return 'Yes' if sum(1 for row in data if row[-1] == 'Yes') > len(data) / 2 else 'No'

        best = self._best_feature(data)
        tree = {features[best]: {}}
        values = set(row[best] for row in data)
        for value in values:
            subset = [row[:best] + row[best+1:] for row in data if row[best] == value]
            sub_features = features[:best] + features[best+1:]
            subtree = self._build_tree(subset, sub_features)
            tree[features[best]][value] = subtree
        return tree

    def _print_tree(self, tree, indent=''):
        if isinstance(tree, dict):
            for key, value in tree.items():
                print(f"{indent}if {key}:")
                self._print_tree(value, indent + '  ')
        else:
            print(f"{indent}then {tree}")

def main():
    parser = argparse.ArgumentParser(description="Decision Tree Classifier")
    parser.add_argument('--csv', required=True, help='CSV file for training')
    args = parser.parse_args()

    clf = DecisionTreeClassifier()
    clf.fit(args.csv)
    clf.print_tree()

if __name__ == "__main__":
    main()
