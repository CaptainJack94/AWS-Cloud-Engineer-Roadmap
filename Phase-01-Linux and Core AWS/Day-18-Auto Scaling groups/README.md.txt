High-Availability AWS Architecture
Date: May 10, 2026
Project Goal:
Transitioned a standalone EC2 instance into a fault-tolerant, auto-scaling web architecture capable of self-healing and load distribution.

Core Components Implemented:
Auto Scaling Group (ASG):

Configured a "Self-Healing" fleet with a minimum capacity of 1 and a maximum of 2.

Integrated CloudWatch Metrics to trigger scaling actions based on CPU/RAM utilization.

Verified "Self-Healing" by manually terminating instances and observing the ASG automatically provisioning replacements.

Application Load Balancer (ALB):

Deployed a Layer-7 Load Balancer to act as the single entry point (DNS) for the application.

Configured Target Groups with active health checks to ensure traffic is only routed to "Healthy" instances.

Security & Networking:

Implemented a "Security Group Chain": The web servers now only accept traffic from the Load Balancer, effectively shielding them from direct public attacks.

Managed multi-AZ deployment across eu-north-1 (Stockholm) to ensure regional resilience.

Key Technical Takeaways:
Infrastructure as Policy: Learned that defining "Desired State" is more powerful than manual management.

Troubleshooting: Resolved connectivity "Timeouts" by auditing Security Group inbound rules and enforcing explicit http protocol handling.

Cloud Evolution: Bridged the gap between DevOps Infrastructure and AI Engineering foundations—understanding that scalable compute is the bedrock of LLM deployment.

Please see screenshots