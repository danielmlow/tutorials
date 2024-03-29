
# Author: Daniel Low 
# Instructions: complete the exercises below. 
# Please submit your .py file on canvas. 
# In this pset we're going to use TFIDF features and sentence embeddings to do
# text classification: classifying whether a Reddit post should belong in 
# r/BipolarReddit or r/BPD. BPD stands for Borderline Personality Disorder, which
# is often misdiagnosed as Bipolar Disorder and vice versa. So it would be interesting
# to see if we can dissociate the two from their language patterns through a classifier.
# Not everyone in this subreddit has a diagnosis or a correct diagnosis, so
# this is just a proof of concept, but many do, so it might inform us of something real.

import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from nltk.stem import WordNetLemmatizer
import nltk
nltk.download('wordnet')                      # download lemmatizer


# Custom classification report
def custom_classification_report(y_test, y_pred, y_proba_1, model_name='model_name', average='binary'):
    precision = metrics.precision_score(y_test, y_pred, average = average)
    recall = metrics.recall_score(y_test, y_pred, average = average)
    specificity = metrics.recall_score(y_test, y_pred, pos_label=0, average = average)    # specificity is the recall of the negative class or control group
    f1 = metrics.f1_score(y_test, y_pred, average = average)
    roc_auc = metrics.roc_auc_score(y_test, y_proba_1)  # IMPORTANT: other metrics take binary predictions y_pred. Here we test different thresholds, so we need probabilities (this will change the ROC AUC score)
    
    results_dict = {
        'Precision':precision,
        'Recall':recall,
        'Specificity':specificity,    
        'F1':f1,
        'ROC AUC':roc_auc,
        }    
    results = pd.DataFrame(results_dict, index=[model_name]).round(3)
    return results



bipolar_bpd  = pd.read_csv('https://mair.sites.fas.harvard.edu/datasets/reddit_bipolar_bpd.csv')
bipolar_bpd  

# Obtain X (which are documents in this case) and y 
docs = bipolar_bpd['post'].values # X, but in this case, it's documents
y = bipolar_bpd['y'].values

# Exercise: For the TFIDF model, 1) tokenize documents into words, (2) then lemmatize each token 
# (3) join the tokens back together into a string for each document
# at the end create a list or array of the lemmatized documents called docs_lemmatized
# ---------------------------------------------------------------------------
# Your code: 
lemmatizer = WordNetLemmatizer()

docs_lemmatized = []
for doc in docs:
    word_list = nltk.word_tokenize(doc)
    word_list_lemmatized = [lemmatizer.lemmatize(w,pos='n') for w in word_list]
    doc_lemmatized= ' '.join(word_list_lemmatized)
    docs_lemmatized.append(doc_lemmatized)

docs_lemmatized = np.array(docs_lemmatized)    
print(docs_lemmatized)


lemmatizer.lemmatize('happier',pos='n') 


# Train-test split
# ---------------------------------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(docs_lemmatized,y, test_size = 0.2, random_state=42)


# TF-IDF
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# If you weren't able to complete the prior step, proceed with docs instead of docs_lemmatized
from sklearn.feature_extraction.text import TfidfVectorizer

# Exercise: Fit TFIDF and train model
# You can use the fit_transform and transform sequentially 
# Alternatively you could place the TFIDF vectorizer in a pipeline along with the model, 
# but let's keep things simple for this pset
# I recommend using ngram_range = (1,3), max_df = 0.9, min_df  = 3. You can also 
# do hyperparameter tuning to find the optimal values for prediction, but let's keep things simple for this pset.
# ---------------------------------------------------------------------------
# your code (should obtain X_train and X_test which are now the tfidf weights): 
vectorizer = TfidfVectorizer(stop_words='english', ngram_range = (1,3), max_df = 0.9, min_df = 3)
X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)

# Train model
# ---------------------------------------------------------------------------
model = LogisticRegression(class_weight='balanced', penalty ='l2')
model.fit(X_train,y_train)
y_proba = model.predict_proba(X_test)       # probabilities for y=0 and y=1

# Evaluate
# ---------------------------------------------------------------------------
y_proba = y_proba                           
y_proba_1 = y_proba[:,1]                    # probabilities for y=1
y_pred = (y_proba_1>=0.5)*1                   # using standard 0.5 threshold

cm = metrics.confusion_matrix(y_test, y_pred, normalize='all')                   # REMEMBER you can also obtain proportions with normalize argument: confusion_matrix(y_test, y_pred, normalize = 'all')
cm_display = metrics.ConfusionMatrixDisplay(cm,display_labels=[0,1]).plot() # sklearn provides a way to plot it. IMPORTANT YOU KNOW WHICH AXIS IS TRUE VS. PREDICTED
cm_df_meaning = pd.DataFrame([['TN', 'FP'],['FN','TP']], index=[0,1], columns=[0,1])
cm_df_meaning 

# Metrics
print(metrics.classification_report(y_test, y_pred))                # here we need to print to view correctly
results  = custom_classification_report(y_test, y_pred, y_proba_1,model_name = 'LogReg', average='weighted') # we care about both classes
results  


# Question: what does each TF-IDF value represent?
# ---------------------------------------------------------------------------
# Your answer (text response):
    # How characteristic or important a word is for a single document.
    
    

# Explaining TFIDF model
# ---------------------------------------------------------------------------
top_k = 40

# # Using sklearn pipeline:
# feature_names = pipe.named_steps["vectorizer"].get_feature_names_out()
# coefs = pipe.named_steps["model"].coef_.flatten() # Get the coefficients of each feature

# Without sklearn pipeline
feature_names = vectorizer.get_feature_names_out()
print(len(feature_names ))
coefs = model.coef_.flatten() # Get the coefficients of each feature

# Visualize feature importances
# Sort features by absolute value
df = pd.DataFrame(zip(feature_names, coefs), columns=["feature", "value"])
df["abs_value"] = df["value"].apply(lambda x: abs(x))
df["colors"] = df["value"].apply(lambda x: "orange" if x > 0 else "dodgerblue")
df = df.sort_values("abs_value", ascending=False) # sort by absolute coefficient value

fig, ax = plt.subplots(1, 1, figsize=(3.5, 6))
ax = sns.barplot(x="value",
            y="feature",
            data=df.head(top_k),
            hue="colors")
ax.legend_.remove()
ax.set_yticklabels(ax.get_yticklabels(), rotation=0, fontsize=10)
ax.set_title(f"Top {top_k} Features", fontsize=14)
ax.set_xlabel("Coef", fontsize=12) # coeficient from linear model
ax.set_ylabel("Feature Name", fontsize=12)
plt.tight_layout()

# Question: What are the 5 most important words for prediction?
# ---------------------------------------------------------------------------
# Your answer (text response):
    # bpd, bipolar, mania, friend, manic



    
# Sentence embeddings model
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
from sentence_transformers import SentenceTransformer, util 

# Encode the documents with their sentence embeddings (we saw one in 
# lecture but you can choose others)
# a list of pre-trained sentence transformers
# https://www.sbert.net/docs/pretrained_models.html
# https://huggingface.co/models?library=sentence-transformers

# Here the progress bar will show you how long it will take to embedd the documents.
 # Should take about 30 seconds.
# If it hangs or something. you can activate the NLP2085 virtual environment from Unit 8
# and install sentence-transformers again: 
# !pip install -U sentence-transformers 
# Let me know if you have issues running the code below
# ---------------------------------------------------------------------------
# Your code here:

    
# all-MiniLM-L6-v2 is optimized for semantic similarity of paraphrases
sentence_embedding_model = SentenceTransformer('all-MiniLM-L6-v2')       # load embedding

# Note: sbert will only use fewer tokens as its meant for sentences, 
print(sentence_embedding_model .max_seq_length)
# you can increase to closer to the base model it was trained on BERT has 512
sentence_embedding_model._first_module().max_seq_length = 500
print(sentence_embedding_model .max_seq_length) # now it takes up to 500, but will be a bit slower to encode and might not change performance a whole lot in this case


# Question: do you need to do preprocessing steps like lemmatizing when using deep learning embeddings? Why or why not?
# ---------------------------------------------------------------------------
# Your answer (text response):
    # No. Cleaning might be good though.
    
    

# Exercise, encode the docs and return docs_embeddings which should have shape
# (416, 384) for 416 docs and a all-MiniLM-L6-v2 has 384 dimensions each doc
# use the show_progress_bar=True argument. Should take about 30 seconds with max seq length = 500. 
# ----------------------------------------------------------------------------
# your code:
docs_embeddings = sentence_embedding_model.encode(docs, convert_to_tensor=True,show_progress_bar=True)
docs_embeddings.shape

# Train-test split and train model
# ---------------------------------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(docs_embeddings,y, test_size = 0.2, random_state=42)
model = LogisticRegression(class_weight='balanced', penalty ='l2')
model.fit(X_train,y_train)
y_proba = model.predict_proba(X_test)       # probabilities for y=0 and y=1

# Evaluate
# ---------------------------------------------------------------------------
y_proba_1 = y_proba[:,1]                      # probabilities for y=1
y_pred = (y_proba_1>=0.5)*1                   # using standard 0.5 threshold
cm = metrics.confusion_matrix(y_test, y_pred, normalize='all')                   # REMEMBER you can also obtain proportions with normalize argument: confusion_matrix(y_test, y_pred, normalize = 'all')
cm_display = metrics.ConfusionMatrixDisplay(cm,display_labels=[0,1]).plot() # sklearn provides a way to plot it. IMPORTANT YOU KNOW WHICH AXIS IS TRUE VS. PREDICTED
cm_df_meaning = pd.DataFrame([['TN', 'FP'],['FN','TP']], index=[0,1], columns=[0,1])
cm_df_meaning 

# Metrics
print(metrics.classification_report(y_test, y_pred))                # here we need to print to view correctly
results  = custom_classification_report(y_test, y_pred, y_proba_1, model_name = 'LogReg', average='weighted') # we care about both classes
results  

# Question: what is the sentence embedding vector representing as a whole? What is each value 
# representing?
# ---------------------------------------------------------------------------
# Your answer (text response):
    # It is representing aspects of the meaning of the document, optimized 
    # for paraphrasing. Each value of each dimension cannot be interpreted directly.


# Question: are TFIDF and sentence embeddings-based models explainable? 
# ---------------------------------------------------------------------------
# Your answer (text response):

    # The TFIDF model is, the sentence embedding is not.
    
    





