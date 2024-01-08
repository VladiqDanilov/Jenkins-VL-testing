pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(
                    branches: [[name: '*main']],   // извлечение из gut (в данном случае, Jenkins должен использовать любую ветку, которая имеет в своем названии main)
                    extensions: [],                 // Расширения ( предпроцесс извлечения кода из git)
                    userRemoteConfigs: [[url: 'https://github.com/VladiqDanilov/Jenkins-VL-testing.git']] // Конфигурация удаленного репозитория
                )
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
