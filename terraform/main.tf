terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.22.0"
    }
  }
}

provider "google" {
  credentials = file("~/.google/credentials/terraform-keys.json")
  project     = "us-accidents-418522"
  region      = "us-east1-b"
} 

resource "google_storage_bucket" "auto-expire" {
  name          = "us-accidents-418522_data_lake"
  location      = "US"
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}