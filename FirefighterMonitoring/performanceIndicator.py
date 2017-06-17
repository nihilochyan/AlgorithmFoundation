
class Indicator(object):
    def __init__(self, *args):
        # movement activity = 1/N*Sigma(1,N){acceleration magnitude > T}
        # T was learned from the movement data using a two component Gaussian Mixture Model.
        self.movementactivity = args[0]
        # given by the median of the absolute linear acceleration magnitude
        self.movementintensity = args[1]
        # is given by the inter-quartile-range of the absolute linear acceleration magnitude.
        self.movementvariability = args[2]
        # use the long-term-spectral variability (LTSV)
        self.speechactivity = args[3]
        # phase = preparation, execution, complete training
        self.phase = args[4]


def calcuActivity(list, t):
    """
    calculate movement activity
    :param list: list of sliding standard deviation of acceleration magnitude
    :param t: threshold learned from the movement data using a two component Gaussian Mixture Model.
    :return: movement activity
    """
    a = 0
    for i in list:
        if i > t:
            a += 1
    b = a/len(list)
    return b


def calcuIntensity(list):
    """
    calculate movement intensity
    :param list: list of linear acceleration magnitude
    :return: median of the absolute linear acceleration magnitude.
    """
    b = list.sorted()
    if len(list)%2 == 0:
        median = (list[len(list)/2]+list[len(list)/2-1])/2
    else:
        median = list[int(len(list)/2)]
    return median


def calcuVariablity(list):
    """
    calculate movement variability
    :param list:   len(list)>12   absolute linear acceleration magnitude
    :return: inter-quartile-range of the absolute linear acceleration magnitude
    """
    list2 = list.sorted()
    a = len(list)/4
    b = 3*len(list)/4
    q1 = list2[int(a)] + (a-int(a))(list2[int(a+2)] - list2[int(a)+1])
    q3 = list2[int(b)] + (b-int(b))(list2[int(b+2)] - list2[int(b)+1])
    IQR = q3 - q1
    return IQR


def calcuSpeechActivity(list):
    """
    LTSV measure(undefined)
    :param list:
    :return:
    """
    pass