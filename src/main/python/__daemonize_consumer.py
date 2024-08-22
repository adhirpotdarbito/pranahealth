import daemon
from __consumer import ConsumeData

if __name__ == "__main__":
    with daemon.DaemonContext():
        consume_data = ConsumeData()
        consume_data.consumeUserData()

