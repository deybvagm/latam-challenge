module "ecs" {
  source                  = "./ECS"
  vpc_id                  = "vpc-0fef121b1916b2913"
  cluster_name            = "demo-api-cluster"
  cluster_service_name    = "demo-api-service"
  cluster_service_task_name = "demo-api-task"
  vpc_id_subnet_list      = ["subnet-023387626efc1bfc1", "subnet-0c233719c73ab73a3", "subnet-0165d907c1dde1dd5", "subnet-022ada054e1051e04", "subnet-0546995c3785de614", "subnet-0155a1eac202431fa"]
  execution_role_arn      = "arn:aws:iam::892367763603:role/ecsTaskExecutionRole"
  image_id                = "892367763603.dkr.ecr.us-east-1.amazonaws.com/ecsdemo:latest"
}
