from sklearn.metrics import confusion_matrix,classification_report
import pandas as pd

def fit_classify(model,x_train,x_test,y_train,y_test):
    model.fit(x_train,y_train)
    y_pred = model.predict(x_test)
    
    print(classification_report(y_test,y_pred))
    cm = confusion_matrix(y_test,y_pred)
    col = ['N','Y']
    print(pd.DataFrame(cm,index=col,columns = col))