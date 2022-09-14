from google.cloud import bigquery
# Construct a BigQuery client object.
client = bigquery.Client()

# dataset_id = 'ari-dp-hun-dev.edm_product_c1'

datasets = [
    "ari-dp-hun-dev.anomaly_sales_c1",
    "ari-dp-hun-dev.raw_sales_c1",
    "ari-dp-hun-dev.edm_customer_c1",
    "ari-dp-hun-dev.edm_product_c1",
    "ari-dp-hun-dev.edm_sales_c1",
    "ari-dp-hun-dev.edm_site_c1"
    ]


for dataset in datasets:
    tables = client.list_tables(dataset)  # Make an API request.

    for table in tables:
            print("{}:{}.{}".format(table.project, table.dataset_id, table.table_id))
