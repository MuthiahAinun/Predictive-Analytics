# 💡Predictive-Analytics - Dow Jones Index Prediction
---
## Project Overview
Proyek ini bertujuan untuk memprediksi harga penutupan saham minggu berikutnya pada indeks Dow Jones menggunakan algoritma regresi. Dengan memanfaatkan data historis, model akan melakukan prediksi harga penutupan saham pada minggu berikutnya.

---
---
## Problem Statements
1. Bagaimana cara memprediksi harga penutupan saham minggu berikutnya secara akurat berdasarkan data historis untuk membantu investor dalam pengambilan keputusan?
2. Algoritma regresi mana yang memberikan hasil paling optimal dalam memprediksi harga saham berdasarkan metrik evaluasi yang relevan?

## Goals
1. Mengembangkan model prediksi harga penutupan saham yang dapat memberikan estimasi yang cukup akurat untuk membantu investor dalam pengambilan keputusan.
2. Mengevaluasi performa berbagai algoritma regresi untuk menentukan model terbaik berdasarkan metrik evaluasi yang sesuai.
---
## Dataset
---
> Dataset yang digunakan adalah data historis indeks Dow Jones, yang berisi informasi harga saham mingguan dari beberapa perusahaan besar. Fitur yang digunakan meliputi harga pembukaan (Open), harga penutupan (Close), volume transaksi (Volume), dan lainnya. Data memiliki 750 baris dan 16 kolom, dengan dua kolom yang memiliki 30 nilai hilang, yaitu pada Kolom percent_change_volume_over_last_wk dan Kolom previous_weeks_volume.
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
Model terbaik adalah **Linear Regression**, dengan nilai MSE terendah (0.0008) dan R2 tertinggi (0.9992), menunjukkan akurasi yang sangat tinggi dalam memprediksi harga saham.

## Conclusion
Model Linear Regression berhasil memberikan hasil prediksi terbaik dibandingkan model lainnya. Model ini dipilih karena akurasinya yang tinggi, kesederhanaannya, dan interpretasi yang mudah.

---
## 📂Folder Structure
```
├── Laporan_submission_1_Predictive_Analytics.md                             # Project report and documentation
├── Proyek_Machine_Learning_Predictive_Analytics_Tsamarah_Muthi'ah_A.ipynb   # Jupyter notebook containing the code and analysis
├── Proyek_Machine_Learning_Predictive_Analytics_Tsamarah_Muthi'ah_A.py      # Script Python
├── README.md                                                                # Project overview and instructions
├── dow_jones_index.csv                                                      # Dataset containing historical Dow Jones index data
├── requirements.txt                                                         # List of required libraries and dependencies
```

## ⚙️Installation
To install the required libraries, run:
```
pip install -r requirements.txt
```

## 📌Usage
1. Run the Jupyter Notebook to preprocess the data and train models.
2. Evaluate model performance using the provided metrics.
3. Compare results and choose the best model.

## License
This project is licensed under the MIT License.

---
