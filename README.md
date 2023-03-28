# 2022_nycu_database
Introduction to Database Systems - Final Project\
2022 Spring, by Prof. 曾意儒
### Introduction

透過 Decision Tree Classifier 分析句子情緒，並連接到 Spotify，推薦使用者相符情緒的音樂。\
為 [Introduction to Artificial Intelligence - Final Project](https://github.com/sheepycat/Music_Recommendation_AI.git) 的延伸 : 改動架構，並加入DBMS。

### Demo


https://user-images.githubusercontent.com/74719131/228342833-33b21057-4c41-4a0a-9228-c2e3ba51d589.mp4


### Application description

1. 預先擷取 Spotify 歌單並輸入至 DBMS 處理資料 (使用 AWS Learner Lab)
2. 預先將 [Emotions dataset](https://www.kaggle.com/datasets/praveengovi/emotions-dataset-for-nlp) 中的資料用 sklearn 中的 DecisionTreeClassifier 訓練情緒分
類器
3. 使用者輸入句子
4. 用情緒分類器判斷輸入句子的情緒，得到 emotion tag
5. 連線 database，用 query 隨機找出符合 emotion tag 的一首歌曲，並輸出歌名、歌手、
url 等資訊
6. 利用 webbrowser 模組根據 url 開啟 Spotify 新分頁

