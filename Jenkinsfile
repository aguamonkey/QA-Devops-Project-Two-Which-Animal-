pipeline {
    agent any
    environment {
        DATABASE_URI = credentials("DATABASE_URI")
        SECRET_KEY = credentials("SECRET_KEY")
        username = credentials("USERNAME")
        password = credentials("PASSWORD")

    }

    stages {
        stage('Test') {
            steps {
                // steps here
                sh 'bash Jenkins/run-tests.sh'
            }
        }
        stage('Build') {
            steps {
                sh 'docker-compose build --parallel'
                sh 'docker login -u ${username} -p ${password}'
            }
        }
        stage('Push') {
            steps {
                
                sh 'docker-compose push'

            }
        }
        stage('Run') {
            steps {
                // steps here
                sh 'bash Jenkins/deploy.sh'
            }
        }
    
    post {
        always{
            junit "junit/*.xml"
            cobertura coberturaReportFile: 'coverage.xml', failNoReports:false
        }
    }

}