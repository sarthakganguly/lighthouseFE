# lighthouseFE
Simplify and Streamline Lighthouse Performance Testing

The LighthouseCLI Wrapper API is a command-line interface (CLI) tool that simplifies Lighthouse performance testing for web applications. With easy integration and streamlined workflows, developers can initiate Lighthouse tests effortlessly. Customize parameters, generate detailed reports, and automate testing in CI pipelines. Optimize your web app's speed and user experience with LighthouseCLI Wrapper API.

## Pre-requisites

This is a Flask app that returns the JSON report from Lighthouse CLI for the given URL.

## Requirements
- Python 3.6 or higher
- Flask
- Lighthouse CLI

## Installation
1. Install Python 3.6 or higher.
2. Install Flask:
`code` pip install Flask
3. Install Lighthouse CLI:
`code` npm install lighthouse-ci

## Usage
1. Start the Flask app
`code` python lighthouse-cli-flask-app.py
2. Open a web browser and navigate to http://localhost:5000.
3. Enter a URL in the input field and click the Submit button.
4. The JSON report from Lighthouse CLI for the given URL will be displayed.
5. Run the following command
`code` curl http://localhost:5000/?url=https://www.google.com

---
[Sarthak Ganguly (TheCodePost)](https://www.thecodepost.org/about)