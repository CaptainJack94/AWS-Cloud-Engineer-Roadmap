## 🚀 Project Case Study: CLI-Driven Custom VPC Architecture & Edge Routing

### 📌 Project Overview
Engineered an isolated, secure-by-default Virtual Private Cloud (VPC) network architecture from the ground up utilizing the AWS CLI within a Windows PowerShell environment. The project establishes a dedicated public edge DMZ tier, configures deterministic routing pathways, and validates structural integrity while strictly avoiding the risks associated with default cloud deployment configurations.

### 🛡️ Core Architectural & Security Design Principles

* **Defense in Depth (Network Isolation):** Rather than relying on the implicit VPC Main Route Table—which exposes an environment to severe lateral configuration risks—a custom **Public Route Table** was explicitly constructed. This ensures that any future private or data subnets added to the VPC remain completely isolated and dark to the public internet by default.
* **Deterministic Egress Control:** Implemented a longest-prefix-match routing engine, injecting a stateless default route (`0.0.0.0/0`) that explicitly directs unknown public internet-bound traffic to a horizontally scaled, software-defined Internet Gateway (IGW).
* **CLI-First Automation & Shell Compatibility:** Developed and optimized standard syntax structures directly within Windows PowerShell, successfully resolving shell-specific aggressive quote-stripping issues by deploying literal shorthand string notations (`'Value=true'`) for VPC attribute modifications.

---

### 🛠️ Technical Execution & Pipeline Steps

1. **Root Boundary Initialization:** Provisioned a master VPC core container allocated to a strict `10.0.0.0/16` private IP footprint (RFC 1918) supporting a theoretical boundary of 65,536 hosts.
2. **DNS Attribute Refactoring:** Modified the underlying VPC fabric properties over the API to explicitly force public FQDN/DNS hostname resolution upon instance initialization.
3. **Subnet Segmentation Audit:** Carved out a `10.0.1.0/24` public DMZ subnet. Conducted an IP allocation audit verifying an `AvailableIpAddressCount` of exactly **251 usable hosts**, accounting for the 5 link-local addresses reserved implicitly by AWS.
4. **Perimeter Bridge Attachment:** Deployed a highly available Internet Gateway asset and structurally bound it to the parent VPC core container.
5. **Route Mapping & Association:** Constructed the custom routing manifest, injected the `0.0.0.0/0` edge transit pathway, and bound the logic directly to the live subnet tier to activate internet access pathways.

---

### 🔬 Telemetry, Verification & Auditing

Before environment deconstruction, network topology integrity was validated via the control plane API. Querying the live route table status confirmed a pristine structural matrix:

```json
{
    "RouteTables": [
        {
            "Associations": [
                {
                    "Main": false,
                    "RouteTableAssociationId": "rtbassoc-04bde5bb3a4d28373",
                    "RouteTableId": "rtb-0d2b87e36c9f9d95e",
                    "SubnetId": "subnet-08405d768135c4dfb"
                }
            ],
            "Routes": [
                {
                    "DestinationCidrBlock": "10.0.0.0/16",
                    "GatewayId": "local",
                    "State": "active"
                },
                {
                    "DestinationCidrBlock": "0.0.0.0/0",
                    "GatewayId": "igw-0faaf27641ab15771",
                    "State": "active"
                }
            ]
        }
    ]
}