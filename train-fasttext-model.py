import fasttext
classifier = fasttext.supervised('cooking.train', 'model_cooking')

result = classifier.test ('cooking.valid')
print result.precision
print result.recall
print result.nexamples
