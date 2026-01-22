# Serverless AI Sentiment Analyzer

A full-stack serverless application that performs real-time sentiment analysis using Generative AI. Built with AWS Lambda, Amazon Bedrock (Nova Micro), and API Gateway.

**Live Demo:** https://d3p9xzountf7p0.cloudfront.net/

## 🏗 Architecture
**Frontend (S3 + CloudFront) → API Gateway → Lambda → Amazon Bedrock**

* **Frontend:** Static HTML/JS hosted on S3, served securely via CloudFront (HTTPS).
* **API Layer:** Amazon API Gateway (HTTP API) handling REST requests with CORS enabled.
* **Compute:** AWS Lambda (Python) executing business logic and error handling.
* **AI Model:** Amazon Bedrock (Nova Micro) performing natural language processing (NLP) to classify text as Positive, Negative, or Neutral.
* **Security:** API throttling (1 RPS) and IAM roles for least-privilege access.

## 🚀 Features
* **Real-time Analysis:** Returns sentiment classification in <500ms.
* **Serverless:** Zero infrastructure management; scales to zero when not in use.
* **Cost Optimized:** Uses Bedrock's Nova Micro model and API Gateway throttling to stay within AWS Free Tier limits.

## 🛠 Tech Stack
* **Cloud:** AWS (Region: us-east-1)
* **Infrastructure:** Lambda, S3, API Gateway, IAM, CloudFront
* **AI/ML:** Amazon Bedrock Runtime (Boto3)
* **Language:** Python (Backend), HTML5/CSS/JavaScript (Frontend)

## 📂 Project Structure
```text
/frontend
  └── index.html           # Client-side UI connecting to API Gateway
/lambda
  └── lambda_function.py   # Python handler for Bedrock interaction
/qr_code_generator.py       # QR code generator script

## 📱 Utility: QR Code Generator
Included in this repo is a simple Python CLI tool to generate QR codes (e.g., for sharing the website link).

**How to Run Locally:**
```bash
# 1. Create environment
python -m venv .venv
# Windows:
.venv\Scripts\activate

# 2. Install dependencies
pip install "qrcode[pil]"

# 3. Run the script
python qr_code_generator.py