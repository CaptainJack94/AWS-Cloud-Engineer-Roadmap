# Autonomous AWS Ingestion Pipeline & Telemetry Microservice

A production-grade, self-monitoring data ingestion microservice engineered in Python and deployed on an AWS EC2 instance. This pipeline autonomously tracks data lake states, protects system resources against race conditions, and handles critical infrastructure failures gracefully.

## 🚀 Core Features & Architecture

### 1. $O(1)$ State Management & Deduplication
* Implements a persistent, optimized file-tracking engine (`processed_files.log`) ensuring $O(1)$ lookup complexity.
* Guarantees that assets residing in the AWS S3 data lake are processed exactly once, drastically reducing redundant computational overhead and AWS API call costs.

### 2. Concurrency Control & Race Condition Prevention
* Engineered a strict file-locking mechanism using a local system sentinel file (`/tmp/s3_inspector.lock`).
* Prevents overlapping execution cycles or data corruption in multi-tenant environments by immediately rejecting secondary processes with a defensive termination routine.

### 3. Fault-Tolerant Architecture & Telemetry
* Implements strict defensive programming patterns utilizing comprehensive `try-except-finally` blocks.
* Configured with live exception-trapping that maps tracebacks and automatically broadcasts critical operational failure alerts (such as `NoSuchBucket` errors) via AWS SNS (Simple Notification Service) to system administrators.
* Employs an infallible cleanup execution block ensuring system locks are released even during catastrophic runtime failure, entirely preventing zombie-lock deadlocks.

### 4. Native Linux Background Automation
* Fully decoupled from manual user execution via integration with the native Linux kernel scheduler (`crontab`).
* Environment execution is completely isolated using absolute virtual environment (`venv`) path mappings.
* Features multi-stream log redirection (`2>&1`) to generate immutable, continuous background audit trails (`cron_output.log`) for seamless historical debugging.

## 🛠️ Tech Stack & Skills Demonstrated

* **Language:** Python 3.9+
* **Cloud Infrastructure:** Amazon Web Services (AWS EC2, S3, SNS, IAM Security Policies)
* **SDKs & Libraries:** Boto3, Botocore
* **Systems Engineering:** Linux System Administration, Crontab Automation, Shell Environment Architecture, Process Orchestration, Logging & Stream Redirection

---

## 📂 System Execution Flow

1. **Cron Daemon Wakes:** Linux wakes up the isolated virtual environment Python interpreter on a recurring schedule.
2. **Lock Evaluation:** The script checks for the presence of `/tmp/s3_inspector.lock`. If present, it gracefully aborts to prevent resource collisions. If clear, the lock is acquired.
3. **Data Lake Scan:** The pipeline queries the designated AWS S3 bucket using `boto3`.
4. **Deduplication:** Object keys are matched against the local state file with $O(1)$ efficiency; only unseeen data triggers downstream staging.
5. **Exception/Cleanup Loop:** * *On Success:* Updates state log, fires success logs, and releases the lock.
    * *On Failure:* Traps the error, dispatches an AWS SNS telemetry payload, clears the system lock, and preserves the traceback log.