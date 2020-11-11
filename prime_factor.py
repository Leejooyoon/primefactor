from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def get_largest_prime_factor():
    num = int(request.args.get("input", ""))
    largest_prime_factor = rtn_largest_prime_factor(num)
    return str(largest_prime_factor)


def rtn_largest_prime_factor(num):
    if num > 1:
        pf = [1]
        for i in range(2, num + 1):

            while num % i == 0:
                size = len(pf)
                num /= i
                pf.append(i)
                i = i + 1
        return pf[size]

    else:
        if num == 1:
            return 1

        else:
            return "Invalid input number. Please try again"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)