from flask import Flask, jsonify
from notion_client import Client
import os

app = Flask(__name__)

notion = Client(auth=os.getenv("NOTION_API_KEY"))

# Reemplaza con el ID de tu base de datos de Notion
database_id = "3ebb2b66e34747f8b7fd5294e9e51bd2"

@app.route('/notion-data', methods=['GET'])
def get_notion_data():
    try:
        response = notion.databases.query(database_id=database_id)
        return jsonify(response['results'])
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True)
