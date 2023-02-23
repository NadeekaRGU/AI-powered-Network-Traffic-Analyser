import pandas as pd
from sklearn.svm import OneClassSVM
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report,confusion_matrix
import pickle
from datetime import datetime


def print_messages(message):
    print(str(datetime.now())+": "+message)


def load_dataset(dataset_type,csv_path,no_of_rows,header):
    type_label = False
    if dataset_type == "Benign":
        type_label = True
    elif dataset_type == "Attack":
        type_label = False

    print_messages("Loading "+ dataset_type+" Data.")
    if header == True:
        df = pd.read_csv(csv_path, nrows=no_of_rows)
    else:
        df = pd.read_csv(csv_path, nrows=no_of_rows, header=None)
    df.dropna()
    df['type'] = type_label
    print_messages(dataset_type+" Data Loaded.")
    return df

def train_one_class_classifier(df_benign):
    print_messages("Training model.")
    X = df_benign.loc[:, df_benign.columns != type]
    y = df_benign.type

    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=1)
    svm = OneClassSVM(kernel='rbf', gamma=0.01, nu=0.05)
    svm.fit(X_train)

    print_messages("Model trained.")
    return svm


def save_model_pickle(classifier, file_name):
    print_messages("Saving model file.")
    pickle_out = open(file_name, "wb")
    pickle.dump(classifier, pickle_out)
    pickle_out.close()
    print_messages("Model file saved.")


def evaluate_model(df_benign, df_attack,model_file):
    print_messages("Evaluating model.")
    df_all = pd.concat([df_attack, df_benign], ignore_index=True)
    X_all = df_all.loc[:, df_all.columns != type]
    y_all = df_all.type

    pickle_in = open(model_file, "rb")
    classifier = pickle.load(pickle_in)

    predictions = classifier.predict(X_all)

    predictions = [False if i == -1 else True for i in predictions]

    print_messages("Model evaluated.")
    print(classification_report(y_all, predictions))


def main():
    benign_csv_path = "datasets/Danmini_Doorbell/benign_traffic.csv"
    no_of_rows_benign = 10000
    df_benign = load_dataset("Benign",benign_csv_path, no_of_rows_benign,header=True)
    svm_classifier = train_one_class_classifier(df_benign)

    model_file_name = "models/ocsvm_danmini_benign.pkl"
    save_model_pickle(svm_classifier,model_file_name)

    attack_csv_path = "datasets/Danmini_Doorbell/mirai_attacks/ack.csv"
    no_of_rows_attack = 10000

    df_attack = load_dataset("Attack", attack_csv_path, no_of_rows_attack,header=True)

    evaluate_model(df_benign,df_attack,model_file_name)


if __name__ == '__main__':
    main()