# 🚀 Automated AWS Ingestion Pipeline with Real-Time Monitoring

A production-grade, fault-tolerant Python MLOps pipeline running on AWS EC2 that autonomously scans, ingests, and tracks files from an upstream AWS S3 data lake while utilizing AWS SNS for real-time telemetry alerting.

---

### 🛠️ Architecture & Key Features

*   **State Management & Cost Optimization:** Implemented a persistent log-tracking system (`processed_files.log`) utilizing $O(1)$ set lookups. This prevents redundant processing of previously ingested imagery, drastically cutting downstream compute costs and API overhead.
*   **Concurrency Control (Race Condition Prevention):** Engineered a process-locking mechanism using a dynamic `/tmp/s3_inspector.lock` tracking file. If a duplicate cron job or worker kicks off while a cycle is active, the pipeline gracefully exits to guarantee data integrity.
*   **Autonomous Operational Alerting:** Integrated `boto3` with an AWS SNS notification tower (Stockholm region). The pipeline possesses situational awareness, actively broadcasting cryptographic payloads to an operator's inbox during anomalies.
*   **Resilient Error Trapping:** Designed dual-layered `try-except-finally` blocks:
    1.  **Soft Failures:** Automatically flags and bypasses isolated security blocks (`AccessDenied`) without halting the wider queue.
    2.  **Hard Failures:** Intercepts catastrophic system/network crashes, captures full `traceback` diagnostics, alerts the engineering team, and ensures the system lock is deleted so the pipeline never deadlocks.

---

### 🧪 Tech Stack

*   **Environment:** AWS EC2 (Amazon Linux 2023)
*   **Cloud Infrastructure:** AWS S3, AWS SNS, IAM Instance Profiles
*   **Language & SDK:** Python 3.9+, Boto3