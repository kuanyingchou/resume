import string

template = string.Template('''

To: 
$email

Hi, $recipient, 

I just saw your posting on Hacker News and am very interested in the $job_title openings at $company. Your company looks very exciting. I'm an engineer from Taiwan with 2.5 years of experience on Android, Web, and Unity3D. You can find more about me in the attachment. Thank you!


Kuan-Ying Chou
Email: kuanyingchou@gmail.com
Phone: (626) 461-4809
Address: 398 Lyndale Ave, San Jose, CA 95127
''')

recipient = raw_input("$recipient: ")
email = raw_input("$email: ")
job_title = raw_input("$job_title: ")
company = raw_input("$company_name: ")

print(template.substitute(
        email = email,
        recipient = recipient, 
        job_title = job_title, 
        company = company))
