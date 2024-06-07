
#### Overview

During this lab, I gained hands-on experience in several key areas of Natural Language Processing (NLP) and web scraping. Here are the major components and learnings from the exercise:

1. **Web Scraping:**
   - Utilized libraries like `requests` and `BeautifulSoup` rather than `Scrapy` to extract data from web sources.
   - Focused on extracting specific elements, in this case, i tested with just the titles from HTML tags with a class of `title`.

2. **Data Storage:**
   - Stored the scraped data in a NoSQL database, MongoDB, which is well-suited for handling unstructured data.
   - Understood the basics of connecting to a MongoDB instance and performing basic insert operations.

3. **NLP Pipeline:**
   - Implemented an NLP pipeline involving text cleaning, tokenization, stop words removal, stemming, lemmatization, POS tagging, and Named Entity Recognition (NER).
   - Used both NLTK and SpaCy libraries to perform these tasks, leveraging their respective strengths.

#### Overall Key Learnings

1. **Difference Between Stemming and Lemmatization:**
   - **Stemming:** This technique reduces words to their base or root form, often by simply removing suffixes. It can produce non-words since it uses heuristic rules (example: "running" becomes "run" or "runn"). In the output, i found `['مهرج', 'جزير', 'لقا', 'افلام', 'وثايق']`. those are stemmed forms, which are not real words.
   - **Lemmatization:** This technique also reduces words to their base or root form but uses a **dictionary-based** approach to ensure that the result is an actual word (example: "running" becomes "run"). In the output, `['مهرجان', 'الجزيرة', 'بلقان', 'للأفلام', 'الوثائقية']` are lemmatized forms which are real words.
   - **My Comparison:** Lemmatization is generally more accurate as it considers the context of the word within a sentence. Stemming is supposdly faster but can lead to less meaningful results.

2. **Part of Speech (POS) Tagging:**
   - **Rule-based POS Tagging:** Uses predefined grammatical rules to assign POS tags to words. It’s straightforward but can be limited by the complexity of the arabic language.

#### Challenges and Solutions

- **Language Support:** While SpaCy provides good support for many languages, some limitations were noted with Arabic. Supplementing SpaCy with additional resources or custom models trained on Arabic text could improve results.
- **Accuracy of NLP Tasks:** Ensuring the accuracy of stemming, lemmatization, and POS tagging for non-English text required using appropriate tools like the `SnowballStemmer` for Arabic.

