from AGENT.Classifier import classify_file
from AGENT.policy_engine import PolicyEngine

engine = PolicyEngine()

file_path = "TESTS/test_file.txt"
classification = classify_file(file_path)
policy = engine.evaluate(classification)

print(f"File: {file_path}")
print(f"Classification: {classification}")
print(f"Policy Decision: {policy['action']}")
