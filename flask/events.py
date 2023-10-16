from flask import Blueprint, request, jsonify, abort

events_bp = Blueprint("events", __name__)

# Sample list of events (replace with your data source)
events = [
    {"id": 1, "name": "Event 1", "description": "Description for Event 1", "tickets": 100},
    {"id": 2, "name": "Event 2", "description": "Description for Event 2", "tickets": 50},
    {"id": 3, "name": "Event 3", "description": "Description for Event 3", "tickets": 200},
]

@events_bp.route("/events", methods=["GET"])
def get_events():
    return jsonify(events)

@events_bp.route("/events/<int:event_id>", methods=["GET"])
def get_event(event_id):
    event = next((e for e in events if e["id"] == event_id), None)
    if event is None:
        abort(404)
    return jsonify(event)

@events_bp.route("/events", methods=["POST"])
def create_event():
    data = request.get_json()
    new_event = {
        "id": len(events) + 1,
        "name": data["name"],
        "description": data["description"],
        "tickets": data["tickets"],
    }
    events.append(new_event)
    return jsonify(new_event), 201

@events_bp.route("/events/<int:event_id>", methods=["PUT"])
def update_event(event_id):
    data = request.get_json()
    event = next((e for e in events if e["id"] == event_id), None)
    if event is None:
        abort(404)
    event["name"] = data["name"]
    event["description"] = data["description"]
    event["tickets"] = data["tickets"]
    return jsonify(event)

@events_bp.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    event = next((e for e in events if e["id"] == event_id), None)
    if event is None:
        abort(404)
    events.remove(event)
    return jsonify({"message": "Event deleted"}), 204
