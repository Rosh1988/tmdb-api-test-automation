FROM python:3.11
ADD test .
ADD .env .
RUN pip install requests pytest pytest-html python-dotenv
CMD ["pytest", "./test_movie.py", "-rA", "--html", "report.html"]
