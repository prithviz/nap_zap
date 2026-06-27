FROM python:3.8

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN python -m nltk.downloader stopwords punkt wordnet

COPY . .

EXPOSE 8080

CMD ["python", "./web_ui.py"]