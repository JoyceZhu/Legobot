import dice
from Legobot.Lego import Lego


class DoIt(Lego):
    def listening_for(self, message):
        return message['text'].split()[0] == '!doit'

    def handle(self, message):
        dice_string = message['text'].split()[1]
        results = dice.roll(dice_string)
        self.reply(message, 'Just DO IT! http://i.imgur.com/7524jhl.gif')

    def get_name(self):
        return 'doit'

    def get_help(self):
        return 'Get some enouragement from superstar cannibal Shia LeBeouf'
