pipeline {
    agent any

    environment {
        IMAGE = "aaryanantala/cli_calculator:jenkins"
        VENV = ".venv"
        PYTHON = "/usr/bin/python3"
        PATH = "/usr/local/bin:${env.PATH}"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM',
                  branches: [[name: '*/main']],
                  userRemoteConfigs: [[
                    url: 'https://github.com/AaryanAntala/cli_calculator.git',
                    credentialsId: 'cli_calc_creds'
                  ]]
                ])
            }
        }

        stage('Create Virtual Environment') {
            steps {
                sh '$PYTHON -m venv $VENV'
                sh '$VENV/bin/pip install --upgrade pip'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '$VENV/bin/pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh '$VENV/bin/pytest -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE .'
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker_creds',
                                                  usernameVariable: 'USER',
                                                  passwordVariable: 'PASS')]) {
                    sh '''
                      echo $PASS | docker login -u $USER --password-stdin
                      docker push $IMAGE
                    '''
                }
            }
        }


        stage('Deploy Container') {
            steps {
                sh '''
                  docker pull $IMAGE
                  # Stop and remove any existing container with the same name
                  docker stop cli_calculator 2>/dev/null || true
                  docker rm cli_calculator 2>/dev/null || true
                  # Stop any container using port 5000
                  docker ps -q --filter "publish=5000" | xargs -r docker stop
                  docker ps -aq --filter "publish=5000" | xargs -r docker rm
                  # Run the new container
                  docker run -d -p 5000:5000 --name cli_calculator $IMAGE
                '''
            }
        }
    }
}
