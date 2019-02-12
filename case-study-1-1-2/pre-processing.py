import csv
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

s = set(stopwords.words('english'))
minimumOccurences = 10

with open('dictionary.csv', mode='w') as dictionaryCsv:
    dictionaryWriter = csv.DictWriter(dictionaryCsv, fieldnames=['term'])
    # dictionaryWriter.writeheader()

    with open('alldocs.txt', mode='w') as abstractListCsv:
        abstractListWriter = csv.DictWriter(abstractListCsv, fieldnames=['path'])
        # dictionaryWriter.writeheader()

        with open('abstract_list.csv') as abstractCsv:
            csvReader = csv.reader(abstractCsv, delimiter=',')
            dictionary = dict()
            for row in csvReader:
                if row[2] == 'id' or len(row) != 5:
                    continue
                print row[2]
                print row[2].split(':')
                name = row[1] + '_' + row[2].split(':')[1].replace("/", "")
                print name
                abstract = row[4].lower()

                abstractPath = 'abstracts/' + name + '.txt'
                abstractListWriter.writerow({'path': abstractPath})

                with open(abstractPath, mode='w') as abstractTxt:
                    abstractWriter = csv.DictWriter(abstractTxt, fieldnames=['text'])
                    # abstractWriter.writeheader()
                    abstractWriter.writerow({'text': abstract})

                tokenizer = RegexpTokenizer(r'\w+')
                abstractWords = tokenizer.tokenize(abstract)
                for word in filter(lambda w: not w in s and not w.isdigit(), abstractWords):
                    if word in dictionary:
                        dictionary[word] += 1
                    else:
                        dictionary[word] = 1

            # print dictionary
            for d in dictionary:
                if dictionary[d] > minimumOccurences:
                    dictionaryWriter.writerow({'term': d})
