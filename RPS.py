victory = {}

def player(prev_play, opponent_history=[]):
  global victory

  n = 3

  if prev_play in ["R","P","S"]:
    opponent_history.append(prev_play)

  guess = "R"

  if len(opponent_history)>n:
    in_put = "".join(opponent_history[-n:])

    if "".join(opponent_history[-(n+1):]) in victory.keys():
      victory["".join(opponent_history[-(n+1):])]+=1
    else:
      victory["".join(opponent_history[-(n+1):])]=1

    possibility =[in_put+"R", in_put+"P", in_put+"S"]

    for i in possibility:
      if not i in victory.keys():
        victory[i] = 0

    predict = max(possibility, key=lambda key: victory[key])

    if predict[-1] == "P":
      guess = "S"
    if predict[-1] == "R":
      guess = "P"
    if predict[-1] == "S":
      guess = "R"


  return guess
