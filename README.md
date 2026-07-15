# Data Analysis Labs Repository

This repository contains a collection of Jupyter Notebooks, datasets, and visual assets organized into a two-week laboratory schedule. The labs focus heavily on data manipulation and analysis using libraries like Pandas and NumPy.

## 📂 Repository Structure

Below is the complete breakdown of the files and directories included in this project:

### Week 1
* **Lab 1**: Contains the primary notebook, `Lab 1.ipynb`.
* **Lab 2**: Contains the primary notebook, `Lab 2.ipynb`.
* **Lab 3 & 4**: Contains the combined notebook, `Lab 3 & 4.ipynb`.
* **Lab 3 & 4 Data**: Includes the accompanying dataset, `hourly_weather_10_days.csv`.

### Week 2

#### Lab 1
* **Pandas Notebooks**: Contains specific lessons on data manipulation, including `dataframe_basics.ipynb`, `handling_missing_data_replace.ipynb`, `pandas_concat.ipynb`, `pandas_group_by.ipynb`, `pandas_merge.ipynb`, and `pandas_pivot.ipynb`.
* **Datasets**: Includes several weather-related CSV files to practice on: `weather.csv`, `weather2.csv`, `weather3.csv`, `weather_by_cities.csv`, and `weather_data.csv`.
* **Visual Aids**: Contains reference images for concepts, including `db_joins.jpg`, `group_by_cities.png`, and `split_apply_combine.png`.

#### Lab 2
* **Notebooks**: Contains practical application notebooks, `Numpy_and_Plotting (1).ipynb` and `Pandas_Hands_on (1).ipynb`.
* **Data Folder**: Includes a `data/` subdirectory containing the dataset `president_heights.csv`.
* **Images Folder**: Includes an `img/` subdirectory containing `sample.png`.

#### Lab 3: Version Control with GitHub
* **Documentation**: Contains guides and cheat sheets for using Git and GitHub, such as `github_basics.md`.
* **Concepts Covered**: Local repository initialization, staging files, committing changes, managing branches, and pushing code to remote repositories.

#### Lab 4:
To-Do List FAST API
* **Application Core**: Contains the `app/` directory with `main.py` (API endpoints and routing logic) and `schemas.py` (Pydantic data models).
* **Server Scripts**: Includes `run.py` to launch the Uvicorn ASGI server.
* **Configuration Files**: Includes `requirements.txt` for project dependencies and `.gitignore`.
* **Visual Aids**: Contains screenshots of Swagger UI API responses (`POST`, `GET`, `PUT`, `DELETE`) for assignment validation.

To-Do List Flask API
* **Application Core**: Contains `app.py`, which handles the API endpoints, routing logic, and in-memory data storage.
* **Configuration Files**: Includes `requirements.txt` for project dependencies and `.gitignore`.
* **Visual Aids**: Contains screenshots of terminal API responses (`POST`, `GET`, `PUT`, `DELETE`) using PowerShell `Invoke-RestMethod` and `curl` for assignment validation.

### Week 3

#### Lab 1: Handling Missing Values and Data Preprocessing
* **Primary Notebook**: `Week_3_Day_1.ipynb`.
* **Concepts Covered**: 
  * Loading and exploring datasets using Pandas.
  * Identifying and diagnosing missing data using analytical summaries and visual heatmaps (`Seaborn` and `Matplotlib`).
  * Practical strategies for handling missing values: dropping highly-missing columns (e.g., `Cabin`, `Ticket`), performing grouped median imputation for numerical data (e.g., `Age` based on `Pclass`), generating missing data indicators, and utilizing mode imputation for categorical data (`Embarked`).
  * Evaluating and visualizing data distributions before and after applying imputation techniques.
* **Datasets**: Utilizes the `titanic.csv` dataset.

#### Lab 2
* **Notebook**: Contains the practical lab notebook `Week_3_Day_2.ipynb`.
* **Topics Covered**:
  * Feature Engineering for Tabular Data
  * Advanced Feature Engineering Techniques
  * Data Augmentation for Images
  * Hands-on Exercises and Experiments
* **Hands-on Activities**:
  * Feature Selection
  * Feature Scaling and Encoding
  * Dimensionality Reduction (PCA)
  * Image Data Augmentation
  * Experimenting with different feature engineering parameters
 
  #### Lab 3
* **Notebook**: Contains the practical lab notebook `Week_3_Day_3.ipynb`.
* **Dataset**: Uses the Titanic dataset for Exploratory Data Analysis (EDA).
* **Topics Covered**:
  * Data Inspection and Summary Statistics
  * Handling Missing Values
  * Univariate Analysis
  * Bivariate Analysis
  * Correlation Analysis
  * Data Visualization
* **Hands-on Activities**:
  * Loading and exploring the dataset with Pandas
  * Analyzing numerical and categorical features
  * Creating histograms, box plots, count plots, and scatter plots
  * Computing descriptive statistics and correlations
  * Visualizing insights using Matplotlib and Seaborn
  * 
