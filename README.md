# 📊 Cryptocurrency Liquidity Prediction for Market Stability

Predicting liquidity levels in the cryptocurrency market using historical trading data to assist exchanges and investors in maintaining market stability.

---

## 🚀 Project Objective

To build a machine learning model that predicts the liquidity ratio of cryptocurrencies using features like price, volume, and market cap. This helps identify potential liquidity crises early.

---

## 📂 Dataset

* **Source**: CoinGecko (CSV - 2022-03-16 and 2022-03-17)
* **Size**: \~2000 records
* **Features**:

  * `price`, `volume`, `market_cap`
  * `price_change_1h`, `price_change_24h`, `price_change_7d`
  * Engineered: `liquidity_ratio`, `price_ma_3`, `volume_ma_3`, `volatility`

---

## ⚖️ Technologies Used

* Python, pandas, numpy, scikit-learn, matplotlib, seaborn
* Flask for deployment
* Google Colab for development

---

## 🔢 Model Details

* **Algorithm**: RandomForestRegressor
* **Target Variable**: `liquidity_ratio`
* **Train/Test Split**: 80/20

### 🔢 Performance

| Metric   | Value |
| -------- | ----- |
| R² Score | 0.86  |
| RMSE     | 0.43  |
| MAE      | 0.36  |

---

## 📚 Project Structure

```
crypto-liquidity-prediction/
├── data/                  # Raw and cleaned datasets
├── notebooks/             # Jupyter notebook
├── models/                # Saved model (liquidity_model.pkl)
├── app/                   # Flask app (app.py, templates/)
├── reports/               # EDA, HLD, LLD, Final Report
└── README.md
```

---

## 🚪 Deployment (Flask)

* Run `app.py`
* Navigate to `http://127.0.0.1:5000/`
* Input: `price`, `volume`, `market_cap`, `price_change_24h`, `price_change_7d`
* Output: Predicted `liquidity_ratio`

---

## 🔧 How to Run

```bash
pip install -r requirements.txt
python app/app.py
```

---

## 📃 Reports Included

* [EDA Report](./reports/EDA_Report.pdf)
* [HLD Document](./reports/HLD.pdf)
* [LLD Document](./reports/LLD.pdf)
* [Final Report](./reports/Final_Report.pdf)
* [Pipeline Architecture](./reports/Pipeline_Architecture.pdf)

---

## ✨ Future Enhancements

* Integrate social media sentiment
* Real-time data streaming
* Try LSTM or Prophet for time-series forecasting

  
---
## 👨‍💼 Author

**Kalyani Khapale**
 [Data Analytics Enthusiast]

