import pandas as pd
import pickle
from datetime import datetime


def print_messages(message):
    print(str(datetime.now())+": "+message)


def evaluate_model(model_file_name,csv_path):
    pickle_in = open(model_file_name, "rb")
    classifier = pickle.load(pickle_in)
    df = pd.read_csv(csv_path, nrows=100)

    df['type'] = -1

    predictions = classifier.predict(df)

    print(predictions)


def main():

    model_file_name = "models/xgb_binary_danmini.pkl"

    print_messages("Evaluating benign data.")
    test_data_csv_benign = "datasets/Ecobee_Thermostat/benign_traffic.csv"
    evaluate_model(model_file_name, test_data_csv_benign)

    print_messages("Evaluating attack data.")
    test_data_csv_attack="datasets/Ecobee_Thermostat/mirai_attacks/ack.csv"
    evaluate_model(model_file_name, test_data_csv_attack)

    print_messages("evaluating unknown data.")
    test_data_csv_unknown = "datasets/sampleunknown.csv"
    evaluate_model(model_file_name, test_data_csv_unknown)


if __name__ == '__main__':
    main()

