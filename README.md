# 2022_nycu_database
Introduction to Database Systems - Final Project\
2022 Spring, by Prof. 曾意儒
### Introduction

透過 Decision Tree Classifier 分析句子情緒，並連接到 Spotify，推薦使用者相符情緒的音樂。

### Demo


https://user-images.githubusercontent.com/74719131/228342833-33b21057-4c41-4a0a-9228-c2e3ba51d589.mp4


### Application description

1. 預先擷取Spotify歌單並輸入至DBMS處理資料
2. 預先將Emotions dataset中的資料用sklearn中的DecisionTreeClassifier訓練情緒分
類器
3. 使用者輸入句子
4. 用情緒分類器判斷輸入句子的情緒，得到emotion tag
5. 連線database，用query隨機找出符合emotion tag的一首歌曲，並輸出歌名、歌手、
url等資訊
6. 利用webbrowser模組根據url開啟Spotify新分頁

