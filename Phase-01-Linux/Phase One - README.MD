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

 ssh -i: Securely connecting to remote instances.

dnf install: Managing Linux packages.

systemctl: Controlling system services (Nginx).

vi: Editing configuration files in the terminal.

sudo adduser:	Implementing identity separation.

ls -l: Auditing file permissions and ownership.

grep: Searching logs for indicators of compromise (IoC).

journalctl: Accessing the system's tamper-resistant binary logs.

exit / ~.:	Maintaining session hygiene and closing attack vectors.



\### 🤖 Lab 2: Automated Bootstrapping

\*\*Goal:\*\* Use "User Data" to automate the deployment of a web server without manual intervention.



\- \*\*Method:\*\* Bash scripting via AWS User Data field.

\- \*\*Outcome:\*\* Reduced deployment time from 5 minutes to 90 seconds.

Security auditing:

who: To verify active user sessions and detect unauthorized access.

ss -tulpn: To audit open network ports and listening services (Attack Surface Mapping).

sudo -l: To evaluate the "Principle of Least Privilege" regarding administrative permissions.

history: Recognized the risk of command-line "leakage" of sensitive credentials.



\---



\## 📂 Project Directory

\- `/scripts`: Contains `bootstrap.sh` for automated Nginx setup.

\- `/notes`: Deep dives into Linux permissions and networking.



\---



