# AI-powered-Network-Traffic-Analyser
This is a prototype of AI-powered traffic analyser for IoT networks.

This application uses a binary classifier and a one-class classifier in the backend to analyse the network traffic and classify it as benign or malicious. A dashboard is created using streamlit-python to visualise analysed data in the front end. When the model identifies malicious traffic, the information related to that record is displayed on the dashboard.

The user has to upload the CSV file with the network traffic information and then the number of streams needs to be selected based on the user preference. Then this application provided an option to choose whether the analysis is done using a one class classifier or a binary class classifier. 

Based on the results highest accuracy is given when the binary class classification is used. The below screenshots will demonstrate the process of model training and the evaluation using these two classification methods.

Training one class classifier with benign_traffic.csv in Danmini_Doorbell dataset (https://archive.ics.uci.edu/ml/machine-learning-databases/00442/Danmini_Doorbell/) and evaluating Danmini_Doorbell mirai_attack ack.csv dataset.
![image1](https://user-images.githubusercontent.com/124127000/220923735-65ae1c5b-355d-4618-b25f-cb49ca5621bb.png)

Evaluating one class classifier predictions with Danmini_Doorbell mirai_attacks udpplain.csv
![image2](https://user-images.githubusercontent.com/124127000/220923822-27f9b9dd-1379-4053-a526-8e636a87bba2.png)

Training binary class classifier with benign_traffic.csv and mirai_attack ack.csv datasets in https://archive.ics.uci.edu/ml/machine-learning-databases/00442/Danmini_Doorbell)
![image3](https://user-images.githubusercontent.com/124127000/220923877-a4755289-5e99-499a-8eec-767d52289d59.png)

Evaluating binary class classifier with Ecobee_Thermostat datasets in https://archive.ics.uci.edu/ml/machine-learning-databases/00442/Ecobee_Thermostat/
![image4](https://user-images.githubusercontent.com/124127000/220923925-b44c2081-4f01-426c-8790-1de188db5a77.png)


Screenshots of the dashboard:

![image5](https://user-images.githubusercontent.com/124127000/220924076-245d60cd-78d5-489d-af8e-0d6c2381cecf.png)

![image6](https://user-images.githubusercontent.com/124127000/220924098-c414ace1-9c96-428c-834e-6b71c27a2ed2.png)

![image7](https://user-images.githubusercontent.com/124127000/220924126-062273d2-3b80-494f-9bf2-f0e2771eb03e.png)

![image8](https://user-images.githubusercontent.com/124127000/220924286-e4380af4-7252-4941-911c-9876633c32be.png)

![image9](https://user-images.githubusercontent.com/124127000/220929070-940c435e-6cb3-4990-8ad9-20c7fad17f46.png)

![image10](https://user-images.githubusercontent.com/124127000/220929135-d4c901f9-7a68-4d92-9193-c1ccd116e56c.png)


#### Required Libraries: 
  streamlit
  matplotlib
  scikit-learn
  
##### Instructions to run:
streamlit run main.py

You can visit the URL similar to http://localhost:8501 (Exact url will be displayed in your prompt)

