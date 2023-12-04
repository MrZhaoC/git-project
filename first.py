def get_info():
    print('aaaaa')


def print_info():
    print('head of get_info')
    get_info()


if __name__ == '__main__':
    print_info()
