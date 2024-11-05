import json
import uuid
from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
# Sample data for demonstration (replace with your actual data)
board_data = [
    {
        "_id": "board-id-01",
        "title": "ZungBii's Trello Board",
        "description": "Trello Web",
        "type": "public",  # 'private'
        "ownerIds": [],  # Users as board admins
        "memberIds": [],  # Users as board members
        "columnOrderIds": [
            "column-id-1",
            "column-id-2",
            "column-id-3",
            "column-id-4",
        ],  # Column order
        "columns": [
            {
                "_id": "column-id-1",
                "boardId": "board-id-01",
                "title": "To Do Column 01",
                "cardOrderIds": [
                    "card-id-01",
                    "card-id-02",
                    "card-id-03",   
                    "card-id-04",
                    "card-id-05",
                    "card-id-06",
                    "card-id-07",
                ],
                "cards": [
                    {
                        "_id": "card-id-01",
                        "columnId": "column-id-1",
                        "title": "Title of card 01",
                        "description": "Markdown Syntax (advanced topic)",
                        "cover": "https://trungquandev.com/wp-content/uploads/2022/07/fair-mern-stack-advanced-banner-trungquandev.jpg",
                        "memberIds": ["test-user-id-01"],
                        "comments": ["test comment 01", "test comment 02"],
                        "attachments": ["test attachment 01", "test attachment 02", "test attachment 03"],
                    },
                    {
                        "_id": "card-id-02",
                        "columnId": "column-id-1",
                        "title": "Title of card 02",
                        "description": None,
                        "cover": None,
                        "memberIds": [],
                        "comments": [],
                        "attachments": [],
                    },
                    {
                        "_id": "card-id-03",
                        "columnId": "column-id-1",
                        "title": "Title of card 03",
                        "description": None,
                        "cover": None,
                        "memberIds": [],
                        "comments": [],
                        "attachments": [],
                    },
                    {
                        "_id": "card-id-04",
                        "columnId": "column-id-1",
                        "title": "Title of card 04",
                        "description": None,
                        "cover": None,
                        "memberIds": [],
                        "comments": [],
                        "attachments": [],
                    },
                    {
                        "_id": "card-id-05",
                        "columnId": "column-id-1",
                        "title": "Title of card 05",
                        "description": None,
                        "cover": None,
                        "memberIds": [],
                        "comments": [],
                        "attachments": [],
                    },
                    {
                        "_id": "card-id-06",
                        "columnId": "column-id-1",
                        "title": "Title of card 06",
                        "description": None,
                        "cover": None,
                        "memberIds": [],
                        "comments": [],
                        "attachments": [],
                    },
                    {
                        "_id": "card-id-07",
                        "columnId": "column-id-1",
                        "title": "Title of card 07",
                        "description": None,
                        "cover": None,
                        "memberIds": [],
                        "comments": [],
                        "attachments": [],
                    },
                ],
            },
            {
                "_id": "column-id-2",
                "boardId": "board-id-01",
                "title": "Inprogress Column 02",
                "cardOrderIds": ["card-id-08", "card-id-09", "card-id-10"],
                "cards": [
                    {
                        "_id": "card-id-08",
                        "columnId": "column-id-2",
                        "title": "Title of card 08",
                        "description": None,
                        "cover": None,
                        "memberIds": [],
                        "comments": [],
                        "attachments": [],
                    },
                    {
                        "_id": "card-id-09",
                        "columnId": "column-id-2",
                        "title": "Title of card 09",
                        "description": None,
                        "cover": None,
                        "memberIds": [],
                        "comments": [],
                        "attachments": [],
                    },
                    {
                        "_id": "card-id-10",
                        "columnId": "column-id-2",
                        "title": "Title of card 10",
                        "description": None,
                        "cover": None,
                        "memberIds": [],
                        "comments": [],
                        "attachments": [],
                    },
                ],
            },
            {
                "_id": "column-id-3",
                "boardId": "board-id-01",
                "title": "Done Column 03",
                "cardOrderIds": ["card-id-11", "card-id-12", "card-id-13"],
                "cards": [
                    {
                        "_id": "card-id-11",
                        "columnId": "column-id-3",
                        "title": "Title of card 11",
                        "description": None,
                        "cover": None,
                        "memberIds": [],
                        "comments": [],
                        "attachments": [],
                    },
                    {
                        "_id": "card-id-12",
                        "columnId": "column-id-3",
                        "title": "Title of card 12",
                        "description": None,
                        "cover": None,
                        "memberIds": [],
                        "comments": [],
                        "attachments": [],
                    },
                    {
                        "_id": "card-id-13",
                        "columnId": "column-id-3",
                        "title": "Title of card 13",
                        "description": None,
                        "cover": None,
                        "memberIds": [],
                        "comments": [],
                        "attachments": [],
                    },
                ],
            },
            {
                "_id": "column-id-4",
                "boardId": "board-id-01",
                "title": "Nothing Column 04",
                "cardOrderIds": ["column-id-4-placeholder-card"],
                "cards": [
                    {
                        "_id": "column-id-4-placeholder-card",
                        "columnId": "column-id-4",
                        "FE_PlaceholderCard": True,  # Flag for frontend placeholder
                    },
                ],
            },
        ],
    }
]


@app.route('/boards/<board_id>', methods=['GET'])
def get_board(board_id):
    for board in board_data:
        if board["_id"] == board_id:
            return jsonify(board), 200
    return jsonify({'error': 'Board not found with ID: ' + board_id}), 404

@app.route('/boards/<board_id>/columns', methods=['POST'])
def add_column(board_id):
    new_column_data = request.get_json()

    # Check if the board exists
    for board in board_data:
        if board["_id"] == board_id:
            # Generate a new unique ID for the column
            new_column_id = len(board['columns']) + 1  # Incremental ID based on existing columns
            new_column_id_str = f"column-id-{uuid.uuid4()}"  # Format ID as "column-id-XX"
            
            # Prepare the new column
            new_column = {
                "_id": new_column_id_str,
                "boardId": board_id,
                "title": new_column_data["title"],
                "cardOrderIds": [],
                "cards": [],
            }

            # Create a placeholder card
            placeholder_card = {
                "_id": f"{new_column_id_str}-placeholder-card",  # Corrected placeholder ID
                "boardId": board_id,
                "columnId": new_column_id_str,
                "FE_PlaceholderCard": True,
            }

            # Add the placeholder card to the new column
            new_column["cards"].append(placeholder_card)
            new_column["cardOrderIds"].append(placeholder_card["_id"])

            # Add the new column to the board's columns and columnOrderIds
            board["columns"].append(new_column)
            board["columnOrderIds"].append(new_column["_id"])

            return jsonify(new_column), 201  # Respond with the newly created column

    return jsonify({'error': f'Board not found with ID: {board_id}'}), 404

@app.route('/boards/<board_id>/columns/<column_id>/cards', methods=['POST'])
def add_card(board_id, column_id):
    new_card_data = request.get_json()
    new_card_id = f"card-id-{uuid.uuid4()}"

    new_card = {
        "_id": new_card_id,
        "columnId": column_id,
        **new_card_data  # This will unpack the other card data (title, description, etc.)
    }

    # Validate and process card data
    for board in board_data:
        if board["_id"] == board_id:
            for column in board["columns"]:
                if column["_id"] == column_id:
                    # Add the new card to the column's cards list
                    column["cards"].append(new_card)
                    # Update cardOrderIds to reflect the new card
                    column["cardOrderIds"].append(new_card["_id"])
                    return jsonify(new_card), 201  # Return the new card and a 201 status
            break
    return jsonify({'error': 'Board not found with ID: ' + board_id}), 404

@app.route('/boards/<board_id>/columns/<column_id>', methods=['DELETE'])
def remove_column(board_id, column_id):
    # Find the board by ID
    for board in board_data:
        if board["_id"] == board_id:
            # Find and remove the column by ID
            board["columns"] = [col for col in board["columns"] if col["_id"] != column_id]
            # Update columnOrderIds to remove the column ID
            board["columnOrderIds"] = [col_id for col_id in board["columnOrderIds"] if col_id != column_id]
            return jsonify({"message": f"Column {column_id} deleted successfully"}), 201
    
    return jsonify({"error": f"Board or Column not found with IDs: {board_id}, {column_id}"}), 404

@app.route('/boards/<board_id>/columns/<column_id>/cards/<card_id>', methods=['DELETE'])
def remove_card(board_id, column_id, card_id):
    # Find the board by ID
    for board in board_data:
        if board["_id"] == board_id:
            # Find the column by ID within the board
            for column in board["columns"]:
                if column["_id"] == column_id:
                    # Find the card by ID within the column
                    column["cards"] = [card for card in column["cards"] if card["_id"] != card_id]
                    column["cardOrderIds"] = [cid for cid in column["cardOrderIds"] if cid != card_id]
                    return jsonify({"message": f"Card {card_id} removed successfully"}), 201
            return jsonify({'error': f'Column not found with ID: {column_id}'}), 404
    return jsonify({'error': f'Board not found with ID: {board_id}'}), 404


@app.route('/boards/<board_id>/columns/<column_id>', methods=['PUT'])
def update_column(board_id, column_id):
    updated_column_data = request.get_json()

    # Find the board by ID
    for board in board_data:
        if board["_id"] == board_id:
            # Find the column and update its details
            for col in board["columns"]:
                if col["_id"] == column_id:
                    col.update(updated_column_data)
                    return jsonify(col), 201
    
    return jsonify({"error": f"Board or Column not found with IDs: {board_id}, {column_id}"}), 404

@app.route('/boards/<board_id>/columns/<column_id>/cards/<card_id>', methods=['PUT'])
def update_card(board_id, column_id, card_id):
    updated_card_data = request.get_json()

    # Find the board by ID
    for board in board_data:
        if board["_id"] == board_id:
            # Find the column by ID within the board
            for column in board["columns"]:
                if column["_id"] == column_id:
                    # Find the card by ID within the column and update it
                    for idx, card in enumerate(column["cards"]):
                        if card["_id"] == card_id:
                            column["cards"][idx] = updated_card_data
                            return jsonify(updated_card_data), 201
                    return jsonify({'error': f'Card not found with ID: {card_id}'}), 404
            return jsonify({'error': f'Column not found with ID: {column_id}'}), 404
    return jsonify({'error': f'Board not found with ID: {board_id}'}), 404


@app.route('/boards/<board_id>/columns/<column_id>/cards/<card_id>/move', methods=['PUT'])
def move_card(board_id, column_id, card_id, target_column_id):
    board = get_board(board_id)
    if board:
        for column in board['columns']:
            if column['_id'] == column_id:
                for card in column['cards']:
                    if card['_id'] == card_id:
                        column['cards'].remove(card)
                        break
                break
        for column in board['columns']:
            if column['_id'] == target_column_id:
                column['cards'].append(card)
                break
        update_board(board)
        return jsonify({'message': 'Card moved successfully'}), 200
    else:
        return jsonify({'error': 'Board not found with ID: ' + board_id}), 404

def update_board(board):
    # Replace this with your actual board update logic (e.g., saving to a database)
    global board_data  # Assuming board_data is a global variable
    board_data = board

if __name__ == '__main__':
    app.run(debug=True)


