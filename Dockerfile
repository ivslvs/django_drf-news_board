FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN mkdir /news_board
WORKDIR /news_board

ADD requirements.txt /news_board/
RUN pip install -r requirements.txt

ADD . /news_board/

ENV PORT=8000

CMD gunicorn news_board.wsgi:application --bind 0.0.0.0:$PORT