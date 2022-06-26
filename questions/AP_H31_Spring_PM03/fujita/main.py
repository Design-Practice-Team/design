import pprint
import logging

from src.controller import Controller

def main():
    try:
        # 注文処理の開始
        ctl = Controller()
        ctl.run()
    except Exception as e:
        logging.exception(e)

if __name__ == "__main__":
    main()