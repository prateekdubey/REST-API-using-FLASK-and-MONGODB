FROM python:3
COPY requirements.txt .
RUN pip3 install  -r requirements.txt
COPY . .
ENV PORT 5000
EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD ["run.py"]

