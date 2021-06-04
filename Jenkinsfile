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
        stage('Ansible') {
            steps{
                
                sh 'bash Jenkins/run-ansible.sh'
                sh 'ansible-playbook -i ansible/configure-swarm/inventory.yaml ansible/configure-swarm/playbook.yaml --extra-vars "ansible_sudo_pass="'
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