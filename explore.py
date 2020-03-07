import pandas as pd
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

sales = pd.read_csv("data/slogans.csv",sep='|')
print(sales.head())
