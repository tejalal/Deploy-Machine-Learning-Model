# Deploy Machine Learning Model
Contains the details of creating, training and deployment of SVC (Support Vector Classifier) for the classification of IRIS Flower dataset.

Repository contains diffeent files

- IRIS.csv: IRIS flower dataset
- trainsave.py: Create, train and save the model
- mainfile.py inside 'api' folder
- pythonClient.py: To test the API using python code
- javaClient.py
This post has four different parts.
- Step 1:First we created the SVC(Support Vector Classifier) using Python and save the trained model. In order to generate the model, open IRIS_SVC.ipynb file in jupyter notebook and execute all the cells one by one. 
- Run testSavedModel to check the generated file for new input (Optional)
- Copy generated model file to api folder
- Install Flask if not already installed by 'pip install flask'
- There is another file in api folder names as mainfil.py, excute it by 'python mainfile.py' 
- 
- Next, We use python Flask framework for creating the Web API through which we can pass the new input to the saved model and can predict the class.
- In the third part, we use Python to consume the Web API
- In the fourth part, we use JAVA to consume the Web API

Please follow [this link](https://tejalal.wordpress.com/2019/01/09/deploy-ml-model/) for the detailed instructions
