import customtkinter    # <- import the CustomTkinter module

def main():
    root_tk = customtkinter.CTk()  # Create the Tk window like you normally do
    root_tk.geometry("840x640")
    root_tk.title("Point of Sale")

    frame = customtkinter.CTkFrame(root_tk, width=200, height=200, fg_color='White',) 
    frame.place(x=400, y=10)



    root_tk.mainloop()


if __name__ == "__main__":
    main()