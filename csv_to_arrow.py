import pyarrow as pa
from pyarrow import csv

if __name__ == "__main__":
    # read CSV
    CSV_NAME = "test.csv"
    table = csv.read_csv(CSV_NAME)
    # write table to arrow
    writer = pa.RecordBatchFileWriter("test.arrow", table.schema)
    writer.write_table(table)
    writer.close()
