# Cloud Operations & Infrastructure as Code (IaC)

This module provides cloud integration scripts across the top cloud providers as well as Infrastructure as Code using Terraform.

## Cloud Providers

### AWS (`aws/`)
- `ec2_setup.md`: Setup guide for launching Amazon EC2 instances.
- `s3_upload.py`: AWS S3 file upload using `boto3`.
- `lambda_function.py`: Serverless AWS Lambda function handler.

### Azure (`azure/`)
- `blob_upload.py`: Azure Blob Storage file upload using `azure-storage-blob`.
- `function_app.py`: Serverless Azure Function App HTTP trigger handler.

### GCP (`gcp/`)
- `cloud_storage_upload.py`: Google Cloud Storage upload using `google-cloud-storage`.
- `cloud_function.py`: Serverless Google Cloud Function HTTP trigger handler.

## Automation & IaC

### Terraform (`terraform/`)
- `main.tf`: AWS provider & EC2 resource provisioning configuration.
- `variables.tf`: Input variables for region, AMI, and instance type.
- `outputs.tf`: Output definitions for provisioned infrastructure details.

### How to Provision
```bash
cd terraform
terraform init
terraform plan
terraform apply
```
