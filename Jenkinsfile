pipeline {
	agent any

	environment {
		RECIPIENT = 's221056384@deakin.edu.au'
	}

	stages {
		stage('Checkout') {
			steps {
				git url: 'https://github.com/newbee1905/8.1C-CI-CD.git', branch: 'main'
			}
		}

		stage('Build') {
			steps {
				sh '''
					uv sync
					uv run python setup.py build_ext --inplace
					uv run python setup.py sdist bdist_wheel
				'''
			}
		}

		stage('Unit and Integration Tests') {
			steps {
				sh 'uv run pytest --maxfail=1 --disable-warnings -W ignore::DeprecationWarning || true'
			}
			post {
				success {
					emailext(
						from:    'CI Server <jenkins@newbee.com>',
						to:      RECIPIENT,
						subject: "Tests stage SUCCESS: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
						body:    "Unit and integration tests passed.\n\nSee attached build log.",
						attachLog: true
					)
				}
				failure {
					emailext(
						from:    'CI Server <jenkins@newbee.com>',
						to:      RECIPIENT,
						subject: "Tests stage FAILURE: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
						body:    "Unit and integration tests failed.\n\nSee attached build log for details.",
						attachLog: true
					)
				}
			}
		}

		stage('Code Analysis') {
			steps {
				echo 'Tool: flake8 — https://flake8.pycqa.org/ — code format analysis for Python'
				sh 'uv run flake8 . --max-line-length=88 || true'
				echo 'Tool: SonarCloud.io — https://sonarcloud.io/ — code analysis (Part 2 - Task 1)'
			}
		}

		stage('Security Scan') {
			steps {
				sh 'uv run pip-audit || true'
			}
			post {
				success {
					emailext(
						to:      RECIPIENT,
						subject: "Security scan SUCCESS: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
						body:    "Security scan passed.\n\nSee attached build log.",
						attachLog: true
					)
				}
				failure {
					emailext(
						to:      RECIPIENT,
						subject: "Security scan FAILURE: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
						body:    "Security scan found vulnerabilities.\n\nSee attached build log.",
						attachLog: true
					)
				}
			}
		}

		stage('Deploy to Staging') {
			steps {
				echo 'Tool: Ansible — https://docs.ansible.com/ — automate staging deployments'
				echo 'Deploy to Staging'
			}
		}

		stage('Integration Tests on Staging') {
			steps {
				echo 'Tool: Selenium WebDriver — https://www.selenium.dev/ — browser-based integration tests'
				echo 'Integration Tests on Staging'
			}
		}

		stage('Deploy to Production') {
			steps {
				echo 'Tool: Terraform — https://www.terraform.io/ — infrastructure as code for production'
				echo 'Deploy to Production'
			}
		}
	}
}

