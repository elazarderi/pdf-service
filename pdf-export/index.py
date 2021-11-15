import logging 
import pdfkit
import json
from sys import platform
import os
from flask import Flask, send_file, request, after_this_request
import time 

logging.basicConfig(level=logging.INFO)
app = Flask(__name__)
pdfkit_config=pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe' if platform == 'win32' else '/usr/local/bin/wkhtmltopdf')


@app.errorhandler(Exception)
def server_error(err):
    app.logger.exception(err)
    return "exception", 500

@app.route("/itay", methods=['GET'])
def hello():
    return "Hello, World!"

@app.route("/writer", methods=['POST'])
def writer_to_pdf():
    logging.info('new request')
    try:
        logging.info('pdfkit config works')

        file_content = get_data(request.data)["file"]
        file_name = get_file_name(get_data(request.data))

        address_pdf = file_name + ".pdf"

        pdfkit.from_string(file_content, address_pdf, configuration=pdfkit_config)

        @after_this_request
        def clean_file(response):
            try:
                os.remove(address_pdf)
                logging.info('File Deleted Successfully')
            except:
                logging.error("Unable to delete file", address_pdf)
            finally:
                return response

        return send_file(address_pdf, as_attachment=True)

    except SystemError:
        raise Exception(SystemError)


def get_data(data):
    return json.loads(data.decode('utf-8'))

def get_file_name(data):
    return data["fileName"] if data['fileName'] else 'output'


if __name__ == '__main__': 
    app.run(port=3001, debug=True, host='0.0.0.0')



