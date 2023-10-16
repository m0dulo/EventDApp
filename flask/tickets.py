from flask import Blueprint, request, jsonify, abort

tickets_bp = Blueprint("tickets", __name__)

# Sample list of purchased tickets (replace with your data source)
purchased_tickets = []

@tickets_bp.route("/purchase", methods=["POST"])
def purchase_ticket():
    data = request.get_json()
    event_id = data.get("event_id")
    quantity = data.get("quantity")

    # Validate event_id and quantity, check if tickets are available
    event = next((e for e in events if e["id"] == event_id), None)
    if event is None or event["tickets"] < quantity:
        abort(400, description="Ticket purchase failed")

    # Deduct purchased tickets from available tickets
    event["tickets"] -= quantity

    # Record the purchase (in-memory for this example)
    purchased_tickets.append({"event_id": event_id, "quantity": quantity})

    return jsonify({"message": "Ticket purchase successful"}), 201

@tickets_bp.route("/purchased_tickets", methods=["GET"])
def get_purchased_tickets():
    return jsonify(purchased_tickets)
