from flask import Flask, jsonify, request
from models import Card, Column, Board

app = Flask(__name__)

# Replace with your actual data or load from a database (based on mock-data.js)
boards = {
    "board-id-01": Board(
        _id="board-id-01",
        title="ZungBii's Trello Board",
        description="Trello Web",
        type="public",
        owner_ids=[],  # Replace with actual user IDs
        member_ids=[],  # Replace with actual user IDs
        column_order_ids=[
            "column-id-01",
            "column-id-02",
            "column-id-03",
            "column-id-04",
        ],
        columns=[
            Column(
                _id="column-id-01",
                board_id="board-id-01",
                title="To Do Column 01",
                card_order_ids=[
                    "card-id-01",
                    "card-id-02",
                    "card-id-03",
                    "card-id-04",
                    "card-id-05",
                    "card-id-06",
                    "card-id-07",
                ],
                cards=[
                    Card(
                        _id="card-id-01",
                        board_id="board-id-01",
                        column_id="column-id-01",
                        title="Title of card 01",
                        description="Markdown Syntax (sẽ ở khóa nâng cao nhé)",
                        cover="https://trungquandev.com/wp-content/uploads/2022/07/fair-mern-stack-advanced-banner-trungquandev.jpg",
                        member_ids=[],  # Replace with actual user IDs
                        comments=["test comment 01", "test comment 02"],
                        attachments=["test attachment 01", "test attachment 02", "test attachment 03"],
                    ),
                    Card(
                         _id='card-id-02', boardId='board-id-01', columnId='column-id-01', title='Title of card 02', description=None, cover=None, memberIds=[], comments=[], attachments=[]
                    ),
                    Card(
                         _id='card-id-03', boardId='board-id-01', columnId='column-id-01', title='Title of card 03', description=None, cover=None, memberIds=[], comments=[], attachments=[]
                    ),
                    Card(
                         _id='card-id-04', boardId='board-id-01', columnId='column-id-01', title='Title of card 04', description=None, cover=None, memberIds=[], comments=[], attachments=[]
                    ),
                    Card(
                         _id='card-id-05', boardId='board-id-01', columnId='column-id-01', title='Title of card 05', description=None, cover=None, memberIds=[], comments=[], attachments=[]
                    ),
                    Card(
                         _id='card-id-06', boardId='board-id-01', columnId='column-id-01', title='Title of card 06', description=None, cover=None, memberIds=[], comments=[], attachments=[]
                    ),
                    Card(
                         _id='card-id-07', boardId='board-id-01', columnId='column-id-01', title='Title of card 07', description=None, cover=None, memberIds=[], comments=[], attachments=[]
                    ),
                ],
            ),
            Column(
                _id="column-id-02",
                board_id="board-id-01",
                title="Inprogress Column 02",
                card_order_ids=["card-id-08", "card-id-09", "card-id-10"],
                cards=[
                    Card(
                        _id="card-id-08",
                        board_id="board-id-01",
                        column_id="column-id-02",
                        title="Title of card 08",
                        description=None,
                        cover=None,
                        member_ids=[],  # Replace with actual user IDs
                        comments=[],
                        attachments=[],
                    ),
                    Card(
                         _id='card-id-09', boardId='board-id-01', columnId='column-id-02', title='Title of card 09', description=None, cover=None, memberIds=[], comments=[], attachments=[]
                    ),
                    Card(
                         _id='card-id-10', boardId='board-id-01', columnId='column-id-02', title='Title of card 10', description=None, cover=None, memberIds=[], comments=[], attachments=[]
                    ),
                ],
            ),
            Column(
                _id="column-id-03",
                board_id="board-id-01",
                title="Done Column 03",
                card_order_ids=["card-id-11", "card-id-12", "card-id-13"],
                cards=[
                    Card(
                        _id="card-id-11",
                        board_id="board-id-01",
                        column_id="column-id-03",
                        title="Title of card 11",
                        description=None,
                        cover=None,
                        member_ids=[],  # Replace with actual user IDs
                        comments=[],
                        attachments=[],
                    ),
                    Card(
                         _id='card-id-12', boardId='board-id-01', columnId='column-id-03', title='Title of card 12', description=None, cover=None, memberIds=[], comments=[], attachments=[]
                    ),
                    Card(
                         _id='card-id-13', boardId='board-id-01', columnId='column-id-03', title='Title of card 13', description=None, cover=None, memberIds=[], comments=[], attachments=[]
                    ),
                ],
            ),
            Column(
                _id="column-id-04",
                board_id="board-id-01",
                title="Nothing Column 04",
                card_order_ids=["column-id-04-placeholder-card"],
                cards=[
                    Card(
                        _id="card-id-14",
                        board_id="board-id-01",
                        column_id="column-id-04",
                        is_placeholder=True  
                    ),
                ],
            ),
        ],
    )
}

# ... API endpoints for retrieving and updating boards, columns, and cards

if __name__ == "__main__":
    app.run(debug=True)