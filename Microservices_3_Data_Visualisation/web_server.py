from concurrent import futures
import logging
import math
import time

import grpc
import data_stream_pb2
import data_stream_pb2_grpc

from datetime import datetime

from flask import Flask, render_template

analytics = []

app = Flask(__name__)
@app.route('/')
def render_homepage():
    return render_template("homepage.html", data = analytics)


class dataStreamServicer(data_stream_pb2_grpc.dataStreamServicer):

    def SendOneFeature(self, request, context):

        global analytics

        # print("Total Number of Must-Play Titles per Video Game Platform (incl. all home consoles)", getattr(request, 'analytic1'))
        # print("Lowest scoring metacritic game of all time:", getattr(request, 'analytic2'))
        # print("Most Loved Genre per Video Game Platform (incl. all home consoles)", getattr(request, 'analytic3'))
        # print("Average metascore of First-Party Titles (incl. all home consoles)", getattr(request, 'analytic4'))
        # print("Current Date:", getattr(request, 'date'))

        analytics = [getattr(request, 'analytic1'), getattr(request, 'analytic2'),
        getattr(request, 'analytic3'), getattr(request, 'analytic4'),
        getattr(request, 'date'), getattr(request, 'analytic4a'),
        getattr(request, 'analytic4b'), getattr(request, 'analytic4c')]






        return data_stream_pb2.HelloRequest(name="1")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    data_stream_pb2_grpc.add_dataStreamServicer_to_server(dataStreamServicer(), server)
    server.add_insecure_port('[::]:40051')
    server.start()

    app.run(host='0.0.0.0')

    server.wait_for_termination()



if __name__ == '__main__':
    logging.basicConfig()
    serve()
