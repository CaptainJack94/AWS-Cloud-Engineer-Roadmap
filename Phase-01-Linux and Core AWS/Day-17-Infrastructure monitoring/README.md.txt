AWS Infrastructure Monitoring & Alerting System
Project Overview:
Implemented a comprehensive monitoring solution for an Amazon EC2 Linux instance using the Unified CloudWatch Agent. This setup bridges the "visibility gap" between AWS infrastructure and the guest Operating System, allowing for real-time tracking of memory and disk utilization.

🛠️ Key Technical Implementations
Custom Metric Collection: Configured the amazon-cloudwatch-agent via a custom config.json to ingest system-level metrics (RAM and Disk Usage) into CloudWatch.  

Log Aggregation: Streamed system boot logs (cloud-init-output.log) into CloudWatch Logs for centralized troubleshooting.

Automated Alerting: Engineered an Amazon SNS (Simple Notification Service) topic and subscription to deliver real-time email alerts when critical thresholds are breached.  

CloudWatch Alarms: Set up high-precision alarms triggered by RAM usage exceeding defined thresholds (e.g., 80%), enabling proactive server management.  

💻 DevOps Workflow & Skills
Linux Administration: Advanced use of systemctl for service management, nano for configuration, and tail for log analysis.

JSON Configuration: Authored complex agent configurations to define metrics namespaces and collection intervals.

Troubleshooting: Resolved synchronization issues by performing manual cache purges of the CloudWatch Agent runtime environment.

Stress Testing: Validated alarm triggers using Linux command-line tools (dd and tmpfs) to simulate high-load scenarios.

📈 Results
Proactive Monitoring: Reduced "blind spots" in server health.

Instant Notification: Successfully received automated email alerts during simulated system stress events, proving the reliability of the notification pipeline.