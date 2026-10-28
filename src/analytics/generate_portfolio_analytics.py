import duckdb

con = duckdb.connect(
    "data/processed/omop_output/omop.duckdb"
)

print("\n================================================")
print("LEVEL 1: PATIENT ANALYTICS")
print("================================================\n")

patient_burden = con.sql("""
SELECT
    person_id,
    COUNT(DISTINCT approved_concept_name) AS condition_count
FROM CONDITION_OCCURRENCE_STANDARDIZED
GROUP BY person_id
ORDER BY condition_count DESC
LIMIT 10
""").df()

print(patient_burden)
patient_burden.to_csv(
    "portfolio_data/patient_burden.csv",
    index=False
)

print("\n================================================")
print("LEVEL 1: POLYPHARMACY ANALYTICS")
print("================================================\n")

polypharmacy = con.sql("""
SELECT
    person_id,
    COUNT(DISTINCT approved_concept_name)
        AS medication_count
FROM DRUG_EXPOSURE_STANDARDIZED
GROUP BY person_id
ORDER BY medication_count DESC
LIMIT 10
""").df()

print(polypharmacy)
polypharmacy.to_csv(
    "portfolio_data/polypharmacy.csv",
    index=False
)

print("\n================================================")
print("LEVEL 2: HEART FAILURE COHORT")
print("COMMON COMORBIDITIES")
print("================================================\n")

hf_comorbidities = con.sql("""
SELECT
    c2.approved_concept_name,
    COUNT(*) AS n
FROM CONDITION_OCCURRENCE_STANDARDIZED c1
JOIN CONDITION_OCCURRENCE_STANDARDIZED c2
    ON c1.person_id = c2.person_id
WHERE c1.approved_concept_name =
    'Congestive heart failure'
AND c2.approved_concept_name <>
    'Congestive heart failure'
GROUP BY c2.approved_concept_name
ORDER BY n DESC
""").df()

print(hf_comorbidities)
hf_comorbidities.to_csv(
    "portfolio_data/hf_comorbidities.csv",
    index=False
)

print("\n================================================")
print("LEVEL 2: HEART FAILURE COHORT")
print("MEDICATION UTILIZATION")
print("================================================\n")

hf_medications = con.sql("""
SELECT
    d.approved_concept_name,
    COUNT(*) AS n
FROM CONDITION_OCCURRENCE_STANDARDIZED c
JOIN DRUG_EXPOSURE_STANDARDIZED d
    ON c.person_id = d.person_id
WHERE c.approved_concept_name =
    'Congestive heart failure'
GROUP BY d.approved_concept_name
ORDER BY n DESC
""").df()

print(hf_medications)
hf_medications.to_csv(
    "portfolio_data/hf_medications.csv",
    index=False
)

print("\n================================================")
print("LEVEL 3: POPULATION ANALYTICS")
print("DISEASE CO-OCCURRENCE NETWORK")
print("================================================\n")

cooccurrence = con.sql("""
SELECT
    c1.approved_concept_name AS disease_1,
    c2.approved_concept_name AS disease_2,
    COUNT(*) AS occurrences
FROM CONDITION_OCCURRENCE_STANDARDIZED c1
JOIN CONDITION_OCCURRENCE_STANDARDIZED c2
    ON c1.person_id = c2.person_id
WHERE c1.approved_concept_name <
      c2.approved_concept_name
GROUP BY disease_1, disease_2
ORDER BY occurrences DESC
LIMIT 10
""").df()

print(cooccurrence)
cooccurrence.to_csv(
    "portfolio_data/cooccurrence.csv",
    index=False
)

print("\n================================================")
print("LEVEL 3: POPULATION ANALYTICS")
print("MULTIMORBIDITY BURDEN")
print("================================================\n")

multimorbidity = con.sql("""
SELECT
    CASE
        WHEN condition_count = 1 THEN '1 condition'
        WHEN condition_count = 2 THEN '2 conditions'
        WHEN condition_count = 3 THEN '3 conditions'
        ELSE '4+ conditions'
    END AS burden_group,
    COUNT(*) AS patients
FROM (
    SELECT
        person_id,
        COUNT(DISTINCT approved_concept_name)
            AS condition_count
    FROM CONDITION_OCCURRENCE_STANDARDIZED
    GROUP BY person_id
)
GROUP BY burden_group
ORDER BY burden_group
""").df()

print(multimorbidity)
multimorbidity.to_csv(
    "portfolio_data/multimorbidity.csv",
    index=False
)