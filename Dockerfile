FROM gcr.io/distroless/python3
LABEL maintainer="coolek8@gmail.com"
ADD src/Converter_USD-RUB.py /
ENTRYPOINT ["python3", "Converter_USD-RUB.py"]
EXPOSE 80