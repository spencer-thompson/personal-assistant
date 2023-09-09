import imaplib
import email
import os
import socket
from dotenv import load_dotenv


# Email server settings
IMAP_SERVER = "imap.gmail.com"
load_dotenv()
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# Directory to save .txt files
SAVE_DIR = os.getenv("SAVE_DIR")

# Contact email address to filter by
SPECIFIC_CONTACT = os.getenv("SPECIFIC_CONTACT")


# Email extraction
def extract_text_from_email(email_address, email_password, specific_contact):
    try:
         # Email server settings
        IMAP_SERVER = 'imap.gmail.com'

        # Connect to the server
        imap_server = imaplib.IMAP4_SSL(IMAP_SERVER)

        # Log in to the email account
        imap_server.login(email_address, email_password)

        # Select the mailbox (inbox)
        mailbox = 'INBOX'
        imap_server.select(mailbox)

        # Search for unread emails from the specific contact
        search_query = f'(UNSEEN FROM "{specific_contact}")'
        status, email_ids = imap_server.search(None, search_query)

        # Check if there are any matching emails
        if email_ids[0]:
            # Get the latest unread email ID
            latest_email_id = email_ids[0].split()[-1]

            # Fetch the email content
            status, email_data = imap_server.fetch(latest_email_id, '(RFC822)')

            # Extract the .txt file content
            email_message = email.message_from_bytes(email_data[0][1])

            for part in email_message.walk():
                content_type = part.get_content_type()
                filename = part.get_filename()

                if filename and filename.endswith(".txt"):
                    # Read the .txt file content as a string
                    txt_content = part.get_payload(decode=True).decode()

                    # Print or use txt_content as needed
                    print("Text Content of .txt File:")
                    print(txt_content)
                    return str(txt_content)
        else:
            print(f"No matching unread emails from {specific_contact} found.")
            return "Empty"

        # Close the connection
        imap_server.logout()
    except socket.gaierror as e:
        print(f"DNS resolution failed: {str(e)}")
    except imaplib.IMAP4.error as e:
        print(f"IMAP error: {str(e)}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage:
# extract_text_from_email('your_email@example.com', 'your_password', 'contact@example.com')




# # Callable Method
# def process_latest_email_from_contact(email_address, email_password, specific_contact, save_dir):
#     try:
#         # Email server settings
#         IMAP_SERVER = 'imap.gmail.com'

#         # Connect to the server
#         imap_server = imaplib.IMAP4_SSL(IMAP_SERVER)

#         # Log in to the email account
#         imap_server.login(email_address, email_password)

#         # Select the mailbox (inbox)
#         mailbox = 'INBOX'
#         imap_server.select(mailbox)

#         # Search for unread emails from the specific contact
#         search_query = f'(UNSEEN FROM "{specific_contact}")'
#         status, email_ids = imap_server.search(None, search_query)

#         # Check if there are any matching emails
#         if email_ids[0]:
#             # Get the latest unread email ID
#             latest_email_id = email_ids[0].split()[-1]

#             # Fetch the email content
#             status, email_data = imap_server.fetch(latest_email_id, '(RFC822)')

#             # Extract and save attachments
#             email_message = email.message_from_bytes(email_data[0][1])

#             for part in email_message.walk():
#                 content_type = part.get_content_type()
#                 filename = part.get_filename()

#                 if filename and filename.endswith(".txt"):
#                     # Save the .txt file to the specified directory
#                     file_path = os.path.join(save_dir, filename)
#                     with open(file_path, "wb") as file:
#                         file.write(part.get_payload(decode=True))

#             print(f"Latest email from {specific_contact} with .txt attachments saved successfully.")
#             # List .txt files in the directory
#             # Text will be printed
#             txt_files = [f for f in os.listdir(SAVE_DIR) if f.endswith(".txt")]

#             for txt_file in txt_files:
#                 file_path = os.path.join(SAVE_DIR, txt_file)
                
#                 with open(file_path, 'r') as file:
#                     txt_content = file.read()
#                     print(f"Text file reads: '{txt_content}'")
#         else:
#             print(f"No matching unread emails from {specific_contact} found.")

    #     # Close the connection
    #     imap_server.logout()
    # except socket.gaierror as e:
    #     print(f"DNS resolution failed: {str(e)}")
    # except imaplib.IMAP4.error as e:
    #     print(f"IMAP error: {str(e)}")
    # except Exception as e:
    #     print(f"An error occurred: {str(e)}")

