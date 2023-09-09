import imapclient
from imapclient import IMAPClient

import receive_email

# Event listener
def on_new_email_handler(folder, uid, message_data):
    # This function will be called when a new email arrives.
    # You can add your email processing logic here.

    print("New email received:")
    print(f"Folder: {folder}")
    print(f"UID: {uid}")
    print(f"Message Data: {message_data}")

if __name__ == "__main__":
    # Connect to the IMAP server
    with IMAPClient(IMAP_SERVER) as client:
        client.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        client.select_folder('INBOX')

        # Start the IDLE mode to listen for new emails
        client.idle()

        # Add a callback function to handle new emails
        client.add_callback(on_new_email_handler, ['EXISTS'])

        # Keep the script running indefinitely
        print("Email listener started. Press Ctrl+C to exit.")
        try:
            while True:
                pass
        except KeyboardInterrupt:
            pass