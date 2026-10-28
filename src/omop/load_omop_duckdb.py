import duckdb

con = duckdb.connect(
    "data/processed/omop_output/omop.duckdb"
)

con.execute("""
CREATE OR REPLACE TABLE
CONDITION_OCCURRENCE_STANDARDIZED AS
SELECT *
FROM read_csv_auto(
'data/processed/omop_output/CONDITION_OCCURRENCE_STANDARDIZED.csv'
)
""")

con.execute("""
CREATE OR REPLACE TABLE
DRUG_EXPOSURE_STANDARDIZED AS
SELECT *
FROM read_csv_auto(
'data/processed/omop_output/DRUG_EXPOSURE_STANDARDIZED.csv'
)
""")

print("DuckDB database created.")