# Generic Buy Now, Pay Later Project group 6

# Group member

Natasha Bourne
Nathan Liu
Quang Ngoc Dao
Nguyen Khue Ngan Vu
Laura Glaspole

# Objective

Create a pipeline to processes merchant, user and transaction data and return top 100 potential merchants 
that we cancollaborate with



# Setup

1. Open up your terminal or command prompt and cd to the root directory of the project folder.
2. Run the following command to install all required python packages (**May take a while to install**):
    ```
    pip3 install -r requirements.txt
    ```
---

## Order of Execution

To achieve the ranking for the top 100 merchants, the notebooks need to be run in the following order. Note that part relate to model selection and trainning in notebook 2 and 4 may take significant time to run. In notebook 4, part relate to trainning SARIMAX for 3930 merchants may take hours :

1. **`1. Download and preliminarily preprocess data.ipynb`**  
   This notebook handles the initial download and preprocessing of the data. It includes the logic from the `download.py` script, which fetches the provided data and external ABS data.

2. **`2. Customer and merchant fraud regression.ipynb`**  
   This notebook processes and analyzes customer and merchant fraud data to provide insights that contribute to the merchant ranking.

3. **`3. External ABS data processing.ipynb`**  
   This notebook processes external ABS data, which is integrated into the analysis for the merchant ranking.

4. **`4. Forcasting merchant performance in near future.ipynb`**  
   This notebook contains models and predictions related to forecasting the future performance of merchants, which influences their ranking. 

5. **`5. Segment merchants by their business.ipynb`**  
   In this notebook, merchants are segmented based on their business categories, adding another layer of analysis for ranking.

6. **`7. Ranking.ipynb`**  
   This notebook compiles all the analysis and data from the previous steps to generate a final ranking of the top 100 merchants.

### Optional

- **`6. Geospatial visualizing.ipynb`**  
   This notebook focuses on geospatial visualizations related to the merchants. It is not required for the ranking but provides additional insights into the geographical distribution of merchants.

- **`8. Summary notebook.ipynb`**  
   This notebook summarizes the entire analysis process and provides an overall trajectory of the project. It serves as a useful guide for understanding the key steps and outcomes.

## Scripts

- **`download.py`**  
   This script is responsible for downloading the provided data and external ABS data. The logic of this script has been incorporated into the first notebook, so it does not need to be run separately.

---