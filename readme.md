# Real-Time Stock Market Dashboard 📈

<p align="center">
  <img src="https://github.com/CodeWithTanim/README-MANAGER/blob/main/Lucid_Realism_A_modern_sleek_and_professional_logo_design_for__3.jpg" alt="Stock Dashboard Banner" style="max-width: 100%; height: auto; width: 400px;">
</p>

<h1 align="center">📊 Real-Time Stock Market Dashboard 🚀</h1>
<p align="center">
  <b>Visualize live stock market data and trends in real time!</b> ⚡<br>
  Analyze financial indicators like Moving Average, RSI and track stock prices easily.<br>
  <sub>Tech Stack: Python, Streamlit, Plotly, Alpha Vantage API</sub>
</p>

---

### 🧠 Introduction

The **Real-Time Stock Market Dashboard** is an interactive and user-friendly data visualization app developed using Python and Streamlit. It leverages the Alpha Vantage API to fetch real-time stock data and calculate technical indicators like Moving Averages and RSI.

This project was built as part of the **Internship Program at [Codec Technologies](http://codectechnologies.in/)**. The goal was to create a practical tool that makes stock market monitoring and analysis easy for everyday users, traders, and students.

---

### 📦 Features

- 📥 **Stock Symbol Input** – Search by stock ticker (e.g., AAPL, TSLA, MSFT)
- 📈 **Live Price Chart** – Interactive Plotly charts for price trends
- ⚙️ **Technical Indicators** – Calculate and visualize RSI & Moving Averages
- 🔄 **Auto Refresh** – Optionally refresh data every few minutes
- 🧾 **Data Logs** – Track and store historical fetched data
- 🎨 **Modern UI** – Built with Streamlit for an elegant and responsive experience

---

### 🚀 How to Run the Project?

#### ✅ Prerequisites:
- Python 3.8 or above
- Alpha Vantage API key (free from [here](https://www.alphavantage.co/support/#api-key))

#### 🛠️ Step-by-step Guide:

```bash
# Step 1: Clone the Repository
git clone https://github.com/CodeWithTanim/stock-dashboard.git
cd stock-dashboard

# Step 2: Set up a Virtual Environment (Recommended)
python -m venv venv
# Activate it:
venv\Scripts\activate       # for Windows
source venv/bin/activate    # for macOS/Linux

# Step 3: Install Required Packages
pip install -r requirements.txt

# Step 4: Add your API key in config.py
# config.py
API_KEY = "YOUR_API_KEY_HERE"

# Step 5: Run the Streamlit App
streamlit run app.py
````

---

### 🗂️ Project Structure

```
stock-dashboard/
│
├── app.py                  ← Main Streamlit application
├── config.py               ← API key configuration
├── requirements.txt        ← Required Python libraries
├── utils/
│   ├── __init__.py
│   ├── stock_api.py        ← Data fetching functions
│   └── indicators.py       ← RSI and Moving Average logic
├── data/
│   └── logs.csv            ← Optional data log file
├── assets/
│   └── logo.png            ← Optional custom logo
└── README.md               ← This documentation file
```

---

### 📤 Deployment (Optional)

You can easily host this dashboard online using **Streamlit Cloud**:

1. Push your project to GitHub
2. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Sign in and connect your GitHub repo
4. Deploy with one click and share your public URL 🚀

---

### ⚠️ Notes

* ⚠️ **Alpha Vantage** limits free users to **5 API requests/minute**.
* If RSI shows `NaN`, it might be due to fewer data points (need at least 14).
* You can customize branding by replacing the logo inside `assets/logo.png`.

---

### ✍️ Author

> Developed with 💖 by **MD SAMIUR RAHMAN TANIM**
> 📍 Internship Project @ [Codec Technologies](http://codectechnologies.in/)
> 🔗 [GitHub](https://github.com/CodeWithTanim) • [LinkedIn](https://www.linkedin.com/in/CodeWithTanim) • [YouTube](https://www.youtube.com/@CodeWithTanim)

---

### 🤝 Contribute

Pull requests are welcome! If you d
# Real-Time Stock Market Dashboard 📈

<p align="center">
  <img src="https://github.com/CodeWithTanim/README-MANAGER/blob/main/Lucid_Realism_A_modern_sleek_and_professional_logo_design_for__3.jpg" alt="Stock Dashboard Banner" style="max-width: 100%; height: auto; width: 400px;">
</p>

<h1 align="center">📊 Real-Time Stock Market Dashboard 🚀</h1>
<p align="center">
  <b>Internship Project for <a href="http://codectechnologies.in/">Codec Technologies</a><br>
  <b>Visualize live stock market data and trends in real time!</b> ⚡<br>
  Analyze financial indicators like Moving Average, RSI and track stock prices easily.<br>
  <sub>Tech Stack: Python, Streamlit, Plotly, Alpha Vantage API</sub>
</p>

---

### 🧠 Introduction

Developed as part of my internship with **Codec Technologies**, the **Real-Time Stock Market Dashboard** is a powerful data visualization web app built using Python and Streamlit. It fetches real-time stock prices and technical indicators from Alpha Vantage API, helping users analyze trends with an interactive UI.

---

### 📦 Features

- 📥 **Stock Symbol Input** – Enter stock ticker (e.g., AAPL, TSLA, MSFT)
- 📈 **Live Price Chart** – Visualize intraday price data using Plotly
- ⚙️ **Technical Indicators** – Calculate and display Moving Averages (MA) and RSI
- 🔄 **Auto Refresh** – Fetch updated data periodically
- 🎨 **Responsive UI** – Built using Streamlit for easy access

---

### 🛠️ Technologies Used

<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white" alt="Plotly">
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/Alpha_Vantage_API-008272?style=for-the-badge" alt="Alpha Vantage">
</p>

---

### 🚀 How to Run the Project?

#### ✅ Prerequisites:
- Python 3.8+
- Alpha Vantage API key (free tier available)

#### 🛠️ Setup:
```bash
# Clone and setup
git clone [your-repo-link]
cd stock-dashboard
pip install -r requirements.txt

# Add API key in config.py
echo "API_KEY = 'YOUR_KEY'" > config.py

# Run the app
streamlit run app.py
```

---

### 🗂️ Project Structure

```
stock-dashboard/
│
├── app.py                  ← Main Streamlit application
├── config.py               ← API key configuration
├── requirements.txt        ← Required Python libraries
├── utils/
│   ├── __init__.py
│   ├── stock_api.py        ← Data fetching functions
│   └── indicators.py       ← RSI and Moving Average logic
├── data/
│   └── logs.csv            ← Optional data log file
├── assets/
│   └── logo.png            ← Optional custom logo
└── README.md 
```

---

### 🌟 Key Learnings (Internship)

- Implemented real-time data visualization with financial APIs
- Developed interactive dashboards using Streamlit
- Applied technical analysis algorithms (RSI, MA)
- Gained experience in Python data processing (Pandas)
- Learned professional code organization and documentation

---

### ✍️ Developer

> [MD SAMIUR RAHMAN TANIM](https://github.com/CodeWithTanim)
> Intern at [Codec Technologies](http://codectechnologies.in/)  
> 🔗 [GitHub](your-github) | [LinkedIn](your-linkedin)  

---

### 📜 Acknowledgments

- Thanks to [Codec Technologies](http://codectechnologies.in/) for the internship opportunity
- Alpha Vantage for their free financial API tier
- Streamlit community for excellent documentation

---
### 🤝 Contribute

Pull requests are welcome! If you discover bugs, improvements, or want to enhance the dashboard, feel free to fork and submit a PR.

---

### 📄 License
MIT License - See [LICENSE](LICENSE) for details.

iscover bugs, improvements, or want to enhance the dashboard, feel free to fork and submit a PR.

---

### 📜 License

This project is licensed under the **MIT License** – use it freely, contribute, and share with credits!

---

### 📡 Connect With Me:

<p align="left">
  <a href="https://fb.com/CodeWithTanim" target="blank"><img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/facebook.svg" alt="Facebook" height="30" width="40" /></a>
  <a href="https://instagram.com/CodeWithTanim" target="blank"><img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg" alt="Instagram" height="30" width="40" /></a>
  <a href="https://www.youtube.com/@CodeWithTanim" target="blank"><img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/youtube.svg" alt="YouTube" height="30" width="40" /></a>
</p>
