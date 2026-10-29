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

## Dataset

This project uses **ACI-Bench** (Ambient Clinical Intelligence Benchmark), a publicly available benchmark corpus of doctor-patient conversations paired with clinical notes. It was published in *Scientific Data* (Nature, 2023) by researchers from Microsoft, Nuance, and the University of Washington.

> Yim, W., Fu, Y., Ben Abacha, A., Snider, N., Lin, T., & Yetisgen, M. (2023). *Aci-bench: a Novel Ambient Clinical Intelligence Dataset for Benchmarking Automatic Visit Note Generation.* Scientific Data, 10, 586. [https://doi.org/10.1038/s41597-023-02487-3](https://doi.org/10.1038/s41597-023-02487-3)

### About ACI-Bench

- **207 encounters** of doctor-patient dialogue paired with structured clinical notes
- Created by domain experts (physicians, scribes, and clinical informaticians) through **role-played encounters**; no real patient data was used or disclosed
- Notes follow a SOAP-inspired structure: *Subjective*, *Objective Exam*, *Objective Results*, and *Assessment & Plan*
- Notes were annotated and cleaned to remove unsupported content and correct errors
- Three encounter types: virtual assistant (`virtassist`), virtual scribe (`virtscribe`), and ambient clinical intelligence (`aci`)
- Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

| Split | Encounters |
|---|---|
| Train | 67 |
| Validation | 20 |
| Test 1 / 2 / 3 | 40 each |

### Data Access

- **Dataset:** [Figshare (DOI: 10.6084/m9.figshare.22494601)](https://doi.org/10.6084/m9.figshare.22494601)
- **Original code:** [github.com/wyim/aci-bench](https://github.com/wyim/aci-bench)

### How It Is Used in This Project

ACI-Bench was originally designed to benchmark automatic note generation. This project uses its clinical notes differently: as realistic, free-text clinical documentation that is transformed into FHIR resources, OMOP CDM tables, and standardized SNOMED CT / RxNorm concepts for analytics.

> **Note:** ACI-Bench encounters are role-played and contain no real patient data. Results in this repository demonstrate a pipeline and methodology, not clinical findings, and should not be used for clinical decision-making.

### Citation

```bibtex
@article{yim2023acibench,
  title   = {Aci-bench: a Novel Ambient Clinical Intelligence Dataset for Benchmarking Automatic Visit Note Generation},
  author  = {Yim, Wen-wai and Fu, Yujuan and Ben Abacha, Asma and Snider, Neal and Lin, Thomas and Yetisgen, Meliha},
  journal = {Scientific Data},
  volume  = {10},
  pages   = {586},
  year    = {2023},
  doi     = {10.1038/s41597-023-02487-3}
}
```

* * *

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
