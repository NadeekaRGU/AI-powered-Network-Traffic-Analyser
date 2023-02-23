import pandas as pd
from sklearn.svm import OneClassSVM
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report,confusion_matrix
import pickle
from datetime import datetime


def print_messages(message):
    print(str(datetime.now())+": "+message)


def evaluate_model_inference(df,model_file):
    print_messages("Evaluating Model Inference.")
    df['type']=True
    X_all = df.loc[:, df.columns != type]

    pickle_in = open(model_file, "rb")
    classifier = pickle.load(pickle_in)

    predictions = classifier.predict(X_all)

    predictions = [False if i == -1 else True for i in predictions]

    print(predictions)

    print_messages("Inference Complete.")



def main():
    model_file_name = "models/ocsvm_danmini_benign.pkl"

    csv_path = "datasets/Danmini_Doorbell/mirai_attacks/udpplain.csv"
    no_of_rows = 100

    df = pd.read_csv(csv_path, nrows=no_of_rows)

    evaluate_model_inference(df,model_file_name)

if __name__ == '__main__':
    main()