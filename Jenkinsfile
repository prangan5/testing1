@Library('vaptshield-lib') _

// VAPTShield security scan — shared library handles the scanner container.
// api: point at your VAPTShield deployment (here: the demo dev server).
pipeline {{
  agent any
  stages {{
    stage('Checkout') {{
      steps {{ checkout scm }}
    }}
    stage('VAPT Shield Scan') {{
      steps {{
        vapt(
          repoUrl: 'https://github.com/prangan5/testing1.git',
          branch: 'main',
          credentialId: 'vaptshield-ci-token',
          api: 'http://10.0.4.92:3000'
        )
      }}
    }}
  }}
}}
