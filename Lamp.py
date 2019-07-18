class Lamp:
    _LAMPS = ['''
          .
     .    |    ,
      \   '   /
       ` ,-. '
    --- (   ) ---
         \ /
        _|=|_
       |_____|
    ''',
    '''
         ,-.
        (   )
         \ /
        _|=|_
       |_____|
    ''']

    def __init__(self, is_turned_on):
        self.is_turned_on = False

    def turn_on(self):
        self.is_turned_on = True
        self._display_image()

    def turn_off(self):
        self.is_turned_on = False
        self._display_image()

    def _display_image(self):

        if self.is_turned_on:
            print(self._LAMPS[0])
        else:
            print(self._LAMPS[1])