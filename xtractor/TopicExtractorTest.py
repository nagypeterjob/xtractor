import unittest
import TopicExtractor
import pandas as pd

#Mock model has n_similarity function
class MockModel():
    def n_similarity():
        return 0.0
    
#Mock model has no n_similarity function, therefore will raise exception
class BadModel():
    def similarity():
        return 1.0

class TestTopicExtractor(unittest.TestCase):
    
    def setUp(self):
        self.mockCategories = [
            {
                "name": "gazdaság",
                "keywords": ['pénz', 'üzlet', 'használt', 'gazdaság','hitel', 'növekedés', 'vállalkozás', 'vállalkozó', 'forint', 'euró']
            }, 
            {
                "name": "sport",
                "keywords": ['labda','autó' ,'pálya','mérkőzés', 'játék', 'meccs', 'szurkoló', 'stadion', 'sport', 'indult', 'mezőny', 'hátrány', 'előny']
            }
        ]
    
        self.extractor = TopicExtractor.TopicExtractor([MockModel()], self.mockCategories)
        
    def testToCategory(self):
        cat = self.extractor.to_category(self.mockCategories)
        self.assertEqual(len(cat), 2)
        self.assertEqual(cat[0].label(), "gazdaság")
        self.assertEqual(len(cat[0].keys()), 10)
    
    def testExtract(self):
        with self.assertRaises(ValueError):
            self.extractor.extract([])
          
    def testExtractWithList(self):
        results = self.extractor.extract(['object'])
        self.assertEqual(len(results), 1)
    
    def testExtractWithDf(self):
        df = pd.DataFrame({"Text": ['row1', 'row2']})
        results = self.extractor.extract(df)
        self.assertEqual(len(results), 2)
    
    def testExtractWithSeries(self):
        df = pd.DataFrame({"Text": ['row1', 'row2']})
        results = self.extractor.extract(df.Text)
        self.assertEqual(len(results), 2)
    
    def testWithMultipleColumns(self):
        df = pd.DataFrame({"Text": ['row1', 'row2'], "Col2": [0, 0]})
        with self.assertRaises(ValueError):
            results = self.extractor.extract(df)
    
    def testWithNotCompatibleModel(self):
        with self.assertRaises(ValueError):
            ext = TopicExtractor.TopicExtractor([BadModel()], self.mockCategories)
    
    def testWithNoData(self):
        ext = TopicExtractor.TopicExtractor([MockModel()], self.mockCategories)
        with self.assertRaises(TypeError):
            ext.extract(None)
        
if __name__ == '__main__':
    unittest.main()