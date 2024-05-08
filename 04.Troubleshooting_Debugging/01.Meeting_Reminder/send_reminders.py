#!/usr/bin/env python3

import sys
import smtplib
import datetime
import email


def usage():
    print("send_reminders: Send meeting reminders")
    print()
    print("invcation:")
    print("send_reminders date|title|emails")
    return 1


def dow(date):
    dateobj = datetime.datetime.strptime(date, "%Y-%m-%d")
    return dateobj.strftime("%A")


def message_template(date, title):
    message = email.message.EmailMessage()
    weekday = dow(date)
    message['Subject'] = "Meeting Reminder: {}".format(title)
    message.set_content(f'''
Hi All,

This is a reminder that you have a meeting with {title} on {date} ({weekday}).

See you there!
                        ''')


def send_message(message, emails):
    server = smtplib.SMTP('localhost')
    message["From"] = "AhindraD@github.com"
    for email in emails.split(','):
        message["To"] = email
        server.send_message(message)
    server.quit()
    pass


def main():
    if len(sys.argv) < 2:
        return usage()

    try:
        date, title, emails = sys.argv[1].split('|')
        message = message_template(date, title)
        send_message(message, emails)
        print("Successfully sent reminders to:", emails)
    except Exception as e:
        print("Failure to send email", file=sys.stderr)
    except Exception as e:
        print("Failure to send email: {}".format(e), file=sys.stderr)


if __name__ == "__main__":
    sys.exit(main())
