# python_test_coverage sends to sonarqube
# pytest tool Installation
```
pip3 install pytest
```

# coverage tool Installation

```
pip3 install coverage
```

# clone the code
```
 git clone https://github.com/chaithanya1812/python_test_coverage.git
```
# get into inside the directory
```
cd python_test_coverage
```
# Running test-cases
```
 pytest
  or
pytest main_test.py
```
![image](https://github.com/chaithanya1812/python_test_coverage/assets/111736742/e75d81fe-f430-4830-b6a6-1739658ce27c)

# Doing code-coverage  
```
coverage run  main_test.py
```

# To see code-coverage report 
```
coverage report
```
![image](https://github.com/chaithanya1812/python_test_coverage/assets/111736742/c1d40def-4626-4f01-baad-aa0a58e32e13)

# converting code-coverage report to xml,so that sonarqube will detect of code-coverage percentage
```
coverage xml
```
# Open the file [ sonar-project.properties ] & modify the below content.
```
sonar.host.url=http://54.157.52.52:9000/  ----> Replace with your url
sonar.projectKey=my-project
sonar.python.coverage.reportPaths=coverage.xml
sonar.login=admin                        ---> Replace the login name
sonar.password=12345                     ---> Replace the login password 
```

# Finally run sonar-scanner coomad
```
sonar-scanner
```

![image](https://github.com/chaithanya1812/python_test_coverage/assets/111736742/bf53525e-262b-4982-9d33-ff0a0e096a26)




