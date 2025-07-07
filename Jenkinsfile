pipeline {
    agent any

    environment { VENV = 'venv' }

    stages {
        stage('Checkout') {
            steps { git url: 'https://github.com/rjabeen04/new_python_jenkins_project.git', branch: 'main' }
        }
        stage('Setup Env') {
            steps {
                sh 'python3 -m venv $VENV'
                sh '. $VENV/bin/activate && pip install --upgrade pip'
            }
        }
        stage('Install Dependencies') {
            steps { sh '. $VENV/bin/activate && pip install -r requirements.txt' }
        }
        stage('Lint') {
            steps { sh '. $VENV/bin/activate && flake8 my_app || true' }
        }
        stage('Run Tests') {
            steps { sh '. $VENV/bin/activate && pytest my_app_tests --junitxml=tests-results.xml' }
        }
        stage('Coverage') {
            steps { sh '. $VENV/bin/activate && pytest --cov=my_app --cov-report=xml' }
        }
        stage('Publish') {
            steps {
                junit 'tests-results.xml'
                cobertura coberturaReportFile: 'coverage.xml'
            }
        }
    }

    post {
        success { echo 'Build succeeded!' }
        failure { echo 'Build failed!' }
    }
}
