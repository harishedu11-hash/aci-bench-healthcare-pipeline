import duckdb

con = duckdb.connect(
    "data/processed/omop_output/omop.duckdb"
)

result = con.sql("""
SELECT
    approved_concept_name,
    COUNT(*) AS n
FROM CONDITION_OCCURRENCE_STANDARDIZED
GROUP BY approved_concept_name
ORDER BY n DESC
""").df()

print(result)