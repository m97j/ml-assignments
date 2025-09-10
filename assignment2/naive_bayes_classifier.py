import csv
import math
import sys
import argparse

class NaiveBayes:
    def __init__(self):
        self.feature_prob = {}
        self.label_prob = {}

    def train(self, filename):
        data = self.read_csv(filename)
        feature_counts, label_counts = self.count_features_and_labels(data)
        self.label_prob = self.compute_label_probabilities(label_counts)
        self.feature_prob = self.compute_feature_probabilities(feature_counts, label_counts)

    def predict(self, filename):
        test_data = self.read_csv(filename)
        predictions = []
        for instance in test_data:
            yes_prob = self.compute_instance_probability(instance, 'Yes')
            no_prob = self.compute_instance_probability(instance, 'No')
            ratio = yes_prob / no_prob if no_prob > 0 else float('inf')
            ratio = round(ratio, 4)
            predictions.append(('Yes', ratio) if ratio > 1 else ('No', ratio))
        return predictions

    def read_csv(self, filename):
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader)                          # 헤더가 없는 경우 이 코드 주석처리 필요함
            data = [row for row in reader]
        ##for row in data:                                 # Spam 데이터 테스트를 위한 코드
            ##row[-1] = 'Yes' if row[-1] == '1' else 'No'  # (label이 yes, no가 아니라 non-spam[0], spam[1]로 되어 있으므로 이를 yes, no로 변환하는 코드)
        return data

    def count_features_and_labels(self, data):
        feature_counts = {}
        label_counts = {'Yes': 0, 'No': 0}
        for instance in data:
            label = instance[-1]
            label_counts[label] += 1
            for i in range(len(instance) - 1):
                feature = (i, instance[i], label)
                if feature not in feature_counts:
                    feature_counts[feature] = 0
                feature_counts[feature] += 1
        return feature_counts, label_counts

    def compute_label_probabilities(self, label_counts):
        total_count = sum(label_counts.values())
        return {label: count / total_count for label, count in label_counts.items()}

    def compute_feature_probabilities(self, feature_counts, label_counts):
        feature_prob = {}
        for feature, count in feature_counts.items():
            _, _, label = feature
            feature_prob[feature] = count / label_counts[label]
        return feature_prob

    def compute_instance_probability(self, instance, label):
        prob = self.label_prob[label]
        for i in range(len(instance)):
            feature = (i, instance[i], label)
            prob *= self.feature_prob.get(feature, 1e-6)
        return prob

def main():
    parser = argparse.ArgumentParser(description="Naive Bayes Classifier")
    parser.add_argument('--train', required=True, help='Training CSV file')
    parser.add_argument('--test', required=True, help='Testing CSV file')
    args = parser.parse_args()

    nb = NaiveBayes()
    nb.train(args.train)
    predictions = nb.predict(args.test)

    for label, ratio in predictions:
        print(f"{label} ({ratio})")

if __name__ == "__main__":
    main()
