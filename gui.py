from tkinter import *
from solver import Solver
import pprint

root = Tk()
root.geometry("455x450")
root.title("Sudoku Instructions")
root.option_add('*Font', 'Montserrat')
root.configure(bg='#D0D0FF')


def tab1():

    def tab2():
        root = Tk()
        root.title("Sudoklver")  # title
        root.option_add('*Font', 'Montserrat ')  # to change text font
        root.geometry("455x450")  # the dimensions of the GUI
        root.configure(bg='#D0D0FF')

        label = Label(root, text="Fill in the numbers and click solve").grid(
            row=0, column=1, columnspan=10)

        errLabel = Label(root, text="", fg="red", wraplength=400)
        errLabel.grid(row=15, column=1, columnspan=10, pady=5)

        solvedLabel = Label(root, text="", fg="green")
        solvedLabel.grid(row=15, column=1, columnspan=10, pady=5)

        cells = {}

        '''
        Edge case1: To validate the number the user inputs, cannot be lesser than 1 or greater that 0, cannot be symbols or letters, this is an edge case which we check for with the function validate_number()
        '''
        def validate_number(number):
            out = (number.isdigit() or number == "") and len(number) < 2
            return out

        reg = root.register(validate_number)

        # Function To design the 3 x3 grid
        def design3x3Grid(row, column, bgcolor):
            for i in range(3):
                for j in range(3):
                    e = Entry(root, width=5, bg=bgcolor, justify="center",
                              validate="key", validatecommand=(reg, "%P"))
                    e.grid(row=row+i+1, column=column+j+1,
                           sticky="nsew", padx=1, pady=1, ipady=5)
                    cells[(row+i+1, column+j+1)] = e

        # Function to design the 9 x 9 grid
        def design9x9Grid():
            color = "#ffffff"
            for rowNo in range(1, 10, 3):
                for colNo in range(0, 9, 3):
                    design3x3Grid(rowNo, colNo, color)
                    if color == "#ffffff":
                        color = "#ffffd0"
                    else:
                        color = "#ffffff"

        # Clears the sudoku board
        def clearValues():
            errLabel.configure(text="")
            solvedLabel.configure(text="")
            for row in range(2, 11):
                for col in range(1, 10):
                    cell = cells[(row, col)]
                    cell.delete(0, "end")

        # Function to get the user value and process it in the sudoku
        def getValues():
            global board
            board = []  # Stores the user input in a 2D array format
            count = 0  # To keep track of the zeros we have
            errLabel.configure(text="")
            solvedLabel.configure(text="")
            for row in range(2, 11):
                rows = []
                for col in range(1, 10):
                    # To get the value of that cell
                    val = cells[(row, col)].get()
                    if val == "":  # If the value is empty we append zero
                        rows.append(0)
                        count += 1
                    else:
                        # We convert it to an integer and append that value to the rows list
                        rows.append(int(val))

                board.append(rows)
            # pprint.pprint(board) #can be uncommented to view the board in 2D format
            '''
            Edge Case 2: If the user hasn't inputted any value which means the board is
            empty and count is 81 and so we return and error message that the user has to 
            input a value
              '''
            if count == 81:
                errLabel.configure(text="Please input some values")

            else:
                updateValues(board)

        btn = Button(root, command=getValues, text="Solve", width=10)
        btn.grid(row=20, column=1, columnspan=5, pady=20)

        btn = Button(root, command=clearValues, text="Clear", width=10)
        btn.grid(row=20, column=5, columnspan=5, pady=20)

        # Updates the cells and displays the solution of sudoku
        def updateValues(s):
            sudo = Solver()  # Creating an object for our class
            sol = sudo.main_solver(s)  # sol = solution
            if sol != "no":
                for rows in range(2, 11):
                    for col in range(1, 10):
                        cells[(rows, col)].delete(0, "end")
                        cells[(rows, col)].insert(0, sol[rows - 2][col - 1])
                solvedLabel.configure(text="Sudoku solved!")
            else:
                errLabel.configure(
                    text="No solution exists for this sudoku Check for same numbers in same row column or grid")

        design9x9Grid()
        root.mainloop()

    '''
    Design for the Instruction Gui
    '''
    label1 = Label(root, text='WELCOME:)', font=('Montserrat', 13),
                   relief='ridge', padx=4, pady=5, borderwidth=5)
    label1.pack()
    button1 = Button(root, text='START', font=('Montserrat', 14), command=tab2)
    button1.pack(side=BOTTOM, pady=5, padx=3)

    text = Text(root, wrap="word", spacing2=5, spacing3=5,
                background="#ffffd0", xscrollcommand=set())
    text.tag_configure('text_body', font=(
        'Montserrat', 13), lmargin1=0, lmargin2=0)
    text.tag_configure('bulleted_list', font=('Montserrat', 13),
                       lmargin1='10m', lmargin2='15m', tabs=['15m'])

    text.insert(
        END, u"\tHERE ARE THE INSTRUCTIONS FOR THE GAME.\n\n", "text_body")
    text.insert(END, u"\u2022\tWhen Inputing the puzzle only numbers 1-9 are allowed, when you try to input a number lesser, greater, symbols or letters it input in the program.\n", 'bulleted_list')
    text.insert(
        END, u"\u2022\tClick the Solve button after inputing the numbers.\n", 'bulleted_list')
    text.insert(
        END, u"\u2022\tEach row contains the numbers from 1 to 9 without repetitions.\n", 'bulleted_list')
    text.insert(
        END, u"\u2022\tEach column contains the numbers from 1 to 9 without repetitions.\n", 'bulleted_list')
    text.insert(
        END, u"\u2022\tThe digits can only occur once per block/grid.\n", 'bulleted_list')
    text.configure(state=DISABLED)
    text.pack()


tab1()
root.mainloop()
