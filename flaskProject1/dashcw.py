import time
import dash
import dash_html_components as html
from dash.dependencies import Input, Output, State
import boto3
from datetime import datetime
from datetime import timedelta
import pandas as pd


def initialize_client():
        client = boto3.client(
            'cloudwatch',
            aws_access_key_id='ASIARCQRXBNDZ7SYB6ZI',
            aws_secret_access_key = 'ZXSMqOHtwBV5ijKY7Wgbd+KGGJ1f/AfeeNuHYJI8',
            aws_session_token = 'FwoGZXIvYXdzEGcaDOuCzt3QAa+R0Wu4jCLMAazhii0UCuv8IJNHkIzLBeynV8JjHTjTvt9Rz6DJELRm3VNQ+26INw+8RKTEx1YesQzBam3pgf7eFhpc4WanxFjoqDqY9Sqe/wU/YXVD5+rtpnqO/b1TjAHmED5aYZL7L+yRZ3z74TnnUZXsQeKblWtTXg8ye7AweINQnYT13z71EpGdeGiG4CmZZ/8ox7QxvhSyz9YuVSCahXXq0oqecVtRK3KGG84R96Hs5Mb0axrl5ssVEqOfC5EsclmWHULx7zM+qw/PuOoscFa9kSig74H9BTItvX+GZyCY2gg7jTom/n+5AnnlSidyXyG9Alj11xAODosYzz4PzHXpPwnaXk3W',
            region_name = 'us-east-1'
        )
        return client


def request_metric(client):
    response = client.get_metric_statistics(
        Namespace='AWS/EC2',
        Period=120,
        StartTime=datetime.utcnow() - timedelta(seconds=600),
        EndTime=datetime.utcnow(),
        MetricName='CPUUtilization',
        Statistics=['Average'],
        Dimensions=[
            {
                'Name': 'InstanceId',
                'Value': 'i-03c209c324dfd72f0'
            }
        ],
    )

    return response


def request_metricNI(client):
    response_ni = client.get_metric_statistics(
        Namespace='AWS/EC2',
        Period=120,
        StartTime=datetime.utcnow() - timedelta(seconds=600),
        EndTime=datetime.utcnow(),
        MetricName='NetworkIn',
        Statistics=['Average'],
        Dimensions=[
            {
                'Name': 'InstanceId',
                'Value': 'i-03c209c324dfd72f0'
            }
        ],
    )

    return response_ni


def request_metricNO(client):
    response_no = client.get_metric_statistics(
        Namespace='AWS/EC2',
        Period=120,
        StartTime=datetime.utcnow() - timedelta(seconds=600),
        EndTime=datetime.utcnow(),
        MetricName='NetworkOut',
        Statistics=['Average'],
        Dimensions=[
            {
                'Name': 'InstanceId',
                'Value': 'i-03c209c324dfd72f0'

            }
        ],
    )

    return response_no

##################################################################################



def request_metricpc2(client):
    response = client.get_metric_statistics(
        Namespace='AWS/EC2',
        Period=120,
        StartTime=datetime.utcnow() - timedelta(seconds=600),
        EndTime=datetime.utcnow(),
        MetricName='CPUUtilization',
        Statistics=['Average'],
        Dimensions=[
            {
                'Name': 'InstanceId',
                'Value': 'i-087f989840783a9ad'
            }
        ],
    )

    return response


def request_metricNIpc2(client):
    response_ni = client.get_metric_statistics(
        Namespace='AWS/EC2',
        Period=120,
        StartTime=datetime.utcnow() - timedelta(seconds=600),
        EndTime=datetime.utcnow(),
        MetricName='NetworkIn',
        Statistics=['Average'],
        Dimensions=[
            {
                'Name': 'InstanceId',
                'Value': 'i-087f989840783a9ad'
            }
        ],
    )

    return response_ni


def request_metricNOpc2(client):
    response_no = client.get_metric_statistics(
        Namespace='AWS/EC2',
        Period=120,
        StartTime=datetime.utcnow() - timedelta(seconds=600),
        EndTime=datetime.utcnow(),
        MetricName='NetworkOut',
        Statistics=['Average'],
        Dimensions=[
            {
                'Name': 'InstanceId',
                'Value': 'i-087f989840783a9ad'

            }
        ],
    )

    return response_no

#########################################################################################

app = dash.Dash(external_stylesheets=['<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap" rel="stylesheet">'])
app.layout = html.Div(
    [
        html.Button("PC WYLLIS", id="button_3"),
        html.Div(children="CPU", id="CPU"),
        html.Div(children="NET IN", id="NET IN"),
        html.Div(children="NET OUT", id="NET OUT"),

        html.Button( "PC MARCUS", id="button_4" ),
        html.Div(children="CPU2", id="CPU2"),
        html.Div(children="NET IN2", id="NET IN2"),
        html.Div(children="NET OUT2", id="NET OUT2"),
    ]
)


@app.callback(
    Output("CPU", "children"),
    [Input("button_3", "n_clicks")])
def first_callback(a):
    while True:
        time.sleep( 5 )
        client = initialize_client()
        response = request_metric( client )
        dfa = pd.DataFrame( response['Datapoints'] )
        return dfa["Average"].values[0], " ", dfa["Unit"].values[0]


@app.callback(
    Output( "NET IN", "children" ),
    [Input( "button_3", "n_clicks" )] )
def second_callback(b):
    while True:
        time.sleep( 5 )
        client = initialize_client()
        response_ni = request_metricNI( client )
        dfb = pd.DataFrame(response_ni['Datapoints'])
        return dfb["Average"].values[0], " ", dfb["Unit"].values[0]


@app.callback(
    Output( "NET OUT", "children" ),
    [Input( "button_3", "n_clicks" )] )
def third_callback(c):
    while True:
        time.sleep( 5 )
        client = initialize_client()
        response_no= request_metricNO(client)
        df = pd.DataFrame( response_no['Datapoints'] )
        return  df["Average"].values[0], " ", df["Unit"].values[0]


#########################################################################################################


@app.callback(
    Output("CPU2", "children"),
    [Input("button_4", "n_clicks")])
def first_callback(a):
    while True:
        time.sleep( 5 )
        client = initialize_client()
        response = request_metricpc2( client )
        dfa = pd.DataFrame( response['Datapoints'] )
        return  dfa["Average"].values[0], " ", dfa["Unit"].values[0]


@app.callback(
    Output( "NET IN2", "children" ),
    [Input( "button_4", "n_clicks" )] )
def second_callback(b):
    while True:
        time.sleep( 5 )
        client = initialize_client()
        response_ni = request_metricNIpc2( client )
        dfb = pd.DataFrame(response_ni['Datapoints'])
        return dfb["Average"].values[0], " ", dfb["Unit"].values[0]


@app.callback(
    Output( "NET OUT2", "children" ),
    [Input( "button_4", "n_clicks" )] )
def third_callback(c):
    while True:
        time.sleep( 5 )
        client = initialize_client()
        response_no= request_metricNOpc2(client)
        df = pd.DataFrame( response_no['Datapoints'] )
        return  df["Average"].values[0], " ", df["Unit"].values[0]



if __name__ == '__main__':
    app.run_server( debug=True, port=8055 )
