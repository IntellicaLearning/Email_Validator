import csv
import re
import dns.resolver
import smtplib
import time


# This Python script is part of the Intellica Learning project.
# It is licensed under the MIT License.
# For more details, please refer to the LICENSE file provided with this project.

# Function to check if email syntax is valid
def is_valid_email(email):
    return re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email)


# Function to check if email is deliverable
def is_deliverable(email):
    # Check if "@" symbol is present in the email
    if '@' not in email:
        return False, "Invalid email syntax"

    # Split the email address to extract the domain
    domain = email.split('@')[1]

    # use try catch to handle exceptions
    try:
        # Query the MX records of the domain
        records = dns.resolver.resolve(domain, 'MX')
        mx_record = str(records[0].exchange)

        # Connect to the SMTP server of the domain
        server = smtplib.SMTP()
        server.set_debuglevel(0)
        server.connect(mx_record)
        server.helo(server.local_hostname)
        server.mail('me@domain.com')

        # Check the response code for the email address
        code, message = server.rcpt(str(email))
        server.quit()

        # If response code is 250, the email address is deliverable
        if code == 250:
            return True, "Email is deliverable"
        else:
            return False, "Email address does not exist or cannot receive mail"

    except dns.resolver.NXDOMAIN:
        return False, "No valid MX records found for the domain"

    except smtplib.SMTPConnectError:
        return False, "Could not connect to SMTP server"

    except smtplib.SMTPServerDisconnected:
        return False, "SMTP server disconnected"

    except Exception as e:
        return False, f"Error: {e}"


# Function to process CSV file
def process_csv(input_file, output_file):
    with open(input_file, 'r') as f_in, open(output_file, 'w', newline='') as f_out:
        reader = csv.DictReader(f_in)
        fieldnames = ['Email', 'Status', 'Remark']
        writer = csv.DictWriter(f_out, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            email = row['Email']
            if is_valid_email(email):
                status, remark = is_deliverable(email)
            else:
                status, remark = False, "Invalid email syntax"
            writer.writerow({'Email': email, 'Status': status, 'Remark': remark})
            # Adding delay to avoid IP blocking
            time.sleep(3)


if __name__ == "__main__":
    input_file = input("Enter the path of the CSV file: ")
    output_file = "output.csv"  # Change this to your desired output file
    process_csv(input_file, output_file)
