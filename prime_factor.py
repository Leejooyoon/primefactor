from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def get_largest_prime_factor(): # 주소창에서 값을 받아와 num 변수에 저장해주는 함수
    num = int(request.args.get("input", ""))  # input= 으로 값을 받아올 수 있게 해줌
    largest_prime_factor = rtn_largest_prime_factor(num)
    return str(largest_prime_factor)


def rtn_largest_prime_factor(num):  # prime factor 를 구하기 위한 함수
    if num > 1:
        pf = []  # 소인수들을 넣을 배열을 만든다
        for i in range(2, num + 1):

            while num % i == 0:  # 2부터 num 까지 모든 수 중에서 나머지가 0인지를 확인하여 소인수를 구별
                size = len(pf)
                num /= i
                pf.append(i)
                i = i + 1
        return pf[size]  # 가장 마지막 소인수 즉 가장 큰 소인수를 return 함

    else:
        if num == 1:
            return 1  # 1인경우에는 1이 가장 큰 소인수므로 1을 return

        else:
            return "Invalid input number. Please try again"  # 그 이외의 숫자는 연산불가능하므로 메시지 출력


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)   # 모든 ip 에서 접속 가능하게 하고 포트는 8080번으로 지정하였습니다.
