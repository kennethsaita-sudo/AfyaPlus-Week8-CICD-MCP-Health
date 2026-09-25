THRESHOLD = 0.85
SCORE = 0.90

print(f"Evaluation score: {SCORE}")
print(f"Threshold: {THRESHOLD}")

if SCORE < THRESHOLD:
    raise SystemExit("Evaluation gate failed")

print("Evaluation gate passed")