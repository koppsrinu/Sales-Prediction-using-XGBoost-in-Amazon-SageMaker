import xgboost
import pandas as pd
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--train', type=str, default='/opt/ml/input/data/train')
    args = parser.parse_args()

    # Load data
    data = pd.read_csv(f'{args.train}/train.csv', header=0)
    
    X = data.iloc[:, :-1]
    y = data.iloc[:, -1]

    dtrain = xgboost.DMatrix(X, label=y)

    # Train model
    model = xgboost.train({'objective': 'reg:squarederror'}, dtrain, num_boost_round=100)

    # Save model
    model.save_model('/opt/ml/model/xgboost-model')
