output "instance_id" {
  description = "ID of the created EC2 instance"
  value       = aws_instance.week7.id
}

output "instance_arn" {
  description = "ARN of the created EC2 instance"
  value       = aws_instance.week7.arn
}
