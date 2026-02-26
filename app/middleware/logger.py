from flask import request
import time
import logging


def request_logger(app):

    logging.basicConfig(level=logging.INFO)

    @app.before_request
    def before_request():
        request.start_time = time.time()

        logging.info(
            f"[REQUEST] {request.method} {request.path}"
        )

    @app.after_request
    def after_request(response):

        duration = time.time() - request.start_time

        logging.info(
            f"[RESPONSE] {request.method} {request.path} "
            f"Status={response.status_code} "
            f"Time={duration:.3f}s"
        )

        return response
