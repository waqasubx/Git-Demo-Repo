#!groovy

pipeline {
    agent any
    stages {
        stage('Checkout')
        {
            GitManager.clone(this, "https://github.com/waqasubx/Git-Demo-Repo.git", "*/main", "waqasubx");
        }
        stage('Hello') {
            steps {
                echo 'Hello World'
            }
        }
    }
}
