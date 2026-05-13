## Day 15: Monitoring & Alerting Proof

| CloudWatch CPU Spike | SNS Email Notification |
| :---: | :---: |
| ![CloudWatch Spike](images/cloudwatch-spike.png) | ![Email Alert](images/email-alert.png) |

### Performance Stress Test (Terminal)
![Terminal Output](images/terminal-stress.png)


Day 15: Infrastructure Monitoring and Automated Alerting
📌 Project Overview
Today’s objective was to implement a "nervous system" for AWS infrastructure. I moved from manual management to automated observability by configuring Amazon CloudWatch and Amazon SNS to monitor system health and provide real-time notifications during performance degradation.

🛠️ Tech Stack & Tools
Service: Amazon CloudWatch (Metrics & Alarms)

Messaging: Amazon SNS (Simple Notification Service)

Compute: Amazon EC2 (Amazon Linux 2023)

Stress Testing: stress utility (Linux)

🚀 Implementation Steps
1. Notification Infrastructure (SNS)
Provisioned an SNS Topic (ServerAlerts) to act as a centralized communication hub.

Configured an Email Subscription and validated the handshake to ensure secure delivery of automated alerts.

2. Monitoring & Thresholds (CloudWatch)
Defined a CloudWatch Alarm targeting the CPUUtilization metric of a specific EC2 instance.

Set a static threshold of > 50% CPU utilization over a 1-minute period.

Integrated the alarm with the SNS topic to trigger an email notification immediately upon state change from OK to ALARM.

3. Verification & Stress Testing
To validate the monitoring pipeline, I performed a simulated system overload:

Connected to the instance via SSH.

Executed a stress test using the stress tool: stress --cpu 2 --timeout 900.

Results: Observed real-time metric spikes in the CloudWatch dashboard. Once the threshold was breached, I successfully received an automated alert email confirming the system was in an "Alarm" state.

📈 Key Takeaways
Proactive vs. Reactive: Learned how to move away from manually checking dashboards to trusting automated alerts.

Cloud Observability: Gained experience in interpreting CloudWatch metric graphs and understanding data aggregation periods.

SRE Principles: Practiced foundational Site Reliability Engineering (SRE) concepts by engineering a test case to prove system reliability.