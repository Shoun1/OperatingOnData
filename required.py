from flask import Flask, jsonify, request
import cv2

app = Flask(__name__)

previous_enemy_locations = []

def detect_enemies_in_frame():
    # Dummy positions for now — replace with your actual detection logic
    return [(150, 220), (450, 300), (640, 480)]


@app.route('/track_movements', methods=['GET'])
def track_movements():
    global previous_enemy_locations
    
    # Detect current enemies
    enemy_locations = detect_enemies_in_frame()

    current_sectors = []
    for enemy in enemy_locations:
        sector_x = enemy[0] // 100
        sector_y = enemy[1] // 100
        current_sectors.append((sector_x, sector_y))

    # Detect movement by comparing sectors
    new_movements = []
    for sec in current_sectors:
        if sec not in previous_enemy_locations:
            new_movements.append({"sector": sec})

    # Update previous locations for next frame
    previous_enemy_locations = current_sectors

    return jsonify({
        "status": "success",
        "new_movements_detected": new_movements
    })


if __name__ == '__main__':
    app.run(debug=True) 
