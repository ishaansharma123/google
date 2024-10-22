from flask import Flask, request, render_template
from google_images_download import google_images_download
import os

app = Flask(__name__)

def download_images(keyword, limit):
    response = google_images_download.googleimagesdownload()
    arguments = {"keywords": keyword, "limit": limit, "print_urls": True, "output_directory": "downloads", "image_directory": keyword}
    paths = response.download(arguments)
    return paths

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    keyword = request.form['keyword']
    limit = int(request.form['limit'])

    download_images(keyword, limit)
    
    return f"Downloaded {limit} images for keyword: {keyword}. Check the 'downloads' folder."

if __name__ == '__main__':
    
    if not os.path.exists('downloads'):
        os.makedirs('downloads')
    app.run(debug=True)
