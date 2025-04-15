from flask import Flask, jsonify, request

app = Flask(__name__)

# Define the image caption dictionary
image_captions = {
    "1_0_1.png": [
      "Batsman is ready to face the ball",
      "batsman is batting",
      "Batsman",
      "Batsman is going to bat",
      "Batsman is batting."
    ],
    "1_0_2.png": [
      "Batsman is ready to face the ball",
      "batsman is batting",
      "Batsman",
      "Batsman is going to bat",
      "Batsman is batting."
    ],
    "1_0_3.png": [
      "Batsman is ready to face the ball",
      "batsman is batting",
      "Batsman",
      "Batsman is going to bat",
      "Batsman is batting."
    ],
    "1_0_4.png": [
      "Batsman is ready to face the ball",
      "batsman is batting",
      "Batsman",
      "Batsman is going to bat",
      "Batsman is batting."
    ],
    "1_0_5.png": [
      "Batsman is ready to face the ball",
      "batsman is batting",
      "Batsman",
      "Batsman is going to bat",
      "Batsman is batting."
    ],
    "1_0_6.png": [
      "Batsman is ready to face the ball",
      "batsman is batting",
      "Batsman",
      "Batsman is going to bat",
      "Batsman is batting."
    ],
    "1_0_7.png": [
      "Batsman is ready to face the ball",
      "batsman is batting",
      "Batsman",
      "Batsman is going to bat",
      "Batsman is batting."
    ],
    "1_0_8.png": [
      "Batsman is ready to face the ball",
      "batsman is batting",
      "Batsman",
      "Batsman is going to bat",
      "Batsman is batting."
    ],
    "1_0_9.png": [
      "Batsman is ready to face the ball",
      "batsman is batting",
      "Batsman",
      "Batsman is going to bat",
      "Batsman is batting."
    ],
    "1_0_10.png": [
      "Batsman is ready to face the ball",
      "batsman is batting",
      "Batsman",
      "Batsman is going to bat",
      "Batsman is batting."
    ],
    "1_0_11.png": [
      "Batsman is ready to face the ball",
      "batsman is batting",
      "Batsman",
      "Batsman is going to bat",
      "Batsman is batting."
    ],
    "1_0_12.png": [
      "Batsman is ready to face the ball",
      "batsman is batting",
      "Batsman",
      "Batsman is going to bat",
      "Batsman is batting."
    ],
    "1_0_13.png": [
      "Batsman is ready to face the ball",
      "batsman is batting",
      "Batsman",
      "Batsman is going to bat",
      "Batsman is batting."
    ],
    "1_0_14.png": [
      "Batsman is ready to face the ball",
      "batsman is batting",
      "Batsman",
      "Batsman is going to bat",
      "Batsman is batting."
    ],
    "1_0_15.png": [
      "Batsman is ready to face the ball",
      "batsman is batting",
      "Batsman",
      "Batsman is going to bat",
      "Batsman is batting."
    ],
    "1_0_16.png": [
      "Batsman is ready to face the ball",
      "batsman is batting",
      "Batsman",
      "Batsman is going to bat",
      "Batsman is batting."
    ],
    "1_0_17.png": [
      "Batsman is ready to face the ball",
      "batsman is batting",
      "Batsman",
      "Batsman is going to bat",
      "Batsman is batting."
    ],
    "1_0_18.png": [
      "Batsman is ready to face the ball",
      "batsman is batting",
      "Batsman",
      "Batsman is going to bat",
      "Batsman is batting."
    ],
    "1_0_19.png": [
      "Batsman is ready to face the ball",
      "batsman is batting",
      "Batsman",
      "Batsman is going to bat",
      "Batsman is batting."
    ],
    "1_0_20.png": [
      "Batsman is ready to face the ball",
      "batsman is batting",
      "Batsman",
      "Batsman is going to bat",
      "Batsman is batting."
    ],
    "1_0_21.png": [
      "Batsman is ready to face the ball",
      "batsman is batting",
      "Batsman",
      "Batsman is going to bat",
      "Batsman is batting."
    ],
    "1_0_22.png": [
      "Batsman is ready to face the ball",
      "batsman is batting",
      "Batsman",
      "Batsman is going to bat",
      "Batsman is batting."
    ],
    "1_0_23.png": [
      "Batsman is ready to face the ball",
      "batsman is batting",
      "Batsman",
      "Batsman is going to bat",
      "Batsman is batting."
    ],
    "1_0_24.png": [
      "Batsman is ready to face the ball",
      "batsman is batting",
      "Batsman",
      "Batsman is going to bat",
      "Batsman is batting."
    ],
    "1_0_25.png": [
      "Batsman is ready to face the ball",
      "batsman is batting",
      "Batsman",
      "Batsman is going to bat",
      "Batsman is batting."
    ],
    "1_0_26.png": [
      "Bowler is bowling the ball",
      "Bowler is bowling ball to batsman",
      "There are two batsman and bowler and wicket keeper and umpire",
      "bowler is bowling to batsman.",
      "bowler is going to bowl to batsman."
    ],
    "1_0_27.png": [
      "Bowler is bowling the ball",
      "Bowler is bowling ball to batsman",
      "There are two batsman and bowler and wicket keeper and umpire",
      "bowler is bowling to batsman.",
      "bowler is going to bowl to batsman."
    ],
    "1_0_28.png": [
      "Bowler is bowling the ball",
      "Bowler is bowling ball to batsman",
      "There are two batsman and bowler and wicket keeper and umpire",
      "bowler is bowling to batsman.",
      "bowler is going to bowl to batsman."
    ],
    "1_0_29.png": [
      "Bowler is bowling the ball",
      "Bowler is bowling ball to batsman",
      "There are two batsman and bowler and wicket keeper and umpire",
      "bowler is bowling to batsman.",
      "bowler is going to bowl to batsman."
    ],
    "1_0_30.png": [
      "Bowler is bowling the ball",
      "Bowler is bowling ball to batsman",
      "There are two batsman and bowler and wicket keeper and umpire",
      "bowler is bowling to batsman.",
      "bowler is going to bowl to batsman."
    ],
    "1_0_31.png": [
      "Bolwer bowled the ball.",
      "bowler has bowled the ball.",
      "Bowler has bowled the ball batsman..."
    ]
  }
  

@app.route('/get_caption', methods=['GET'])
def get_caption():
    # Get image name from query parameters
    image_name = request.args.get('image_name')
    
    # Check if image name exists in the dictionary
    if image_name in image_captions:
        return jsonify({image_name: image_captions[image_name]})
    else:
        return jsonify({"error": "Image not found"}), 404

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
