import data_handler as dh
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import GradientBoostingRegressor

x_train, x_test, y_train, y_test = dh.get_data("./insurance.csv")
params = {'n_estimators': 100, 'learning_rate': 0.2, 'max_depth': 2, 'random_state': 0, 'loss': 'squared_error'}

model = GradientBoostingRegressor(**params)
model.fit(x_train, y_train)
mse = mean_squared_error(y_test, model.predict(x_test))

print(mse)

test_score = np.zeros((params["n_estimators"],), dtype=np.float64)
print(test_score)