# AWS Cloud Sandbox: Host Hardening & Perimeter Defense

A hands-on project focused on Linux system administration, host-level hardening, and cloud-native network security. This project documents the defense lifecycle of an Amazon Linux 2023 EC2 instance—moving from an actively targeted public host to an isolated, secure environment using a Defense-in-Depth strategy.

## 🛠️ Technical Implementation & Milestones

### 1. Host-Level Hardening (`sshd_config`)
Secured the internal OS layer by auditing and refactoring the SSH daemon configuration file (`/etc/ssh/sshd_config`). Stripped away the entry mechanisms relied upon by automated internet botnets:
* **Disabled Password Authentication:** Enforced strict asymmetric cryptographic authentication (`.pem` keys), eliminating vulnerability to brute-force dictionary attacks.
* **Disabled Root Login:** Blocked direct external root access (`PermitRootLogin no`), enforcing the privilege-escalation model (`sudo`) from standard unprivileged service accounts (`ec2-user`).
* **Enforced Connection Throttling:** Dropped unauthenticated connection requests at the threshold using strict `[preauth]` hooks.

### 2. Network Perimeter Defense (AWS Security Groups)
Shifted the defensive posture from the host operating system to the AWS global network fabric to reduce compute resource consumption and minimize the server's attack surface.
* **Implemented Strict IP Whitelisting:** Revoked the wide-open inbound internet rule (`0.0.0.0/0`) on Port 22.
* **Stateful Firewalls:** Leveraged AWS Security Group stateful filtering rules to isolate access exclusively to standard/IPv6 transit points matching administrative endpoints (`/32` / `/128` CIDR boundaries).
* **Attack Surface Reduction:** Successfully rendered the instance completely invisible to public-facing internet scanning utilities (e.g., Shodan, ZMap).

### 3. Log Analytics & Incident Response
Analyzed real-time system logs to verify defensive barriers and map the infrastructure lifecycle.
* Monitored system telemetry logs using `systemd` and `journalctl`.
* Successfully audited the underlying authentication handshakes to confirm the explicit drop of unauthorized transport layer packets.

---

## 🔬 Architectural & Cyber Security Theory Mastered

* **Defense in Depth:** Implementing multi-layered security controls across the Network Layer (Security Groups), Host Layer (OS configuration), and Application/Identity Layer.
* **Least Privilege:** Constraining network routing tables and authentication rules to the absolute minimum necessary requirements.
* **IMDSv1 vs. IMDSv2 (Mitigation of SSRF):** Explored the mechanics of the AWS Instance Metadata Service (`169.254.169.254`), detailing how the session-oriented tokens of IMDSv2 block Server-Side Request Forgery and dynamic IAM session credential harvesting.
* **Cloud Security Specializations:** Explored sub-domains within the enterprise cloud ecosystem, including NetSec, IAM Engineering, DevSecOps, GRC, and SecOps/Incident Response.

---

## 📈 Roadmap Progression
* **Phase 1: Linux & Host Hardening** ── *Complete*
* **Phase 2: Cloud Infrastructure & Advanced Multi-Tier VPC Networking** ── *Up Next*