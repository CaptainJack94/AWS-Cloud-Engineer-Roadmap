# Autonomous AWS Data Ingestion & ML Sharding Pipeline

An enterprise-ready, automated MLOps data ingestion service engineered on AWS infrastructure. This system acts as a resilient background daemon that continuously syncs a local Linux machine learning storage layer with a central cloud data lake (AWS S3), executing real-time data sharding on incoming byte streams.

## 🚀 Key Features

* **Cloud-Native Data Ingestion:** Leverages `boto3` to stream raw object payloads securely across the AWS global network from S3 to an EC2 instance.
* **Deterministic Deduplication:** Utilizes an $O(1)$ state-tracking manifest manifest loop (`processed_files.log`) to evaluate inventory and completely eliminate redundant downloads, saving on egress costs and cloud bandwidth.
* **Automated Dataset Partitioning:** Dynamically evaluates a randomized mathematical distribution engine to shard files into a standard Machine Learning matrix (`train` / `val` / `test`) at a strict **80/10/10 split** upon entry.
* **Defensive System Engineering:** Implemented a system-level process lock (`/tmp/s3_inspector.lock`) to prevent race conditions and execution overlaps during overlapping cron cycles.
* **Real-Time Telemetry Alerts:** Integrated with AWS SNS (Simple Notification Service) via standard SMTP protocols to instantly broadcast stack traces and critical error metrics directly to an administrator's inbox in the event of a runtime crash.

---

## 🏗️ Architecture & Infrastructure Flow

1. **Trigger:** A Linux `cron` daemon fires the ingestion engine autonomously every 5 minutes inside an isolated Python virtual environment.
2. **Lock Gate:** The script verifies the absence of a PID lock file to guarantee mutual exclusion.
3. **Inventory Sync:** The engine fetches the S3 metadata layer and intersects it against the local processed file manifest.
4. **Sharding Engine:** New objects are evaluated against a random float generation loop:
   * $\text{Roll} < 0.80 \rightarrow$ Routed to `/dataset/train/`
   * $0.80 \le \text{Roll} < 0.90 \rightarrow$ Routed to `/dataset/val/`
   * $\text{Roll} \ge 0.90 \rightarrow$ Routed to `/dataset/test/`
5. **State Update:** The file is downloaded, local storage structures are built dynamically if missing, and the manifest is updated.

---

## 🛠️ Tech Stack & Tools
* **Cloud Infrastructure:** AWS (EC2, S3, SNS, IAM)
* **Languages & SDKs:** Python 3.9+, Boto3 (AWS SDK)
* **Automation & Systems:** Linux Bash, Crontab scheduling, POSIX file locking
* **ML Infrastructure Theory:** Dataset Splitting, Data Drift Prevention, FinOps Egress Optimization

---

## 📊 Sample Production Output

```text
Scanning bucket: hardi-mlops-data-2026...
🆕 Found new package: IMG_20191109_145257.jpg
🚚 Streaming IMG_20191109_145257.jpg from S3 down to train/ folder...
✅ successfully sorted IMG_20191109_145257.jpg!

🆕 Found new package: IMG_20191109_173514.jpg
🚚 Streaming IMG_20191109_173514.jpg from S3 down to test/ folder...
✅ successfully sorted IMG_20191109_173514.jpg!

Worker cycle complete. Log updated. Lock released.