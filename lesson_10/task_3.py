CHANNELS = ["BBC", "Discovery", "TV1000"]


class TVController:
    def __init__(self, channels):
        self.channels = channels
        self._current = channels[0]

    def current_channel(self):
        return self._current

    def first_channel(self):
        self._current = self.channels[0]
        return self.current_channel()

    def last_channel(self):
        self._current = self.channels[-1]
        return self.current_channel()

    def turn_channel(self, channel_num):
        if self._is_exist(channel_num - 1):
            self._current = self.channels[channel_num - 1]
        return self.current_channel()

    def next_channel(self):
        if self.channels[-1] == self._current:
            self._current = self.channels[0]
        else:
            self._current = self.channels[self.channels.index(self._current) + 1]
        return self.current_channel()

    def previous_channel(self):
        if self.channels[0] == self._current:
            self._current = self.channels[-1]
        else:
            self._current = self.channels[self.channels.index(self._current) - 1]
        return self.current_channel()

    def is_exist(self, channel):
        return "Yes" if self._is_exist(channel) else "No"

    def _is_exist(self, channel):
        if type(channel) == int:
            return True if len(self.channels) >= channel else False
        if type(channel) == str:
            return True if channel in self.channels else False
        return False


controller = TVController(CHANNELS)

print(controller.first_channel())
print(controller.last_channel())
print(controller.turn_channel(1))
print(controller.next_channel())
print(controller.previous_channel())
print(controller.current_channel())
print(controller.is_exist(4))
print(controller.is_exist("BBC"))