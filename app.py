from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/')
def homepage():
    """This route returns some HTML."""
    return '''
    <h1>This is the home page</h1>
    <p>The homepage here responds to <code>GET</code> requests by default. The <code>/hallo</code> route responds only to <code>POST</code> requests, so you can make one with JavaScript by using the form below.</p>
    <form id="nameForm">
        <input type="text" id="name" placeholder="Enter your name here...">
        <input type="submit" value="Submit Form">
    </form>
    <div id="outputArea" style="color: green; font-weight: bold;"></div>
    <script>
        document.addEventListener('DOMContentLoaded', function () {
            console.log('loaded');
            var form = document.getElementById('nameForm');
            form.addEventListener('submit', function (e) {
                e.preventDefault();
                var postData = {
                    name: document.getElementById('name').value
                };

                fetch('/hallo', {
                    method: 'POST',
                    body: JSON.stringify(postData)

                })
                    .then(res => res.json())
                    .then(json => {
                        console.log(json)
                        var outputArea = document.getElementById('outputArea');
                        outputArea.innerHTML = json.greetings;
                    })
                    .catch(err => console.log('err', err));
            });
        });

    </script>
    '''


@app.route("/hallo", methods=['POST'])
def hallo():
    """This route only responds to POST requests."""
    message = request.get_json(force=True)

    name = message['name']
    response = {
        'greetings':'Hallo ' + name + "!"
    }
    print('sending to frontend: {}'.format(response))
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
