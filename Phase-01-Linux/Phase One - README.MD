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

-----------------------------------------------------

Lab 3: Server Hardening & User Administration

Today’s focus was on transforming a default AWS EC2 instance into a hardened, monitored node using the Principle of Least Privilege (PoLP).🛠️ 

Tasks & Key Accomplishments

SSH Port Translocation: Successfully moved the SSH daemon from default Port 22 to a custom port (2200) to mitigate automated brute-force attacks.

AWS Security Group Alignment: Configured Inbound Rules to synchronize with internal OS changes, resolving "Connection Timeout" hurdles.

System Patching: Executed a full system update using dnf update to patch known vulnerabilities (CVEs).

Identity Management: Created a restricted auditor user account and managed group memberships (wheel) to delegate administrative powers safely.

Sudo Accountability: Practiced "Privilege Escalation" and verified the digital "paper trail" using modern Linux journaling tools.

🔍 Troubleshooting Log

Error Encountered                      Root Cause                                                        Solution

Connection timed out     AWS Security Group was still blocking Port 2200.          Added Custom TCP rule for Port 2200 in AWS Console.

Permission denied           Username typo (ec2user vs ec2-user).                     Corrected syntax to match Amazon Linux defaults.

No such file or directory      Attempted to find /var/log/secure.              Learned that AL2023 uses binary journalctl for security logs.


# Check the Sudo Audit Trail
sudo journalctl _COMM=sudo

# Follow SSH logs in real-time
sudo journalctl -u sshd -f

# Securely offboard a user and their data
sudo userdel -r auditor

# Check system memory and uptime
free -h && uptime

Lab 4: More Linux permissions and security:

Key learning points today:

Issue: ssh: Could not resolve hostname p

Root Cause: Missing flag syntax in the CLI.

Solution: Corrected the command to include the port flag:

ssh -i "LinuxServerKey.pem" -p 2200 ec2-user@<IP>

Hardening: Verified the SSH daemon is listening on Port 2200 using ss -tulpn.

2. Linux Core Skills & Permissions
The Octal Rule: Learned to translate rwx into numeric values:

chmod 400: Strict read-only for the owner (Required for AWS .pem keys).

chmod 755: Public read/execute, private write (Standard for directories).

Ownership: Used chown root:root to simulate protecting system files from standard users.

Process Management: Used top and htop to monitor system resources and ps aux | grep ssh to audit running services.

3. Security Auditing with journalctl
Log Investigation: Used journalctl -u ssh to audit login attempts.

Real-time Monitoring: Practiced journalctl -f to watch system events as they happen.

Kernel Security: Identified and investigated a RETBleed (Spectre v2) CPU vulnerability warning.

Action Taken: Verified hardware mitigations using tail /sys/devices/system/cpu/vulnerabilities/*.

4. AWS Storage Security (EBS)
Encryption at Rest: Verified that the EBS volume is encrypted using AWS KMS.

The "Snapshot & Swap" Workflow: Learned the architectural process for encrypting unencrypted volumes by copying snapshots with encryption enabled.

Action Taken: Verified hardware mitigations using tail /sys/devices/system/cpu/vulnerabilities/*.

Key Commands Catalog

Command                              Purpose

ssh -p 2200                 Connect via non-standard port

lsblk -f                    View disk partitions and filesystem UUID

schmod 400                        Secure private keys

sudo dnf update -y            Apply latest security patches to the OS

journalctl -p err                Filter logs for system errors only

export                             Manage environment variables

\---



\## 📂 Project Directory

\- `/scripts`: Contains `bootstrap.sh` for automated Nginx setup.

\- `/notes`: Deep dives into Linux permissions and networking.



\---



