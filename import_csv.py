import nltk,csv,numpy
from nltk import sent_tokenize, word_tokenize, pos_tag
reader = csv.reader(open('/Users/arundavid/dev/ml/review.csv', 'rU'), delimiter= ",",quotechar='|')
ratings = {}
counter = 0
for line in reader:
  ratings[counter] = {}
  ratings[counter]['id'] = line[5]
  ratings[counter]['rating'] = line[9]
  ratings[counter]['title'] = line[10]
  ratings[counter]['message'] = line[11]
  counter = counter + 1

  # example data: ratings[0] = {'id': 123, 'rating': 5, 'title': 'Good App', 'message': 'App is very useful' }

for rating in ratings:
  print(' =====>>>>> ' + ratings[rating]['rating'] + ' >> ' + ratings[rating]['title'] + ' >> ' + ratings[rating]['message'])
