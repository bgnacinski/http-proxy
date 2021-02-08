FROM python:3.8.5
WORKDIR /root/proxy/

EXPOSE 1080

COPY . .
CMD ["python3", "proxy.py"]
