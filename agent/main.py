import json
import os
import sys

def load_tree(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

class ReflectionAgent:
    def __init__(self, tree_data):
        self.tree = {node['id']: node for node in tree_data}
        self.state = {
            "answers": {},
            "axis1": {"internal": 0, "external": 0},
            "axis2": {"contribution": 0, "entitlement": 0},
            "axis3": {"self": 0, "altro": 0}
        }
    
    def get_dominant(self, axis):
        scores = self.state[axis]
        if not scores: return ""
        # If there's a tie, we default to the first key, or could handle it. Let's just max.
        return max(scores, key=scores.get)

    def interpolate(self, text):
        if not text:
            return ""
        
        # Replace {NODE_ID.answer}
        for node_id, answer in self.state["answers"].items():
            text = text.replace(f"{{{node_id}.answer}}", answer)
        
        # Replace {axis1.dominant}, {axis2.dominant}, etc.
        for axis in ["axis1", "axis2", "axis3"]:
            dom = self.get_dominant(axis)
            text = text.replace(f"{{{axis}.dominant}}", dom)
            
        # Generate {summary_reflection}
        summary_reflection = ""
        a1_dom = self.get_dominant("axis1")
        a2_dom = self.get_dominant("axis2")
        a3_dom = self.get_dominant("axis3")
        
        if a1_dom == "internal" and a2_dom == "contribution" and a3_dom == "altro":
            summary_reflection = "You are operating with high agency and outward focus. Keep leading by example."
        elif a1_dom == "external" or a2_dom == "entitlement":
            summary_reflection = "Notice where you are giving up control or expecting things to just happen. Reclaiming your agency is the first step."
        else:
            summary_reflection = "You are in a mixed space, balancing personal responsibility with a growing awareness of your impact."
            
        text = text.replace("{summary_reflection}", summary_reflection)
        return text

    def process_signals(self, signal_string, chosen_option):
        if not signal_string:
            return
        parts = signal_string.split('|')
        for part in parts:
            if ':' not in part: continue
            split_part = part.split(':')
            if len(split_part) == 3:
                opt, axis, trait = split_part
                if opt == chosen_option:
                    if axis in self.state and trait in self.state[axis]:
                        self.state[axis][trait] += 1

    def run(self):
        current_node_id = "START"
        
        while current_node_id:
            node = self.tree.get(current_node_id)
            if not node:
                print(f"Error: Node {current_node_id} not found.")
                break
                
            node_type = node.get("type")
            text = node.get("text")
            options = node.get("options")
            target = node.get("target")
            
            if text:
                interpolated_text = self.interpolate(text)
            
            if node_type == "start":
                print(f"\n[START] {interpolated_text}")
                current_node_id = target
            
            elif node_type == "question":
                print(f"\n{interpolated_text}")
                opts = options.split('|') if options else []
                for i, opt in enumerate(opts):
                    print(f"  {i+1}. {opt}")
                
                choice = -1
                while True:
                    try:
                        choice = int(input(f"> Choose an option (1-{len(opts)}): ")) - 1
                        if 0 <= choice < len(opts):
                            break
                        print("Invalid choice. Try again.")
                    except ValueError:
                        print("Please enter a number.")
                
                chosen_option = opts[choice]
                self.state["answers"][current_node_id] = chosen_option
                
                if node.get("signal"):
                    self.process_signals(node["signal"], chosen_option)
                
                current_node_id = target
                
            elif node_type == "decision":
                rules = options.split(';')
                routed = False
                for rule in rules:
                    if rule.startswith("answer="):
                        condition, target_node = rule.replace("answer=", "").split(':')
                        valid_answers = condition.split('|')
                        parent_id = node.get("parentId")
                        if self.state["answers"].get(parent_id) in valid_answers:
                            current_node_id = target_node
                            routed = True
                            break
                    elif rule.startswith("condition="):
                        condition_parts, expected, target_node = rule.replace("condition=", "").split(':')
                        axis, attr = condition_parts.split('.')
                        
                        if attr == "dominant":
                            if self.get_dominant(axis) == expected:
                                current_node_id = target_node
                                routed = True
                                break
                
                if not routed:
                    current_node_id = target
                    
            elif node_type == "reflection":
                print(f"\n[REFLECTION] {interpolated_text}")
                input("(Press Enter to continue...)")
                current_node_id = target
                
            elif node_type == "bridge":
                print(f"\n[BRIDGE] {interpolated_text}")
                current_node_id = target
                
            elif node_type == "summary":
                print(f"\n[SUMMARY]\n{interpolated_text}")
                current_node_id = target
                
            elif node_type == "end":
                print(f"\n[END] {interpolated_text}\n")
                break
                
            else:
                current_node_id = target

if __name__ == "__main__":
    if len(sys.argv) > 1:
        tree_path = sys.argv[1]
    else:
        tree_path = os.path.join(os.path.dirname(__file__), '../tree/reflection-tree.json')
        
    try:
        tree_data = load_tree(tree_path)
        agent = ReflectionAgent(tree_data)
        agent.run()
    except Exception as e:
        print(f"Error running agent: {e}")
