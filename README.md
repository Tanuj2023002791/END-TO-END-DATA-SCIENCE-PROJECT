# END-TO-END-DATA-SCIENCE-PROJECT

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: JAMI TANUJ

*INTERN ID*: CT06DL1326

*DOMAIN*: DATA SCIENCE

*DURATION*: 6 WEEKS

*MENTOR*: NEELA SANTHOSH

## DESCRIPTION

## 🎧 End-to-End Music Review Sentiment Analysis Project — Explained Step by Step

## 🎯 Objective:
To build, train, and deploy a machine learning model that predicts whether a music review is positive or negative. This project demonstrates the complete Data Science lifecycle — from preprocessing raw text to deploying a REST API using Flask.

✅ Step 1: Data Collection & Preparation
We created a small, manually labeled dataset containing short reviews of music or songs.
Each review reflects the opinion of a listener, marked as either: Positive (1) — for favorable feedback like “This track is a masterpiece!” Negative (0) — for criticism like “This song was painfully bad.” We stored the reviews and labels in a structured format (using pandas.DataFrame), preparing it for machine learning.

✅ Step 2: Text Preprocessing and Vectorization
Machine learning algorithms require numerical input, not raw text. So, we used CountVectorizer to transform the text reviews into numerical vectors. This technique counts the frequency of each word and turns each sentence into a vector of word counts — enabling the model to recognize patterns in language linked to sentiment.

✅ Step 3: Model Training We trained a Logistic Regression classifier — a lightweight yet effective algorithm for binary classification tasks. The model learned from the training data which word patterns are commonly associated with positive vs. negative music reviews. For example, words like "amazing" or "love" may suggest positive sentiment, while "boring" or "trash" hint at negativity.

✅ Step 4: Saving the Model and Vectorizer
Once trained, both the model and vectorizer were saved using joblib. This ensures we don’t have to retrain the model every time we want to make predictions. We can simply load and use the saved files in our web application.

✅ Step 5: API Creation with Flask
We developed a REST API using Flask, enabling real-time predictions through HTTP requests.
The API has:
*GET / → a welcome route
*POST /predict → accepts a JSON review, processes it with the vectorizer, and returns:
   *Predicted sentiment ("Positive" or "Negative")
   *Model’s confidence score

✅ Step 6: Deployment Using Replit
After testing locally, we deployed the project using Replit, an online IDE that lets Python apps run on the web.
Steps followed:
 *Uploaded all files to Replit (model.py, app.py, model.pkl, etc.)
 *Configured the environment to use port 8080
 *Ran the Flask app and got a public URL
 Now, anyone can access our Music Review Sentiment API through this link and use it in real time.

✅ Step 7: API Testing
We tested the deployed API using tools like ReqBin, where we sent a sample movie review in the form of a POST request.
The API successfully returned whether the review was positive or negative, along with a confidence percentage showing how sure the model was about its prediction.

🔗 Final Deployment URL:
The project was successfully deployed to this live link:

https://4ab52e12-3b5c-44cb-b1d7-01831b720de8-00-l7a2z6d96aau.sisko.replit.dev/

## OUTPUT:

1. In the replit:
![Image](https://github.com/user-attachments/assets/5be1c489-a810-42bd-9850-c6bd824eb0f2)

2. After the training in online one:
![Image](https://github.com/user-attachments/assets/8d5464d2-ae8a-4353-9230-7bf301584e4f)

3. After trying in the online api testing tool:
![Image](https://github.com/user-attachments/assets/ea7c31f3-12a9-4617-a1ca-c44593187f4d)






