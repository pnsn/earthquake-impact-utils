#!/usr/bin/env python

# stdlib imports
import os.path
import sys
import tempfile
import shutil
import sys

# hack the path so that I can debug these functions if I need to
homedir = os.path.dirname(os.path.abspath(__file__))  # where is this script?
shakedir = os.path.abspath(os.path.join(homedir, '..', '..'))
# put this at the front of the system path, ignoring any installed mapio stuff
sys.path.insert(0, shakedir)

from impactutils.transfer.emailsender import EmailSender

def test_send(smtp_servers,sender,recipients):
    subject = 'Testing...'
    message = 'This is a test message.'
    cancel_msg = 'This is a cancel message.'
    zip_file = 'test.zip'
    props = {'smtp_servers':smtp_servers,
             'sender':sender,
             'subject':subject,
             'recipients':recipients,
             'message':message}
    thisfile = os.path.abspath(__file__) #where is this script?
    thisdir = os.path.dirname(os.path.abspath(__file__)) #what folder are we in?

    #send a file
    sender = EmailSender(properties=props,local_files=[thisfile])
    sender.send()
    sender.cancel(cancel_content=cancel_msg)

    #send a directory, and zip it
    props['zip_file'] = zip_file
    sender = EmailSender(properties=props,local_files=[thisfile])
    sender.send()
    sender.cancel(cancel_content=cancel_msg)

if __name__ == '__main__':
    smtp_server = sys.argv[1]
    sender = sys.argv[2]
    recipients = sys.argv[3:]
    test_send([smtp_server],sender,recipients)
