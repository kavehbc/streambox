import streambox as sb


@sb.decorators.cache
def run_my_function(result, _check=False):
    print("Print from inside function only runs the first time")
    return result


def main():
    print("Starting...")
    a = 5
    result_1 = run_my_function(a, _check=True)
    print("Result: ", result_1)

    result_2 = run_my_function(a, _check=False)
    print("Next Result: ", result_2)


if __name__ == '__main__':
    main()
