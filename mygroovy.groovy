#!groovy

// pipeline {
//     agent any
//     stages {
//         stage('Hello') {
//             steps {
//                 echo 'Hello World from mygroovy.groovy'
//             }
//         }
//     }
// }
def example1() {
  println 'Hello from example1'
}

def example2() {
  println 'Hello from example2'
}

return this
