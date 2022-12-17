import random

class LuckyDraw:

    def __init__(self, participants):
        self.participants = participants
        random.shuffle(self.participants)
        self.next_participant = 0
        self.r = int(random.random() * (len(self.participants)-1) + 1)

    def addParticipants(self, participants):
        self.participants = self.participants + random.shuffle(participants)

    def nextGift(self):
        next_present = (self.next_participant + self.r) % len(self.participants)
        provider = self.participants[self.next_participant]
        receiver = self.participants[next_present]
        self.next_participant = self.next_participant+1
        return f"{provider} -> {receiver}"

    def drawNext(self):
        return self.nextGift() if self.next_participant < len(self.participants) else "抽完"
