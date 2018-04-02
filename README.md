[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![CircleCI](https://circleci.com/gh/nagypeterjob/xtractor/tree/master.svg?style=svg)](https://circleci.com/gh/nagypeterjob/xtractor/tree/master)

```
       _                   _             
 __ __| |_  _ _  __ _  __ | |_  ___  _ _ 
 \ \ /|  _|| '_|/ _` |/ _||  _|/ _ \| '_|
 /_\_\ \__||_|  \__,_|\__| \__|\___/|_|  
                                         
xtractor
Topic extractor with the idea of generating labels using genism.n_similarity
by Peter Nagy
```
## Overview

xtractor is little package which aims to label text automatically harnessing the power of pre-trained word vectors. </br>
The idea is the following: 
- You must provide one or more genism compatible pre-trained word vectors
- You must define categories with keywords
- You must provide a tokenized text features you want to label
- Run the extractor to label input text
- The extractor digests the cosine distance of each word (vector) in the sentence and each keyword (vector)
- Then it chooses the most "similar" category as label

## Installation

```bash
$ pip install xtractor
```

## Usage

See `example.py` for a more detailed example.

```python
from xtractor import TopicExtractor as te
extractor = te.TopicExtractor(models=models, categories=categories)
labels = extractor.extract(pandas_data_frame)
```

## Parameters

#### TopicExtractor(models=models, categories=categories)

##### models 
- list of genism compatible models

##### categories
- list of categories
Format:

#### extract(X=pandas_dataframe)
- input pandas data frame or python list
- in case X is a pandas dataframe, it must have only one column (the feature column) 
- X can be a regular python `list`
- the features are expected to be tokenized string (e.g. following format: `['Tokenized', 'string']`)
- the return value is a regular `list` containing the category names (labels) for each input row respectively (e.g. in case of a 2 row input `['economy', 'sport']`)

## Precision
It really depends on the quality of you pre-trained word vector and on the quality of your intuitively defined category keywords.
In my use case I have used these [vectors](https://github.com/facebookresearch/fastText/blob/master/pretrained-vectors.md) and played with several iterations of keywords. <br/>
I have reached around 69% precision which is not bad. With more carefully picked keywords it can be enhanced.

## F.A.Q.

* Q: Why did you make this?
  A: Because I looked for a way to automatically label huge amount of (hungarian) text and I found no simple way.
  
 ## Author

* peter nagy | nagypeterjob@gmail.com


