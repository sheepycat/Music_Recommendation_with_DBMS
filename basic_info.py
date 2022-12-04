import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split


def basic_info ():
    train_data = pd.read_csv("train.txt", header=None, sep=";", names=["sentence","emo"], encoding="utf-8")
    test_data = pd.read_csv("test.txt", header=None, sep=";", names=["sentence","emo"], encoding="utf-8")
    val_data = pd.read_csv("val.txt", header=None, sep=";", names=["sentence","emo"], encoding="utf-8")
    df = pd.concat([train_data,test_data, val_data])
    df['emo'].unique()
    labelencoder = LabelEncoder()
    df['emo_encoded'] = labelencoder.fit_transform(df['emo'])
    df[['emo','emo_encoded']].drop_duplicates(keep='first')
    sentences = df.sentence.values
    y = df.emo.values
    x_train,x_test,y_train,y_test = train_test_split(sentences,y, test_size=0.1,shuffle=True, random_state=41)
    return x_train,x_test,y_train,y_test