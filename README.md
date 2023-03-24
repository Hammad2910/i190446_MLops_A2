# Dockrized Closing Price Prediction Model Wrapped up in Flask Application Using Jenkins
## Data set and ML Model
We used the dataset of Pakistan Stock Exchange from Kaggle. It has 3222 records. It has different attributes like Date, Open, High, Low, Close, Change and Volume. Our target class is Close. We are using Linear Regression model for predicting the closing values.
## ML FLOW
We have also integrated our model with ML FLOW. Here are the sample screen shot of MLFLOW Interface.
<a href="https://www.flickr.com/photos/197979836@N06/52768787053/in/dateposted-public/" title="mlflow"><img src="https://live.staticflickr.com/65535/52768787053_bcb54a6790_h.jpg" alt="mlflow"></a>

Here is the screenshot of metrices shown on ML FLOW

<a href="https://www.flickr.com/photos/197979836@N06/52768788245/"><img src="https://live.staticflickr.com/65535/52768788245_d4c5cbf2b0.jpg" alt="mlflow results" /></a>


## Basic CICD Pipleline
We have created a BASIC CICD pipleine by running GIthub Jobs like Pylint for checking the syntax and CodeQL for security purposes


## Flask Apllication
We have wrapped up our model inside a basic Flask Apllication. Here is the Screen Shot of it

![flask app interface](https://live.staticflickr.com/65535/52768627579_1f53938c30.jpg)

<a href="https://www.flickr.com/photos/197979836@N06/52768381551/"><img src="https://live.staticflickr.com/65535/52768381551_1b0405c930.jpg" alt="app result" /></a>



## Dockerization of Flask Application
We have dockerized our Flask Application. It is lisntening on local host 5001. Here is the screen shot of running container of our Flask Application

![container](https://live.staticflickr.com/65535/52768627584_0c744a8d62.jpg)




## Integration with Jenkins
We have Integrated our Docker image with Jenkins. Here is the screenshots of jobs run by jenkins

![jenkins jobs2](https://live.staticflickr.com/65535/52768373266_68e4f997ca.jpg)


![jenkins jobs 1](https://live.staticflickr.com/65535/52768812945_0cc883ce92.jpg)








