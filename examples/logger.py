import streambox as sb
import time


@sb.decorators.logger
def run_my_function(result):
    print("Function started")
    time.sleep(2)
    return result


def main():
    result_1 = run_my_function(5)
    print("Result: ", result_1)


if __name__ == '__main__':
    main()
