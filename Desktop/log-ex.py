import logging
import sys
logging.basicConfig(filename="file1",filemode='a',format='%(asctime)s- %(message)s',level=logging.INFO or logging.ERROR)
num1=sys.argv[1]
num=int(num1)
try:
    if num>0:
        print(num)
        logging.info("done")
    else:
        logging.error("invalid")
        raise Exception("invalid output")

finally:
    print("finished")