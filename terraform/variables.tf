variable "credentials" {
  description = "My Credentials"
  default     = "~/.google/credentials/terraform-keys.json"
}
variable "project" {
  description = "Project"
  default     = "us-accidents-418522"
}

variable "region" {
  description = "Project"
  default     = "us-east1-b"
}
variable "location" {
  description = "Project Location"
  default     = "US"
}

variable "bq_dataset_name" {
  description = "My BigQuery Dataset Name"
  default     = "us_accidents"
}

variable "gcs_bucket_name" {
  description = "My Storage Bucket Name"
  default     = "data_lake"
}


variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}
