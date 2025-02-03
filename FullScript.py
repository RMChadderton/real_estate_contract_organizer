import datetime
import tkinter as tk
from tkinter import messagebox

def is_weekend(date):
    return date.weekday() >= 5

def is_holiday(date):
    holidays = [
        (1, 1),  # New Year's Day
        (6, 19),  # Juneteenth National Independence Day
        (7, 4),  # Independence Day
        (11, 11),  # Veterans Day
        (12, 25),  # Christmas Day
    ]
    month, day = date.month, date.day
    if (month, day) in holidays:
        return True
    elif month == 1 and date.weekday() == 0 and 15 <= day <= 21:  # Birthday of Martin Luther King, Jr.
        return True
    elif month == 2 and date.weekday() == 0 and 15 <= day <= 21:  # Washington's Birthday
        return True
    elif month == 5 and date.weekday() == 0 and 25 <= day <= 31:  # Memorial Day
        return True
    elif month == 9 and date.weekday() == 0 and 1 <= day <= 7:  # Labor Day
        return True
    elif month == 10 and date.weekday() == 0 and 8 <= day <= 14:  # Columbus Day
        return True
    elif month == 11 and date.weekday() == 3 and 22 <= day <= 28:  # Thanksgiving Day
        return True
    return False

def next_workday(date):
    while is_weekend(date) or is_holiday(date):
        date += datetime.timedelta(days=1)
    return date

def generate_email():
    execution_date = execution_date_entry.get()
    escrow_period = int(escrow_period_entry.get())
    inspection_period = int(inspection_period_entry.get())
    financing_period = int(financing_period_entry.get())
    closing_date = closing_date_entry.get()
    property_address = property_address_entry.get()
    client_names = client_names_entry.get()

    execution_date = datetime.datetime.strptime(execution_date, "%m/%d/%Y")
    closing_date = datetime.datetime.strptime(closing_date, "%m/%d/%Y")
    escrow_end_date = next_workday(execution_date + datetime.timedelta(days=escrow_period))
    inspection_end_date = next_workday(execution_date + datetime.timedelta(days=inspection_period))
    financing_end_date = next_workday(execution_date + datetime.timedelta(days=financing_period))

    subject_line = f"UNDER CONTRACT: {property_address}"
    email_body = f"Dear {client_names},\n\n"
    email_body += f"Congratulations on your recent contract execution for the property at {property_address}! "
    email_body += "Here are the important dates and buyer's responsibilities for your transaction:\n\n"
    email_body += f"1. Contract Execution Date: {execution_date.strftime('%m/%d/%Y')}\n"
    email_body += f"2. Escrow Period Ends: {escrow_end_date.strftime('%m/%d/%Y')}\n"
    email_body += "   - Buyer's responsibility: Deposit earnest money into escrow account\n"
    email_body += f"3. Inspection Period Ends: {inspection_end_date.strftime('%m/%d/%Y')}\n"
    email_body += "   - Buyer's responsibility: Complete all desired inspections and negotiate any repairs or credits\n"
    email_body += f"4. Financing Period Ends: {financing_end_date.strftime('%m/%d/%Y')}\n"
    email_body += "   - Buyer's responsibility: Obtain final loan approval and commitment from lender\n"
    email_body += f"5. Closing Date: {closing_date.strftime('%m/%d/%Y')}\n"
    email_body += "   - Buyer's responsibility: Conduct final walkthrough, sign closing documents, and provide funds for closing\n\n"
    email_body += "Please note that this email is not intended as legal advice, and you should consult with a licensed attorney for any legal questions or concerns regarding your transaction.\n\n"
    email_body += "Best regards,\n"
    email_body += "Your Real Estate Agent"

    # Create a new window to display the email content
    email_window = tk.Toplevel(window)
    email_window.title("Generated Email")

    # Create a text widget to display the email content
    email_text = tk.Text(email_window, wrap=tk.WORD)
    email_text.insert(tk.END, f"Subject: {subject_line}\n\n{email_body}")
    email_text.pack(expand=True, fill=tk.BOTH)

    # Create a button to close the email window
    close_button = tk.Button(email_window, text="Close", command=email_window.destroy)
    close_button.pack()

def generate_inspector_email():
    property_address = property_address_entry.get()
    client_names = client_names_entry.get()

    subject_line = f"Inspector Recommendations for {property_address}"
    email_body = f"Dear {client_names},\n\n"
    email_body += f"I hope this email finds you well. As we move forward with the purchase of {property_address}, I wanted to provide you with some recommended inspectors in the area:\n\n"
    email_body += "1. FBI Inspections: 813.409.3249\n"
    email_body += "2. Get The Facts: 813.785.4620\n"
    email_body += "3. HomeTeam: 813.632.0550\n\n"
    email_body += "These inspectors have a great reputation and have worked with many of my clients in the past. They are thorough, professional, and will provide you with a detailed report of the property's condition.\n\n"
    email_body += "Please feel free to reach out to them directly to schedule your inspection. If you have any questions or need further assistance, don't hesitate to contact me.\n\n"
    email_body += "Best regards,\n"
    email_body += "Your Real Estate Agent"

    # Create a new window to display the email content
    email_window = tk.Toplevel(window)
    email_window.title("Inspector Recommendations")

    # Create a text widget to display the email content
    email_text = tk.Text(email_window, wrap=tk.WORD)
    email_text.insert(tk.END, f"Subject: {subject_line}\n\n{email_body}")
    email_text.pack(expand=True, fill=tk.BOTH)

    # Create a button to close the email window
    close_button = tk.Button(email_window, text="Close", command=email_window.destroy)
    close_button.pack()

def generate_end_of_inspection_notice():
    property_address = property_address_entry.get()
    client_names = client_names_entry.get()
    inspection_end_date = next_workday(datetime.datetime.strptime(execution_date_entry.get(), "%m/%d/%Y") + datetime.timedelta(days=int(inspection_period_entry.get())))

    subject_line = f"End of Inspection Notice for {property_address}"
    email_body = f"Dear {client_names},\n\n"
    email_body += f"This is a friendly reminder that the inspection period for the property at {property_address} will end on {inspection_end_date.strftime('%m/%d/%Y')}.\n\n"
    email_body += "Please ensure that you have completed all desired inspections and have negotiated any repairs or credits with the seller by this date.\n\n"
    email_body += "If you have any questions or concerns, please don't hesitate to reach out to me.\n\n"
    email_body += "Best regards,\n"
    email_body += "Your Real Estate Agent"

    # Create a new window to display the email content
    email_window = tk.Toplevel(window)
    email_window.title("End of Inspection Notice")

    # Create a text widget to display the email content
    email_text = tk.Text(email_window, wrap=tk.WORD)
    email_text.insert(tk.END, f"Subject: {subject_line}\n\n{email_body}")
    email_text.pack(expand=True, fill=tk.BOTH)

    # Create a button to close the email window
    close_button = tk.Button(email_window, text="Close", command=email_window.destroy)
    close_button.pack()

def generate_end_of_financing_notice():
    property_address = property_address_entry.get()
    client_names = client_names_entry.get()
    financing_end_date = next_workday(datetime.datetime.strptime(execution_date_entry.get(), "%m/%d/%Y") + datetime.timedelta(days=int(financing_period_entry.get())))

    subject_line = f"End of Financing Notice for {property_address}"
    email_body = f"Dear {client_names},\n\n"
    email_body += f"This is a friendly reminder that the financing period for the property at {property_address} will end on {financing_end_date.strftime('%m/%d/%Y')}.\n\n"
    email_body += "Please ensure that you have obtained final loan approval and commitment from your lender by this date.\n\n"
    email_body += "If you have any questions or concerns, please don't hesitate to reach out to me.\n\n"
    email_body += "Best regards,\n"
    email_body += "Your Real Estate Agent"

    # Create a new window to display the email content
    email_window = tk.Toplevel(window)
    email_window.title("End of Financing Notice")

    # Create a text widget to display the email content
    email_text = tk.Text(email_window, wrap=tk.WORD)
    email_text.insert(tk.END, f"Subject: {subject_line}\n\n{email_body}")
    email_text.pack(expand=True, fill=tk.BOTH)

    # Create a button to close the email window
    close_button = tk.Button(email_window, text="Close", command=email_window.destroy)
    close_button.pack()

def generate_closing_notice_1():
    property_address = property_address_entry.get()
    client_names = client_names_entry.get()
    closing_date = datetime.datetime.strptime(closing_date_entry.get(), "%m/%d/%Y")

    subject_line = f"Closing Notice #1 for {property_address}"
    email_body = f"Dear {client_names},\n\n"
    email_body += f"I hope this email finds you well. As we approach the closing date for the property at {property_address}, I wanted to provide you with some important information.\n\n"
    email_body += f"We are currently scheduled to close on {closing_date.strftime('%m/%d/%Y')}. I will be working closely with the title company to ensure a smooth closing process.\n\n"
    email_body += f"Additionally, we will be conducting a final walkthrough of the property on {(closing_date - datetime.timedelta(days=1)).strftime('%m/%d/%Y')}, either in-person or virtually, to ensure that the property is in the agreed-upon condition.\n\n"
    email_body += "If you have any questions or concerns, please don't hesitate to reach out to me.\n\n"
    email_body += "Best regards,\n"
    email_body += "Your Real Estate Agent"

    # Create a new window to display the email content
    email_window = tk.Toplevel(window)
    email_window.title("Closing Notice #1")

    # Create a text widget to display the email content
    email_text = tk.Text(email_window, wrap=tk.WORD)
    email_text.insert(tk.END, f"Subject: {subject_line}\n\n{email_body}")
    email_text.pack(expand=True, fill=tk.BOTH)

    # Create a button to close the email window
    close_button = tk.Button(email_window, text="Close", command=email_window.destroy)
    close_button.pack()

def generate_closing_notice_2():
    property_address = property_address_entry.get()
    client_names = client_names_entry.get()
    closing_date = datetime.datetime.strptime(closing_date_entry.get(), "%m/%d/%Y")

    subject_line = f"Closing Notice #2 for {property_address}"
    email_body = f"Dear {client_names},\n\n"
    email_body += f"I hope you're excited for the upcoming closing of the property at {property_address} tomorrow, {closing_date.strftime('%m/%d/%Y')}!\n\n"
    email_body += "Please remember to bring the following items to closing:\n"
    email_body += "- Government-issued photo ID\n"
    email_body += "- Certified or cashier's check for the closing funds (your lender will provide the exact amount)\n"
    email_body += "- Any additional documents requested by your lender or the title company\n\n"
    email_body += "All named buyers on the contract must be present at closing to sign the necessary documents.\n\n"
    email_body += f"Also, don't forget that we have scheduled the final walkthrough of the property for today, {(closing_date - datetime.timedelta(days=1)).strftime('%m/%d/%Y')}.\n\n"
    email_body += "If you have any last-minute questions or concerns, please feel free to contact me.\n\n"
    email_body += "Best regards,\n"
    email_body += "Your Real Estate Agent"

    # Create a new window to display the email content
    email_window = tk.Toplevel(window)
    email_window.title("Closing Notice #2")

    # Create a text widget to display the email content
    email_text = tk.Text(email_window, wrap=tk.WORD)
    email_text.insert(tk.END, f"Subject: {subject_line}\n\n{email_body}")
    email_text.pack(expand=True, fill=tk.BOTH)

    # Create a button to close the email window
    close_button = tk.Button(email_window, text="Close", command=email_window.destroy)
    close_button.pack()

def generate_internal_checklist():
    execution_date = execution_date_entry.get()
    escrow_period = int(escrow_period_entry.get())
    inspection_period = int(inspection_period_entry.get())
    financing_period = int(financing_period_entry.get())
    closing_date = closing_date_entry.get()
    property_address = property_address_entry.get()
    agent_name = agent_name_entry.get()
    brokerage_name = brokerage_name_entry.get()

    execution_date = datetime.datetime.strptime(execution_date, "%m/%d/%Y")
    closing_date = datetime.datetime.strptime(closing_date, "%m/%d/%Y")
    escrow_end_date = next_workday(execution_date + datetime.timedelta(days=escrow_period))
    inspection_end_date = next_workday(execution_date + datetime.timedelta(days=inspection_period))
    financing_end_date = next_workday(execution_date + datetime.timedelta(days=financing_period))

    subject_line = f"Internal Checklist for {property_address}"
    email_body = f"Executed Date: {execution_date.strftime('%m/%d/%Y')}\n"
    email_body += f"Property Address: {property_address}\n\n"
    email_body += "Checklist:\n\n"
    email_body += f"1. [ ] Check on wiring instruction connection with title company by {next_workday(execution_date + datetime.timedelta(days=1)).strftime('%m/%d/%Y')}\n"
    email_body += f"2. [ ] Check on escrow deposit by {next_workday(execution_date + datetime.timedelta(days=2)).strftime('%m/%d/%Y')} (unless escrow period has passed)\n"
    email_body += f"3. [ ] Send insurance email from software by {next_workday(execution_date + datetime.timedelta(days=7)).strftime('%m/%d/%Y')}\n"
    email_body += f"4. [ ] Send conclusion of inspection period notice by {(inspection_end_date - datetime.timedelta(days=1)).strftime('%m/%d/%Y')}\n"
    email_body += f"5. [ ] Check with lender on appraisal ordering and client application by {next_workday(inspection_end_date + datetime.timedelta(days=1)).strftime('%m/%d/%Y')}\n"
    email_body += f"6. [ ] Check with lender on appraisal outcome and client application by {(financing_end_date - datetime.timedelta(days=5)).strftime('%m/%d/%Y')}\n"
    email_body += f"7. [ ] Send 'End of Financing Notice' by {(financing_end_date - datetime.timedelta(days=1)).strftime('%m/%d/%Y')}\n"
    email_body += f"8. [ ] Send closing notice #1 by {(closing_date - datetime.timedelta(days=7)).strftime('%m/%d/%Y')}\n"
    email_body += f"9. [ ] Send closing notice #2 by {(closing_date - datetime.timedelta(days=2)).strftime('%m/%d/%Y')}\n\n"
    email_body += f"Escrow End Date: {escrow_end_date.strftime('%m/%d/%Y')}\n"
    email_body += f"Inspection End Date: {inspection_end_date.strftime('%m/%d/%Y')}\n"
    email_body += f"Financing End Date: {financing_end_date.strftime('%m/%d/%Y')}\n"
    email_body += f"Closing Date: {closing_date.strftime('%m/%d/%Y')}\n\n"
    email_body += f"{agent_name}\n"
    email_body += f"{brokerage_name}"

    # Create a new window to display the email content
    email_window = tk.Toplevel(window)
    email_window.title("Internal Checklist")

    # Create a text widget to display the email content
    email_text = tk.Text(email_window, wrap=tk.WORD)
    email_text.insert(tk.END, f"Subject: {subject_line}\n\n{email_body}")
    email_text.pack(expand=True, fill=tk.BOTH)

    # Create a button to close the email window
    close_button = tk.Button(email_window, text="Close", command=email_window.destroy)
    close_button.pack()


# Create the main window
window = tk.Tk()
window.title("Real Estate Transaction Checklist")

# Create and pack the input fields
execution_date_label = tk.Label(window, text="Contract Execution Date (MM/DD/YYYY):")
execution_date_label.pack()
execution_date_entry = tk.Entry(window)
execution_date_entry.pack()

escrow_period_label = tk.Label(window, text="Escrow Period (in days):")
escrow_period_label.pack()
escrow_period_entry = tk.Entry(window)
escrow_period_entry.pack()

inspection_period_label = tk.Label(window, text="Inspection Period (in days):")
inspection_period_label.pack()
inspection_period_entry = tk.Entry(window)
inspection_period_entry.pack()

financing_period_label = tk.Label(window, text="Financing Period (in days):")
financing_period_label.pack()
financing_period_entry = tk.Entry(window)
financing_period_entry.pack()

closing_date_label = tk.Label(window, text="Closing Date (MM/DD/YYYY):")
closing_date_label.pack()
closing_date_entry = tk.Entry(window)
closing_date_entry.pack()

property_address_label = tk.Label(window, text="Property Address:")
property_address_label.pack()
property_address_entry = tk.Entry(window)
property_address_entry.pack()

client_names_label = tk.Label(window, text="Client's Names:")
client_names_label.pack()
client_names_entry = tk.Entry(window)
client_names_entry.pack()

agent_name_label = tk.Label(window, text="Agent's Name:")
agent_name_label.pack()
agent_name_entry = tk.Entry(window)
agent_name_entry.pack()

brokerage_name_label = tk.Label(window, text="Brokerage Name:")
brokerage_name_label.pack()
brokerage_name_entry = tk.Entry(window)
brokerage_name_entry.pack()

# Create and pack the generate buttons
generate_button = tk.Button(window, text="Generate Email", command=generate_email)
generate_button.pack()

generate_inspector_button = tk.Button(window, text="Generate Inspector Recommendations",
                                      command=generate_inspector_email)
generate_inspector_button.pack()

generate_internal_button = tk.Button(window, text="Generate Internal Checklist", command=generate_internal_checklist)
generate_internal_button.pack()

generate_inspection_notice_button = tk.Button(window, text="Generate End of Inspection Notice",
                                              command=generate_end_of_inspection_notice)
generate_inspection_notice_button.pack()

generate_financing_notice_button = tk.Button(window, text="Generate End of Financing Notice",
                                             command=generate_end_of_financing_notice)
generate_financing_notice_button.pack()

generate_closing_notice_1_button = tk.Button(window, text="Generate Closing Notice #1",
                                             command=generate_closing_notice_1)
generate_closing_notice_1_button.pack()

generate_closing_notice_2_button = tk.Button(window, text="Generate Closing Notice #2",
                                             command=generate_closing_notice_2)
generate_closing_notice_2_button.pack()

# Run the Tkinter event loop
window.mainloop()
