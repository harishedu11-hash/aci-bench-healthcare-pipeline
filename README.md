I think this is the perfect time to write the README.

Why now?

Because you've reached a major milestone:

Clinical Notes
      ↓
NLP
      ↓
FHIR R4
      ↓
OMOP CDM
      ↓
Athena Vocabulary
      ↓
SNOMED CT
      ↓
RxNorm
      ↓
DuckDB Analytics


Most READMEs are written for developers.

Your README should be written for:

Clinicians
Digital Health Professionals
Health Informaticians
Researchers
OHDSI Community Members
Recruiters
Engineers


A cardiologist should be able to understand the problem without knowing Python.

README.md
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

```text
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

Pipeline Components
1. Clinical NLP

Clinical notes are processed to identify:

Conditions
Medications
Clinical entities

Example:

Input:

Patient has congestive heart failure. Continue Lasix and Lisinopril.

Output:

{
  "conditions": [
    "congestive heart failure"
  ],
  "medications": [
    "lasix",
    "lisinopril"
  ]
}

2. FHIR Interoperability Layer

The extracted information is transformed into FHIR R4 resources:

Patient
Encounter
Condition
MedicationStatement
Bundle

Example:

{
  "resourceType": "Condition",
  "clinicalStatus": {
    "text": "active"
  },
  "verificationStatus": {
    "text": "confirmed"
  }
}


FHIR enables healthcare information exchange between systems.

3. OMOP Common Data Model

FHIR resources are transformed into OMOP CDM tables:

FHIR	OMOPPatient	PERSON
Encounter	VISIT_OCCURRENCE
Condition	CONDITION_OCCURRENCE
MedicationStatement	DRUG_EXPOSURE

Generated tables:

PERSON
VISIT_OCCURRENCE
CONDITION_OCCURRENCE
DRUG_EXPOSURE
4. Vocabulary Standardization

Clinical terms are mapped to standard vocabularies downloaded from ATHENA:

Conditions

Mapped to:

SNOMED CT

Examples:

Source Term	SNOMED ConceptHypertension	Essential hypertension
Depression	Depressive disorder
Congestive heart failure	Congestive heart failure
Arthritis	Arthritis
Medications

Mapped to:

RxNorm

Examples:

Source Medication	RxNorm ConceptLasix	Lasix
Lisinopril	Lisinopril Oral Product
Synthroid	Synthroid
Tylenol	Acetaminophen Oral Film Product
Analytics Framework

The project demonstrates analytics at three levels frequently used in Digital Health and OHDSI research.

Level 1 — Patient Analytics

Questions:

Which patients have the highest disease burden?
Which patients receive the largest number of medications?

Example Insight:

Patient D2N001 has four chronic conditions and represents the highest disease burden in the cohort.

Level 2 — Cohort Analytics

Questions:

What comorbidities occur among heart failure patients?
Which medications are used among heart failure patients?

Example Insight:

Heart failure patients commonly present with:

Mitral valve regurgitation
Hypertension
Type 2 diabetes

Common medications include:

Lasix
Lisinopril
Level 3 — Population Analytics

Questions:

Which diseases tend to occur together?
How common is multimorbidity?

Example Insight:

Most common disease relationships:

Congestive heart failure ↔ Mitral valve regurgitation
Essential hypertension ↔ Mitral valve regurgitation
Congestive heart failure ↔ Essential hypertension

Multimorbidity distribution:

29 patients with one condition
7 patients with two conditions
2 patients with three conditions
1 patient with four or more conditions
Technologies Used
Clinical Standards
HL7 FHIR R4
OMOP Common Data Model
SNOMED CT
RxNorm
Data & Analytics
Python
Pandas
DuckDB
Terminology Services
ATHENA Vocabulary Repository
Example Use Cases
Clinical Decision Support

Identify patients with complex disease profiles.

Population Health

Analyze disease prevalence and multimorbidity patterns.

Clinical Research

Construct disease-specific cohorts.

Digital Health Interoperability

Exchange healthcare information through FHIR resources.

Future Enhancements

Planned extensions include:

Interactive clinical analytics dashboard
Disease co-occurrence network visualization
Cohort exploration interface
FHIR Observation resources
OMOP Measurement table generation
Additional ATHENA vocabulary integration
Author

Harish Mohankumar

MSc Health Informatics Karolinska Institutet

Research Collaboration: National University of Singapore (NUS) Department of Biomedical Informatics

Focus Areas:

Digital Health
Clinical NLP
Interoperability
FHIR
OMOP CDM
Healthcare Analytics

---

A good README should allow a clinician or healthcare researcher to understand the project in 5 minutes without reading a single line of code. This README is written exactly with that goal. 🚀