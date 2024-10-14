import os
from urllib.request import urlretrieve
from datetime import datetime, timedelta

def download_synthetic():
    """
    """

    output_path = "../data/tables/synthetic/"
    
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    filenames = ["consumer_fraud_probability.csv",
                 "consumer_user_details.parquet",
                 "merchant_fraud_probability.csv",
                 "tbl_consumer.csv",
                 "tbl_merchants.parquet"]
    
    # download non-transaction files
    for file in filenames:
        urlretrieve(f"https://d29z7mpjjgf7tr.cloudfront.net/{file}", output_path + file)

    print("Successfully downloaded non-transaction files.")
    
    ###############################################################

    transaction_output_path = output_path + "transactions/"

    if not os.path.exists(transaction_output_path):
        os.makedirs(transaction_output_path)

    dates = date_range("2021-02-28", "2022-10-26")

    url_dict = {1: "part-00001-cfff5211-ef46-4b99-a6ed-63c9b2c7fe15.c000.snappy.parquet",
                2: "part-00003-b265e002-bffa-4201-a2a4-590ab25f4477.c000.snappy.parquet",
                3: "part-00005-bd1de064-b854-4ca3-9886-c1f7ca24ac73.c000.snappy.parquet"
    }

    # download transaction files
    # files are downloaded individually instead of as a folder...
    # ...since Cloudfront doesn't allow for download of directories
    for date in dates:

        if date <= "2021-08-27": # end point for first snapshot of data
            part = 1
        elif date >= "2022-02-28": # start point for third snapshot of data
            part = 3
        else:
            part = 2
            
        url = url_dict[part]
        urlretrieve(f"https://d29z7mpjjgf7tr.cloudfront.net/transactions/order_datetime={date}/{url}",
                    f"{transaction_output_path}{date}.parquet")
        
        print(f"Downloaded {date}")

    print("Successfully downloaded transaction files.")

def download_abs():
    """
    """

    output_path = "../data/tables/abs"

    if not os.path.exists(output_path):
        os.makedirs(output_path)
        
    files = ["ABS_2021.csv", "postcode_correspondences_2021.csv", "SA2_2021_AUST_GDA2020.shp"]

    for f in files:
        # define source and destination
        from_url = f"https://d29z7mpjjgf7tr.cloudfront.net/abs/{f}"
        to_file = f"{output_path}/{f}"

        urlretrieve(from_url, to_file) # download to relevant directory

    print("Successfully downloaded ABS files.")


def date_range(start_date, end_date):
    """
    """

    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    delta = timedelta(days = 1)
    
    dates = []

    while start <= end:
        dates.append(start.strftime("%Y-%m-%d"))
        start += delta
        
    return dates
