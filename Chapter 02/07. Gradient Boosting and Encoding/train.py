import matplotlib.pyplot as plt

import data_handler as dh
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import GradientBoostingRegressor

x_train, x_test, y_train, y_test = dh.get_data("./insurance.csv")
params = {'n_estimators': 100, 'learning_rate': 0.1, 'max_depth': 3, 'random_state': 0, 'loss': 'squared_error'}

model = GradientBoostingRegressor(**params)
model.fit(x_train, y_train)
mse = mean_squared_error(y_test, model.predict(x_test))

test_score = np.zeros((params["n_estimators"],), dtype=np.float64)
for i, y_pred in enumerate(model.staged_predict(x_test)):
    test_score[i] = model.loss_(y_test, y_pred)

fig = plt.figure(figsize=(6, 6))
plt.subplot(1, 1, 1)
plt.title('Deviance')
plt.plot(np.arange(params["n_estimators"]) + 1,
         model.train_score_,
         'b-',
         label='Training Set Deviance')
plt.plot(np.arange(params["n_estimators"]) + 1,
         test_score,
         'r-',
         label='Test Set Deviance')
plt.legend(loc='upper right')
fig.tight_layout()
plt.show()