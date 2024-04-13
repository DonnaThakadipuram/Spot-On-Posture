import cv2
import mediapipe as mp
import numpy as np
import time
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose



#------------------------------------------

def calculate_angle(a,b,c):
    a = np.array(a) # First
    b = np.array(b) # Mid
    c = np.array(c) # End
    
    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = np.abs(radians*180.0/np.pi)
    
    if angle >180.0:
        angle = 360-angle
        
    return angle 




#------------------------------------------

def main():
    cap = cv2.VideoCapture(0)

    angle = 0

    count = 0

    stage = None

    text = None

    start_time = time.time()

    run = True

    ## Setup mediapipe instance
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while run:
            ret, frame = cap.read()
            
            # Recolor image to RGB
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
        
            # Make detection
            results = pose.process(image)
        
            # Recolor back to BGR
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            
            # Extract landmarks
            try:
                landmarks = results.pose_landmarks.landmark
                
                # Get coordinates
                shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
                wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
                
                # Calculate angle
                angle = calculate_angle(shoulder, elbow, wrist)
                
                # Visualize angle
                cv2.putText(image, str(angle), 
                            tuple(np.multiply(elbow, [640, 480]).astype(int)), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                                    )

                if angle > 170:
                    stage = "Up"
                    text = "Up"
                elif angle < 40 and stage == "Up":
                    stage = "Down"
                    text = "Down"
                    count += 1
                    
                        
            except:
                pass


            cv2.rectangle(image, (0,0), (225, 73), (245, 117, 16), -1)

            cv2.putText(image, 'REPS', (15,12), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
            cv2.putText(image, str(count), (10,60), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)

            cv2.putText(image, 'STAGE', (65,12), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
            cv2.putText(image, text, (60,60), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)
            
            
            # Render detections
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                    mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                    mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
                                    )               
            
            cv2.imshow(str(angle), image)

            key = cv2.waitKey(1)  # Check for key press events (1 millisecond delay)
            if key & 0xFF == ord('q'):
                print("pressed q")
                run = False  # Exit the loop if 'q' is pressed

            elapsed_time = time.time() - start_time
            if elapsed_time >= 15.0:  # Exit after 5 seconds
                print("time reached")
                run = False

    cap.release()
    cv2.destroyAllWindows()
    return count

result = main()



# Function to read data from file and return as a dictionary
def read_data(filename):
    person_data = {}
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            parts = line.split()
            name = parts[0]
            squat_number = int(parts[1])
            press_number = int(parts[2])
            person_data[name] = {'squat': squat_number, 'press': press_number}
    return person_data

# Function to write updated data back to file
def write_data(filename, data):
    with open(filename, 'w') as file:
        for name, info in data.items():
            squat_number = info['squat']
            press_number = info['press']
            file.write(f"{name} {squat_number} {press_number}\n")

# Read existing data from file
filename = 'database.txt'
person_data = read_data(filename)

# Open the file for reading
with open('name.txt', 'r') as file:
    name = file.readline()  # Read all lines from the file

# Update squat number for "Ananya" to a new value (e.g., 5)
target_person = name
if target_person in person_data:
    new_press_number = result  # New squat number for "Ananya"
    person_data[target_person]['press'] = new_press_number
    print(f"Updated press number for {target_person} to {new_press_number}")

    # Write updated data back to file
    write_data(filename, person_data)
else:
    print(f"{target_person} not found in the data.")

