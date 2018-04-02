import pandas as pd

#Category type for managing categories
class Category:
    def __init__(self,name, keywords):
        self.name = name
        self.keywords = keywords
    def keys(self):
        return self.keywords
    def label(self):
        return self.name

class TopicExtractor:
    def __init__(self, models, categories):
        self.validate_models(models)        
        self.models = models
        self.categories = self.to_category(categories)
        self.results = []
    
    def argmax(self, pairs):
        return max(pairs, key=lambda x: x[1])[0]

    def argmax_index(self, values):
        return self.argmax(enumerate(values))
    
    def validate_models(self, models):
        for model in models:
            n_similarity = getattr(model, "n_similarity", None)
            if callable(n_similarity):
                continue
            else:
                raise ValueError("Model ({}) is not genism compatible".format(model))
                
    def to_category(self, categories):
        cgs = []
        for cat in categories:
            try:
                cgs.append(Category(cat['name'], cat['keywords']))
            except:
                raise ValueError('Provided category has no "name" or "keywords" key')
        return cgs
        
    def extract(self, X):
        iterable = 0
        
        if  len(X) == 0:
                raise ValueError('Provided data has no length')
        
        if isinstance(X, list) or isinstance(X, pd.Series):
            iterable = pd.DataFrame({"data": X})
        elif isinstance(X, pd.DataFrame):
            col_names = X.columns.values.tolist()
            if len(col_names) == 1:
                iterable = X
            else:
                raise ValueError('Multiple columns found. Cannot figure out column name to work with')
        else:
            raise ValueError('Cannot figure out provided data')
        
        for row in iterable.itertuples():
            _ , text = row
            predictions = []
            for category in self.categories:
                model_scores = []
                for model in self.models:
                    pred = 0
                    try: 
                        pred = model.n_similarity(category.keys(), text)
                    except:
                        pred = 0
                    model_scores.append(pred)
                predictions.append(max(model_scores))
            self.results.append(self.categories[self.argmax_index(predictions)].label())
        return self.results