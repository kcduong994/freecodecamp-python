```python
"""
Build an Email Simulator

This workshop demonstrates object-oriented programming by simulating
email communication between users.

The program supports:
- Creating users with individual inboxes
- Sending emails between users
- Storing sender, receiver, subject, body, and timestamp information
- Listing emails in an inbox
- Tracking read and unread states
- Reading full email content
- Deleting emails
- Validating email numbers

Concepts practiced:
- Classes and objects
- Constructors and instance attributes
- Instance methods
- Object composition
- Lists and indexing
- Date and time formatting
- String representations
- Input validation
"""


import datetime


class Email:
    """
    Represent an email sent from one user to another.

    Each Email object stores its sender, receiver, subject, body,
    creation timestamp, and read status.
    """

    def __init__(self, sender, receiver, subject, body):
        """
        Initialize a new email.

        Args:
            sender: The User object sending the email.
            receiver: The User object receiving the email.
            subject: The subject line of the email.
            body: The main content of the email.
        """

        # Store the sender and receiver as User objects.
        self.sender = sender
        self.receiver = receiver

        # Store the email content.
        self.subject = subject
        self.body = body

        # Record the date and time when the email is created.
        self.timestamp = datetime.datetime.now()

        # New emails are unread by default.
        self.read = False

    def mark_as_read(self):
        """Mark the email as read."""

        self.read = True

    def display_full_email(self):
        """
        Display the complete email and mark it as read.

        The timestamp is formatted as:
        YYYY-MM-DD HH:MM
        """

        # Opening an email changes its status to read.
        self.mark_as_read()

        print("\n--- Email ---")
        print(f"From: {self.sender.name}")
        print(f"To: {self.receiver.name}")
        print(f"Subject: {self.subject}")
        print(
            f"Received: "
            f"{self.timestamp.strftime('%Y-%m-%d %H:%M')}"
        )
        print(f"Body: {self.body}")
        print("------------\n")

    def __str__(self):
        """
        Return a concise string representation of the email.

        This representation is used when displaying emails
        in an inbox listing.
        """

        # Select the label based on the current read status.
        status = "Read" if self.read else "Unread"

        return (
            f"[{status}] From: {self.sender.name} | "
            f"Subject: {self.subject} | "
            f"Time: {self.timestamp.strftime('%Y-%m-%d %H:%M')}"
        )


class User:
    """
    Represent a user who can send and receive emails.

    Each user has a name and an individual Inbox object.
    """

    def __init__(self, name):
        """
        Initialize a new user.

        Args:
            name: The display name of the user.
        """

        self.name = name

        # Every user receives a separate inbox.
        self.inbox = Inbox()

    def send_email(self, receiver, subject, body):
        """
        Create an email and deliver it to another user's inbox.

        Args:
            receiver: The User object receiving the email.
            subject: The email subject.
            body: The email body.
        """

        # Create a new Email object using the current user as sender.
        email = Email(
            sender=self,
            receiver=receiver,
            subject=subject,
            body=body,
        )

        # Add the new email to the receiver's inbox.
        receiver.inbox.receive_email(email)

        # Confirm successful delivery.
        print(
            f"Email sent from {self.name} "
            f"to {receiver.name}!\n"
        )

    def check_inbox(self):
        """Display all emails currently stored in the user's inbox."""

        print(f"\n{self.name}'s Inbox:")
        self.inbox.list_emails()

    def read_email(self, index):
        """
        Read an email using its displayed number.

        Args:
            index: The one-based email number shown to the user.
        """

        self.inbox.read_email(index)

    def delete_email(self, index):
        """
        Delete an email using its displayed number.

        Args:
            index: The one-based email number shown to the user.
        """

        self.inbox.delete_email(index)


class Inbox:
    """
    Store and manage the emails received by a user.

    The inbox supports receiving, listing, reading, and deleting emails.
    """

    def __init__(self):
        """Initialize an empty inbox."""

        self.emails = []

    def receive_email(self, email):
        """
        Add a received email to the inbox.

        Args:
            email: The Email object to store.
        """

        self.emails.append(email)

    def list_emails(self):
        """Display a numbered list of all emails in the inbox."""

        # Handle the case where the inbox contains no emails.
        if not self.emails:
            print("Your inbox is empty.\n")
            return

        print("\nYour Emails:")

        # Start numbering from 1 for a user-friendly display.
        for index, email in enumerate(self.emails, start=1):
            print(f"{index}. {email}")

    def read_email(self, index):
        """
        Display a selected email.

        Args:
            index: The one-based email number selected by the user.
        """

        # Stop if there are no emails to read.
        if not self.emails:
            print("Inbox is empty.\n")
            return

        # Convert the displayed one-based number to a zero-based index.
        actual_index = index - 1

        # Validate that the requested email exists.
        if actual_index < 0 or actual_index >= len(self.emails):
            print("Invalid email number.\n")
            return

        # Displaying the email also marks it as read.
        self.emails[actual_index].display_full_email()

    def delete_email(self, index):
        """
        Delete a selected email.

        Args:
            index: The one-based email number selected by the user.
        """

        # Stop if there are no emails to delete.
        if not self.emails:
            print("Inbox is empty.\n")
            return

        # Convert the displayed one-based number to a zero-based index.
        actual_index = index - 1

        # Validate that the requested email exists.
        if actual_index < 0 or actual_index >= len(self.emails):
            print("Invalid email number.\n")
            return

        # Remove the selected email from the list.
        del self.emails[actual_index]

        print("Email deleted.\n")


def main():
    """Demonstrate the main features of the email simulator."""

    # Create two users with separate inboxes.
    tory = User("Tory")
    ramy = User("Ramy")

    # Tory sends an email to Ramy.
    tory.send_email(
        ramy,
        "Hello",
        "Hi Ramy, just saying hello!",
    )

    # Ramy sends a reply to Tory.
    ramy.send_email(
        tory,
        "Re: Hello",
        "Hi Tory, hope you are fine.",
    )

    # Ramy checks his inbox and sees one unread email.
    ramy.check_inbox()

    # Ramy opens the first email, which marks it as read.
    ramy.read_email(1)

    # Ramy deletes the first email.
    ramy.delete_email(1)

    # Ramy checks his inbox again to confirm the deletion.
    ramy.check_inbox()


# Run the demonstration only when this file is executed directly.
if __name__ == "__main__":
    main()
```
