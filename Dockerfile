FROM python
EXPOSE 8082
WORKDIR /maorweb/code
COPY . .
RUN pip install -r requirements.txt
CMD ["python","frontend.py"]
