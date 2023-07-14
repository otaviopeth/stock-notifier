import smtplib
import sys


def send_mail(message, stock_ticker, msg_to):
    try:
        smtp_obj = smtplib.SMTP('smtp.outlook.com', 587)
        smtp_obj.ehlo()
        smtp_obj.starttls()
        msg_from = ''
        from_pass = ''
        smtp_obj.login(msg_from, from_pass)
        msg = '''
                {}
                '''.format(message)
        smtp_obj.sendmail(msg_from, msg_to, 'Subject: {} \n{}'.format(stock_ticker, msg))
        smtp_obj.quit()

    except:
        sys.exit()
