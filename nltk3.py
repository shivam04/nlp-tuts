from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
#create an object of class PorterStemmer
porter = PorterStemmer()
lancaster = LancasterStemmer()
def stemSentence(sentence):
    token_words=word_tokenize(sentence)
    print(token_words)
    stem_sentence=[]
    for word in token_words:
        stem_sentence.append(porter.stem(word))
        stem_sentence.append(" ")
    return "".join(stem_sentence)


sentence="Pythoners are very intelligent and work very pythonly and now they are pythoning their way to success."
print(porter.stem(sentence))

x=stemSentence(sentence)
print(x)