import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle,os

df=pd.read_csv('homeprices.csv')
x=df[['Area']]
y=df['Price']

model = LinearRegression()
model.fit(x,y)
os.makedirs('models', exist_ok=True)
with open('models/house_price_model.pkl', 'wb') as file:
    pickle.dump(model, file) 
print("Model trained and saved successfully.")   

