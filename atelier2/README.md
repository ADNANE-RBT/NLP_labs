### My Evaluation of Approaches

1. **One-Hot Encoding**:
    - **Pros**: Simple to implement, no assumptions about the data.
    - **Cons**: Results in very high-dimensional and sparse vectors, lacks semantic meaning and similarity between words, suffers from the curse of dimensionality.

2. **Bag of Words (BoW)**:
    - **Pros**: Easy to implement, captures the frequency of words, straightforward for text classification tasks.
    - **Cons**: Ignores word order, context, and semantics. High-dimensional and sparse.

3. **TF-IDF (Term Frequency-Inverse Document Frequency)**:
    - **Pros**: Weighs down the frequent but less informative words, more informative than BoW for distinguishing documents.
    - **Cons**: Still ignores the semantics and context, remains high-dimensional and sparse.

4. **Word2Vec (Skip-Gram and CBOW)**:
    - **Pros**: Captures semantic relationships between words, results in dense and lower-dimensional vectors, efficient to compute.
    - **Cons**: Requires large corpora to learn good quality embeddings, can miss out on some contextual nuances.

5. **GloVe (Global Vectors for Word Representation)**:
    - **Pros**: Captures global statistical information about the corpus, results in dense vectors, good for capturing semantic relationships.
    - **Cons**: Requires a large corpus and significant computational resources, does not dynamically adapt to new data.

6. **FastText**:
    - **Pros**: Extends Word2Vec by considering subword information (character n-grams), captures morphological information well, can handle out-of-vocabulary words better.
    - **Cons**: Computationally more intensive due to the subword modeling, requires a large corpus for training.

### TSNE Plotting
TSNE (t-distributed Stochastic Neighbor Embedding) was used to visualize the high-dimensional word vectors in a 2D space. This helps in understanding the clustering and relative distances between word vectors from different models, offering a qualitative comparison of the embeddings.

### General Conclusion
- Traditional methods like One-Hot Encoding and BoW are simple and interpretable but suffer from high dimensionality and lack of semantic understanding.
- TF-IDF improves over BoW by adding importance weighting but still lacks contextual understanding.
- Word2Vec, GloVe, and FastText provide dense, lower-dimensional embeddings that capture semantic relationships between words.
- FastText's subword approach is particularly useful for morphologically rich languages and handling out-of-vocabulary words.
- Visualizations with TSNE demonstrate how these models group semantically similar words together, highlighting the effectiveness of dense embeddings over sparse representations.

### Learnings from the Lab
During this lab, I learned the following key points:

1. **Different Techniques for Word Embedding**: Understanding and applying One-Hot Encoding, BoW, TF-IDF, Word2Vec (Skip-Gram and CBOW), GloVe "even though it didnt work", and FastText.
2. **Trade-offs**: Recognizing the trade-offs between simplicity and computational efficiency versus the ability to capture semantic meaning and context.
3. **Practical Application**: Gaining hands-on experience with implementing these techniques and observing their behavior on a dataset.
4. **Dimensionality Reduction and Visualization**: Using TSNE to visualize high-dimensional word vectors in 2D, which aids in qualitative analysis of the embeddings.
5. **Real-World Relevance**: Understanding the practical implications of choosing different word embedding techniques for various NLP tasks such as text classification, sentiment analysis, and more.

This lab provided a comprehensive overview of word embeddings, enabling me to make informed decisions about which techniques to use based on the specific requirements of my NLP projects.