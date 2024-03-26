FROM python:3.10-slim

COPY test.py /test.py
CMD [ "python", "/test.py"]
