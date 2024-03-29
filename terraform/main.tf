terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.22.0"
    }
  }
}

provider "google" {
  credentials = file(var.credentials)
  project     = var.project
  region      = var.region
} 

resource "google_storage_bucket" "auto-expire" {
  name          = "${var.project}_${var.gcs_bucket_name}"
  location      = var.location
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

//Resource name "Name of the resource block within terraform"
resource "google_bigquery_dataset" "us_accidents_dataset" {
  dataset_id = var.bq_dataset_name
  location   = var.location
}