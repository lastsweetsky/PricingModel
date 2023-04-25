import pandas as pd
import numpy as np
import pickle

from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split, GridSearchCV

file_path = "output_data.csv"
save_path = "model.pkl"


def process_training_data(data):
    data = data[['mkt_id', 'output_own_price', 'output_own_cost', 'output_comp_price', 'output_own_share', 'output_X',
                 'output_own_profits', 'output_own_sales']]

    data['price_diff'] = data['output_own_price'] - data['output_comp_price']

    data['profit_per_unit'] = data['output_own_price'] - data['output_own_cost']

    grouped_data = data.groupby('mkt_id')

    X = []
    y = []

    for _, group in grouped_data:
        X_group = group[
            ['output_own_price', 'output_comp_price', 'output_own_share', 'output_X', 'price_diff', 'profit_per_unit']]
        y_group = group['output_own_sales']

        X.append(X_group)
        y.append(y_group)

    X = np.concatenate(X)
    y = np.concatenate(y)

    return X, y


def train_model(X_train, y_train):
    param_grid = {
        'n_estimators': [100, 200, 300],
        'learning_rate': [0.01, 0.1, 0.5],
        'max_depth': [3, 4, 5]
    }

    model = GradientBoostingRegressor()
    grid_search = GridSearchCV(model, param_grid=param_grid, cv=3)
    grid_search.fit(X_train, y_train)

    best_estimator = grid_search.best_estimator_
    with open(save_path, 'wb') as f:
        pickle.dump(best_estimator, f)

    return best_estimator


def predict_price(mkt_id, date, own_price, own_cost, comp_price, own_profits, own_X, own_share):
    new_data = pd.DataFrame({'mkt_id': [mkt_id],
                             'output_date': [date],
                             'output_own_price': [own_price],
                             'output_own_cost': [own_cost],
                             'output_comp_price': [comp_price],
                             'output_own_profits': [own_profits],
                             'output_X': [own_X],
                             'output_own_share': [own_share],
                             'output_own_sales': [np.nan]
                             })

    new_data['output_date'] = pd.to_datetime(new_data['output_date'])
    X_new, _ = process_training_data(new_data)
    with open(save_path, 'rb') as f:
        loaded_model = pickle.load(f)

    predicted_sales = loaded_model.predict(X_new)
    predicted_price = predicted_sales[0] * (own_price - own_cost)
    print(predicted_price)
    return predicted_price


if __name__ == "__main__":
    data = pd.read_csv(file_path)
    X, y = process_training_data(data)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = train_model(X_train, y_train)
    accuracy = model.score(X_test, y_test)
    print('Accuracy:', accuracy)
    rmse = mean_squared_error(y_test, model.predict(X_test), squared=False)
    print('RMSE:', rmse)
    predict_price(44, '2020-01-01', 7.05, 5.9, 7.11, 15.065, 42.8, 0.5152673)
