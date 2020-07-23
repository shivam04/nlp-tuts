from nltk.stem.snowball import SnowballStemmer

englishStemmer=SnowballStemmer("french")
print(englishStemmer.stem("voudrais"))