# End-to-end_Text_Summerization
##create IAM user for deplyment
    -Policy:
    -1. AmazonEC2ContainerRegistryFullAccess
    -2. AmazonEC2FullAccess

##creaye ecr repo to store docker image(ECR)
    -URI: 349970765913.dkr.ecr.eu-north-1.amazonaws.com/texts

##create ec2 ubuntu machine
##open ec2 machine and run commands
    -sudo apt-get update -y
    -sudo apt-get upgrade

    -curl -fsSL https://get.docker.com -o get-docker.sh
    -sudo sh get-docker.sh
    -sudo usermod -aG docker ubuntu

##make ec2 self-hosted(connect github with ec2, if i commited on github, ec2 update     automatically)
    -setting>actions>runner>new self hosted runner> choose os> then run command one by one

    -go project settings on github
    -open action then runner
    -click new runner(linux) and run those commands one by one in ec2 command line.


##setting up github seacrets
    -AWS_ACCESS_KEY_ID= 1st of downloaded csv files

    -AWS_SECRET_ACCESS_KEY= 2st of downloaded csv files

    -AWS_REGION = find your AWS region of the account

    -AWS_ECR_LOGIN_URI = ECR copied url befor slash

    -ECR_REPOSITORY_NAME = ECR copied url after slash


