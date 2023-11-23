pipeline {
    agent any

    stages {
        stage('Starting') {
            steps {
                echo 'Starting App'
            }
        }

        stage('Test') {
            steps {
                echo 'Testing'
            }
        }

        stage('Deploy') {
                    steps {
                        echo 'Deploy App'
                    }
                }

        stage('Hello') {
            steps {
                echo 'Hello World'
            }
        }
    }
    post{
        failure
        {
            sleep 2
            echo 'Building failure'
        }
    }
}
