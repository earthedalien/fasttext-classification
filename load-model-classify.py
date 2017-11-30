import fasttext
model = fasttext.load_model ('model.bin')
texts = ['I wrote it on a slip of paper and handed it to him myself', 'Twice or thrice I prepared to go, but some difficulty came in my way']
labels = classifier.predict(texts)
print labels
