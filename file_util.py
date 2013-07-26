def getChannels():
    with open("channels") as f:
        return f.read().split();

