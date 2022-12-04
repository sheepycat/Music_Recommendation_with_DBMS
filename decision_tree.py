import sklearn
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import tree
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report,  precision_score, recall_score



def decision_tree(x_train,x_test,y_train,y_test):
    print("-------------Decision Tree-------------")
    clf=Pipeline(steps=[("cv",CountVectorizer(stop_words='english', ngram_range=(1,1))),
                ("Dt",tree.DecisionTreeClassifier(criterion="entropy",random_state=50,min_samples_leaf=6))])#,max_depth=MAX_DEPTH
    clf.fit(x_train, y_train)
    y_pred_test = clf.predict(x_test)
    print(classification_report(y_test, y_pred_test))
    print("\nAccuracy for Decision Tree model:",sklearn.metrics.accuracy_score(y_test, y_pred_test))

    acc_score = sklearn.metrics.accuracy_score(y_pred_test,y_test)
    prec_score = precision_score(y_test,y_pred_test, average='macro')
    recall = recall_score(y_test, y_pred_test,average='macro')
    print('Decision Tree Model')
    print(str('Accuracy: '+'{:04.2f}'.format(acc_score*100))+'%')
    print(str('Precision: '+'{:04.2f}'.format(prec_score*100))+'%')
    print(str('Recall: '+'{:04.2f}'.format(recall*100))+'%')
    
    return clf

