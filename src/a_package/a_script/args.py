from argparse import ArgumentParser


def get_args():
    parser = ArgumentParser()

    ###########################################################################
    # Argument group
    ###########################################################################
    parser.add_argument(
        "--int-to-print",
        "-i",
        dest="int_to_print",
        default=0,
        type=int,
        help="The int that the script will print",
    )

    cfg = parser.parse_args()
    return cfg
