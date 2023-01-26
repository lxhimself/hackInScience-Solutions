alice = ["I", "II", "III"]
bob = ["I", "II"]
silvester = ["II", "III"]


def love_meet(bob, alice):
    meetpoints = set(alice).intersection(bob)
    return(meetpoints)



def affair_meet(bob, alice, silvester):
    alicepoints = set(alice)
    aliceohnebob = alicepoints.symmetric_difference(bob)
    affairpoints = set(silvester).intersection(alice)
    spots = set(affairpoints).intersection(aliceohnebob)
    return(spots)



affair_meet(bob, alice, silvester)


