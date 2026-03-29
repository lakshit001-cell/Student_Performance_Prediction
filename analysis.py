import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import joblib 


url="https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/Students_Alcohol_Consumption/student-mat.csv"
df=pd.read_csv(url)


df["parent_edu"]=df['Medu']+df['Fedu']
df['ic']=df['internet'].apply(lambda x: 1 if x=='yes' else 0)

required_cols = ['studytime', 'absences', 'parent_edu','health','failures','ic',"Dalc","Walc"]

x=df[required_cols]
y=df["G3"]
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

model=LinearRegression()
model.fit(x_train,y_train)
prediction=model.predict(x_test)


print(model.coef_)
mse=mean_squared_error(y_test,prediction)
rmse1=np.sqrt(mse)
print(rmse1)




model1=RandomForestRegressor(n_estimators=100,max_depth=2,random_state=42)
model1.fit(x_train,y_train)
prediction1=model1.predict(x_test)
rmse=np.sqrt(mean_squared_error(y_test,prediction1))
print(rmse)

joblib.dump(model1,"student_model.pkl")
scores=cross_val_score(model1,x,y,cv=10,scoring="neg_mean_squared_error")
print(scores)
avg_rmse=np.sqrt(-scores.mean())
print(avg_rmse)

