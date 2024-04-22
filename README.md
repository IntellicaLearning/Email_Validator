  Email Validator

Email Validator ✉️
==================

Features 🚀
-----------

*   Validates email syntax using regular expressions.
*   Checks if the email domain has valid MX (Mail Exchange) records.
*   Establishes an SMTP connection to the recipient's mail server to verify deliverability.
*   Outputs the validation results (status and remarks) to an output CSV file.

Prerequisites 📋
----------------

*   Python 3.x 🐍
*   Required Python packages:
    *   `dnspython`: for DNS resolution.
    *   `smtplib`: for SMTP connection.

You can install the required packages using `pip`:

    pip install dnspython

Usage 📝
--------

1.  Clone or download the repository to your local machine.
2.  Navigate to the directory containing the Python script.
3.  Run the script by executing the following command:

    python email_validator.py

When prompted, enter the path of the CSV file containing the list of email addresses to validate.

The script will process the CSV file and generate an output CSV file (`output.csv`) with validation results.

Input CSV Format 📄
-------------------

The input CSV file should have at least one column containing email addresses. The script expects the header of this column to be labeled as `Email`.

Example input CSV format:

    Email
    Chintu@example.com
    Rishi@Intellica.in
    

Output CSV Format 📤
--------------------

The output CSV file (`output.csv`) will contain three columns:

1.  `Email`: The email address.
2.  `Status`: Boolean value indicating whether the email is deliverable (`True`) or not (`False`).
3.  `Remark`: Additional information about the validation result.

Notes 📝
--------

*   To avoid being blocked by mail servers, the script adds a delay of 3 seconds between each email validation request.
*   Ensure that your network connection allows DNS resolution and SMTP connections.

License 📄
----------

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
