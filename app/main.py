from flask import Flask, request
import glob
import json
import sys
import importlib


app = Flask(__name__)




# Setup redirect and hosting of frontend

@app.route('/')
def base():
    return "SAT"

@app.route('/plugins')
def list_plugins():
    plugin_dirss = [i.split('/')[-2] for i in glob.glob("/app/plugins/*/", recursive=False)]
    return json.dumps(plugin_dirs)

@app.route('/plugins/<path:plugin>')
def list_plugin_features(plugin):
    features = [i.split('/')[-1].split('.')[-2] for i in glob.glob("/app/plugins/{}/*.py".format(plugin), recursive=False)]
    return json.dumps(features)

@app.route('/plugins/<path:plugin>/<path:feature>')
def exec_feature(plugin,feature):
    data=request.args.get('data')
    mod = importlib.import_module('plugins.{}.{}'.format(plugin,feature))
    return mod.run(data)



if __name__ == '__main__':
    app.debug = True
    app.run(port=8080, host="0.0.0.0")
