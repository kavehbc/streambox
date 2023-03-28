import streambox as sb


@sb.decorators.retry(max_tries=5, delay_seconds=None)
def run_my_function(result):
    print("Function started")
    raise Exception("This is a custom error!")
    return result


def main():
    result_1 = run_my_function(5)
    print("Result: ", result_1)


if __name__ == '__main__':
    main()
