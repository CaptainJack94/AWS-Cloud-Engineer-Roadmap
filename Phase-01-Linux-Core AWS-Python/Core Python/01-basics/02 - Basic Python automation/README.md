Project Update: Cloud Deployment & Environment Security📝

 Overview
 
 Successfully migrated the Content Governance Engine from a local development environment to a live AWS EC2 instance. This phase focused on "production-hardening" the script, ensuring it runs securely in a remote Linux environment.
 
 🛠 Technical Milestones
 
 Remote Infrastructure: Provisioned and configured an Amazon Linux 2023 (t2.micro) instance, managing connectivity via SSH and RSA key pairs.
 
 Identity & Access Management (IAM): Implemented IAM Roles to provide the EC2 instance with secure, credential-less access to AWS services, adhering to the "Principle of Least Privilege.
 
 "Linux System Administration:
 
 Managed file system permissions (chmod, chown) to secure data integrity.
 
 Navigated the Linux CLI to manage files, directories, and system logs.
 
 Environment Isolation: Deployed the application within a Python Virtual Environment (venv) to prevent dependency conflicts and ensure a clean production footprint.
 
 Debugging & Resolution: Identified and resolved pathing issues and file-naming conflicts (Data Integrity) during the remote deployment process.
 
 🏗 Deployment Workflow
 
 SSH Tunneling: Established a secure connection to the remote host.
 
 Code Ingestion: Transferred logic (file_handler.py) and schema (data.json) to the server.
 
 Dependency Management: Initialized venv and installed the boto3 SDK for future AWS integration.Execution: Validated the moderation engine in a headless (CLI-only) environment.
