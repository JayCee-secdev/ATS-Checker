# ATS Resume Reviewer (Project Raccoon - Phase 1)

## Overview
An automated Resume Reviewer built with Python and Flask. This tool is designed to mimic Applicant Tracking Systems (ATS) by parsing resume files (PDF/DOCX), extracting raw text, and comparing keywords against target job descriptions.

While currently rule-based, the architecture is designed to support Machine Learning classifiers in future iterations for sentiment analysis and semantic matching.

## Features
* **Ingestion:** Supports PDF and DOCX file parsing.
* **Sanitization:** Validates file types and strips potential malicious formatting before processing.
* **Analysis:** Calculates keyword overlap scores between candidate resumes and job descriptions.
* **Feedback:** Provides actionable missing keyword reports.

## Tech Stack
* **Backend:** Python, Flask
* **Data Processing:** (Planned) Pandas, NumPy
* **NLP/ML:** (Planned) spaCy / scikit-learn
* **Frontend:** HTML/CSS (Jinja2 Templates)
