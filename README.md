
---

## 🧠 Machine Learning Assignments

이 저장소는 2개의 머신러닝 과제(ML1, ML2)의 구현 코드를 모아둔 포트폴리오입니다.  
각 과제는 **GitHub에는 코드만** 포함되어 있으며, **상세 실행 결과와 분석 보고서는 Kaggle Notebook**에서 확인할 수 있습니다.

---

## 📁 Repository Structure
```
ML/
  assignment1/   # Decision Tree Classifier (ID3)
  assignment2/   # Naive Bayes Classifier
```

---

## 📌 Assignment 1 — Decision Tree Classifier (ID3)
**목표**  
- 엔트로피와 정보이득 기반으로 최적의 분할을 찾아 트리 구조 생성  
- if-then 규칙 형태로 출력하여 분류 로직 시각화

**구현 내용**  
- CSV 데이터 로드 및 전처리  
- 엔트로피 / 정보이득 계산  
- 최적 feature 선택 및 재귀적 트리 생성  
- 결과를 콘솔에 if-then 규칙 형태로 출력

**실행 방법**
```bash
python decision_tree_classifier.py --csv ./data/playtennis.csv
```

**상세 결과 및 분석**  
🔗 [Kaggle Notebook - ML1](https://www.kaggle.com/ml1-link)

---

## 📌 Assignment 2 — Naive Bayes Classifier
**목표**  
- 조건부 확률 기반으로 분류 모델 생성  
- 테스트 데이터에 대해 Yes/No 분류 및 확률 비율 출력

**구현 내용**  
- 학습 데이터 기반 feature/label 확률 계산  
- 테스트 데이터에 대해 추론 수행  
- 결과를 콘솔에 출력 (예: `Yes (2.34)`)

**실행 방법**
```bash
python naive_bayes_classifier.py --train ./data/spam_train.csv --test ./data/spam_test.csv
```

**상세 결과 및 분석**  
🔗 [Kaggle Notebook - ML2](https://www.kaggle.com/ml2-link)

---

## 📂 Data
- 모든 과제의 데이터는 수업 자료 또는 교내 Private Dataset으로 **공개 불가**
- 동일한 형식의 예시 데이터는 Kaggle 공개 데이터셋 또는 UCI ML Repository 참고 가능
- Kaggle Notebook에서는 Private Dataset을 사용하여 실행 후 결과만 공개

---

## 📜 License
이 저장소의 코드는 자유롭게 참고 가능하나, 데이터는 포함되어 있지 않습니다.

---

