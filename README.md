# 💡Predictive Analytics - Dow Jones Index Prediction
---
## Project Overview
This project aims to predict the closing stock prices for the following week on the Dow Jones Index using regression algorithms. By leveraging historical data, the model will forecast next week’s stock closing prices.

---
## Problem Statements
1. How can we accurately predict next week's stock closing prices based on historical data to assist investors in making informed decisions?
2. Which regression algorithm provides the most optimal results in stock price prediction based on relevant evaluation metrics?

## Goals
1. Develop a predictive model for stock closing prices that can provide sufficiently accurate estimates to support investor decision-making.
2. Evaluate the performance of various regression algorithms to determine the best model based on appropriate evaluation metrics.

---
## Dataset
---
> The dataset used consists of historical Dow Jones Index data, containing weekly stock price information from several major companies. Features include opening price (Open), closing price (Close), trading volume (Volume), and more. The data has 750 rows and 16 columns, with two columns containing 30 missing values: `percent_change_volume_over_last_wk` and `previous_weeks_volume`.

---

## Algorithms Used
1. **Linear Regression**
2. **Decision Tree**
3. **Random Forest**
4. **Support Vector Regression (SVR)**
5. **Gradient Boosting**

## Evaluation Metrics
1. Mean Squared Error (MSE)
2. R2 Score
3. Mean Absolute Error (MAE)
4. Root Mean Squared Error (RMSE)
5. Mean Absolute Percentage Error (MAPE)

## Best Model
The best-performing model is **Linear Regression**, with the lowest MSE (0.0008) and the highest R2 score (0.9992), indicating excellent accuracy in stock price prediction.

## Conclusion
The Linear Regression model successfully delivered the most accurate predictions among all tested models. It was chosen due to its high accuracy, simplicity, and ease of interpretation.

---
## 📂Folder Structure
```
├── Laporan_submission_1_Predictive_Analytics.md # Project report and documentation
├── Proyek_Machine_Learning_Predictive_Analytics_Tsamarah_Muthi'ah_A.ipynb # Jupyter notebook containing the code and analysis
├── Proyek_Machine_Learning_Predictive_Analytics_Tsamarah_Muthi'ah_A.py # Python script
├── README.md # Project overview and instructions
├── dow_jones_index.csv # Dataset containing historical Dow Jones index data
├── requirements.txt # List of required libraries and dependencies
```

## ⚙️Installation
To install the required libraries, run:
```
pip install -r requirements.txt
```


## 📌Usage
1. Run the Jupyter Notebook to preprocess the data and train the models.
2. Evaluate model performance using the provided metrics.
3. Compare the results and select the best-performing model.

## License
This project is licensed under the MIT License.
