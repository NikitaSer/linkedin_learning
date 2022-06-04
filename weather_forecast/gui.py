import json
import traceback

import config
from tkinter import *
from tkinter import ttk
from wf_email import DailyDigestEmail
from wf_scheduler import DailyDigestSheduler


class DailyDigestGUI:
    def __init__(self, root):
        self.__root = root
        self.__root.title("Daily Digest")
        title_label = ttk.Label(
            self.__root,
            text="\U0001F4DC Daily Digest \U0001F4DC",
            font="Algerian 32 bold",
            justify=CENTER,
        )
        title_label.pack(padx=5, pady=5)
        self.__style = ttk.Style()
        self.__style.configure("TButton", font=("Arial", 12, "bold"))
        self.__style.configure("Header.TLabel", font=("Arial", 12, "bold"))

        recipients_frame = ttk.Frame(self.__root)
        recipients_frame.pack(padx=5, pady=5)
        self.__add_recipient_var = StringVar()
        self.__recipient_list_var = Variable()
        self.__build_gui_recipients(
            recipients_frame, self.__add_recipient_var, self.__recipient_list_var
        )

        schedule_frame = ttk.Frame(self.__root)
        schedule_frame.pack(padx=5, pady=5)
        self.__hour_var = StringVar()
        self.__minute_var = StringVar()
        self.__build_gui_schedule(schedule_frame, self.__hour_var, self.__minute_var)

        contents_frame = ttk.Frame(self.__root)
        contents_frame.pack(padx=5, pady=5)
        self.__quote_var = IntVar()
        self.__weather_var = IntVar()
        self.__twitter_var = IntVar()
        self.__wikipedia_var = IntVar()
        self.__build_gui_content(
            contents_frame,
            self.__quote_var,
            self.__weather_var,
            self.__twitter_var,
            self.__wikipedia_var,
        )

        sender_frame = ttk.Frame(self.__root)
        sender_frame.pack(padx=5, pady=5)
        self.__sender_email_var = StringVar()
        self.__sender_password_var = StringVar()
        self.__build_gui_sender(
            sender_frame, self.__sender_email_var, self.__sender_password_var
        )

        controls_frame = ttk.Frame(self.__root)
        controls_frame.pack(padx=5, pady=5)
        self.__build_gui_controls(controls_frame)

        self.__email = DailyDigestEmail()
        self.__scheduler = DailyDigestSheduler()
        self.__scheduler.start()
        self.__root.protocol("WM_DELETE_WINDOW", self.__shutdown)

        try:
            self.__load_config()
        except Exception as e:
            print(f"Exception: {e}\ntraceback: {traceback.print_exc()}")

            self.__add_recipient_var.set("")
            self.__recipient_list_var.set(self.__email.recipients_list)

            self.__hour_var.set("10")
            self.__minute_var.set("05")

            self.__quote_var.set(self.__email.content["quote"]["include"])
            self.__weather_var.set(self.__email.content["weather"]["include"])
            self.__twitter_var.set(self.__email.content["twitter"]["include"])
            self.__wikipedia_var.set(self.__email.content["wikipedia"]["include"])

            self.__sender_email_var.set(self.__email.sender_credentials["email"])
            self.__sender_password_var.set(self.__email.sender_credentials["password"])

    def __build_gui_recipients(self, master, add_recipient_var, recipient_list_var):
        header = ttk.Label(master, text="Recipients:", style="Header.TLabel")
        spacer_frame = ttk.Frame(master)

        recipients_entry = ttk.Entry(master, width=40, textvariable=add_recipient_var)
        recipients_scrollbar = ttk.Scrollbar(master, orient=VERTICAL)
        recipients_scrollbar.grid(row=4, column=1, sticky=N + S + W + E)
        recipients_listbox = Listbox(
            master,
            listvariable=recipient_list_var,
            selectmode="multiple",
            width=40,
            height=5,
        )
        recipients_listbox.configure(yscrollcommand=recipients_scrollbar.set)
        recipients_scrollbar.config(command=recipients_listbox.yview)

        add_button = ttk.Button(
            master, text="Add Recipient", command=self.__add_recipient
        )
        remove_button = ttk.Button(
            master,
            text="Remove Selected",
            command=lambda: self.__remove_selected_recipients(
                recipients_listbox.curselection()
            ),
        )

        header.grid(row=0, column=0)
        recipients_entry.grid(row=1, column=0)
        add_button.grid(row=2, column=0)
        spacer_frame.grid(row=3, column=0, pady=5)
        recipients_listbox.grid(row=4, column=0)
        remove_button.grid(row=5, column=0)

    def __build_gui_schedule(self, master, hour_var, minute_var):
        header = ttk.Label(master, text="Scheduled time (24hr):", style="Header.TLabel")
        hour_spinbox = ttk.Spinbox(
            master,
            from_=0,
            to=23,
            textvariable=hour_var,
            wrap=True,
            width=3,
            justify=CENTER,
            font="Arial 12",
        )
        minute_spinbox = ttk.Spinbox(
            master,
            from_=0,
            to=59,
            textvariable=minute_var,
            wrap=True,
            width=3,
            justify=CENTER,
            font="Arial 12",
        )

        header.grid(row=0, column=0, columnspan=2)
        hour_spinbox.grid(row=1, column=0, sticky=E, padx=2, pady=5)
        minute_spinbox.grid(row=1, column=1, sticky=W, padx=2, pady=5)

    def __build_gui_content(
        self, master, quote_var, weather_var, twitter_var, wikipedia_var
    ):
        header = ttk.Label(master, text="Digest Contents:", style="Header.TLabel")
        quote_checkbox = Checkbutton(
            master,
            text="Motivational Quote",
            onvalue=True,
            offvalue=False,
            variable=quote_var,
        )
        weather_checkbox = Checkbutton(
            master,
            text="Weather Forecast",
            onvalue=True,
            offvalue=False,
            variable=weather_var,
        )
        twitter_checkbox = Checkbutton(
            master,
            text="Twitter Trends",
            onvalue=True,
            offvalue=False,
            variable=twitter_var,
        )
        wikipedia_checkbox = Checkbutton(
            master,
            text="Wikipedia Article",
            onvalue=True,
            offvalue=False,
            variable=wikipedia_var,
        )

        header.grid(row=0, column=0, columnspan=2)
        quote_checkbox.grid(row=1, column=0, sticky=W)
        weather_checkbox.grid(row=2, column=0, sticky=W)
        twitter_checkbox.grid(row=1, column=1, sticky=W)
        wikipedia_checkbox.grid(row=2, column=1, sticky=W)

    def __build_gui_sender(self, master, sender_email_var, sender_password_var):
        header = ttk.Label(master, text="Sender Credentials:", style="Header.TLabel")
        email_label = ttk.Label(master, text="Email:")
        email_entry = ttk.Entry(master, width=40, textvariable=sender_email_var)
        password_label = ttk.Label(master, text="Password")
        password_entry = ttk.Entry(
            master, width=40, show="*", textvariable=sender_password_var
        )

        header.grid(row=0, column=0, columnspan=2)
        email_label.grid(row=1, column=0, pady=2, sticky=E)
        email_entry.grid(row=1, column=1, pady=2, sticky=W)
        password_label.grid(row=2, column=0, pady=2, sticky=E)
        password_entry.grid(row=2, column=1, pady=2, sticky=W)

    def __build_gui_controls(self, master):
        update_button = ttk.Button(
            master, text="Update Settings", command=self.__update_settings
        )
        send_button = ttk.Button(master, text="Manual Send", command=self.__manual_send)

        update_button.grid(row=0, column=0, padx=5, pady=5)
        send_button.grid(row=0, column=1, padx=5, pady=5)

    def __add_recipient(self):
        new_recipient = self.__add_recipient_var.get()
        if new_recipient != "":
            recipient_list = self.__recipient_list_var.get()
            if recipient_list != ("",):
                self.__recipient_list_var.set(recipient_list + (new_recipient,))
            else:
                self.__recipient_list_var.set((new_recipient,))
            self.__add_recipient_var.set("")

    def __remove_selected_recipients(self, selection):
        recipient_list = list(self.__recipient_list_var.get())
        for index in reversed(selection):
            recipient_list.pop(index)
        self.__recipient_list_var.set(recipient_list)

    def __update_settings(self):
        print("Updating settings...")
        self.__email.recipients_list = list(self.__recipient_list_var.get())
        self.__email.content["quote"]["include"] = self.__quote_var.get()
        self.__email.content["weather"]["include"] = self.__weather_var.get()
        self.__email.content["twitter"]["include"] = self.__twitter_var.get()
        self.__email.content["wikipedia"]["include"] = self.__wikipedia_var.get()

        self.__email.sender_credentials = {
            "email": self.__sender_email_var.get(),
            "password": self.__sender_password_var.get(),
        }

        self.__scheduler.schedule_daily(
            int(self.__hour_var.get()),
            int(self.__minute_var.get()),
            self.__email.send_email,
        )

    def __manual_send(self):
        print("Manually sending email digest...")
        self.__email.send_email()

    def __shutdown(self):
        print("Shutting down the scheduler...")
        self.__scheduler.stop()
        self.__scheduler.join()
        try:
            self.__save_config()
        except Exception as e:
            print(f"Exception: {e}\ntraceback: {traceback.print_exc()}")
        self.__root.destroy()

    def __save_config(self, file_path=config.WF_CONFIG):
        config = {
            "add_recipient": self.__add_recipient_var.get(),
            "recipient_list": self.__recipient_list_var.get(),
            "hour": self.__hour_var.get(),
            "minute": self.__minute_var.get(),
            "quote": self.__quote_var.get(),
            "weather": self.__weather_var.get(),
            "twitter": self.__twitter_var.get(),
            "wikipedia": self.__wikipedia_var.get(),
            "sender_email": self.__sender_email_var.get(),
            "sender_password": self.__sender_password_var.get(),
        }
        with open(file_path, "w") as file:
            json.dump(config, file, indent=4)

    def __load_config(self, file_path=config.WF_CONFIG):
        with open(file_path) as file:
            config = json.load(file)
            self.__add_recipient_var.set(config["add_recipient"])
            self.__recipient_list_var.set(config["recipient_list"])
            self.__hour_var.set(config["hour"])
            self.__minute_var.set(config["minute"])
            self.__quote_var.set(config["quote"])
            self.__weather_var.set(config["weather"])
            self.__twitter_var.set(config["twitter"])
            self.__wikipedia_var.set(config["wikipedia"])
            self.__sender_email_var.set(config["sender_email"])
            self.__sender_password_var.set(config["sender_password"])
        self.__update_settings()


if __name__ == "__main__":
    root = Tk()
    app = DailyDigestGUI(root)
    root.mainloop()
