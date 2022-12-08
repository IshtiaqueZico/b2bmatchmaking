# Python backend
from flask import Flask, request

app = Flask(__name__)

@app.route('/match', methods=['POST'])
def match():
  # Parse the list of companies and preferences from the request
  companies = request.form['companies'].split(',')
  preferences = request.form['preferences']

  # Create a list of pairs, with each pair containing a company and their preferred partner
  pairs = [(c, preferences[c]) for c in companies]

  # Sort the pairs in descending order of preference
  pairs.sort(key=lambda x: x[1], reverse=True)

  # Initialize the list of matched pairs
  matches = []

  # Iterate over the pairs and match each company with their preferred partner
  for (c1, p1), (c2, p2) in zip(pairs, pairs[1:]):
    # If the first company's preferred partner is the second company and vice versa, they are a match
    if c1 == p2 and c2 == p1:
      matches.append((c1, c2))

  # Return the list of matched pairs
  return str(matches)

if __name__ == '__main__':
  app.run()
