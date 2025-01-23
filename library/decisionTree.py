# import random
# from graphviz import Digraph

# data = {
#     "nodes": [
#         {"id": "A", "label": "Start Game"},
#         {"id": "B", "label": "Ball Out of Field?"},
#         {"id": "C", "label": "Yes - Call Corner or Throw-In"},
#         {"id": "D", "label": "No - Check for Foul"},
#         {"id": "E", "label": "Foul?"},
#         {"id": "F", "label": "Yes - Call Free Kick or Penalty"},
#         {"id": "G", "label": "No - Check Kickoff Done"},
#         {"id": "H", "label": "Kickoff Done?"},
#         {"id": "I", "label": "Yes - Continue Game"},
#         {"id": "J", "label": "No - Call Kickoff"}
#     ],
#     "edges": [
#         {"source": "A", "target": "B"},
#         {"source": "B", "target": "C", "label": "Yes", "probability": 0.6},
#         {"source": "B", "target": "D", "label": "No", "probability": 0.4},
#         {"source": "D", "target": "E"},
#         {"source": "E", "target": "F", "label": "Yes", "probability": 0.4},
#         {"source": "E", "target": "G", "label": "No", "probability": 0.6},
#         {"source": "G", "target": "H"},
#         {"source": "H", "target": "I", "label": "Yes", "probability": 0.9},
#         {"source": "H", "target": "J", "label": "No", "probability": 0.1}
#     ]
# }

# q_table = {node['id']: {edge['target']: 0 for edge in data['edges'] if edge['source'] == node['id']} for node in data['nodes']}

# REWARD_SUCCESS = 1
# PENALTY_FAILURE = -1
# LEARNING_RATE = 0.1
# DISCOUNT_FACTOR = 0.9

# def update_q_table(q_table, state, action, reward, next_state, learning_rate=0.1, discount_factor=0.9):
#     current_q = q_table[state][action]
#     max_future_q = max(q_table[next_state].values(), default=0)
#     new_q = (1 - learning_rate) * current_q + learning_rate * (reward + discount_factor * max_future_q)
#     q_table[state][action] = new_q

# dot = Digraph()

# for node in data["nodes"]:
#     dot.node(node["id"], node["label"])

# for edge in data["edges"]:
#     dot.edge(edge["source"], edge["target"], label=edge.get("label", ""))

# def make_decision_and_learn():
#     current_node = "A"
#     path = [current_node]

#     while True:
#         outgoing_edges = [edge for edge in data["edges"] if edge["source"] == current_node]
        
#         if not outgoing_edges:
#             break

#         actions = [edge["target"] for edge in outgoing_edges]
#         q_values = [q_table[current_node][action] for action in actions]
        
#         epsilon = 0.1
#         if random.uniform(0, 1) < epsilon:
#             next_node = random.choice(actions)
#         else:
#             max_q_value = max(q_values)
#             best_actions = [actions[i] for i, q in enumerate(q_values) if q == max_q_value]
#             next_node = random.choice(best_actions)
        
#         if next_node in ["C", "F", "I"]:
#             reward = REWARD_SUCCESS
#         else:
#             reward = PENALTY_FAILURE if next_node in ["J"] else 0
        
#         next_state = next_node
#         update_q_table(q_table, current_node, next_node, reward, next_state, LEARNING_RATE, DISCOUNT_FACTOR)
        
#         path.append(next_node)
#         current_node = next_node

#         if current_node in ["C", "F", "I", "J"]:
#             break

#     return path

# path = make_decision_and_learn()
# decisions = [data['nodes'][int(node, 36) - 10]['label'] for node in path if node != 'A']
# print(f"Simulasi : {' -> '.join(decisions)}")
