import os
import sys
import logging
import fire


logging.basicConfig(stream=sys.stderr, level=logging.INFO)
logger = logging.getLogger()

def main():
    logger.info("Start processing")
    logger.info("Done.")


def main_script():
    fire.Fire(main)

if __name__ == "__main__":
    fire.Fire(main)