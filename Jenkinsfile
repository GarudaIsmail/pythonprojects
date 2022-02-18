pipeline {
    agent any

    parameters {
        string(name: 'rolename', defaultValue: 'jenkins_role', description: 'Workspace/environment file to use for deployment')
        string(name: 'accountid', defaultValue: '941039889978', description: 'accountid variable to pass to Terraform')
        string(name: 'region', defaultValue: 'ap-south-1', description: 'region variable to pass to Terraform')
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
                sh "${env.WORKSPACE}/shell/config.sh '${params.accountid}' '${params.rolename}' '${params.region}'"
                // sh "aws sts get-caller-identity"
            }
        }
    }
}
