:: set up repository in ecr to push the image to
set MY_ECR_REPOSITORY=idc-classifer
set MY_AWS_REGION=us-east-1
aws ecr create-repository --repository-name %MY_ECR_REPOSITORY%  --region %MY_AWS_REGION%



