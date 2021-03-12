import random

class Slot:
    def __init__(self, name, win_rate):
        self.name = name
        self.pull_cnt = 0
        self.win_cnt = 0
        self.win_rate = win_rate
    
    def pull(self):
        result = random.random() >= (1 - self.win_rate)
        self.pull_cnt += 1

        if result == True:
            self.win_cnt += 1

        return result
    
    def get_name(self):
        return self.name

    def get_win_percent(self):
        return self.win_cnt / self.pull_cnt
    
    def get_pull_cnt(self):
        return self.pull_cnt

def get_best_slot():
    best = slots[0]
    for slot in slots:
        if slot.get_win_percent() > best.get_win_percent():
            best = slot
    return best

def greedy_epsilon(epsilon, iterations):
  
  for r in range(iterations):
      should_choose_random = random.random() <= epsilon
      if should_choose_random:
          print("choosing a random slot...")
          rand_slot = slots[random.randint(0,3)]
          rand_slot.pull()
      else:
          best = get_best_slot()
          best.pull()

def main():

    slot_a = Slot("winny", .75)
    slot_b = Slot("slot_b", .7)
    slot_c = Slot("slot_c", .5)
    slot_d = Slot("slot_d", .45)

    slots = [slot_a, slot_b, slot_c, slot_d]

    #pull all slots once initially
    for slot in slots:
        slot.pull()

    epsilon = .05
    iterations = 1000
    greedy_epsilon(epsilon, iterations)

    for slot in slots:
        print("slot: " + slot.get_name() + " win_per: " + str(slot.get_win_percent()) + " pulls: " + str(slot.get_pull_cnt()))

    best_slot = get_best_slot()
    print("best slot: " + best_slot.get_name())
    print("win_percent: " + str(best_slot.get_win_percent()))
    print("pulls: " + str(best_slot.get_pull_cnt()))

main()

