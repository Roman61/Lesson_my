from Singleton import singleton


@singleton
class Hendlers:

    def __init__(self):
        self.events_hendlers = {}
        self.function = []

    def clear(self):
        self.events_hendlers = {}
        self.function = []

    def hendler(self, event: str, func: callable):
        function = self.events_hendlers.get(event)

        if function is None:
            self.events_hendlers[event] = [func]
        else:
            function.append(func)

    def dispactch(self, event: str, data):
        function = self.events_hendlers.get(event)

        if function is None:
            raise ValueError(f'Unknown event {event}')

        for func in function:
            func(data)


'''
        self.event_current = None
        self.event_done = None
        self.event_selected = None
        self.event_summon = None
        self.event_move_to_up = None
        self.event_move_to_down = None

        self.hendler.dispactch('door_opening', self.event_opening)
        self.hendler.dispactch('door_closing', self.event_closing)
        self.hendler.dispactch('door_close', self.event_close)
        self.hendler.dispactch('door_open', self.event_open)

'''
