FROM python:3.11
ADD test .
RUN pip install requests pytest pytest-html
CMD ["pytest", "./test_hello.py", "-rA", "--html", "report.html"]
