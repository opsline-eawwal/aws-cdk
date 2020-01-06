from flask import Flask
from rds_cdk import core, MyTestStack

app = Flask(__name__)

@app.route('/')
def helloIndex():
    return 'Hello Infra Launcher'

@app.route('/launchStack')
def synthRDS():
    app = core.App(outdir='outputDir')
    MyTestStack(app, "cdkTest")
    app.synth()
    return 'Done'

