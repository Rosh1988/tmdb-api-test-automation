FROM python:3.11
ADD tests .
RUN pip install requests pytest pytest-html
CMD ["pytest", "./test_movie.py", "-rA", "--html", "report.html"]
