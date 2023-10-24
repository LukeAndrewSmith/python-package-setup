from a_package.a_script.args import get_args
import logging
import coloredlogs

coloredlogs.install(level=logging.INFO)


def say_hello():
    cfg = get_args()
    print("Hello: this is a command line script")
    if cfg.int_to_print > 0:
        logging.info("Processing user input")
        print(f"You asked me to print: {cfg.int_to_print}")
