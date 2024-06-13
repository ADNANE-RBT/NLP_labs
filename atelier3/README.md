# Lab 3 - Natural Language Processing with Sklearn

## Objective

The main purpose of this lab is to get familiar with Natural Language Processing (NLP) language models using the Sklearn library. We aim to establish a comprehensive preprocessing pipeline, encode data vectors using various methods, train multiple models, evaluate them using standard metrics, and interpret the results to choose the best model.

## Work to Do

### Part 1: Language Modeling / Regression

#### Dataset
The dataset used for this part is available [here](https://github.com/dbbrandt/short_answer_granding_capstone_project/blob/master/data/sag/answers.csv).

#### Steps

1. **Preprocessing Pipeline**:
   - Tokenization
   - Stemming
   - Lemmatization
   - Stop words removal
   - Discretization

2. **Data Vector Encoding**:
   - Word2Vec (CBOW and Skip Gram)
   - Bag of Words
   - TF-IDF

3. **Model Training**:
   - SVR
   - Naive Bayes
   - Linear Regression
   - Decision Tree

4. **Model Evaluation**:
   - Use metrics like MSE and RMSE to evaluate the models
   - Choose the best model and justify the choice

5. **Result Interpretation**:
   - Interpret the obtained results for the best model

### Part 2: Language Modeling / Classification

#### Dataset
The dataset used for this part is available on [Kaggle](https://www.kaggle.com/datasets/jp797498e/twitter-entity-sentiment-analysis).

#### Steps

1. **Preprocessing Pipeline**:
   - Tokenization
   - Stemming
   - Lemmatization
   - Stop words removal
   - Discretization

2. **Data Vector Encoding**:
   - Word2Vec (CBOW and Skip Gram)
   - Bag of Words
   - TF-IDF

3. **Model Training**:
   - SVM
   - Naive Bayes
   - Logistic Regression
   - Ada Boosting

4. **Model Evaluation**:
   - Use metrics like Accuracy, Loss, F1 Score, and BLEU score
   - Choose the best model and justify the choice

5. **Result Interpretation**:
   - Interpret the obtained results for the best model

## Best Model Selection

### Best Model by Embedding Type


- **CBOW**: 
  - **Model**: SVM
  - **Metrics**:
    - Accuracy: 0.5383
    - F1 Score: 0.5126
    - Precision: 0.5323
    - Recall: 0.5334

- **Skip Gram**:
  - **Model**: SVM
  - **Metrics**:
    - Accuracy: 0.5887
    - F1 Score: 0.5763
    - Precision: 0.57945
    - Recall: 0.5812

### Overall Best Model

Comparing the best models from both embeddings, SVM with Skip Gram embeddings has the highest performance across all metrics:
- **Accuracy**: 0.5845
- **F1 Score**: 0.5723
- **Precision**: 0.5734
- **Recall**: 0.5823

### Interpret the Obtained Results

**SVM with Skip Gram Embeddings**: This combination provides the highest accuracy and the best balance between precision and recall, as indicated by the F1 Score. This suggests that the SVM model is effective in distinguishing between different sentiment classes when using Skip Gram embeddings, which capture the context around each word more effectively than CBOW for this dataset.

**Conclusion**: The SVM model with Skip Gram embeddings is the best choice for this Twitter Sentiment Analysis task. It has the highest accuracy and F1 Score, indicating it makes the most reliable and balanced predictions. The rich contextual information provided by Skip Gram embeddings enhances SVM's classification capabilities, making it the optimal model for this dataset.

## Tools Used
- Google Colab or Kaggle
- GitLab/GitHub
- Spacy
- NLTK
- Sklearn

## Learnings
During this lab, I learned how to establish a comprehensive NLP preprocessing pipeline, apply different encoding methods, and train various models. I gained experience in evaluating models using standard metrics and interpreting results to select the best model. Additionally, I understood the significance of contextual information in embeddings and its impact on model performance.