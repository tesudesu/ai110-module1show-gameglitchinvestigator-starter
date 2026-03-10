# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

  The game is a guess the number game. There is a field to enter a guess. After entering a guess, there are hints (e.g. go lower). On the left panel, you can choose the difficulty setting out of easy, medium, and hard. The difficulty levels differ based on the range of the correct number and the number of attempts allowed.

- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

  1. After typing in the "Enter your guess" field, the field shows "Press Enter to apply". However, pressing Enter does nothing.

  2. When the game is over, clicking "New Game" does nothing.

  3. The hints are backwards. For example, under Developer Debug Info, I could see that the secret number was 50. However, when I typed a number lower than 50, the hint told me to go lower, and when I typed a number greater than 50, the hint told me to go higher.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? 

  Claude

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

  I got an error in the terminal when I ran pytest tests/. The AI said the tests/ directory needs an __init__.py to be a valid Python package. After taking its suggestion to add the file, pytest worked.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

  This is not really a situation where the AI was wrong but that it could have done better. Previously, the AI identified an issue where in every even turn, the secret variable was turned into a string. The AI removed that logic. The AI also fixed the incorrect hints in the check_guess function. However, I noticed the except TypeError logic containing the same hint strings in the function. I asked the AI what that was about, and the AI explained that that code block was no longer needed because the code transforming secret into a string had already been fixed and suggested to remove the code block. I agreed and asked the AI to remove it. I felt that after fixing a piece of code, ideally the AI would point out other related areas of the code base to fix, rather than leaving me to detect stale code.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

  I asked the AI to write tests. I ran them and all the tests passed. While this still isn't a foolproof way of ensuring that there are no more problems, running tests (covering a variety of cases) gives more confidence that a bug is fixed.

- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.

  I like the test_parse_guess_decimal test in test_game_logic.py. This test checks that when a user enters a decimal, the decimal is automatically truncated. I thought this was a neat logic. I tested it in the app as well and it worked as expected.

- Did AI help you design or understand any tests? How?

  Yes, I asked the AI to implement tests in the test_game_logic.py file. The tests are pretty easy to understand, so I didn't specifically ask the AI to explain any. 

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.

  When I tested the app, I didn't notice that the secret number was changing when I submitted a guess. I asked the AI if the secret number changes, and the AI explained that it doesn't change during a game session but it changes when the "New Game" button is pressed. I tested this in the app, and the AI was right. The current logic is mostly correct - a new secret number should be generated for each new game. However, when the "New Game" button is pressed, the game doesn't restart, so it creates the impression that the secret number changes mid-game. 

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

  Every time a user interacts with a Streamlit app (e.g. clicks a button, types in a field), the entire script reruns. Session state is used to store information that should persist, e.g. the secret number. Session state is reset when the browser is refreshed/restart or when the Streamlit server restarts.

- What change did you make that finally gave the game a stable secret number?

  I asked the AI to fix the New Game button, which should clear the session states when pressed.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

  I learned pytest from this module. I also learned that coding assistants can be asked to generate tests. I will be sure to incorporate tests into my code in the future. 

- What is one thing you would do differently next time you work with AI on a coding task?

  I would probably ask it to explain the code, tell me how the current code works, before asking it to fix something. I found that sometimes it was hard to understand the changes that it was suggesting, so I couldn't really make an informed decision on the spot whether to accept or reject the changes. Having a stronger understanding of the existing code would make this process easier.

- In one or two sentences, describe how this project changed the way you think about AI generated code.

  It can really help you once you get used to it! But it can also make one reliant on it such that one forgets how to write code (recognizing code is different from writing it line by line).

