pipeline {
    agent any
    environment {
        DATABASE_URI = credentials("DATABASE_URI")
        SECRET_KEY = credentials("SECRET_KEY")

    }

    stages {
        stage('Test') {
            steps {
                // steps here
                sh 'bash Jenkins/run-tests.sh'
            }
        }
        stage('Build-Push') {
            steps {
            sh 'bash Jenkins/build-push.sh'

            }
        }
        stage('Ansible') {
            steps {
                // steps here
            }
        }
        stage('Run') {
            steps {
                // steps here
                sh 'bash Jenkins/deploy.sh'
            }
        }
    }
    post {
        always{
            junit "junit/*.xml"
            cobertura coberturaReportFile: 'coverage.xml', failNoReports:false
        }
    }

}