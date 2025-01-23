# import math

# # Fungsi untuk menghitung jarak antar dua titik
# def calculate_distance(x1, y1, x2, y2):
#     return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# # Fungsi untuk mendapatkan robot terdekat dengan bola
# def get_closest_robot(robots, ball_position):
#     closest_robot = None
#     min_distance = float('inf')
#     for robot in robots:
#         if robot['role'] != "kiper":  # Kiper tidak mengejar bola
#             distance = calculate_distance(robot['position'][0], robot['position'][1], ball_position[0], ball_position[1])
#             if distance < min_distance:
#                 min_distance = distance
#                 closest_robot = robot
#     return closest_robot

# # Fungsi untuk mengatur pergerakan robot
# def move_robot_towards_ball(robot):
#     robot['is_moving'] = True

# def display_status(robot):
#     status = "bergerak" if robot['is_moving'] else "diam"
#     print(f"{robot['name']} ({robot['role']}) berada di {robot['position']}, status: {status}")

# def display_positions(robots, ball_position):
#     print(f"Posisi Bola: {ball_position}")
#     for robot in robots:
#         display_status(robot)

# # Decision tree untuk menentukan aksi robot
# def decision_tree(robots, ball_position):
#     closest_robot = get_closest_robot(robots, ball_position)
#     for robot in robots:
#         if robot == closest_robot:
#             move_robot_towards_ball(robot)
#         else:
#             robot['is_moving'] = False

# def main():
#     kiper = {"name": "Kiper", "role": "kiper", "position": (100, 300), "is_moving": False}
#     back = {"name": "Back", "role": "back", "position": (300, 300), "is_moving": False}
#     striker = {"name": "Striker", "role": "striker", "position": (600, 300), "is_moving": False}
#     robots = [kiper, back, striker]

#     ball_position = (400, 300)  # Posisi awal bola

#     running = True
#     while running:
#         # Simulasi pergerakan bola atau input lainnya
#         ball_position = (ball_position[0] + 1, ball_position[1])  # Misal bola bergerak

#         decision_tree(robots, ball_position)
#         display_positions(robots, ball_position)

#         # Simulasi berhenti setelah beberapa iterasi (contoh)
#         if ball_position[0] > 450:
#             running = False

# if __name__ == "__main__":
#     main()



import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn import tree

# Langkah 1-2: Membaca dataset dari CSV dan menampilkannya
data = pd.read_csv('/home/joan/Downloads/BASESTATION - R2C - WARRIOR (coba)/assets/decision_tree_dataset.csv')
print("Dataset:")
print(data.head())

# Langkah 3: Preprocessing Data (Encoding data kategorikal)
encoder = LabelEncoder()
columns_to_encode = ['Posisi Lawan', 'Jarak Lawan', 'Luas Area Bebas', 'Kecepatan Robot', 'Orientasi Robot', 'Jumlah Lawan Terdekat']
for column in columns_to_encode:
    data[column] = encoder.fit_transform(data[column])

print("\nData setelah encoding:")
print(data.head())

# Langkah 4: Split Dataset menjadi training dan testing set
X = data.drop('Keputusan', axis=1)
y = data['Keputusan']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Langkah 5: Train Decision Tree
model = DecisionTreeClassifier(criterion='entropy', random_state=42)
model.fit(X_train, y_train)

print("\nStruktur Decision Tree:")
tree.plot_tree(model, filled=True)

# Langkah 6: Evaluasi Model
y_pred = model.predict(X_test)
print(f"\nAkurasi: {accuracy_score(y_test, y_pred)}")
print("\nLaporan Klasifikasi:")
print(classification_report(y_test, y_pred))

# Menyimpan model decision tree sebagai file PNG (opsional)
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(25,20))
_ = tree.plot_tree(model, feature_names=X.columns, class_names=model.classes_, filled=True)
fig.savefig("decision_tree.png")
