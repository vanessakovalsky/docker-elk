from flask import Flask
app = Flask(__name__)

import logging
import logstash
import sys

HOST = 'logstash'

app.test_logger = logging.getLogger('python-logstash-logger')
app.test_logger.setLevel(logging.INFO)
app.test_logger.addHandler(logstash.LogstashHandler(HOST, 5959, version=1))


@app.route('/')
def hello_world():
    app.test_logger.info("Hello there")
    return 'Hello, World!'

app.run(host='0.0.0.0', port=5555)