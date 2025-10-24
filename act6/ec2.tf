variable "instance_type" {
  description = "The type instance EC2"
  type        = string
  default     = "t2.micro"
}

locals {
  instance_count = 2
  instance_name  = "act6-Ikerdev1-Alandev2"
}

resource "aws_instance" "alan_server_terr" {
  count         = local.instance_count
  ami           = "ami-0ca4d5db4872d0c28" # Amazon Linux 2 AMI (HVM), SSD Volume Type - us-east-2
  instance_type = var.instance_type

  tags = {
    Name = local.instance_name
  }
}

output "server_name" {
  value = aws_instance.alan_server_terr.tags.Name
}