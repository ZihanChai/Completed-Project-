class LightSwitch():
    ''' A class to turn on or off a switch'''

    def __init__(self, switch):
        '''(LightSwitch, str) -> NoneType
        Create a new switch with it current status on or off.
        REQ: switch can only be 'on' or 'off'
        '''
        # Create a variable represent the status of the switch
        self.switch_status = False
        self.switch = switch
        # Determine whether the switch's default status is on or off
        if(self.switch == 'on'):
            self.switch_status = True
        elif(self.switch == 'off'):
            self.switch_status = False

    def __str__(self):
        '''(LightSwitch) -> str
        Return a string represent the switch is on or off
        '''
        # Determine the current status of the switch
        if(self.switch_status is True):
            result = 'I am on'
        elif(self.switch_status is False):
            result = 'I am off'
        return result

    def turn_on(self):
        '''(LightSwitch) -> NoneType
        Return a NoneType and turn the switch on
        REQ: If the switch is already on, nothing changes.
        '''
        # Change the switch to on
        self.switch_status = True

    def turn_off(self):
        '''(LightSwitch) -> NoneType
        Return a NoneType and turn the switch off
        REQ: If the switch is already on, nothing changes.
        '''
        # Change the switch to on
        self.switch_status = False

    def flip(self):
        '''(LightSwitch) -> NoneType
        Return a NoneType and turn the switch off if it was on, and turn it on
        if it was off
        '''
        # Determine the current status of switches and change it
        if(self.switch_status is True):
            self.switch_status = False
        elif(self.switch_status is False):
            self.switch_status = True


class SwitchBoard():
    '''A class turn on or off a a group switches'''

    def __init__(self, switch):
        '''(SwitchBoard, int) -> NoneType
        Create the input number of switches with default status off.
        '''
        # Create a empty list
        self.switch_list = []
        i = 0
        # Create the input number's switches and set it defalut status to off
        while (i < switch):
            switches = LightSwitch('off')
            self.switch_list.append(switches)
            i += 1

    def flip(self, switch):
        '''(SwitchBoard, int) -> NoneType
        Return a Nonetype and change the input number'th switch to on or off
        '''
        # Determine the current status of switches and change it
        if(switch.switch_status is True):
            switch.switch_status = False
        elif(switch.switch_status is False):
            switch.switch_status = True

    def flip_every(self, index):
        '''(SwitchBoard, int) -> NoneType
        Return a Nonetype and change the every input number'th switch
        to on or off.
        REQ: index <= the total number of switchess
        '''
        self.index = index
        # Change every index'th number of switches status
        for i in range(len(self.switch_list)):
            if(i % self.index == 0):
                self.flip(self.switch_list[i])

    def reset(self):
        '''(SwitchBoard) -> NoneType
        Return a Nonetype and change the every switch off.
        '''
        # Change all switches to off
        for i in range(len(self.switch_list)):
            self.switch_list[i].switch_status = False

    def which_switch(self):
        '''(SwitchBoard) -> list of int
        Return a list of integer of the number'th of switches are on.
        '''
        # Create a empty list
        self.new_list = []
        # Add every switch is on to the list
        for i in range(len(self.switch_list)):
            if(self.switch_list[i].switch_status is True):
                self.new_list.append(i)
        return self.new_list[:]

    def __str__(self):
        '''(SwitchBoard) -> str
        Return a str that state the number'th of switches are on.
        '''
        # Create an empty string
        switch_on = ""
        # Add number in the list to the string
        for i in range(len(self.which_switch())):
            switch_on += ' ' + str(self.which_switch()[i])
        return 'The following switches are on: ' + switch_on
