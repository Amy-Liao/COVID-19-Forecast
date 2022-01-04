import pandas as pd
from sklearn.linear_model import LinearRegression

'''dealing with the data'''
def preprocessing(country):
    rows = data.loc[(data['countriesAndTerritories'] == country)]
    x = rows['dateRep'].iloc[::-1].reset_index(drop=True)
    for i in range(x.size):
        x[i] = i
    size = x.size
    secondx=[]
    for j in range (size):
        secondx.insert(j, [j])
    y = rows['cases'].iloc[::-1].reset_index(drop=True)
    secondy=[]
    for s in range (size):
        secondy.insert(s, y[s])
    return secondx,secondy,size

'''train the model'''
def train(x,y,size):
    x_train = x[int(size*0.3):]
    y_train = y[int(size*0.3):]
    #build model
    model = LinearRegression()
    model.fit(x_train, y_train)
    predictions = model.predict([[size], [size+1], [size+2], [size+3], [size+4], [size+5], [size+6]])
    for i in range(7):
        if predictions[i]<1:
            predictions[i]=0
        predictions[i] = int(predictions[i])
    return predictions

def main():
    countrylist = data.countriesAndTerritories.unique().tolist()
    l=[]
    for k in range(len(countrylist)):
        x,y, size = preprocessing(countrylist[k])
        predictions = train(x,y, size)
        l.append(predictions)
    dat = ['10/9', '10/10', '10/11', '10/12', '10/13', '10/14', '10/15']
    result = pd.DataFrame(zip(*l), columns = countrylist, index=dat)
    result.to_csv('StudentID_HW1.csv')

'''file import'''
dataset_file_path = "your/dataset/path/dataset.csv"
data = pd.read_csv(dataset_file_path)
main()
