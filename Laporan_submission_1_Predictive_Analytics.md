# Laporan Proyek Machine Learning - Tsamarah Muthi'ah Abdullah
---
## 🌏Domain Proyek

```Prediksi Pergerakan Saham pada Dow Jones Index```

**Latar Belakang:**

```Pergerakan saham yang dinamis memerlukan prediksi untuk membantu investor mengambil keputusan. Dengan menganalisis data historis, kita dapat memprediksi pergerakan saham.```

**Referensi:**
```
Chen, M., & Wei, Y. (2018). Stock Market Prediction using Machine Learning: A Systematic Review. Journal of Economic and Financial Studies.
Yu, H., & Yan, X. (2019). Predicting Stock Price Movements with Machine Learning Techniques. IEEE Transactions on Knowledge and Data Engineering.
```
---

## 🎯Business Understanding

### Problem Statements:
---
- Bagaimana memprediksi perubahan harga saham berdasarkan data historis?
- Algoritma regresi mana yang paling akurat untuk memprediksi pergerakan harga saham?

### Goals:

- Menghasilkan model prediksi harga saham dengan akurasi tinggi menggunakan berbagai algoritma regresi.
- Memilih model terbaik berdasarkan metrik evaluasi dan mempertimbangkan kelebihan serta kekurangannya.

### Solution Statement:

- Menggunakan 5 algoritma regresi, yaitu Linear Regression, Random Forest , Decision Tree, SVR, dan Gradient Boosting.
- Melakukan evaluasi dengan metrik MSE, R2 Score, MAE, RMSE, dan MAPE untuk membandingkan performa model.
---
## 1️⃣Data Understanding
Dataset diambil dari UCI Machine Learning Repository.
```sh
Link = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00312/dow_jones_index.zip'
```

```
Dataset yang digunakan dalam proyek ini adalah dataset indeks saham Dow Jones. Dataset ini berisi data historis pergerakan harga saham pada indeks Dow Jones Industrial Average (DJIA), yang merupakan salah satu indeks pasar saham paling berpengaruh di Amerika Serikat.
```

### 🔎Variabel pada Dow Jones Index Dataset:
- quarter: Kuartal keuangan (1, 2, 3, atau 4).
- stock: Kode saham perusahaan.
- date: Tanggal transaksi.
- open: Harga pembukaan saham.
- high: Harga tertinggi selama periode tersebut.
- low: Harga terendah selama periode tersebut.
- close: Harga penutupan saham.
- volume: Volume perdagangan saham.
- percent_change_price: Persentase perubahan harga saham.
- percent_change_volume_over_last_wk: Persentase perubahan volume perdagangan dibanding minggu sebelumnya.
- previous_weeks_volume: Volume perdagangan pada minggu sebelumnya.
- next_weeks_open: Harga pembukaan saham pada minggu berikutnya.
- next_weeks_close: Harga penutupan saham pada minggu berikutnya.
- percent_change_next_weeks_price: Persentase perubahan harga saham pada minggu berikutnya.
- days_to_next_dividend: Jumlah hari sampai dividen berikutnya.
- percent_return_next_dividend: Persentase pengembalian pada dividen berikutnya.

#### Dataset ini berisi beberapa fitur penting, antara lain:
```
1. Tanggal - Waktu pengambilan data.
2. Harga Pembukaan (Open) - Harga pembukaan saham pada awal hari perdagangan.
3. Harga Tertinggi (High) - Harga tertinggi yang dicapai dalam satu hari perdagangan.
4. Harga Terendah (Low) - Harga terendah yang dicapai dalam satu hari perdagangan.
5. Harga Penutupan (Close) - Harga penutupan saham pada akhir hari perdagangan.
6. Volume Perdagangan (Volume) - Jumlah unit saham yang diperdagangkan dalam satu hari.
7. Perubahan (Change) - Persentase perubahan harga saham pada hari tersebut.
```
```Tujuan penggunaan dataset ini adalah untuk memprediksi harga penutupan saham pada minggu berikutnya berdasarkan data historis tersebut.```

## 2️⃣Data Preparation
Teknik data preparation yang dilakukan pada tahap ini meliputi:
```
1. Data Cleaning : Tahapan ini bertujuan untuk mengecek informasi nilai hilang pada data. Nilai hilang dapat mengganggu proses analisis dan prediksi jika tidak ditangani dengan baik. Pada tahapan ini juga dilakukan Teknik imputasi dengan rata-rata untuk mengisi nilai hilang pada kolom 'percent_change_volume_over_last_wk' dan 'previous_weeks_volume'.
2. Konversi Data : Simbol dolar ($) pada kolom harga dapat menghambat proses perhitungan sehingga perlu dikonversi menjadi tipe data numerik (float).
3. Encoding : Encoding diperlukan untuk mengubah data kategorikal menjadi numerik agar dapat digunakan dalam algoritma pembelajaran mesin.
4. Normalisasi : Normalisasi bertujuan untuk menyamakan skala data numerik agar model dapat belajar secara optimal.
5. Seleksi Fitur : Seleksi fitur dilakukan untuk mengurangi dimensionalitas dan mempertahankan variabel yang memiliki korelasi tinggi terhadap variabel target. Pada tahap ini, kolom 'date' dihapus karena tidak relevan dalam proses prediksi.
6. Pembagian Data : Tahapan ini bertujuan untuk membagi data menjadi data latih dan data uji guna menguji performa model secara objektif.
```
## 3️⃣Modeling
1. Pada tahap modeling, berbagai algoritma regresi digunakan untuk memprediksi harga penutupan saham minggu berikutnya,yaitu:
- **Linear Regression:**
```
Kelebihan: Sederhana, mudah diinterpretasikan, dan efektif jika hubungan antara variabel bersifat linear.
Kekurangan: Kurang akurat jika terdapat hubungan non-linear antara variabel.
```
- **Decision Tree Regressor:**
```
Kelebihan: Mampu menangani data non-linear, mudah diinterpretasikan.
Kekurangan: Rentan terhadap overfitting terutama pada data dengan banyak fitur.
```
- **Random Forest Regressor:**
```
Kelebihan: Mengurangi overfitting dibandingkan Decision Tree dengan menggabungkan banyak pohon keputusan.
Kekurangan: Lebih kompleks dan membutuhkan lebih banyak sumber daya komputasi.
```
- **Support Vector Regressor (SVR):**
```
Kelebihan: Efektif dalam data berdimensi tinggi dan robust terhadap outlier
Kekurangan: Waktu komputasi yang tinggi pada dataset besar.
```
- **Gradient Boosting Regressor:**
```
Kelebihan: Akurasi yang tinggi dengan cara menggabungkan model yang lemah secara bertahap.
Kekurangan: Rentan terhadap overfitting jika parameter tidak diatur dengan baik.
```
---
> Proses pemodelan dilakukan dengan mengatur parameter default pada masing-masing model. Setelah itu, dilakukan evaluasi menggunakan metrik seperti MSE, R2 Score, MAE, RMSE, dan MAPE. Setelah melakukan perbandingan dari semua model, didapatkan bahwa Linear Regression memiliki performa terbaik dengan nilai MSE terendah (0.0008), R2 tertinggi (0.9992), MAE terendah (0.0189), RMSE terendah (0.0289), dan MAPE terendah (4.44%). Oleh karena itu, model terbaik yang dipilih adalah Linear Regression, karena memberikan akurasi yang tinggi dan interpretasi yang mudah, dibandingkan model lain yang cenderung lebih kompleks dan rentan terhadap overfitting.
---

## 4️⃣Evaluation

```Pada tahap evaluasi, metrik yang digunakan adalah MSE, R2 Score, MAE, RMSE, dan MAPE```

**MSE (Mean Squared Error):**
```
- Mengukur rata-rata kesalahan kuadrat antara nilai prediksi dan nilai aktual. Semakin kecil nilainya, semakin baik model dalam memprediksi nilai sebenarnya.
- Formula: MSE = (1/n) * Σ(actual - predicted)^2
- Metrik ini bekerja dengan menghitung selisih antara nilai aktual dan nilai prediksi, kemudian mengkuadratkan selisih tersebut dan menghitung rata-ratanya.
- MSE sangat sensitif terhadap outlier karena menggunakan kuadrat dari kesalahan.
```
**R2 Score (Coefficient of Determination):**
```
- Mengukur seberapa baik model menjelaskan variabilitas data aktual. Semakin mendekati 1, semakin baik model dalam menjelaskan data.
- Formula: R2 = 1 - (Σ(actual - predicted)^2 / Σ(actual - mean_actual)^2)
- R2 Score mengukur proporsi variansi dalam variabel dependen yang dapat dijelaskan oleh variabel independen.
```
**MAE (Mean Absolute Error):**
```
- Mengukur rata-rata kesalahan absolut antara nilai prediksi dan aktual. Semakin kecil nilainya, semakin akurat prediksi model.
- Formula: MAE = (1/n) * Σ|actual - predicted|
- Metrik ini bekerja dengan menghitung rata-rata dari nilai absolut kesalahan prediksi.
```
**RMSE (Root Mean Squared Error):**
```
- Akar dari MSE, mengembalikan satuan data asli sehingga lebih mudah diinterpretasikan. Semakin rendah, semakin baik.
- Formula: RMSE = sqrt(MSE)
- Metrik ini bekerja dengan menghitung akar dari MSE, sehingga lebih mudah dipahami dalam konteks satuan aslinya.
```
**MAPE (Mean Absolute Percentage Error):**
```
- Mengukur persentase kesalahan rata-rata absolut. Semakin rendah persentasenya, semakin akurat model.
- Formula: MAPE = (1/n) * Σ(|actual - predicted| / |actual|) * 100%
- Metrik ini bekerja dengan menghitung rata-rata persentase kesalahan absolut terhadap nilai aktual.
```
### Hasil evaluasi:
```
Berdasarkan hasil evaluasi, berikut perbandingan performa model:
Linear Regression: MSE: 0.0008, R2: 0.9992, MAE: 0.0189, RMSE: 0.0289, MAPE: 4.44%
Decision Tree: MSE: 0.0031, R2: 0.9970, MAE: 0.0338, RMSE: 0.0554, MAPE: 24.62%
Random Forest: MSE: 0.0016, R2: 0.9985, MAE: 0.0244, RMSE: 0.0396, MAPE: 13.65%
SVR: MSE: 0.0196, R2: 0.9808, MAE: 0.0789, RMSE: 0.1398, MAPE: 25.08%
Gradient Boosting: MSE: 0.0011, R2: 0.9990, MAE: 0.0184, RMSE: 0.0327, MAPE: 11.87%
```
---
### Kesimpulan:
> Model terbaik adalah Linear Regression karena memiliki nilai MSE, MAE, RMSE, dan MAPE terendah serta R2 tertinggi dibandingkan model lainnya. Hal ini menunjukkan bahwa model ini paling akurat dalam memprediksi harga penutupan saham minggu berikutnya.

> Meskipun model Gradient Boosting juga memiliki performa yang mendekati Linear Regression dengan MSE: 0.0011 dan R2: 0.9990, Linear Regression tetap lebih unggul pada beberapa metrik lainnya. Selain itu, Linear Regression juga lebih sederhana dan mudah diinterpretasikan, sehingga menjadi pilihan terbaik.
---
_Catatan:_
Semua detail penjelasan setiap tahapan juga sudah ada dalam notebook.

