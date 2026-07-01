from AGENT.policy_engine import PolicyEngine

engine = PolicyEngine()

print(engine.evaluate("PAN"))          # should print "block"
print(engine.evaluate("Confidential")) # should print "alert"
print(engine.evaluate("Public"))       # should print "log"
print(engine.evaluate("Random"))   