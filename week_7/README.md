# Week 7 – Generative AI & Cloud

## Contents
- **GenAI/** → Text generation, image generation, chatbot demo
- **Cloud/** → AWS, Azure, GCP examples + Terraform automation

## How to Run
1. Install dependencies: `pip install transformers diffusers boto3 azure-storage-blob google-cloud-storage`
2. Run GenAI demos:
   - `python text_generation.py`
   - `python image_generation.py`
   - `python chatbot_demo.py`
3. Cloud:
   - AWS: `python s3_upload.py`
   - Azure: `python blob_upload.py`
   - GCP: `python cloud_storage_upload.py`
4. Terraform: `terraform init && terraform apply`
