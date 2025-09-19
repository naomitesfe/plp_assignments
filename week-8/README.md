# CORD-19 Data Explorer - Streamlit App

This project explores the `metadata.csv` dataset from the **CORD-19 Research Challenge** using Python, Pandas, Matplotlib, Seaborn, and Streamlit.

## Project Structure

Data_analysis_with_python/
│── app.py # Streamlit app
│── unzipped_data/ # Folder containing metadata.csv
│── README.md

## Dataset

This project uses the CORD-19 dataset. The CSV file is too large to include in the repository.  

To run this project:

1. Download `metadata.csv` from Kaggle:  
   [CORD-19 Kaggle Dataset](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge)  
2. Place the file in `/unzipped_data/`  
3. Run the notebooks or Streamlit app

## Requirements

```bash
pip install pandas streamlit matplotlib seaborn
Run the App
bash
Copy code
cd Data_analysis_with_python
streamlit run app.py 
```

## Features
- Load and explore the dataset

- Show dataset shape, columns, missing values

- Display basic statistics and visualizations

- Interactive widgets (e.g., year slider) in Streamlit


## Notes
- Use encoding="utf-8" when reading CSV to avoid Unicode errors

- Place metadata.csv in the unzipped_data/ folder

