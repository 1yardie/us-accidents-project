terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.22.0"
    }
  }
}

provider "google" {
  credentials = "./google/terraform-keys.json"
  project     = "us-accidents-418522"
  region      = "us-east1-b"
} 