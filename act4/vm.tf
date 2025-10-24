resource "aws_instance" "mi_instancia" {
  ami           = "ami-0c02fb55956c7d316"
  instance_type = "t2.micro"
  tags = {
    Name = "instancia-terraform-actividad4"
  }
}