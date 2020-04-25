from smtplib import SMTP
import email.message


def sendmailg(gserver , gport ,guser, gpass , mailfrom , mailto , subject , msg , ishtml = 0):
    mailmsg = email.message.Message()
    mailmsg['From'] = mailfrom
    mailmsg['To'] = mailto
    mailmsg['Subject'] = subject

    if ishtml == 1:
        mailmsg.add_header('Content-Type','text/html')
    else:
        mailmsg.add_header('Content-Type','text/plain')

    mailmsg.set_payload (msg, 'utf-8')
    with SMTP(gserver , gport)  as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(guser, gpass)
        smtp.sendmail(mailfrom, mailto,mailmsg.as_string())
        smtp.quit()
