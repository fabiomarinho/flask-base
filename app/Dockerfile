FROM python:3.6.1-alpine
RUN pip install --upgrade pip
ADD requirements.txt requirements.txt
RUN pip install -r "requirements.txt"
EXPOSE 5000
CMD ["python","/app/app.py"]