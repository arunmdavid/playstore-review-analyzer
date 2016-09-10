import nltk,csv,numpy
from nltk import sent_tokenize, word_tokenize, pos_tag
reader = csv.reader(open('/Users/arundavid/dev/ml/review.csv', 'rU'), delimiter= ",",quotechar='|')
list = {}
counter = 0
for line in reader:
  list[counter] = {}
  list[counter]['id'] = line[5]
  list[counter]['rating'] = line[9]
  list[counter]['title'] = line[10]
  list[counter]['message'] = line[11]
  counter = counter + 1

  # example data: list[0] = {'id': 123, 'rating': 5, 'title': 'Good App', 'message': 'App is very useful' }

for rating in list:
  print(' =====>>>>> ' + list[rating]['rating'] + ' >> ' + list[rating]['title'] + ' >> ' + list[rating]['message'])
