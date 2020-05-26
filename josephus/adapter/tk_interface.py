import tkinter as tk
import tkinter.filedialog
import tkinter.simpledialog
from josephus.interface.interface import Interface
 
class TkWindow(Interface):
    def __init__(self, master=None):
        super().__init__()
        master.geometry('700x600')
        tk.Label(master, text='Game of Josephus Ring', font=('Arial', 30)).pack(side=tk.TOP)

        self.frame_input = tk.Frame(master)
        tk.Label(self.frame_input, text='START', font=('Arial', 20)).grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self.frame_input, text='STEP', font=('Arial', 20)).grid(row=1, column=0, padx=10, pady=10)
        tk.Label(self.frame_input, text='People', font=('Arial', 20)).grid(row=2, column=0, padx=10, pady=10)

        self.var_start = tk.StringVar()
        self.var_start.set('1')
        self.var_start.trace('w', self.set_start_value_)
        self.entry_start = tk.Entry(self.frame_input, textvariable=self.var_start, font=('Arial', 15), width=4)
        self.entry_start.grid(row=0, column=1)

        self.var_step = tk.StringVar()
        self.var_step.set('1')
        self.var_step.trace('w', self.set_step_value_)
        self.entry_step = tk.Entry(self.frame_input, textvariable=self.var_step, font=('Arial', 15), width=4)
        self.entry_step.grid(row=1, column=1)

        self.hint_strat_text = tk.StringVar()
        self.hint_strat_text.set('')
        self.hint_start_label = tk.Label(self.frame_input, textvariable=self.hint_strat_text, font=('Arial', 10))
        self.hint_start_label.grid(row=0, column=2, padx=10, pady=10)
        self.hint_step_text = tk.StringVar()
        self.hint_step_text.set('')
        self.hint_step_label = tk.Label(self.frame_input, textvariable=self.hint_step_text, font=('Arial', 10))
        self.hint_step_label.grid(row=1, column=2, padx=10, pady=10)


        self.button_file = tk.Button(self.frame_input, text='open file', font=('Arial', 15), command=self.create_and_show_reader)
        self.button_file.grid(row=2, column=1)
        self.frame_input.place(x=10, y=50)
        
        self.button_ok = tk.Button(master, text='OK', font=('Arial', 15), width=8, command=self.create_josephus_)
        self.button_ok.place(x=120, y=520)

        self.text_people = tk.Text(master, font=('Arial', 15), height=12, width=20)
        self.text_people.place(x=30, y=230)
        
        self.var_result = tk.StringVar()
        self.var_result.set('')
        self.label_result = tk.Label(master, textvariable=self.var_result, font=('Arial', 15), height=15, width=25, bg='white', justify=tk.LEFT)
        self.label_result.place(x=300, y=200)
        
        frame_out = tk.Frame(master)
        self.button_next = tk.Button(frame_out, text='NEXT', font=('Arial', 15), width=8, command=self.next_)
        self.button_next.grid(row=0, column=0)
        self.button_run = tk.Button(frame_out, text='RUN', font=('Arial', 15), width=8, command=self.run)
        self.button_run.grid(row=1, column=0)
        self.button_clear = tk.Button(frame_out, text='CLEAR', font=('Arial', 15), width=8, command=self.clear)
        self.button_clear.grid(row=2, column=0)
        self.button_quit = tk.Button(frame_out, text='Quit', font=('Arial', 15), width=8, command=self.quit)
        self.button_quit.grid(row=3, column=0)
        frame_out.pack(side=tk.RIGHT)

    def set_start_value_(self, *argv):
        try:
            self.set_start_value(self.var_start.get())
            self.hint_strat_text.set('')
        except ValueError:
            self.set_start_value('1')
            self.hint_strat_text.set('please input an integer more than 0')
    
    def set_step_value_(self, *argv):
        try:
            self.set_step_value(self.var_step.get())
            self.hint_step_text.set('')
        except:
            self.set_step_value('1')
            self.hint_step_text.set('please input an integer more than 0')

    def create_and_show_reader(self):
        self.text_people.delete(0.0, tk.END)
        target_file: str = ''
        filepath = tkinter.filedialog.askopenfilename(initialdir='data', title='Open file')
        filenames = self.get_namelist_from_zip(filepath)
        if filenames:
            content: str = ''
            for each in filenames:
                content = content + each + '\n'
            target_file = tkinter.simpledialog.askstring('Input target file', content)
            if not target_file:
                return self.create_and_show_reader()
        try:
            self.create_reader(filepath, target_file)
        except FileNotFoundError:
            tk.messagebox.showwarning(title='Warning', message='please input valid path and target file')
        self.text_people.insert(tk.END, self.get_people_info(self.reader))

    def create_josephus_(self):
        content = self.text_people.get(0.0, tk.END).strip()
        if not content:
            return
        try:
            self.create_josephus(content)
        except:
            tk.messagebox.showwarning(title='Warning', message='please input correct format in the text box\nfor example: Bob, 12')
            return
        try:
            self.check_strat_value()
        except ValueError:
            tk.messagebox.showwarning(title='Warning', message=f'The value of start range from 1 to {len(self.josephus)}')

    def next_(self):
        try:
            some_one = next(self.josephus)
            self.var_result.set(f'{some_one.name}\t{some_one.age}')
        except StopIteration:
            self.var_result.set("That's all")
        except AttributeError:
            pass

    def run(self):
        try:
            self.var_result.set(self.get_result())
        except:
            pass

    def clear(self):
        self.var_result.set('')

    def quit(self):
        exit()
