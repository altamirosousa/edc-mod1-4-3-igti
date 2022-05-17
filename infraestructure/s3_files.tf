resource "aws_s3_bucket_object" "job_spark" {
  bucket = aws_s3_bucket.dl.id
  key    = "emr-code/pyspark/job_spark_from_tf.py"
  acl    = "private"
  source = "../infraestructure/edc_3_4_job_spark.py"
  etag   = filemd5("../infraestructure/edc_3_4_job_spark.py")
}