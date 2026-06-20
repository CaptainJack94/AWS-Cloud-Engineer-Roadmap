### 🚀 Project: AWS Multi-Layer Network Perimeter Lab
**Date:** June 20, 2026

#### 📋 Overview
Today, I successfully architected and deployed a multi-layered, defense-in-depth network perimeter inside a custom AWS VPC. The goal of this lab was to implement a strict "Least Privilege" traffic policy for an EC2 public-facing server, forcing inbound and outbound packets through both a stateful firewall and a stateless network boundary.

#### ⚙️ What I Engineered
* **Custom Networking Layout:** Formatted and carved out a fresh public subnet slice (`172.31.48.0/20`) within a master `172.31.0.0/16` VPC topology. Enabled dynamic public IP pooling settings.
* **Stateless Firewall Construction:** Engineered a custom **Network ACL (NACL)** from scratch. Hardened the subnet edge by replacing the default wide-open AWS routing rules with an explicit rule hierarchy.
* **Ephemeral Port Mapping:** Handled the stateless return packet flow requirement by explicitly mapping TCP inbound traffic pairs alongside outbound **Ephemeral Ports (1024-65535)** targeted precisely at my client WAN address.
* **Compute Provisioning:** Deployed a test instance running Amazon Linux 2023 (`t2.micro`), successfully locking its virtual interface to an IP-restricted Security Group.

#### 🔧 Real-World Troubleshooting & Diagnostics
* **Subnet Mapping Alignments:** Fixed a classic AWS default-deny issue where the newly provisioned instance lacked a native public IPv4 mapping due to default subnet configurations.
* **Network Variable Auditing:** Diagnosed an infrastructure mismatch where local private LAN IPs (`192.168.1.x`) were initially utilized for remote cloud ACL tracking, successfully correcting the target perimeter rules to monitor public external WAN targets (`0.0.0.0/0`).
* **Active Session Isolation Drills:** Intentionally simulated a high-security emergency isolation drill. By dynamically updating the stateless NACL outbound rules to `DENY`, I successfully validated that active TCP/SSH streams freeze instantaneously at the subnet boundary, proving the "amnesia architecture" mechanics of stateless packet filters over stateful firewalls.

#### 🧰 Skills Demonstrated
* AWS Cloud Infrastructure (VPC, NACL, Security Groups, EC2 Routing)
* Subnet Masking & CIDR Block Strategy (`/16` vs `/20`)
* Network Security Architecture & Perimeter Defense-in-Depth
* Live Infrastructure Troubleshooting & Traffic Pattern Analysis