#import the tkinter module to make GUI, and main file to import CalculatorBackend
import tkinter as tk
from backend import CalculatorBackend

#calculator Class for GUI of claculator
class Calculator:
    #constructor method to initiliaze window
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        # Create backend
        self.backend = CalculatorBackend()

        #one entry for the expression
        self.entry = tk.Entry(root, font=("Arial", 18), borderwidth=5, relief=tk.RIDGE, justify="right")
        self.entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)
        
        #call the function to layout all other buttons
        self.create_buttons()
        
    def create_buttons(self):
        """function to create all buttons of calculator at the same time"""
        buttons = [
            "7", "8", "9", "/", "√",
            "4", "5", "6", "*", "x²",
            "1", "2", "3", "-", "sin",
            "0", ".", "=", "+", "cos",
            "tan", "asin", "acos", "atan", "C"
        ]

        row = 1
        col = 0
        #loop through the list of buttons
        for button in buttons:
            tk.Button(
                self.root,
                text=button,
                width=6,
                height=2,
                font=("Arial", 12),
                command=lambda b=button: self.on_button_click(b)
            ).grid(row=row, column=col, padx=5, pady=5)
            #create that button and using grid insert it into the window

            #increment col so that next button will be placed correctly
            col += 1
            #after 4 columns now move to the next row
            if col > 4:
                col = 0
                row += 1

    
    def on_button_click(self, button):
        """function to evaluate what will happen when the each button is pressed"""
        try:
            #if = button is pressed just use rhe evaluate function from backend file
            if button == "=":
                # Backend evaluates expression
                result = self.backend.evaluate()
                self.display_result(result)

            #when C button is pressed, clear the entry using the function from the backend
            elif button == "C":
                self.backend.clear()
                self.entry.delete(0, tk.END)

            #when the square root is pressed, evaluate the square root using the function from backend
            elif button == "√":
                value = float(self.entry.get())
                result = self.backend.sqrt_of(value)
                self.display_result(result)
            
            #when the square is pressed, evaluate the square using the function from backend
            elif button == "x²":
                value = float(self.entry.get())
                result = self.backend.square_of(value)
                self.display_result(result)

            #when trig functions are used, evaluate them using trig function from backend
            elif button in ["sin", "cos", "tan", "asin", "acos", "atan"]:
                value = float(self.entry.get())
                result = self.backend.trig(button, value)
                self.display_result(result)

            #for all other cases use add_token function
            else:
                # Normal digit/operator goes to backend expression
                self.backend.add_token(button)
                self.entry.insert(tk.END, button)

        except Exception:
            #if something happens just give error and clear the entry
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error")
            self.backend.clear()

    
    def display_result(self, result):
        """Display result and update backend expression so user can continue calculations."""
        self.entry.delete(0, tk.END)

        # Make 5.0 display as 5
        if isinstance(result, float) and result.is_integer():
            result = int(result)
            
        self.entry.insert(tk.END, result)
        #update the expression with the value itself
        self.backend.set_expression(str(result))


if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
