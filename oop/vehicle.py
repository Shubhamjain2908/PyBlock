class Vehicle:
    
    def __init__(self, starting_top_speed = 100):
        """ Default Constructor """
        self.top_speed = starting_top_speed
        self.__warnings = [] # __ means a private variable (only accessible inside the class) 

    # This method is called whenever we try to output a class
    def __repr__(self):
        print('Printing...')
        return 'Top Speed: {}, Warnings: {}'.format(self.top_speed, len(self.__warnings))

    def add_warning(self, warning_text):
        if len(warning_text) > 0:
            self.__warnings.append(warning_text)

    def drive(self):
        print('I am driving but certainly not faster than {}'.format(self.top_speed))
