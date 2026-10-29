# ACI-Bench Healthcare Pipeline

## Overview

Healthcare data is often stored as unstructured clinical notes, making it difficult to exchange information between systems and perform analytics at scale.

This project demonstrates an end-to-end Digital Health pipeline that transforms free-text clinical documentation into standardized healthcare data models and actionable analytics.

The pipeline converts clinical notes into:

- Structured clinical concepts using Natural Language Processing (NLP)
- HL7 FHIR resources for interoperability
- OMOP Common Data Model (CDM) tables for analytics
- SNOMED CT and RxNorm standardized concepts using ATHENA vocabularies
- Clinical and population health insights using DuckDB analytics

---

## Clinical Motivation

A physician may document:

> "Patient has congestive heart failure and hypertension. Continue Lasix and Lisinopril."

While humans can easily understand this information, computers struggle to:

- Exchange the information between healthcare systems
- Analyze patient populations
- Identify cohorts
- Study treatment patterns
- Conduct research

This project demonstrates how clinical documentation can be transformed into standardized healthcare data suitable for clinical analytics and research.

---

## Architecture

The pipeline transforms unstructured clinical notes into standardized, analytics-ready healthcare data in five stages:

```
Clinical Notes
        ↓
Natural Language Processing
        ↓
FHIR R4 Resources
        ↓
OMOP Common Data Model
        ↓
ATHENA Standard Vocabularies
        ↓
DuckDB Analytics
```

* * *

## Pipeline Components

### 1. Clinical NLP

Clinical notes are processed to identify:

- Conditions
- Medications
- Other clinical entities

**Input**

> "Patient has congestive heart failure. Continue Lasix and Lisinopril."

**Output**

```json
{
  "conditions": ["congestive heart failure"],
  "medications": ["lasix", "lisinopril"]
}
```

### 2. FHIR Interoperability Layer

The extracted information is transformed into FHIR R4 resources:

- Patient
- Encounter
- Condition
- MedicationStatement
- Bundle

**Example**

```json
{
  "resourceType": "Condition",
  "clinicalStatus": { "text": "active" },
  "verificationStatus": { "text": "confirmed" }
}
```

FHIR enables healthcare information exchange between systems.

### 3. OMOP Common Data Model

FHIR resources are transformed into OMOP CDM tables:

| FHIR Resource | OMOP Table |
|---|---|
| Patient | PERSON |
| Encounter | VISIT_OCCURRENCE |
| Condition | CONDITION_OCCURRENCE |
| MedicationStatement | DRUG_EXPOSURE |

### 4. Vocabulary Standardization

Clinical terms are mapped to standard vocabularies downloaded from ATHENA.

**Conditions → SNOMED CT**

| Source Term | SNOMED Concept |
|---|---|
| Hypertension | Essential hypertension |
| Depression | Depressive disorder |
| Congestive heart failure | Congestive heart failure |
| Arthritis | Arthritis |

**Medications → RxNorm**

| Source Medication | RxNorm Concept |
|---|---|
| Lasix | Lasix |
| Lisinopril | Lisinopril Oral Product |
| Synthroid | Synthroid |
| Tylenol | Acetaminophen Oral Film Product |

* * *

## Analytics Framework

The project demonstrates analytics at three levels commonly used in Digital Health and OHDSI research.

### Level 1 — Patient Analytics

- Which patients have the highest disease burden?
- Which patients receive the largest number of medications?

> **Example insight:** Patient D2N001 has four chronic conditions and represents the highest disease burden in the cohort.

### Level 2 — Cohort Analytics

- What comorbidities occur among heart failure patients?
- Which medications are used among heart failure patients?

> **Example insight:** Heart failure patients commonly present with mitral valve regurgitation, hypertension, and type 2 diabetes. Common medications include Lasix and Lisinopril.

### Level 3 — Population Analytics

- Which diseases tend to occur together?
- How common is multimorbidity?

**Most common disease relationships**

- Congestive heart failure ↔ Mitral valve regurgitation
- Essential hypertension ↔ Mitral valve regurgitation
- Congestive heart failure ↔ Essential hypertension

**Multimorbidity distribution**

| Conditions per Patient | Patients |
|---|---|
| One | 29 |
| Two | 7 |
| Three | 2 |
| Four or more | 1 |

* * *

## Technologies Used

- **Clinical Standards:** HL7 FHIR R4, OMOP Common Data Model, SNOMED CT, RxNorm
- **Data & Analytics:** Python, Pandas, DuckDB
- **Terminology Services:** ATHENA Vocabulary Repository

* * *

## Example Use Cases

- **Clinical Decision Support:** Identify patients with complex disease profiles
- **Population Health:** Analyze disease prevalence and multimorbidity patterns
- **Clinical Research:** Construct disease-specific cohorts
- **Digital Health Interoperability:** Exchange healthcare information through FHIR resources

* * *

## Future Enhancements

- Interactive clinical analytics dashboard
- Disease co-occurrence network visualization
- Cohort exploration interface
- FHIR Observation resources
- OMOP Measurement table generation
- Additional ATHENA vocabulary integration

* * *

## Author

**Harish Mohankumar**
MSc Health Informatics

**Focus Areas:** Digital Health · Clinical NLP · Interoperability · FHIR · OMOP CDM · Healthcare Analytics

* * *

*A good README should allow a clinician or healthcare researcher to understand the project in 5 minutes without reading a single line of code.* 🚀
