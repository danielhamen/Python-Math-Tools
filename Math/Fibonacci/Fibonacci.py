class Fibonacci:
    """
    A class to get the Fibonacci sequence
    """

    def __init__(self, Length):
        self.StartValue = 0
        self.NextValue = 1
        self.Length = Length
    
    # Starts the sequence
    def Start(self):
        Sequence = [str(self.StartValue)]
        Step = False

        for i in range(0, self.Length):
            if Step is True:
                self.StartValue = self.StartValue + self.NextValue

                Sequence.append(str(self.StartValue))

                Step = False

            elif Step is False:
                self.NextValue = self.StartValue + self.NextValue

                Sequence.append(str(self.NextValue))

                Step = True

        return Sequence
