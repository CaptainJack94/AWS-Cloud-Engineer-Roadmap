WS CloudWatch Logging Lab: Amazon Linux 2023
🎯 Objective
Configured an Amazon EC2 instance running Amazon Linux 2023 (AL2023) to automatically stream system logs to AWS CloudWatch using the unified CloudWatch Agent.

🛠️ Tech Stack
Cloud: AWS (EC2, CloudWatch, IAM)

OS: Amazon Linux 2023

Agent: amazon-cloudwatch-agent

Languages: JSON (Configuration), Bash

🚀 Key Achievements & Troubleshooting
During this lab, I successfully navigated several "real-world" configuration hurdles:

1. IAM Role & Metadata Validation
Ensured the EC2 instance had the correct CloudWatchAgentServerPolicy. Verified the attachment using the Instance Metadata Service (IMDSv2):

Bash
TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" ...`
curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/iam/info
2. Path Syntax & Debugging
Identified and corrected configuration errors including:

Relative vs. Absolute Paths: Corrected "var/log/..." to "/var/log/..." to ensure the agent could locate the log files from the root directory.

Typo Correction: Fixed directory naming errors in the config.json that were preventing the agent from initializing the log stream.

3. AL2023 Compatibility
Discovered that AL2023 does not generate /var/log/messages by default. Adapted the solution by:

Redirecting the agent to collect from /var/log/cloud-init-output.log.

Understanding the shift toward systemd-journald in modern Amazon Linux distributions.

📊 Results
Successfully established a log stream pipeline where system events are captured in real-time and visible in the CloudWatch Logs Console with a 1-day retention policy for cost-optimization.