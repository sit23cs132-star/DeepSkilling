# Week 7 – Generative AI & Cloud Integration

Welcome to the **Week 7** module of the Python Full Stack Engineering Deep Skilling program. This module covers hands-on implementations for Generative AI applications and Cloud deployment across AWS, Azure, GCP, and Terraform IaC.

---

## 📂 Contents & Architecture

```text
week_7/
├── GenAI/              # Generative AI Application Demos
│   ├── text_generation.py   # Text generation with Hugging Face GPT-2
│   ├── image_generation.py  # Image generation with Diffusers & Stable Diffusion
│   ├── chatbot_demo.py      # Rule-based baseline chatbot demo
│   └── README.md
├── Cloud/              # Multi-Cloud & Infrastructure as Code (IaC)
│   ├── aws/            # AWS EC2 guide, S3 upload script, & Lambda handler
│   ├── azure/          # Azure Blob upload script & Function App handler
│   ├── gcp/            # GCP Cloud Storage script & Cloud Function handler
│   ├── terraform/      # Terraform IaC configurations (main.tf, variables.tf, outputs.tf)
│   └── README.md
└── Week_7.md           # Module Documentation
```

---

## 🚀 How to Run

### 1. Prerequisites & Dependencies
Install the required Python packages:
```bash
pip install transformers diffusers boto3 azure-storage-blob google-cloud-storage torch accelerate
```

### 2. Generative AI Demos
Navigate to `week_7/GenAI`:
- **Text Generation**: `python text_generation.py`
- **Image Generation**: `python image_generation.py`
- **Chatbot Demo**: `python chatbot_demo.py`

### 3. Cloud Integration Scripts
Navigate to `week_7/Cloud`:
- **AWS S3**: `python aws/s3_upload.py`
- **Azure Blob**: `python azure/blob_upload.py`
- **GCP Storage**: `python gcp/cloud_storage_upload.py`

### 4. Terraform Provisioning
Navigate to `week_7/Cloud/terraform`:
```bash
terraform init
terraform plan
terraform apply
```
