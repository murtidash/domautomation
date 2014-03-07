

def findgameprocess(gg):
    processes = check_output(['ps','ax']).splitlines()
    prore = ".*?dom4.*?%s"
    for pro in processes:
        mo = re.search(prore % gg.servername,pro)
        if mo:
            return pro
    return None


def killgame(game):
    processline = findgameprocess(game)
    if not processline:
        return None
    pidre =



