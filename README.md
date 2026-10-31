<h1 align="center">🎬 IMDb Movie Analytics Dashboard</h1>

<p align="center">
  Explore 1,000 popular movies from 2006 to 2016: the best and worst rated, how many were released each year, and more, all in one Python dashboard.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12%2B-blue?logo=python&logoColor=white" alt="Python 3.12+">
  <img src="https://img.shields.io/badge/pandas-data%20analysis-150458?logo=pandas&logoColor=white" alt="pandas">
  <img src="https://img.shields.io/badge/Matplotlib-charts-11557c" alt="Matplotlib">
  <img src="https://img.shields.io/badge/Tkinter-GUI-orange" alt="Tkinter">
  <img src="https://img.shields.io/badge/status-learning%20project-brightgreen" alt="Learning project">
</p>

---

## 📸 Preview

<h2>Dashboard window<h2>
<img width="550" height="400" alt="Screenshot 2026-10-31 200127" src="https://github.com/user-attachments/assets/43f9df28-1405-43c7-a384-c2120c5523a9" />
<h2>Top 10 rated<h2>
<img width="550" height="400" alt="Screenshot 2026-10-31 200140" src="https://github.com/user-attachments/assets/e0cb9b40-4948-4c9b-a49a-3b359c3ea89d" />
    <h2>Releases per year<h2>
 <img width="550" height="400" alt="Screenshot 2026-10-31 200133" src="https://github.com/user-attachments/assets/b667a2b0-45b1-4380-9d98-df57b2256dbd" />

---

## 📑 Table of contents

- [About the project](#-about-the-project)
- [Features](#-features)
- [Tech stack](#️-tech-stack)
- [Dataset](#-dataset)
- [Getting started](#-getting-started)
- [Project structure](#-project-structure)
- [How it works](#️-how-it-works)
- [What I learned](#-what-i-learned)
- [Known limitations](#️-known-limitations)
- [Future improvements](#-future-improvements)

---

## 🎯 About the project

This project loads a real-world movie dataset with **pandas**, cleans it, and presents the results in two ways:

1. A **Tkinter window** that lists the 10 highest-rated and 10 lowest-rated movies, with their directors.
2. **Matplotlib charts** that show how many movies were released each year and which movies have the top ratings.

I built it to practice the full path from raw data to a finished result: load, clean, analyze, and visualize.

---

## ✨ Features

- ⭐ **Top 10 highest-rated movies**, with rating, title, and director
- ❌ **Bottom 10 lowest-rated movies**, shown side by side with the top list
- 📊 **Bar chart** of the number of movie releases per year (2006 to 2016)
- 🏆 **Horizontal bar chart** of the top 10 highest-rated movies
- 🧹 **Data cleaning**: missing revenue and Metascore values are filled in, so the data has no gaps
- 🖥️ A simple desktop window, so there is no browser or server to set up

---

## 🛠️ Tech stack

| Tool | Used for |
|---|---|
| Python 3.12+ | the programming language |
| pandas | loading, cleaning, sorting, and counting the data |
| Matplotlib | the charts |
| Tkinter | the dashboard window (included with Python) |

> Python 3.12 or newer is needed because the code reuses double quotes inside f-strings, which older versions don't allow.

---

## 📦 Dataset

The project uses the **IMDb Movie Data (2006 to 2016)** dataset, a CSV file with 1,000 movies. Each row includes:

`Rank`, `Title`, `Genre`, `Description`, `Director`, `Actors`, `Year`, `Runtime (Minutes)`, `Rating`, `Votes`, `Revenue (Millions)`, `Metascore`

The dataset is available on Kaggle. Download `IMDB-Movie-Data.csv` and put it in the `data/` folder. Check the dataset page for its license before reusing it.

---

## 🚀 Getting started

**1. Make sure Python 3.12 or newer is installed**

```bash
python --version
```

**2. Clone this repository**

```bash
git clone https://github.com/TvSivajaswanth/IMDb-Movie-Analytics.git
```

**3. Install the required packages**

```bash
pip install pandas matplotlib
```

**4. Add the dataset**

Place `IMDB-Movie-Data.csv` inside the `data/` folder.

**5. Run the dashboard**

```bash
python main.py
```

> Run the command from the project folder, because the code looks for the data at `data/IMDB-Movie-Data.csv`.

> The two chart windows open first. Close them to see the dashboard window.

---

## 📁 Project structure

```
imdb-dashboard/
├── main.py                  # the whole application
├── data/
│   └── IMDB-Movie-Data.csv  # the dataset (you add this)
├── screenshots/             # images used in this README
└── README.md
```

---

## ⚙️ How it works

**1. Load and rename**

```python
df = pd.read_csv("data/IMDB-Movie-Data.csv")
df = df.rename(columns={"Runtime (Minutes)": "Runtime", "Revenue (Millions)": "Revenue"})
```

Shorter column names are easier to type and read.

**2. Clean the missing values**

| Column | Filled with | Why |
|---|---|---|
| `Revenue` | the **median** | a few blockbusters earn huge amounts, and the median isn't pulled up by them the way the mean is |
| `Metascore` | the **mean** | scores are spread fairly evenly, so the mean is a fair middle value |

**3. Sort to find the best and worst**

```python
top10_rated = df.sort_values("Rating", ascending=False).head(10)
bottom10_rated = df.sort_values("Rating", ascending=True).head(10)
```

**4. Show the lists in Tkinter**

The program loops through each row with `iterrows()` and creates a `Label` for each movie, inside two `LabelFrame` boxes placed side by side.

**5. Draw the charts**

- `value_counts().sort_index()` counts the movies in each year, in order, for the bar chart
- `barh` draws the top 10 as horizontal bars, and `invert_yaxis()` puts the highest rating at the top

---

## 📚 What I learned

- Loading and exploring CSV data with **pandas**
- Handling missing values, and choosing between the mean and the median
- Sorting, slicing, and counting data with `sort_values`, `head`, and `value_counts`
- Looping over DataFrame rows with `iterrows()`
- Drawing bar and horizontal bar charts with **Matplotlib**
- Building a layout in Tkinter with `Frame` and `LabelFrame`
- Combining a data-analysis script with a desktop interface

---

## ⚠️ Known limitations

- The charts open in separate Matplotlib windows instead of inside the dashboard
- The dashboard window only appears after the chart windows are closed
- The movie lists are plain labels, so they can't be scrolled, searched, or sorted
- The data path is relative, so the program must be run from the project folder

---

## 🔮 Future improvements

- [ ] Embed the charts inside the Tkinter window (as in my Expense Tracker project)
- [ ] Add a genre filter and a year filter
- [ ] Add a search box for movie titles and directors
- [ ] Chart rating against revenue, to see whether better movies earn more
- [ ] Show the top directors by average rating
- [ ] Show the most common genres
- [ ] Add a file-not-found message if the dataset is missing
- [ ] Use a scrollable table (`ttk.Treeview`) for the full dataset

---

## 📄 License

This project is open source and free to use for learning. The dataset belongs to its original authors, so check its license before reusing it.
