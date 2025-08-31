# Legal Fine tuned LLM

SaaS product:
It can review contracts and answer legal policy questions with citations, audit logs, etc

1. data strategy and pipeline

public data (US/India jurisdictions)
    - legal texts
    - contracts
    - QnA

https://www.atticusprojectai.org/cuad

pipeline
- ingestion on s3 aws (documents pdf, docx, OCR)
- normalization - text cleaning, section detection, chunking by logical sections, citation extraction
- label - create lightweight labeling tasks - accept/reject model clause presence, risk level
- governance - dataset source, license, jurisdiction,

https://boto3.amazonaws.com/v1/documentation/api/latest/index.html
