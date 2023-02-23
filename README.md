# AI-powered-Network-Traffic-Analyser
This is a prototype of AI-powered traffic analyser for IoT networks.

This application uses a binary classifier and a one-class classifier in the backend to analyse the network traffic and classify it as benign or malicious. A dashboard is created using streamlit-python to visualise analysed data in the front end. When the model identifies malicious traffic, the information related to that record is displayed on the dashboard.

The user has to upload the CSV file with the network traffic information and then the number of streams needs to be selected based on the user preference. Then this application provided an option to choose whether the analysis is done using a one class classifier or a binary class classifier. 

Based on the results highest accuracy is given when the binary class classification is used. The below screenshots will demonstrate the process of model training and the evaluation using these two classification methods.

Train one class classification with benign_traffic.csv in Danmini_Doorbell dataset (https://archive.ics.uci.edu/ml/machine-learning-databases/00442/Danmini_Doorbell/)
![MicrosoftTeams-image](https://user-images.githubusercontent.com/124127000/220912838-f15d768b-9889-4ac8-b6e4-c495fb54a8f6.png)

Test one class classification with -------------
![MicrosoftTeams-image (1)](https://user-images.githubusercontent.com/124127000/220916408-9219d18f-907c-4866-bc5b-fce5293bec13.png)

Train binary class classification with ------------
![MicrosoftTeams-image (2)](https://user-images.githubusercontent.com/124127000/220916866-76830e26-7114-4b55-a1c7-e16b7734c630.png)

Test binary class classification with -----------
![MicrosoftTeams-image (3)](https://user-images.githubusercontent.com/124127000/220917076-79a43dec-cfab-4ae3-af38-14ec3c07c322.png)
