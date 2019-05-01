import pyarrow as pa
from pyarrow import csv

if __name__ == "__main__":
    # read CSV
    CSV_NAME = "test.csv"
    # make sure bools are read correctly
    options = csv.ConvertOptions(
            column_types = {
                "bool": pa.bool_()
            })
    table = csv.read_csv(CSV_NAME, convert_options = options)
    # write table to arrow
    writer = pa.RecordBatchFileWriter("test.arrow", table.schema)
    writer.write_table(table)
    writer.close()
