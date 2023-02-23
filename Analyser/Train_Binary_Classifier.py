import pandas as pd
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report,confusion_matrix
import pickle
from datetime import datetime


def print_messages(message):
    print(str(datetime.now())+": "+message)


def load_dataset(dataset_type,csv_path,no_of_rows,header):
    type_label = False
    if dataset_type == "Benign":
        type_label = 0
    elif dataset_type == "Attack":
        type_label = 1


    print_messages("Loading "+ dataset_type+" Data.")
    if header == True:
        df = pd.read_csv(csv_path, nrows=no_of_rows)
    else:
        df = pd.read_csv(csv_path, nrows=no_of_rows, header=None)
    df.dropna()
    df['type'] = type_label
    print_messages(dataset_type+" Data Loaded.")
    return df


def train_binary_classifier(df_all):
    X = df_all.loc[:, df_all.columns != type]
    y = df_all.type

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

    classifier = XGBClassifier()
    classifier.fit(X_train, y_train)

    predictions = classifier.predict(X_test)
    print(classification_report(y_test, predictions))

    return classifier


def save_model_pickle(classifier, file_name):
    print_messages("Saving model file.")
    pickle_out = open(file_name, "wb")
    pickle.dump(classifier, pickle_out)
    pickle_out.close()
    print_messages("Model file saved.")


def main():
    benign_csv_path = "datasets/Danmini_Doorbell/benign_traffic.csv"
    no_of_rows_benign = 10000
    df_benign = load_dataset("Benign",benign_csv_path, no_of_rows_benign,header=True)

    attack_csv_path = "datasets/Danmini_Doorbell/mirai_attacks/ack.csv"
    no_of_rows_attack = 10000

    df_attack = load_dataset("Attack", attack_csv_path, no_of_rows_attack, header=True)

    df_all = pd.concat([df_attack, df_benign], ignore_index=True)

    classifier = train_binary_classifier(df_all)

    model_file_name = "models/xgb_binary_danmini.pkl"
    save_model_pickle(classifier,model_file_name)

if __name__ == '__main__':
    main()

