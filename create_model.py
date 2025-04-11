import pandas as pd
import pickle

df = pd.read_csv("diet_data.csv")
diet_dict = df.set_index('disease').T.to_dict()

with open("model.pkl", "wb") as f:
    pickle.dump(diet_dict, f)
