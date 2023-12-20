import secrets
import string
from ..service.sendmail import send_email_background
from jinja2 import Environment, FileSystemLoader
from fastapi import BackgroundTasks
from ..service.sendmail import conf

class Utils():
    @staticmethod
    def generate_random_code():
        characters = string.ascii_letters + string.digits
        code = ''.join(secrets.choice(characters) for _ in range(6))
        return code
    
    def user_registration_authentication(background_tasks: BackgroundTasks, email, body_data):
        env = Environment(loader=FileSystemLoader(conf.TEMPLATE_FOLDER))
        template = env.get_template('emailVerification.html')
        # Render the template with the dictionary
        html_output = template.render(body_data)
        send_email_background(background_tasks, f'Registration E-mail Verification', f'{email}', html_output)
        return {"status": "success", "message": "User registered successfully"}
    
    def forgot_password_authentication(background_tasks: BackgroundTasks, email, body_data):
        env = Environment(loader=FileSystemLoader(conf.TEMPLATE_FOLDER))
        template = env.get_template('passwordverification.html')
        html_output = template.render(body_data)
        send_email_background(background_tasks, f'Forgot Password Verification', f'{email}', html_output)
        return {"status": "success", "message": "forgot password code sent successfully"}