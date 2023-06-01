from flask import Flask, request
import subprocess
import json
import os
import urllib.parse

def strip_domain_name(url):
  """Strips the domain name from the given URL."""
  parsed_url = urllib.parse.urlparse(url)
  domain_name = parsed_url.netloc
  return domain_name

def read_file(filename):
  """Reads the contents of the file and returns a string."""
  with open(filename, "r") as f:
    return f.read()

# lighthouse https://google.com --output=json --output-path=./report.json
app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
  """Returns the JSON report from Lighthouse CLI for the given URL."""
  url = request.args.get("url")
  if not url:
    return "Please provide a URL."

  chromeFlags = "--headless"
  options = " --output=json --quiet --output-path=./"+ strip_domain_name(url) + "report.json"
  lighthouse_command = "lighthouse" + " " + url + options
  print('command = '+ lighthouse_command)
  lighthouse_process = subprocess.call(lighthouse_command, shell=True)
  print('Processed')
  lighthouse_output = read_file(strip_domain_name(url)+'report.json')

  print('Output =' + lighthouse_output)
  lighthouse_report = json.loads(lighthouse_output)
  return "1"

if __name__ == "__main__":
  app.run(debug=False)