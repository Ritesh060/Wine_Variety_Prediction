# Wine_Variety_Prediction
A model with a Flask website and API for predicting the Variety of wine running on localhost. 

## Dataset
The dataset used to train the model can be found [here](https://drive.google.com/file/d/1ra9lwNjK9G8Ns0bAfzipD0u3Xwii5hc0/view).

## Final Model
The final model can be found [here](https://drive.google.com/file/d/1j1Xk_2G3YyQn8wZSloMe_JSGKUKgU0gU/view?usp=share_link).

## Link to download all the files together as a zip
All files can be dowloaded using this [link](https://drive.google.com/file/d/1AtquUDEisdY7OlGh57XHVZTYWhklXSis/view?usp=share_link).

## Insights
Insights on the data are found by visualising and calculating the mean of parameters or by analysing count of parameters. This analysis can be found [here](https://github.com/Ritesh060/Wine_Variety_Prediction/blob/main/Data_Analysis.ipynb).

## Model Training
Wine Variety is to predicted from a given set of parameters. The parameters chosen were "review_title", "review_description", "points" and "winery" as they had zero null values so more entries can be used for training which lead to better results. The algorithms used were Logistic Regression, Random Forest Classifier, Naive Bayes Classifier, K-nearest Neighbour classifier, Decision Tree Classifier and SVM Classifier to check for the highest accuracies. The highest accuracy found among these were by SVM Classifier which was over 96%. 
<br><br>
For final model, deep learning model was made by creating  Word Embedding and LSTM layers in the neural network. An accuracy of over 99% was achieved using this model. This is the final model being used for the API and the application.

## Builing API
The API was made using Flask framework and can be called in Postman application after the server is active for predicting the wine variety. This API can also be used for request methods. 

## Building Application
A website was made using HTML and CSS and was linked to the model using Flask framework.

## How to run the Application and the API??
First of all download the model file and the dataset and transfer it to the directory where the rest of the files are kept. <br><br>
Then go to the terminal which is opened in the same directory as "main.py" and run the following code:
```shell
python main.py
```
<br> A link will be generated which will be linked to the website for prediction. 
<br> The API link will be [http://127.0.0.1:5000/predict_api](http://127.0.0.1:5000/predict_api), this link can be put in Postman application for requesting predictions.

## Demo of the website and API

The demo demonstrating the website and API and can be found [here](https://www.youtube.com/watch?v=wx2nyWc_ais).
