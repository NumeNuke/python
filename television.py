class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self)-> None:
        '''
        Sets up the television values
        '''
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL


    def power(self) -> None:
        '''
        Turn the TV on if its off or off if its on.
        '''
        if self.__status == False:
            self.__status = True
        elif self.__status == True:
            self.__status = False

    def mute(self)-> None:
        '''
        Mutes the tv and if its already muted it unmutes it
        '''
        if self.__status:
            if self.__muted == False:
                self.__muted = True
            else:
                self.__muted = False

    def channel_up(self)-> None:
        '''
        Turns the tv channel up and if its turned up at max it switches to the min channel
        '''
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self)-> None:
        '''
        Turn the tv channel down and if its activated at min then it switches it to the max channel
        '''
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self)-> None:
        '''
        Turns the volume up by 1 if the tv is on,unmuting the volume and if its max it stays max
        '''
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1


    def volume_down(self)-> None:
        '''
        Turn the tv volume down if the tv is on,unmuting the volume and if its min it stays min
        '''
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        '''
        Returns the status of the television Power, Channel, Volume
        '''
        if self.__muted:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}"
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"


