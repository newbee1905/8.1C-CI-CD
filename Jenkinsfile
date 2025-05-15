pipeline {
	agent any

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
		}

		stage('Code Analysis') {
			steps {
				sh 'uv run flake8 . --max-line-length=88 || true'
			}
		}

		stage('Security Scan') {
			steps {
				sh 'uv run pip-audit || true'
			}
		}

		stage('Deploy to Staging') {
			steps {
				echo 'Deploy to Staging'
			}
		}

		stage('Integration Tests on Staging') {
			steps {
				echo 'Integration Tests on Staging'
			}
		}

		stage('Deploy to Production') {
			steps {
				echo 'Deploy to Production'
			}
		}
	}
}

