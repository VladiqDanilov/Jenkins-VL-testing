pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/VladiqDanilov/Jenkins-VL-testing.git']])
            }
        }
        stage('Run') {
            steps {
                git branch: 'main', url: 'https://github.com/VladiqDanilov/Jenkins-VL-testing.git'
                sh 'python3 ops.py'
            }
        }
        stage('Test'){
            steps{
                sh 'python3 -m pytest'
            }
        }
    }
}
