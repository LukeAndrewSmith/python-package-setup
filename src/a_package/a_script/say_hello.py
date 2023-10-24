from a_package.a_script.args import get_args


def say_hello():
    cfg = get_args()
    print("Hello: this is a command line script")
    if cfg.int_to_print > 0:
        print(f"You asked me to print: {cfg.int_to_print}")
        print("Why would you do such a thing?")
