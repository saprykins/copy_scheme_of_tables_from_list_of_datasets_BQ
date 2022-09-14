# get_tables_from_list_of_datasets_BQ

Help to copy schemes of BigQuery datasets (when the list of DS is provided) from one project to another project

The script provides the results that can be put in xls-file in the following way: 

Save schemes in file:  
```
bq show --format=prettyjson Project1:BQDataset.Table1 | jq '.schema.fields' > schema.json
```

Create tables from file:  
```
bq mk --table project:dataset.table source_file.json
```
