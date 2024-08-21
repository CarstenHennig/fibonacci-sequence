from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        input_end = int(request.form.get('inputEnd'))
        result = your_python_function(input_end)
    return render_template('index.html', result=result)

def your_python_function(inputEnd):
    fibonacci_sequence = [0, 1]

    while fibonacci_sequence[-1] < inputEnd:
        fib_added = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        if fib_added >= inputEnd:
            break
        fibonacci_sequence.append(fib_added)

    return ', '.join(map(str, fibonacci_sequence))

if __name__ == '__main__':
    app.run(debug=True)
