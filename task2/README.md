
This project provisions a **highly available**, **secure**, and **scalable** AWS infrastructure for the **OnFinance AI** solution, including:

-   VPC with public/private subnets
    
-   EKS Cluster with worker nodes
    
-   Load Balancer
    
-   RDS Database
    
-   S3 bucket
    
-   IAM roles and policies
## Prerequisites

-   Terraform >= v1.3+
    
-   AWS CLI configured with sufficient permissions
    
-   kubectl installed
    
-   An IAM user/role with admin access to create AWS resources
## Project Structure

task2/\
├── main.tf            # Main entry point\
├── variables.tf       # Input variables\
├── outputs.tf         # Outputs\
├── provider.tf        # AWS Provider

## Setup Instructions
### 1. Clone the Repository

`git clone <repo-url>`\
`cd terraform/` 

----------

### 2. Initialize Terraform

`terraform init` 

This will download the necessary providers.

----------

### 3. Customize Variables

Create the `terraform.tfvars` file and provide your inputs:

`# terraform.tfvars`\
`region        = "us-east-1"`\
`cluster_name  = "onfinance-eks-cluster"`\
`vpc_cidr_block = "10.0.0.0/16"`\
`public_subnets  = ["10.0.1.0/24", "10.0.2.0/24"]`\
`private_subnets = ["10.0.3.0/24", "10.0.4.0/24"]`\
`db_username   = "admin"`\
`db_password   = "YourSecurePassword123"` 

> **Secrets like `db_password` should be stored securely** using AWS Secret Manager or variables in the CI/CD pipeline.

----------

### 4. Plan the Infrastructure

`terraform plan -out=tfplan` 

This shows what Terraform will create without making changes.

----------

### 5. Apply and Deploy the reosurces

`terraform apply` 

Confirm with `yes` to create all resources.
