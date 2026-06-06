## 🚀 Project Case Study: Multi-Layer Perimeter Defense, IAM Governance & Telemetry Logging

### 📌 Project Overview
Advanced a baseline cloud network boundary into a highly resilient, monitored infrastructure enclave via the AWS CLI using Windows PowerShell. This engineering sprint implemented a strict Defense-in-Depth traffic filtration matrix, executed an Attribute-Based Access Control (ABAC) identity audit, and instrumented live VPC Flow Logs to feed automated network telemetry into Amazon CloudWatch.

### 🛡️ Core Security Architecture & Engineering Milestones

* **Defense in Depth (Stateful vs. Stateless Firewalls):** Engineered a dual-barrier security matrix to isolate instance layers from edge-subnet boundaries:
  * **Instance Security Layer:** Provisioned a stateful Security Group restricting inbound SSH handshakes explicitly to a strict `/32` CIDR block matching the administrator's public workstation IP.
  * **Subnet Security Boundary:** Deployed a custom Network ACL. Because NACLs are stateless, explicit traffic paths were mapped for both the inbound request path (Port 22 from the whitelisted workstation) and the outbound return path over the ephemeral port range (`1024–65535`).
* **Principle of Least Privilege & Governance Audit:** Constructed a declarative customer-managed IAM JSON policy enforcing rigid attribute-based governance. The schema restricts highly destructive state actions (`ec2:StartInstances`, `ec2:StopInstances`, `ec2:RebootInstances`) behind an explicit condition block checking for resource tags (`aws:ResourceTag/Environment = Sandbox`).
* **Boundary Enforcement Validation:** Execution of the IAM manifest returned a secure `AccessDenied` flag under the active developer profile (`AI_developer`). This validated real-world separation of duties: confirming the build identity possessed the authority to manipulate network layers but was properly box-fenced away from modifying account privilege directories. 
* **Continuous Telemetry Instrumentation:** Activated VPC Flow Logs across all elastic network interfaces, setting a capture type of `ALL` to stream raw packet metadata directly into an Amazon CloudWatch Log Group. This enables advanced parsing queries (e.g., filtering for `action="REJECT"`) to actively monitor perimeter reconnaissance or port scanning.

---

### 🛠️ Technical Execution & Pipeline Reference

1. **Workstation Context Resolution:** Dynamically pulled and stored the administrative workstation's public IP address as an active environment variable string.
2. **Stateful Perimeter Injection:** Authorized the tight inbound TCP rule on Port 22 within the custom Security Group container.
3. **Stateless NACL Provisioning:** Created explicit rule tokens (`Rule 100` Inbound / `Rule 110` Outbound) and re-associated the live subnet fabric away from the broad default VPC ACL.
4. **Offline Schema Linting:** Utilized local shell file engines to output the IAM manifest to disk, executing an offline schema validation to verify syntax, brackets, and logical commas were structurally complete.
5. **Telemetry Stream Initialization:** Carved out a dedicated CloudWatch Log Group (`VPC-Edge-Perimeter-Telemetry`) and initialized the native VPC logging pipe.

---

### 🔬 Telemetry & Verification Audit Data

Querying the custom Network ACL plane confirmed the successful binding of the stateless rule matrix and the enforcement of the standard zero-trust default-deny catch-all layer:

```json
{
    "NetworkAcls": [
        {
            "Entries": [
                {
                    "CidrBlock": "0.0.0.0/0",
                    "Egress": true,
                    "PortRange": { "From": 1024, "To": 65535 },
                    "Protocol": "6",
                    "RuleAction": "allow",
                    "RuleNumber": 110
                },
                {
                    "CidrBlock": "0.0.0.0/0",
                    "Egress": true,
                    "Protocol": "-1",
                    "RuleAction": "deny",
                    "RuleNumber": 32767
                },
                {
                    "CidrBlock": "81.79.140.132/32",
                    "Egress": false,
                    "PortRange": { "From": 22, "To": 22 },
                    "Protocol": "6",
                    "RuleAction": "allow",
                    "RuleNumber": 100
                },
                {
                    "CidrBlock": "0.0.0.0/0",
                    "Egress": false,
                    "Protocol": "-1",
                    "RuleAction": "deny",
                    "RuleNumber": 32767
                }
            ],
            "IsDefault": false,
            "VpcId": "vpc-0d5cceb1cd67ab851"
        }
    ]
}