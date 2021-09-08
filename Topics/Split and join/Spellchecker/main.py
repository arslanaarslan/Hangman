dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']
              
words = input().split()

misspelled_words = [word for word in words if word not in dictionary]

if len(misspelled_words) > 0:
    for misspelled_word in misspelled_words:
        print(misspelled_word)
else:
    print("OK")
