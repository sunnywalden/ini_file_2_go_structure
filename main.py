#!python3
# Author: sunnywalden@gmail.com


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


if __name__ == '__main__':
    conf_path = "./confs/demo.ini"

    f = open(conf_path, "r")
    secrets_list = f.readlines()

    for i in range(0, len(secrets_list)):
        secret_info = secrets_list[i]
        secret_name = secret_info.split(" = ")[0]

        if secret_name.isspace() or secret_name == "" or secret_name == " ":
            continue

        golang_param_name = "".join(list(map(str.capitalize, secret_name.split("_"))))

        print(golang_param_name + " string `ini:" + '"' + secret_name + '"`')

