from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import matplotlib.pyplot as pl
from wordcloud import WordCloud
from math import log, sqrt
import pandas as pd
import numpy as np

mls = pd.read_csv('abcd.csv')
mls.head()


