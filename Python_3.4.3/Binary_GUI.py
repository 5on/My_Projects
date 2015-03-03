from tkinter import *

class Binary (Frame):

#Initial Window -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= 
    def __init__(self):                                                                                 
        Frame.__init__(self)
        self.master.title("Binary")
        self.master.geometry("400x200")
        self.master.resizable(0, 0)
        self.grid()
        
        #Variables
        self._input = IntVar()
        self._output = IntVar()
        #=======   
        
        #Buttons
        self._buttonIntToBin = Button(self,
                                      text = "Integer to Binary",
                                      command = self._intToBin)
        self._buttonIntToBin.grid(row = 2, column = 1)
        self._buttonBinToInt = Button(self,
                                      text = "Binary to Integer",
                                      command = self._binToInt)
        self._buttonBinToInt.grid(row = 3, column = 1)
        self._buttonRangeOfInt = Button(self,
                                         text = "Range of Integers",
                                         command = self._rangeOfInt)
        self._buttonRangeOfInt.grid(row = 4, column = 1)
        #========

        #Entries
        self._entryInput = Entry(self,
                                 textvariable = self._input) 
        self._entryInput.grid(row = 2, column = 2)
        self._entryOutput = Entry(self,
                             textvariable = self._output)
        self._entryOutput.grid(row = 4, column = 2)        
        #========

        #Labels
        self._labelInput = Label(self,
                                 text = "Input\Low range")
        self._labelInput.grid(row = 1, column = 2)
        self._labelSelection = Label(self,
                                     text = "Process")
        self._labelSelection.grid(row = 1, column = 1)
        self._labelOutput = Label(self,
                                  text = "Output\High range")
        self._labelOutput.grid(row = 3, column = 2) 
        self._labelRange = Label(self,
                                 text = "Range")
        self._labelRange.grid(row = 1, column = 3)
        #=======
        
        #ListBoxes + Scrollbars
        self._listRange = Listbox(self)
        self._listRange.grid(row = 2, rowspan = 5,
                             column = 3, columnspan = 5)

    #Functions ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-       
    def _intToBin(self):
        """
        Extracts the variables from entries and places them in local variables.
        After extracting self._input, it converts it to binary in the binary variable.
        The functions return binary's value in the self._entryOutput entry.
        """
        intx = self._input.get()
        binary = self._output
        binary = int(bin(intx)[2: ]) 
        self._output.set(binary)
        
    def _binToInt(self):
        """
        Same procedure as _intToBin, except it converts a binary number to its integer value.
        """
        binary = self._input.get()
        intx = 0
        for digit in binary:
            intx = intx * 2 + int(digit)
        self._output.set(intx)

    def _rangeOfInt(self):
        """
        Extracts the variables from the self._entryInput and self._entryOutput
            entries into local variables.
        These variables serve as the low and high range for the loop
            that breaks when lowrange > highrange.
        """
        lowrange = self._input.get()
        highrange = self._output.get()
        binary = 0
        while True:
            if lowrange > highrange:
                break
            else:
                binary = int(bin(lowrange)[2: ])
                self._listRange.insert(END, binary)
                lowrange += 1
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-      
       
#Main Function =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=       
def main():
    Binary().mainloop()
    
main()
#=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
