import sys

try:
    rps = input('rock, paper, scissors, or quit? [rpsq]')
    assert rps in 'qrps', 'what is it?'
except AssertionError as err:
    print(str(err))
else:
    if rps == 'q':
        sys.exit(0)
    elif rps in 'rps':
        print('play_game(rps)')