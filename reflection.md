# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

---When I first ran the game using Streamlit, the interface worked but several parts of the logic behaved incorrectly. One bug was that the hint messages were reversed. For example, when my guess was higher than the secret number, the game sometimes told me to go “HIGHER” instead of “LOWER.” Another bug was that decimal inputs like 31.5 were accepted and automatically converted to integers, which should not happen in a number guessing game. A third issue caused the game to crash with a TypeError when the secret number was converted to a string and compared to an integer guess.


## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

I used GitHub Copilot and ChatGPT to help analyze the logic and explain why certain parts of the code were failing. One correct suggestion from the AI was identifying that the hint direction in the check_guess function was reversed. After reviewing the comparison logic and testing it in the game, I confirmed that the AI’s suggestion fixed the issue. One misleading suggestion was when the AI initially suggested a complex fix for the type error instead of identifying that the code was converting the secret number to a string. I verified the correct fix by manually tracing the code and removing the string conversion so both values stayed integers.


## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

To confirm my fixes worked, I manually tested the game by running it with Streamlit and entering different guesses. For example, I tested cases where the guess was higher than the secret and verified that the game correctly displayed “Go LOWER.” I also created automated tests using pytest to verify the check_guess function. The tests confirmed that guesses greater than the secret return “Too High” and guesses lower return “Too Low.” AI helped generate the structure of the pytest tests, but I reviewed the results and confirmed they passed before considering the bug fixed.


## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

Streamlit reruns the entire script every time the user interacts with the interface, such as pressing a button or entering input. Because of this, the game must store information like the secret number, score, and attempts in st.session_state. Session state acts like memory that persists between reruns of the app. Without session state, the game would reset every time the page refreshed or the user entered a guess.


## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

---

One habit I want to reuse in future projects is writing small tests to verify that functions behave correctly. Using pytest helped confirm that the guessing logic worked after fixing the bugs. Next time I work with AI on a coding task, I will double-check its suggestions carefully because AI can sometimes provide incorrect or overly complicated solutions. This project showed me that AI-generated code is useful for guidance but still requires careful review and testing by the developer.