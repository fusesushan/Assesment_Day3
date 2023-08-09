from abc import ABC, abstractmethod

# Abstract interface for notification senders
class NotificationSender(ABC):
    @abstractmethod
    def send_notification(self, recipient, message):
        pass

# Concrete implementation of NotificationSender for sending emails
class EmailSender(NotificationSender):
    def send_notification(self, recipient, message):
        # Code to send an email
        print(f"Sending email to {recipient}: {message}")

# High-level module: NotificationService
class NotificationService:
    def __init__(self, notification_sender):
        self.notification_sender = notification_sender

    def send_notification(self, recipient, message):
        self.notification_sender.send_notification(recipient, message)

# Creating an instance of the EmailSender (low-level module)
email_sender = EmailSender()

# Creating an instance of the NotificationService (high-level module) using Dependency Inversion
notification_service = NotificationService(email_sender)

# Sending a notification using the NotificationService
notification_service.send_notification("sushan.kattel@fusemachines.com", "Hello, Welcome to FuseMachines!!!")
