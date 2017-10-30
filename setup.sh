cd /Users/emretekinalp/PycharmProjects/MayaPrototypeTool
coverage run test.py
coverage xml
python-codacy-coverage --r coverage.xml

exit 0