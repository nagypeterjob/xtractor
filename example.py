from gensim.models import Word2Vec
from xtractor import TopicExtractor as te
import pandas as pd

#hu.bin supposed to be a genism compatible word vector
model = Word2Vec.load("hu/hu.bin")

'''
This list contains your label names.
You need to choose keywords carefully as they a the hearth and soul of the whole topic extraction.
'''
categories = [
            {
                "name": "economy",
                "keywords": ['money', 'bussiness', 'used', 'economy','credit', 'growth', 'entrepreneur', 'euro']
            }, 
            {
                "name": "sport",
                "keywords": ['ball','car' ,'rank','match', 'game', 'fan', 'stadium', 'sport', 'run']
            }
        ]

'''
Example DataFrame.
These are supposed to be tokenized sentences, hence the list form.
'''
df = pd.DataFrame({"Text": [

    ['Poulter', 'wins', 'Houston', 'play-off', 'clinch', 'final', 'Masters spot'], #sport
    ['General', 'Principle', 'wins', 'Irish', 'Grand', 'National'], #sport
    ['Facebook', 'chief', 'fires', 'back', 'Apple', 'boss'] #economy
]})

extractor = te.TopicExtractor([model], categories)
results = extractor.extract(df)

print(results)