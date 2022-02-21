pipeline {
    agent any

    parameters {
        string(name: 'RoleName', defaultValue: 'jenkins_role', description: 'Workspace/environment file to use for deployment')
        string(name: 'AccountId', defaultValue: '941039889978', description: 'accountid variable to pass to Terraform')
        string(name: 'region', defaultValue: 'us-east-1', description: 'region variable to pass to Terraform')
        string(name: 'trg_accountid', defaultValue: '220934115347', description: 'ami sharing target account')
        string(name: 'ami_name', defaultValue: 'AIO_Test01_Veera', description: 'ami sharing target account')
    }
    stages {
        stage('Cloning Git') {
         steps {
             git branch: 'main', url: 'https://github.com/GarudaIsmail/pythonprojects.git'
         }
       }
        stage('Connecting To Aws') {
            steps {
                //sh(
                  //  script: "python3 ${env.WORKSPACE}/bin/s3bucket.py '${params.JOB_NAME}' 2>&1",
                    //returnStdout: true
                //)
                sh "chmod +x ${env.WORKSPACE}/shell/config.sh"
                sh "${env.WORKSPACE}/shell/config.sh '${params.AccountId}' '${params.RoleName}' '${params.region}' '${params.trg_accountid}' '${params.ami_name}'"
                // sh "aws sts get-caller-identity"
            }
        }
    }
}
