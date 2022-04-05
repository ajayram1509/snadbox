import json
from flask import Flask, request, jsonify
from .utils import start_compile
app = Flask(__name__)


@app.route('/', methods=['POST'])
def update_record():
    payload = json.loads(request.data)
    exec_type = payload['exec_type']
    file = request.files['file']
    filename  = file.name
    box_id = 10
    response = start_compile(exec_type, file, filename, box_id)
    # with open('/tmp/data.txt', 'w') as f:
    #     f.write(json.dumps(new_records, indent=2))
    return jsonify(response)

app.run(debug=True)