from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize
import nltk

# nltk.download()


sentences = ["Super movie","great day","disaster in haiti after hurricane"# mixed sentiment example with slang and constrastive conjunction "but"
             ]


def sentimentcalc(sentence):
    sid = SentimentIntensityAnalyzer()
    print(sentence)
    ss = sid.polarity_scores(sentence)
    print(ss)
    for k in sorted(ss):
        print(k, ss[k])
    print()
