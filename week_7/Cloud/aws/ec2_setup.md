# AWS EC2 Setup Guide

This guide details setting up an Amazon EC2 instance for hosting GenAI and cloud workloads.

## Setup Steps

### Option A: Via AWS Management Console
1. Log into the AWS Management Console and navigate to **EC2**.
2. Click **Launch Instance**.
3. Name your instance (e.g., `Week7-GenAI-Cloud`).
4. Select an AMI (e.g., Amazon Linux 2023 or Ubuntu 22.04 LTS).
5. Choose an Instance Type (`t2.micro` for free tier testing or GPU instances like `g4dn.xlarge` for GenAI model inference).
6. Select or create a Key Pair for SSH access.
7. Configure Security Group rules:
   - Allow SSH (Port 22)
   - Allow HTTP (Port 80) / HTTPS (Port 443) if hosting a web service
8. Click **Launch Instance**.

### Option B: Via AWS CLI
```bash
aws ec2 run-instances \
    --image-id ami-12345678 \
    --count 1 \
    --instance-type t2.micro \
    --key-name MyKeyPair \
    --security-group-ids sg-903004f8 \
    --subnet-id subnet-6e7f829e
```
