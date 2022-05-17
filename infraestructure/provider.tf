provider "aws" {
  region = var.aws_region
}

# Centralizar o arquivo de controle de estado do terraform
terraform {
  backend "s3" {
    bucket = "terraform-state-igti-Altamiro-EDC-4-4"
    key    = "state/igti/mod1/terraform.tfstate"
    region = "us_east_1"
  }
}