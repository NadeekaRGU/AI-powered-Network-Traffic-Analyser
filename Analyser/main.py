import streamlit as st
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
import pickle
import matplotlib.pyplot as plt

pickle_one_class = open("models/ocsvm_danmini_benign.pkl","rb")
pickle_binary = open("models/xgb_binary_danmini.pkl","rb")
svm = pickle.load(pickle_one_class)
xgb = pickle.load(pickle_binary)


def perform_predict(df,classifier):
    if classifier=="oneclass":
        return perform_oneclass_prediction(df)

    elif classifier=="binary":
        return perform_binary_prediction(df)


def perform_binary_prediction(df):
    predictions = xgb.predict(df)
    return predictions


def perform_oneclass_prediction(df):
    predictions = svm.predict(df)
    predictions = [False if i == -1 else True for i in predictions]
    return predictions

def main():
    st.title("Welcome to the Network Traffic Analyser")

    step_1 = "<h3>Step 1 - Network Traffic File Upload</h3>"


    st.markdown(step_1, unsafe_allow_html=True)
    result = ""

    uploaded_file = st.file_uploader("Please upload the network traffic file")
    dataframe = None

    if uploaded_file is not None:
        dataframe = pd.read_csv(uploaded_file)

        size = dataframe.shape[0]

        step_2="<h3>Step 2 - Data Range Selection</h3>"
        step_2_1 = "<h5>If you want to analyse specific set of rows please enter starting and ending rows. Otherwise leave them as it is.</h5>"
        st.markdown(step_2, unsafe_allow_html=True)
        st.markdown(step_2_1, unsafe_allow_html=True)

        start = st.number_input('Enter Starting Row',min_value=1, max_value=(size-1),value=1,format='%d')-1
        end = st.number_input('Enter Ending Row',min_value=2, max_value=size,value=size,format='%d')-1

        dataframe = dataframe.iloc[start:end]

        step_3 = "<h3>Step 3 - Classifier Selection</h3>"

        st.markdown(step_3, unsafe_allow_html=True)

        step_3_1 ="<h5>The backend of the network traffic analyser integrated with two classification approaches.</h5>"

        st.markdown(step_3_1, unsafe_allow_html=True)

        step_3_2 = "<ul><li>Binary classification (Trained with XGB)</li><li>One class classification (Trained with One Class SVM)</li></ul>"

        st.markdown(step_3_2, unsafe_allow_html=True)

        step_3_3 = "<p>Please note that there can be issues of detection when using one-class classification approach. Therefore, <b>recomnded to use binary classification</b>.</p>"

        st.markdown(step_3_3, unsafe_allow_html=True)

        ques = st.radio( "You have the option to select the classifier to analyse the traffic. Which classifier you want to use?", ('Binary Classifier','One Class Classifier'))


        if st.button("Predict"):
            classifier=""
            if ques == 'Binary Classifier':
                classifier="binary"
                dataframe['type'] = -1

            if ques == 'One Class Classifier':
                classifier="oneclass"
                dataframe['type'] = False

            attack_count=0
            benign_count=0

            result = perform_predict(dataframe,classifier)

            for x in result:
                if (x ==0 or x ==False):
                    benign_count=benign_count+1
                elif (x ==1 or x ==True):
                    attack_count=attack_count+1

            labels = 'Attack', 'Benign'

            sizes = [attack_count, benign_count]
            explode = (0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

            fig1, ax1 = plt.subplots()
            ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                    shadow=True, startangle=90)
            ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

            st.pyplot(fig1)
            st.success("Number of Attack Traffic Data: "+str(attack_count)+". Number of Benign Traffic Data:"+str(benign_count))


if __name__ == '__main__':
    main()
