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

--------------------------------------------------

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

-----------------------------------------------

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

Key Commands:

Command,Purpose
ssh -p 2200 - Connect to a server via a non-standard port (Security through obscurity).

lsblk -f - "View disk partitions, mount points, and unique filesystem UUIDs."

chmod 400 - Secure private keys by making them read-only for the owner (Required for .pem files).

sudo dnf update -y - Apply the latest security patches and updates to the OS automatically.

journalctl -p err - "Filter system logs to show only ""Error"" level messages and above."

export - View or manage environment variables (used for API keys or system paths).

----------------------------------------------------------
Lab 5: Linux Administration:

Today I focused on the internal mechanics of Linux and investigated system level processes.

1. Network Interface Auditing
Command used: ip addr & ping

Key Learning: Identified the difference between the Loopback interface (lo) for internal communication and the Primary interface (ens5) used for VPC and Internet traffic.

Verification: Confirmed DNS resolution and ICMP reachability to external hosts (google.com).

2. Advanced Web Troubleshooting with curl
Concept: Used curl (Client URL) as a diagnostic tool rather than just a browser.

AWS Metadata (IMDSv2): Successfully retrieved instance metadata (Instance ID, Public Hostname) using the secure IMDSv2 token-based method.

Security Note: Practiced using PUT requests to generate session tokens, preventing SSRF vulnerabilities.

3. Web Server Deployment & Hardening
Service: Installed and configured Nginx using dnf.

Process Management: Analyzed the Master/Worker process model.

Master Process: Runs as root to manage the service.

Worker Processes: Run as the nginx user to handle traffic (Principle of Least Privilege).

Lifecycle Control: Mastered systemctl for start, stop, enable (persistence), and status checks.

4. System Resource Investigation
Process Tracking: Used ps aux | grep nginx to audit running IDs (PIDs).

Storage Auditing: Used df -h to monitor EBS volume utilization (NVMe storage) and ensure system stability.

💡 Architectural Insights (AWS SAA Alignment)
Security Groups: Verified that local connectivity (localhost:80) can succeed while external connectivity fails if Inbound Rules are not explicitly configured.

High Availability: Learned the importance of systemctl enable to ensure service recovery after an EC2 reboot or Auto Scaling event.

🔧 Tools & Ciphers Used
dnf | systemctl | curl | ps | grep | df | IMDSv2

---------------------------------------------

Day 6: Linux Administration - File permissions, Ownership and Bash scripting

1. The "Security Guard" (Permissions & chmod)
Concept: Mastered the Numerical (Octal) Notation for file security.

4 (Read), 2 (Write), 1 (Execute).

Key Command: chmod 600 secret_plan.txt

Successfully locked down a sensitive file so only the root user could access it, simulating a "Private Key" security scenario.

The SAA Connection: Applied the chmod 400 logic required for securing .pem keys in AWS.

2. Administrative Ownership (chown)
Command used: sudo chown root:root secret_plan.txt

Learning: Experimented with Privilege Separation. By transferring ownership to the superuser, I verified that the standard ec2-user is restricted from modifying critical system files without explicit sudo escalation.

3. Infrastructure as Code: Bash Scripting
Script Creation: Built setup_web.sh using the nano text editor.

Functionality: * Implemented Command Substitution using $(hostname) to make the script context-aware.

Integrated System Auditing commands (df -h) into the script workflow.

Execution: Used chmod +x to grant the file "Execute" permissions, transforming a text file into a functional system tool.

4. File Management & Safety
Commands: mv (Move/Rename), cp (Copy/Backup), and ls -la (Viewing hidden system files).

Best Practice: Learned to create .bak copies of configuration files before attempting modifications—a critical skill for production environment stability.

 
chmod +x [file] - Grant Execute permission -  Turning a script into a runnable program.

chown [user]:[group] - Change file owner - Securing a database config file from standard users.

nano [file] - Terminal Text Editor - Editing configuration files or writing automation scripts.

ls -la - List All (including Hidden) - Auditing .ssh keys or .bash_history for security.

$(command) - Command Substitution - Pulling live data (like hostname) into a script variable.
\---



\## 📂 Project Directory

\- `/scripts`: Contains `bootstrap.sh` for automated Nginx setup.

\- `/notes`: Deep dives into Linux permissions and networking.



\---



