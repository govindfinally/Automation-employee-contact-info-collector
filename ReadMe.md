


# 📌 Internship Outreach Automation with Selenium

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Selenium](https://img.shields.io/badge/Selenium-Web%20Automation-brightgreen)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-orange)
![Excel](https://img.shields.io/badge/Excel-Automation-lightgrey)

> 🚀 Automating company outreach research using **Selenium** & **Hunter.io** for instant email + LinkedIn data extraction, all neatly saved into Excel.

---

## 🌟 Project Overview

This project is a **fully automated data enrichment tool** that:

1. Reads a list of company names from an Excel file 📂
2. Uses **Selenium WebDriver** to navigate to [Hunter.io](https://hunter.io/domain-search) 🔍
3. Searches each company, scrapes:

   * ✅ Domain
   * ✅ Employee names
   * ✅ Email addresses
   * ✅ Job positions
   * ✅ LinkedIn presence indicator
4. Appends the results into an **existing Excel sheet** without duplicates 📊

---

## ✨ Why This Project Stands Out

* **⚡ End-to-End Automation** – From input to output, no manual clicks needed.
* **🛡️ Robust Error Handling** – Skips failed searches, keeps going without crashing.
* **📈 Scalable** – Can handle hundreds of companies in a single run.
* **🔄 Data Integrity** – Automatically merges with existing outreach lists and removes duplicates.
* **💼 Real-World Use Case** – Ideal for sales, recruitment, and marketing teams.

---

## 🛠️ Tech Stack

* **Python** – Core programming language
* **Selenium** – Browser automation & dynamic content scraping
* **Pandas** – Data wrangling & Excel integration
* **OpenPyXL** – Excel I/O operations
* **Hunter.io** – Lead generation platform

---

## 📂 File Structure

```plaintext
automation_project/
│
├── main.py                 # Main automation script
├── requirements.txt        # Dependencies list
├── README.md               # This file
└── data/
    ├── already_existing.xlsx  # Input & output Excel
```

---

## 🚀 How to Run

1️⃣ **Clone the repository**

```bash
git clone https://github.com/govindfinally/Automation-employee-contact-info-collector.git
cd Automation-employee-contact-info-collector
```

2️⃣ **Install dependencies**

```bash
pip install -r Requirement.txt
```

3️⃣ **Run the script**

```bash
python main.py
```

4️⃣ **Enter your Excel file path** when prompted (or press `Enter` to use the default).

---

## 🧠 Key Skills Demonstrated

✅ **Web Scraping with Selenium** – Handling dynamic pages, form submissions, waits, and element selection.
✅ **Browser Automation** – Simulating human actions for repetitive tasks.
✅ **Data Processing** – Cleaning, merging, and deduplicating datasets.
✅ **Error Handling** – Graceful handling of timeouts and failures.
✅ **Excel Automation** – Reading/writing large datasets seamlessly.

---

## 📊 Example Output

| Company Name | Employee\_Names        | Emails                                                                               | Positions       | LinkedIn\_Present |
| ------------ | ---------------------- | ------------------------------------------------------------------------------------ | --------------- | ----------------- |
| puchai.com   | John Doe, Jane Smith   | [john@puchai.com](mailto:john@puchai.com), [jane@puchai.com](mailto:jane@puchai.com) | CEO, HR Manager | Yes               |
| abc.com      | Alex Johnson, Mary Lee | [alex@abc.com](mailto:alex@abc.com)                                                  | CTO             | No                |

---

## 🔮 Future Improvements

* 🌐 Multi-source scraping (LinkedIn, Crunchbase, etc.)
* 📬 Automated email sending integration
* 📊 Dashboard to visualize company outreach progress

---

## 📢 About Me

💡 *I specialize in building automated solutions that save time, reduce costs, and scale outreach processes.*
If you're looking for someone who can combine **data engineering**, **automation**, and **business impact**, let's connect!

📧 Email: *[govindmohanty4@gmail.com.com](mailto:your.email@example.com)*
💼 LinkedIn: *[www.linkedin.com/in/govind-mohanty-123a0b231](#)*
🐙 GitHub: *[https://github.com/govindfinally](#)*
