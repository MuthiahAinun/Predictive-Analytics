# -*- coding: utf-8 -*-
"""Proyek_Machine_Learning_Predictive_Analytics_Tsamarah_Muthi'ah_A.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/github/MuthiahAinun/Predictive-Analytics/blob/main/Proyek_Machine_Learning_Predictive_Analytics_Tsamarah_Muthi'ah_A.ipynb

# 📚Proyek Machine Learning- Predictive Analytics: [Dow-Jones-Index-dataset]
- **Nama:** [Tsamarah Muthi'ah Abdullah]
- **Email:** [a135xaf486@devacademy.id]
- **ID Dicoding:** [a135xaf48]

## **🌏Domain Proyek**
Prediksi Pergerakan Saham pada Dow Jones Index

- **Latar Belakang:**
Pergerakan saham yang dinamis memerlukan prediksi untuk membantu investor mengambil keputusan. Dengan menganalisis data historis, kita dapat memprediksi pergerakan saham.

- **Referensi:**
1. Chen, M., & Wei, Y. (2018). Stock Market Prediction using Machine Learning: A Systematic Review. Journal of Economic and Financial Studies.
2. Yu, H., & Yan, X. (2019). Predicting Stock Price Movements with Machine Learning Techniques. IEEE Transactions on Knowledge and Data Engineering.

## **🎯Business Understanding**

**Problem Statements:**
1. Bagaimana memprediksi perubahan harga saham berdasarkan data historis?
2. Algoritma regresi mana yang paling akurat untuk memprediksi pergerakan harga saham?

**Goals**

1. Menghasilkan model prediksi harga saham dengan akurasi tinggi menggunakan berbagai algoritma regresi.
2. Memilih model terbaik berdasarkan metrik evaluasi dan mempertimbangkan kelebihan serta kekurangannya.

**Solution Statement:**

1. Menggunakan 5 algoritma regresi, yaitu Linear Regression, Random Forest , Decision Tree, SVR, dan Gradient Boosting.
2. Melakukan evaluasi dengan metrik MSE, R2 Score, MAE, RMSE, dan MAPE untuk membandingkan performa model.

# Import Library
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

"""# 1. Data Understanding

Dataset diambil dari UCI Machine Learning Repository.

**Link =** 'https://archive.ics.uci.edu/ml/machine-learning-databases/00312/dow_jones_index.zip'
"""

dataset = 'dow_jones_index.csv'

# Load Dataset
df = pd.read_csv(dataset)
print('\nShape of data:', df.shape)

print('Columns:', df.columns)

print(df.head())

print("Informasi Dataset:")
print(df.info())

print('\nStatistik Deskriptif:')
print(df.describe())

print("Jumlah data:", len(df))

"""**Variabel pada Dow Jones Index Dataset:**

1. quarter: Kuartal keuangan (1, 2, 3, atau 4).
2. stock: Kode saham perusahaan.
3. date: Tanggal transaksi.
4. open: Harga pembukaan saham.
5. high: Harga tertinggi selama periode tersebut.
6. low: Harga terendah selama periode tersebut.
7. close: Harga penutupan saham.
8. volume: Volume perdagangan saham.
9. percent_change_price: Persentase perubahan harga saham.
10. percent_change_volume_over_last_wk: Persentase perubahan volume perdagangan dibanding minggu sebelumnya.
11. previous_weeks_volume: Volume perdagangan pada minggu sebelumnya.
12. next_weeks_open: Harga pembukaan saham pada minggu berikutnya.
13. next_weeks_close: Harga penutupan saham pada minggu berikutnya.
14. percent_change_next_weeks_price: Persentase perubahan harga saham pada minggu berikutnya.
15. days_to_next_dividend: Jumlah hari sampai dividen berikutnya.
16. percent_return_next_dividend: Persentase pengembalian pada dividen berikutnya.
"""

# Data Visualization dan Exploratory Data Analysis (EDA)
print('\nData Visualization dan Exploratory Data Analysis (EDA):')
sns.set(style="whitegrid")

# Visualisasi distribusi harga pembukaan (open)
plt.figure(figsize=(10, 6))
sns.histplot(df['open'].str.replace('$', '').astype(float), bins=30, kde=True)
plt.title('Distribusi Harga Pembukaan Saham')
plt.xlabel('Harga Pembukaan')
plt.show()

# Visualisasi distribusi volume perdagangan
plt.figure(figsize=(10, 6))
sns.histplot(df['volume'].astype(float), bins=30, kde=True)
plt.title('Distribusi Volume Perdagangan')
plt.xlabel('Volume')
plt.show()

# Visualisasi pairplot untuk analisis hubungan variabel
sns.pairplot(df)
plt.title('Visualisasi Korelasi Antar Variabel')
plt.show()

"""# 2. Data Preparation

Teknik data preparation yang dilakukan pada tahap ini meliputi data cleaning, konversi data, encoding, normalisasi, seleksi fitur, dan pembagian data.

## A. Data Cleaning
"""

# 1. Informasi Statistik untuk Kolom dengan Nilai Hilang
print('Statistik untuk kolom percent_change_volume_over_last_wk:')
print(df['percent_change_volume_over_last_wk'].describe())
print('Jumlah nilai hilang:', df['percent_change_volume_over_last_wk'].isnull().sum())

print('Statistik untuk kolom previous_weeks_volume:')
print(df['previous_weeks_volume'].describe())
print('Jumlah nilai hilang:', df['previous_weeks_volume'].isnull().sum())

# Mengecek jumlah missing values di setiap kolom
print(df.isnull().sum())

"""**Tahapan ini bertujuan untuk mengecek informasi nilai hilang pada data. Nilai hilang dapat mengganggu proses analisis dan prediksi jika tidak ditangani dengan baik.**"""

# 2. Imputasi Nilai Hilang dengan Mean

df['percent_change_volume_over_last_wk'].fillna(df['percent_change_volume_over_last_wk'].mean(), inplace=True)
df['previous_weeks_volume'].fillna(df['previous_weeks_volume'].mean(), inplace=True)

# Informasi Statistik untuk Kolom dengan Nilai Hilang setelah Imputasi
print('\nStatistik untuk kolom percent_change_volume_over_last_wk setelah imputasi:')
print(df['percent_change_volume_over_last_wk'].describe())
print('\nJumlah nilai hilang:', df['percent_change_volume_over_last_wk'].isnull().sum())

print('\nStatistik untuk kolom previous_weeks_volume setelah imputasi:')
print(df['previous_weeks_volume'].describe())
print('\nJumlah nilai hilang:', df['previous_weeks_volume'].isnull().sum())

"""**Teknik yang digunakan adalah imputasi dengan rata-rata untuk mengisi nilai hilang pada kolom 'percent_change_volume_over_last_wk' dan 'previous_weeks_volume'.**

## B. Konversi Data
"""

# 3. Menghapus simbol dolar dan mengonversi ke float
for col in ['open', 'high', 'low', 'close', 'next_weeks_open', 'next_weeks_close']:
    df[col] = df[col].replace('[\$,]', '', regex=True).astype(float)

"""**Simbol dolar ($) pada kolom harga dapat menghambat proses perhitungan sehingga perlu dikonversi menjadi tipe data numerik (float).**

## C. Encoding
"""

# 4. Encoding Variabel Kategorikal
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
df['stock'] = encoder.fit_transform(df['stock'])

"""**Encoding diperlukan untuk mengubah data kategorikal menjadi numerik agar dapat digunakan dalam algoritma pembelajaran mesin.**

## D. Normalisasi
"""

# 5. Feature Scaling
scaler = StandardScaler()
num_cols = df.select_dtypes(include=['float64', 'int64']).columns
df[num_cols] = scaler.fit_transform(df[num_cols])

"""**Normalisasi bertujuan untuk menyamakan skala data numerik agar model dapat belajar secara optimal.**

## E. Seleksi Fitur
"""

# 6. Feature Selection
# Menghapus kolom date sebelum menghitung korelasi jika ada
if 'date' in df.columns:
    df = df.drop(['date'], axis=1)
correlation_matrix = df.corr()
print('\nMatriks Korelasi:')
print(correlation_matrix)

"""**Seleksi fitur dilakukan untuk mengurangi dimensionalitas dan mempertahankan variabel yang memiliki korelasi tinggi terhadap variabel target. Pada tahap ini, kolom 'date' dihapus karena tidak relevan dalam proses prediksi.**

## F. Data Splitting
"""

# 7. Data Splitting
from sklearn.model_selection import train_test_split
X = df.drop(['next_weeks_close'], axis=1)
y = df['next_weeks_close']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print('\nData berhasil dipisahkan menjadi data latih dan data uji.')

"""**Tahapan ini bertujuan untuk membagi data menjadi data latih dan data uji guna menguji performa model secara objektif.**

# 3. Modeling

1. Pada tahap modeling, berbagai algoritma regresi akan digunakan untuk memprediksi harga penutupan saham minggu berikutnya,yaitu:

- **Linear Regression:**
  - Kelebihan: Sederhana, mudah diinterpretasikan, dan efektif jika hubungan antara variabel bersifat linear.
  - Kekurangan: Kurang akurat jika terdapat hubungan non-linear antara variabel.

- **Decision Tree Regressor:**
  - Kelebihan: Mampu menangani data non-linear, mudah diinterpretasikan.
  - Kekurangan: Rentan terhadap overfitting terutama pada data dengan banyak fitur.

- **Random Forest Regressor:**
  - Kelebihan: Mengurangi overfitting dibandingkan Decision Tree dengan menggabungkan banyak pohon keputusan.
  - Kekurangan: Lebih kompleks dan membutuhkan lebih banyak sumber daya komputasi.

- **Support Vector Regressor (SVR):**
  - Kelebihan: Efektif dalam data berdimensi tinggi dan robust terhadap outlier
  - Kekurangan: Waktu komputasi yang tinggi pada dataset besar.

- **Gradient Boosting Regressor:**
  - Kelebihan: Akurasi yang tinggi dengan cara menggabungkan model yang lemah secara bertahap.
  - Kekurangan: Rentan terhadap overfitting jika parameter tidak diatur dengan baik.

2. Proses pemodelan dilakukan dengan mengatur parameter default pada masing-masing model. Setelah itu, dilakukan evaluasi menggunakan metrik seperti MSE, R2 Score, MAE, RMSE, dan MAPE.

3. Setelah melakukan perbandingan dari semua model, didapatkan bahwa Linear Regression memiliki performa terbaik dengan nilai MSE terendah (0.0008), R2 tertinggi (0.9992), MAE terendah (0.0189), RMSE terendah (0.0289), dan MAPE terendah (4.44%). Oleh karena itu, model terbaik yang dipilih adalah **Linear Regression**, karena memberikan akurasi yang tinggi dan interpretasi yang mudah, dibandingkan model lain yang cenderung lebih kompleks dan rentan terhadap overfitting.
"""

# Modeling
models = {
    'Linear Regression': LinearRegression(),
    'Decision Tree': DecisionTreeRegressor(random_state=42),
    'Random Forest': RandomForestRegressor(random_state=42),
    'SVR': SVR(),
    'Gradient Boosting': GradientBoostingRegressor(random_state=42)
}

"""# 4. Evaluation"""

for name, model in models.items():
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)
    mae = mean_absolute_error(y_test, predictions)
    rmse = np.sqrt(mse)
    mape = np.mean(np.abs((y_test - predictions) / y_test)) * 100
    print(f'\n{name} - MSE: {mse:.4f}, R2 Score: {r2:.4f}, MAE: {mae:.4f}, RMSE: {rmse:.4f}, MAPE: {mape:.2f}%')

"""# **Hasil evaluasi:**

1. Pada tahap evaluasi, metrik yang digunakan adalah MSE, R2 Score, MAE, RMSE, dan MAPE:
  - **MSE (Mean Squared Error):**
    - Mengukur rata-rata kesalahan kuadrat antara nilai prediksi dan nilai aktual. Semakin kecil nilainya, semakin baik model dalam memprediksi nilai sebenarnya.
    - Formula: MSE = (1/n) * Σ(actual - predicted)^2
    - Metrik ini bekerja dengan menghitung selisih antara nilai aktual dan nilai prediksi, kemudian mengkuadratkan selisih tersebut dan menghitung rata-ratanya.
    - MSE sangat sensitif terhadap outlier karena menggunakan kuadrat dari kesalahan.

   - **R2 Score (Coefficient of Determination):**
    - Mengukur seberapa baik model menjelaskan variabilitas data aktual. Semakin mendekati 1, semakin baik model dalam menjelaskan data.
    - Formula: R2 = 1 - (Σ(actual - predicted)^2 / Σ(actual - mean_actual)^2)
    - R2 Score mengukur proporsi variansi dalam variabel dependen yang dapat dijelaskan oleh variabel independen.

  - **MAE (Mean Absolute Error):**
    - Mengukur rata-rata kesalahan absolut antara nilai prediksi dan aktual. Semakin kecil nilainya, semakin akurat prediksi model.
    - Formula: MAE = (1/n) * Σ|actual - predicted|
    - Metrik ini bekerja dengan menghitung rata-rata dari nilai absolut kesalahan prediksi.

  - **RMSE (Root Mean Squared Error):**
    - Akar dari MSE, mengembalikan satuan data asli sehingga lebih mudah diinterpretasikan. Semakin rendah, semakin baik.
    - Formula: RMSE = sqrt(MSE)
    - Metrik ini bekerja dengan menghitung akar dari MSE, sehingga lebih mudah dipahami dalam konteks satuan aslinya.

  - **MAPE (Mean Absolute Percentage Error):**
    - Mengukur persentase kesalahan rata-rata absolut. Semakin rendah persentasenya, semakin akurat model.
    - Formula: MAPE = (1/n) * Σ(|actual - predicted| / |actual|) * 100%
    - Metrik ini bekerja dengan menghitung rata-rata persentase kesalahan absolut terhadap nilai aktual.

2. Berdasarkan hasil evaluasi, berikut perbandingan performa model:
  - Linear Regression: MSE: 0.0008, R2: 0.9992, MAE: 0.0189, RMSE: 0.0289, MAPE: 4.44%
  - Decision Tree: MSE: 0.0031, R2: 0.9970, MAE: 0.0338, RMSE: 0.0554, MAPE: 24.62%
  - Random Forest: MSE: 0.0016, R2: 0.9985, MAE: 0.0244, RMSE: 0.0396, MAPE: 13.65%
  - SVR: MSE: 0.0196, R2: 0.9808, MAE: 0.0789, RMSE: 0.1398, MAPE: 25.08%
  - Gradient Boosting: MSE: 0.0011, R2: 0.9990, MAE: 0.0184, RMSE: 0.0327, MAPE: 11.87%

## **Kesimpulan:**

  Model terbaik adalah Linear Regression karena memiliki nilai MSE, MAE, RMSE, dan MAPE terendah serta R2 tertinggi dibandingkan model lainnya. Hal ini menunjukkan bahwa model ini paling akurat dalam memprediksi harga penutupan saham minggu berikutnya.

  Meskipun model Gradient Boosting juga memiliki performa yang mendekati Linear Regression dengan MSE: 0.0011 dan R2: 0.9990, Linear Regression tetap lebih unggul pada beberapa metrik lainnya. Selain itu, Linear Regression juga lebih sederhana dan mudah diinterpretasikan, sehingga menjadi pilihan terbaik.

"""