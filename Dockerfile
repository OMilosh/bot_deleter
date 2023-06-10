FROM python:latest

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade pip && pip install -r requirements.txt

WORKDIR /app

COPY  bot_log.log bot.py ./ 

CMD [ "python3", "bot.py" ]