from itertools import zip_longest

def check_arg(p, str_):
    return isinstance(p, str) and p[:len(str_)] == str_ and (p[len(str_)].isupper() or ('0' <= p[len(str_)] <= '9'))

def getFilterList(arg, str_):
    return [p for p in arg if check_arg(p, str_)]

def getPairList(cables, sockets):
    return [[p, s] for [p, s] in zip(getFilterList(cables, "cable"), getFilterList(sockets,"socket"))]

def createAllValidParam(plugs, sockets, cables):
    return [p for p in zip_longest(getPairList(cables, sockets), getFilterList(plugs, "plug"))]

def fix_wiring(plugs, sockets, cables):
    return ["plug " + p[0][0] + " into " + p[0][1] + " using " + p[1] if p[1]
            else "weld " + p[0][0] + " to " + p[0][1] + " without plug"
            for p in createAllValidParam(plugs, sockets, cables) if p[0]]

def main():
    plugs = ['plug1', 'plug2', 'plug3']
    sockets = ['socket1', 'socket2']
    cables = ['cable1', 'cable2']
    for c in fix_wiring(plugs, sockets, cables):
        print(c)

if __name__ == "__main__":
    main()