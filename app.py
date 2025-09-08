from flask import Flask, render_template, request, flash, redirect, url_for
import smtplib
# ...existing code...
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# ...existing code...
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

# Portfolio data
portfolio_data = {
    'name': 'Aderine Perez',
    'title': 'Good Coder and Problem Solver',
    'location': 'Coimbatore, Tamil Nadu',
    'bio': 'Passionate full-stack developer specializing in Python, web technologies, and creative problem-solving. I love building innovative solutions that make a difference.',
    'skills': [
        {'name': 'Python', 'level': 90, 'category': 'Backend'},
        {'name': 'Flask', 'level': 85, 'category': 'Backend'},
        {'name': 'HTML/CSS', 'level': 88, 'category': 'Frontend'},
        {'name': 'JavaScript', 'level': 80, 'category': 'Frontend'},
        {'name': 'Git/GitHub', 'level': 85, 'category': 'Tools'},
        {'name': 'Problem Solving', 'level': 92, 'category': 'Core'},
    ],
    'projects': [
        {
            'title': 'WeatherCheck',
            'description': 'A comprehensive weather application where users can check weather information for any location worldwide. Features real-time data and intuitive interface.',
            'technologies': ['CSS', 'HTML', 'JavaScript', 'Weather API'],
            'github': 'https://github.com/Aderine2006/WeatherCheck',
            'type': 'Web Application',
            'status': 'Completed'
        },
        {
            'title': 'RecipeFinder',
            'description': 'An interactive web application that helps users discover recipes for their favorite dishes. Perfect for cooking enthusiasts looking for new culinary adventures.',
            'technologies': ['CSS', 'HTML', 'JavaScript', 'Recipe API'],
            'github': 'https://github.com/Aderine2006/RecipeFinder',
            'type': 'Web Application',
            'status': 'Completed'
        },
        {
            'title': 'QR Code Generator',
            'description': 'Advanced Python-based QR code generator with customization options including color changes, border adjustments, and resizing capabilities. Goes beyond basic black and white codes.',
            'technologies': ['Python', 'PIL', 'qrcode', 'tkinter'],
            'github': 'https://github.com/Aderine2006/Qrcode_generator',
            'type': 'Desktop Application',
            'status': 'Completed'
        }
    ],
    'social': {
        'github': 'https://github.com/Aderine2006',
        'linkedin': 'https://www.linkedin.com/in/aderine-perez',
        'leetcode': 'https://leetcode.com/u/Aderine_2487',
        'email': 'your.email@example.com'  # Update with your actual email
    }
}

@app.route('/')
def index():
    return render_template('index.html', data=portfolio_data)

@app.route('/contact')
def contact():
    return render_template('contact.html', data=portfolio_data)

@app.route('/send_message', methods=['POST'])
def send_message():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        
        # Here you can implement email sending logic
        # For now, we'll just flash a success message
        flash('Thank you for your message! I\'ll get back to you soon.', 'success')
        
        # In a real application, you might want to:
        # 1. Save to database
        # 2. Send email notification
        # 3. Use a service like SendGrid or Gmail SMTP
        
        return redirect(url_for('contact'))

@app.route('/project/<project_title>')
def project_detail(project_title):
    project = next((p for p in portfolio_data['projects'] if p['title'].lower().replace(' ', '') == project_title.lower()), None)
    if project:
        return render_template('project_detail.html', project=project, data=portfolio_data)
    else:
        flash('Project not found!', 'error')
        return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', data=portfolio_data), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)