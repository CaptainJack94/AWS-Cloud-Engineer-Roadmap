\# ☁️ AWS Cloud Engineer Roadmap: Phase 1

> \*\*Status:\*\* In Progress | \*\*Certification:\*\* AWS Cloud Practitioner (Completed)



This repository tracks my journey from Cloud Practitioner to Cloud Engineer. It contains my lab notes, automation scripts, and architecture diagrams.



\---



\## 🐧 Module 1: Linux \& EC2 Fundamentals

In this module, I moved from the AWS Management Console to the Command Line Interface (CLI) to manage cloud infrastructure.



\### 🛠️ Lab 1: Manual Web Server Deployment

\*\*Goal:\*\* Manually provision an EC2 instance and configure a web server via SSH.



\- \*\*OS:\*\* Amazon Linux 2023 (AMI)

\- \*\*Instance Type:\*\* t3.micro

\- \*\*Key Commands Mastered:\*\*

&#x20;   - `ssh -i`: Securely connecting to remote instances.

&#x20;   - `dnf install`: Managing Linux packages.

&#x20;   - `systemctl`: Controlling system services (Nginx).

&#x20;   - `vi`: Editing configuration files in the terminal.



\### 🤖 Lab 2: Automated Bootstrapping

\*\*Goal:\*\* Use "User Data" to automate the deployment of a web server without manual intervention.



\- \*\*Method:\*\* Bash scripting via AWS User Data field.

\- \*\*Outcome:\*\* Reduced deployment time from 5 minutes to 90 seconds.



\---



\## 📂 Project Directory

\- `/scripts`: Contains `bootstrap.sh` for automated Nginx setup.

\- `/notes`: Deep dives into Linux permissions and networking.



\---



