from collections import deque

# ---------------- STACK ----------------
print("STACK QUESTIONS:")

# Practical 1
momo = []
momo.append('Step1')
momo.append('Step2')
momo.append('Step3')
momo.pop()  # Undo one
print("Q: In MoMo, push ['Step1','Step2','Step3']. Undo one. Which steps are left?")
print("Ans:", momo)

# Practical 2
ur = []
ur.append('Note1')
ur.append('Note2')
ur.append('Note3')
ur.pop()
ur.pop()
ur_top = 'empty' if len(ur) == 0 else ur[-1]
print("Q: UR pushes ['Note1','Note2','Note3']. Undo two. Which is top?")
print("Ans:", ur_top)

# Challenge: Reverse "RWANDALOVE" using stack
word = "RWANDALOVE"
stack = []
for ch in word:
    stack.append(ch)
reversed_word = ""
while stack:
    reversed_word += stack.pop()
print("Q: Reverse 'RWANDALOVE' using stack.")
print("Ans:", reversed_word)

# Reflection
print("Q: Why stack gives priority to latest action?")
print("Ans: Because stack follows LIFO (Last In First Out), the most recent action is handled first.")

# ---------------- QUEUE ----------------
print("\nQUEUE QUESTIONS:")

# Practical 1
chuk = deque(["P1","P2","P3","P4","P5","P6","P7"])
for _ in range(5):
    chuk.popleft()
print("Q: At CHUK, 7 patients queue. After 5 served, who is front?")
print("Ans:", chuk[0])

# Practical 2
airtel = deque(["C1","C2","C3","C4","C5","C6"])
served_first = airtel.popleft()
served_second = airtel.popleft()
print("Q: At Airtel, 6 clients queue. Who is second served?")
print("Ans:", served_second)

# Challenge: Queue vs Stack for airplane boarding
print("Q: Queue vs Stack for boarding airplanes. Which is fair?")
print("Ans: Queue is fair because passengers board in order of arrival (FIFO). Stack would cause last arrival to board first, which is unfair.")

# Reflection
print("Q: Why FIFO ensures fairness in air travel?")
print("Ans: FIFO (First In First Out) is fair because the first passenger to arrive is also the first to board, avoiding disorder.")
